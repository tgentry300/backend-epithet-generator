import os
import json
import random


class FileManager:
    """Handle local file system IO."""

    @staticmethod
    def get_extension(path):
        """Get file extension from file path."""
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode='r', *args, **kwargs):
        with open(path, mode=mode, *args, **kwargs) as handle:
            return json.load(handle)


class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def from_json(cls, path, fields=True, *args, **kwargs):
        data = cls.files.read_json(path, *args, **kwargs)
        if fields:
            representation = (data, data.keys())
        else:
            representation = data
        return representation

    @classmethod
    def strategies(cls, file_extension, intent='read'):
        input_strategies = {'json': cls.from_json}
        if intent == 'read':
            return input_strategies[file_extension]


class EpithetGenerator:
    """Handle creation of epithets"""

    vocab = Vocabulary()

    def select_random(self, path):
        "Selects random word from each column and returns a string"
        vocab_dict = self.vocab.from_file(path)

        col_1_random = random.choice(vocab_dict[0]['Column 1'])
        col_2_random = random.choice(vocab_dict[0]['Column 2'])
        col_3_random = random.choice(vocab_dict[0]['Column 3'])

        epithet = f"Thou {col_1_random} {col_2_random} {col_3_random}"
        return epithet

    def gen_multiple_epithets(self, path, num):
        "Generates list of given number of epithets"
        multiple_epithets = []
        for _ in range(num):
            multiple_epithets.append(self.select_random(path))
        return multiple_epithets
