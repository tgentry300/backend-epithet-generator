# Instructions for Sprint B

## Objectives
- Demonstrate decoupling application logic from [views](http://flask.pocoo.org/docs/1.0/views/)
- Demonstrate benefits of decoupling in terms of code reuse and unit testing.

## Introduction
In sprint A we defined a minimal Flask application project structure as a Python 
package with four modules: \_\_init__.py, app.py, helpers.py, and test_helpers.py.
The four modules were included in the definition of a minimal Flask application 
because they represent a clean separation of concerns:
- all application configuration and instances are in the package's init module
- all application routes are included in the app module
- all application logic is included in the helpers module
- all unit tests for the helpers module are included in the test_helpers module


In this assignment we will continue where sprint A concluded by:
1. decoupling application logic from views using "helper" classes.
2. unit testing blocks of application logic.
1. serving views of epithets and the insult kit vocabulary.



## Adding Application Logic

### The helpers.py File
This module will be used to define much of our application logic before 
demonstrating more extensible ways of structuring projects. At this point, what 
is important is that we want to separate application logic from views as much 
as possible to promote code reuse and simplify testing. For example, to 
generate epithets for this assignment we'll need to:
1. read a file containing the [Shakespeare Insult Kit](http://www.pangloss.com/seidel/shake_rule.html) .
2. convert the contents of the file to a dictionary of lists keyed 
for each column of words in the insult kit.
3. select a random word from each column in column order.
4. create a formatted string of the randomly selected words.
 
Without separating application logic from views, each view would have redundant 
implementations of these four behaviors. As views are added, the redundant code 
will quickly become difficult to maintain. Instead, we'll keep our application 
[DRY](https://code.tutsplus.com/tutorials/3-key-software-principles-you-must-understand--net-25161) 
by factoring out classes to encapsulate these behaviors.

1. Add the following class to the helpers.py file. It'll be used to handle 
different file types.
```python
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
```

We'll also need a helper for transforming different data formats into a consistent
representation of the Shakespeare Insult Kit. Otherwise, every view added to 
the Flask application would have to handle transforming data from different 
formats. For example, the backend-epithet-generator/resources directory 
contains CSV, JSON, and SQLite versions of the insult kit. Each of these formats 
requires a different strategy for converting it into a consistent representation 
that can be used throughout an application -- in this case a dictionary of lists.


This conversion is beyond the scope of the FileManager class, because what 
does a file manager need to know about linguistics? If you look at columns of 
the insult kit, each column is a different part of speech forming a grammar of 
adjectives, compound-adjectives, and nouns. This order has to be maintained 
for epithets to be intelligible, because the difference between "Thou measle 
ill-breeding infectious" and "Thou infectious, ill-breading measle" is meaningful. 
We'll factor out a Vocabulary class for handling order and other requirements of 
language that may occur.

1. Add the following class to the helpers.py file. It'll be used to transform 
different file types returned by the FileManager class into a dictionary of 
lists representation keyed for each column of the insult kit.

```python
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
        if intent is 'read':
            return input_strategies[file_extension]
```


## Assignment
We now have everything we need to start the assignment. If you haven't done so 
already, please add the provided classes to the helpers.py file and complete 
the remainder of the assessment.

1. Unit test each of the two provided classes.
2. Define an EpithetGenerator class with methods to:
    1. select one random word from each column of the list.
    2. generate a quantity of epithets from a vocabulary file loaded from a path.
4. Unit test the EpithetGenerator class.
5. Use the EpithetGenerator class in the '/' route to serve a randomly 
generated epithet.
6. Use the Vocabulary class in the '/vocabulary' route to serve the vocabulary 
used to generate the epithet.
7. In the helpers.py file, add docstrings explaining what each code block 
does, for both provided and created classes.