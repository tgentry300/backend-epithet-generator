from .helpers import Vocabulary, EpithetGenerator, FileManager

json_path = '../../resources/data.json'

test_json_path = "./test_data.json"

data_representation = {}


class TestFileManager:

    file_manager = FileManager()

    def test_get_extension(self):
        """Test that actually gets extension"""
        assert self.file_manager.get_extension(json_path) == "json"

    def test_read_json(self):
        """Test that actually reads json"""
        assert len(self.file_manager.read_json(test_json_path)
                   .get("Column1")) == 3


class TestVocab:

    vocab = Vocabulary()

    def test_from_file(self):
        """Tests that a tuple of data is returned"""
        assert type(self.vocab.from_file(json_path)) is tuple
        assert type(self.vocab.from_file(json_path)[0]) is dict

    def test_from_json(self):
        """Tests that a tuple of data is returned"""
        assert type(self.vocab.from_json(json_path)) is tuple
        assert type(self.vocab.from_file(json_path)[0]) is dict


class TestEpithetGenerator:

    epithet_gen = EpithetGenerator()

    def test_select_random(self):
        """Tests for random selection"""
        assert type(self.epithet_gen.select_random(json_path)) is str

    def test_gen_multiple_epithets(self):
        """Tests for multiple epithets"""
        mul_epth = self.epithet_gen.gen_multiple_epithets(json_path, 3)

        assert len(mul_epth) == 3
        assert type(mul_epth) is list
