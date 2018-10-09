# Instructions for Iteration One

## Objectives
- Instantiate and configure an instance of a Flask application
- Define view functions and routes for GET requests
- Serve JSON encoded responses
- Demonstrate a minimal project structure
- Demonstrate decoupled approach for defining application logic



## Initialize Repository
1. Clone the master branch of this repository to a convenient location and change directories into the cloned repository.
    ```bash
    git clone ...
    cd ...
    ```
    
2. Create an iteration-a branch for work in progress and add the recommended Python 
[local .gitignore](https://github.com/github/gitignore) starter file from GitHub. git also has 
[global .gitignore](https://help.github.com/articles/ignoring-files/) settings which are convenient but do 
not commit ignored files to project repositories. For this assignment, we will use local .gitignore files, but 
exploring global .gitignore settings is encouraged. An example use-case for global .gitignores is to add your IDE or
text editor artifacts to your $HOME/.gitignore_global file. Using global ignores in this way keeps unnecessary ignore
statements out of projects which increases the visible of project specific ignores.
    ```bash
    git checkout -b iteration-a
    curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore
    ```
    - curl displays contents of URLs to stdout (the terminal screen) and the > operator redirects stout to the provided filename
    - review contents of the recommended .gitignore file to see commonly ignored Python artifacts
    - do not commit virtualenvs to version control. It is unnecessary 
    and has considerable storage costs. Instead of adding this overhead to Python projects, use pipenv or similar tools 
    to centrally manage isolated environments.
    
3. Delete all sections of the downloaded .gitignore file except sections listed below. Unless a statement in the 
downloaded .gitignore collides with a name of a project resource, it is not necessary to remove any of the entries, 
but we will for the sake of being explicit. It is probable that files from each of these sections could end up in a 
Flask project. The others are less probable and can be ignored later if introduced. Alternatively, 
you can add the removed sections to your $HOME/.gitignore_global file to still protect the assignment repo and all 
other repos on your computer. 
    - Byte-compiled / optimized / DLL files
    - C extensions
    - Installer logs
    - Unit test / coverage reports
    - Flask stuff
    - pyenv
    - Environments
    
4. Stage the .gitignore file and create an initial commit of the development branch.
    
    
 ## Configuring Development Environments
 To demonstrate effective environment management with pipenv, we will create a virtualenv for each sprint of this 
 assignment by creating Pipfile and Pipfile.lock files from the directories of each sprint. These directories should
 be created in the ./submissions folder of the cloned repository.
 
 1. Create a directory for sprint_a and create an isolated environment 
 ```bash
 mkdir ./submissions/sprint_a
 cd .submissions/sprint_a
 pipenv install flask
 pipenv install python-dotenv
 pipenv install pytest --dev
 pipenv --venv
```
By not specifying a version of flask, python-dotenv, or pytest; the latest version of each package was installed. This 
is indicated in Pipfile with asterisks for package versions instead of a [version specifier](https://www.python.org/dev/peps/pep-0440/#version-specifiers).  
Now that packages are installed, we can use pip to discover which versions of these packages were installed and 
pin the dependencies in our Pipfile accordingly. pipenv pins package versions in Pipfile.lock, but it is a good practice 
to add our version requirements to Pipfile should Pipfile.lock need regenerating.
```bash
pip show <package-name>
```
1. Use pip to discover the versions of packages that were installed with pipenv in the previous step.
    - these are the project's requirements a.k.a dependencies
    - all other installed packages are transitive dependencies required by project dependencies
2. Use the version matching [clause](https://www.python.org/dev/peps/pep-0440/#version-specifiers) to pin the exact version
of these packages in Pipenv

## Structuring Projects
There are many ways to structure Flask applications, but not all project structures are equal. We will start the Epithet
Generator project as a single Python package with four files and evolve the project structure according to Flask 
best-practices when needed.

1. Although a single file is sufficient for minimal Flask applications, we define a minimal application as a
 Python package consisting of four files: app.py, helpers.py, test_helpers.py, and the package's \__init__.py file. We
 will focus on these four files first before showing how to refactor the project structure for
 [large projects](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications) 
 in a later sprint.
```bash
pwd
./submissions/sprint_a
touch __init__py
touch app.py
touch helpers.py
touch test_helpers.py
touch .env
```

|File|Description
|---|---|
\_\_init__.py| Organize Flask configuration and app instances.
app.py| Organize defined routes. You may see this file called app.py or <project-name>.py in other projects. Flask defaults to loading app.py, so we will default to using app.py here, but the name is arbitrary and can be configured with the FLASK_APP environment variable.
helpers.py| Organize application logic keeping it decoupled from routes defined in app.py. By decoupling application and routing, application logic can be easily reused in other areas of an application or in other projects.
test_helpers.py| Organize unit and integration tests for the Flask application. In larger applications, helpers in helpers.py would be distributed across multiple packages, each with a test_<package-name>.py file of tests.
.env| Store application configuration management as environment variables. This file is not considered in the four files of a Flask application as .env files are used across programming languages and frameworks.


## Instantiating Flask
It is common to see instances of Flask applications instantiated simply as "app = Flask(\__name__)"; however, Flask
 recommends the [factory method](http://flask.pocoo.org/docs/1.0/patterns/appfactories/) design pattern instead. 
 The benefit of factories, in Flask and elsewhere, is that object creation logic is consolidated in one location making 
 the code easier to understand and maintain. Factories can also be used to consolidate creation of different classes of 
 objects when it is not known in advance which objects are needed. In the case of Flask, this could mean instantiating 
 instances of the Flask application, databases, etc.... These resources are used throughout an application's codebase, 
 so it is beneficial to have their configuration and  intialized instances in one location to be imported elsewhere in 
 the project when needed. We'll follow Flask's recommendation and use a factory defined in the project's \__init__.py 
 file to configure and initialize an instance of the Flask class to be used in the app.py, helpers.py, 
 and test_helpers.py files.

### In the \__init__.py File
1. Define a function named configure_app
2. In the configure_app function; import os, dotenv, and flask
3. Use the [os.path.dirname()](https://pymotw.com/3/os.path/index.html) method to assign the current working directory 
    to a variable named PROJECT_ROOT
4. Use dotenv.load_dotenv(), 
    [os.path.join()](https://pymotw.com/3/os.path/index.html#building-paths), and the PROJECT_ROOT variable to load 
    environment variables automatically from the .env file. 
5. Instantiate and return an instance of Flask from the configure_app function.
6. Use the configure_app function to assign an instance of the Flask application to a variable identifier labeled app.

### In the .env File
Add to following to the .env file. The FLASK_APP environment variable tells flask which file to use to 
load applications, and the FLASK_ENV environment variable is used to tell flask which environment configuration to use.
Flask defaults to production if FLASK_ENV is not defined, which disables flask debugging, so setting FLASK_ENV to 
development prevents configuring the Flask debug parameter. If FLASK_ENV is set to development, debugging is 
automatically enabled.
```bash
FLASK_APP=app
FLASK_ENV=development
```

### In the app.py File
1. import the instance of app from the sprint_a package. A package in Python is any directory with an \__init__.py 
 file. By defining the configure_app and using it to instantiate an instance of Flask in the \__init__.py file, we can 
 import app directory from the project's root package i.e. sprint_a.


## Defining Routes
1. Open app.py and import the configure_app function defined previously to instantiate an instance of Flask
2. Using the app.route decorator:
    - bind a view function called generate_epithets to '/' to serve a randomly generated epithet.
    - bind a view function called vocabulary to '/vocabulary' to serve all vocabulary words.
3. Have these functions return a JSON representation of {"epithets": []} and {"vocabulary": []} respectively.


## Starting Flask's Development Server
At this point, we have defined a working Flask application and can verify our progress by starting Flask's development
server and navigating to the routes we defined.
1. Launch the pipenv shell within the project's root directory i.e. submissions/sprint_a
2. Once the shell is open, start the Flask application using flask run as shown below.
3. Navigate to http://127.0.0.1:5000 and verify both routes are serving their respective payloads configured in the
previous section.
4. If both routes are serving their payloads, this sprint of the assignment is complete.

```bash
flask run
```


## Rubric


| |Professional|Acceptable|Unprofessional
---|---|---|---
|Initialize Repository|listed|listed|listed
|Configuring Development Environments|listed|listed|listed
|Structuring Projects|listed|listed|listed
|Instantiating Flask|listed|listed|listed
|Defining Routes|listed|listed|listed
|Starting Flask's Development Server|listed|listed|listed

1. Initialize Repository
    1. Professional
        1. repository contains:
            - .gitignore file containing the requested sections of Github's default Python .gitignore file
            - a README.md file describing the project
        2. repository does not contain:
            - virtualenv and other artifacts such as IDE/editor configuration, .pyc files, pytest's cache directory, etc...
        3. commit message of the initial commit briefly describes the intent of the project
        4. all work was completed on the sprint-a branch of the repository
    2. Acceptable
        1. repository contains:
            - .gitignore file containing Github's entire default Python .gitignore file
    3. Unprofessional
        1. repository contains:
            - virtualenv and other artifacts such as IDE/editor configuration, .pyc files, pytest's cache directory, etc...
        2. repository does not contain:
            - a README.md file describing the project
        3. commit messages lack sufficient information to understand why changes were made. Version control tracks what
            changed, developers are responsible for describing why changes are made
            
2. Configuring Development Environments
    1. Professional
        1. Pipfile specifies i.e. pins the:
            - versions of each installed package using the version matching clause
        2. Pipfile.lock
            - the file exists
        3. Both Pipfile and Pipfile.lock are committed
    2. Acceptable
        1. Pipfile specifies i.e. pins the:
            - versions of each installed package using the compatible version clause
        2. Pipfile, but not Pipfile.lock, was committed and a version specifier was used
    3. Unprofessional
        1. Pipfile specifies i.e. pins the:
            - versions of each installed package using asterisks
        2. Pipfile, but not Pipfile.lock, was committed and a version specifier was not used
    
3. Structurting Projects
4. Instantiating Flask
5. Defining Routes
6. Starting Flask's Development Server
