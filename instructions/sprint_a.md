# Instructions for Sprint A

## Objectives
- Demonstrate version control best-practices for starting Flask projects.
- Demonstrate a minimal Flask project structure.
- Configure and instantiate an instance of a Flask application using the factory method design pattern.
- Define view functions and routes for GET requests.
- Serve JSON encoded responses.



## Initialize Repository
1. Fork this repo then clone the master branch of this repository to a convenient 
location and change directories into the cloned repository.
    ```bash
    git clone <url_of_your_fork_of_the_repo>
    cd backend-epithet-generator
    ```
    
2. Create a sprint-a branch for work in progress and add the recommended Python 
[local .gitignore](https://github.com/github/gitignore) starter file from GitHub.
    ```bash
    git checkout -b sprint-a
    curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore
    ```
    curl displays contents of URLs to stdout, a.k.a the terminal, and the > operator redirects stdout to the specified 
    file. If the file does not exist, the redirect operator creates the file. If the provided file does exist, it 
    will be overwritten with the contents of the URL. For additional examples of curl, 
    [this tutorial](https://gist.github.com/caspyin/2288960) explores the GitHub API using curl.
    
    - Review the contents of the recommended .gitignore file to see commonly ignored Python artifacts.
    - Notice GitHub recommends not committing virtualenvs to version control. It is unnecessary and has considerable 
    storage costs. Instead, use pipenv to centrally manage environments outside of project repositories.
    
    If curl is not installed, it can be installed with most package managers.
    
    ```bash
    #MacOS
    brew install curl
    
    #Windows
    choco install curl
    ```
    
3. Delete all sections of the downloaded .gitignore file except sections listed below. Unless a statement in the 
downloaded .gitignore collides with a name of a project resource, it is not necessary to remove any of the entries, 
but we will for the sake of being explicit. It is probable that files from each of these sections could end up in a 
Flask project. The others are less probable and can be ignored later if introduced. Alternatively, 
you can add the removed sections to your [$HOME/.gitignore_global](https://help.github.com/articles/ignoring-files/)
file to protect all git repositories on your computer from these files without adding the ignore statements to each
project.
    - Byte-compiled / optimized / DLL files
    - C extensions
    - Installer logs
    - Unit test / coverage reports
    - Flask stuff
    - pyenv
    - Environments
    
4. Stage the .gitignore file and create an initial commit of the sprint-a branch.
    
    
 ## Configuring Development Environments
 To demonstrate effective environment management with pipenv, we will create a virtualenv for each sprint of this 
 assignment by creating Pipfile and Pipfile.lock files from the directories of each sprint. These directories should
 be created in the ./submissions folder of the cloned repository.
 ```bash
 mkdir submissions/sprint_a
 cd submissions/sprint_a
 pipenv install flask
 pipenv install python-dotenv
 pipenv install pytest --dev
 pipenv --venv
```

## Structuring Projects
There are many ways to structure Flask applications, but not all project structures are equal. We will start the Epithet
Generator project as a single Python package with four files and evolve the project structure according to Flask 
best-practices when needed.

1. Although a single file is sufficient for minimal Flask applications, we define a minimal application as a
 Python package consisting of four files: app.py, helpers.py, test_helpers.py, and the package's \_\_init__.py file. We
 will focus on these four files first before showing how to refactor the project structure for
 [large projects](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications) 
 in a later sprint.
```bash
pwd
./submissions/sprint_a
touch __init__.py
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
It is common to see instances of Flask applications instantiated simply as "app = Flask(\__name__)". However, Flask
 recommends using the [factory method](http://flask.pocoo.org/docs/1.0/patterns/appfactories/) design pattern.
 The benefit of using this pattern is that object creation logic is consolidated in one location making 
 the code easier to understand and maintain. Factories can also be used to simplify creation of different classes of 
 objects when it is not known in advance which objects are needed. In the case of Flask, this could mean instantiating 
 instances of the Flask application, databases, etc.... These resources are used throughout an application's codebase, 
 so it is beneficial to have their configuration and instantiated instances in one location to be imported elsewhere in 
 the project when needed. We'll follow Flask's recommendation and use a factory defined in the project's \_\_init__.py 
 file to configure and initialize an instance of the Flask class used throughout the project.

### In the \_\_init__.py File
1. Define a function named configure_app
2. In the configure_app function; import os, dotenv, and flask
3. Use the [os.path.dirname()](https://pymotw.com/3/os.path/index.html) method to assign the current working directory 
    to a variable named PROJECT_ROOT
4. Use dotenv.load_dotenv(), 
    [os.path.join()](https://pymotw.com/3/os.path/index.html#building-paths), and the PROJECT_ROOT variable to load 
    environment variables automatically from the .env file. 
5. Instantiate and return an instance of Flask from the configure_app function.
6. Use the configure_app function to assign an instance of the Flask application to a variable labeled app.

### In the .env File
Add to following to the .env file. 
```bash
FLASK_APP=app
FLASK_ENV=development
```
- The FLASK_APP environment variable tells Flask which file & variable to use when loading applications. If FLASK_APP is 
not defined, Flask will default to app but we'll define it here to be explicit.
- The FLASK_ENV environment variable tells Flask which environment settings to use. If FLASK_ENV is not set, Flask will 
default to production environment settings which disables Flask's debug mode for security purposes. Setting FLASK_ENV to 
development enables debugging.


### In the app.py File
Import the instance of app from the sprint_a package. A package in Python is any directory with an \_\_init__.py 
 file. By defining the configure_app and using it to instantiate an instance of Flask in the \_\_init__.py file, we can 
 import app directly from the project's root directory.


## Defining Routes
1. In app.py, use the app.route decorator to:
    - bind a view function called generate_epithets to '/'. This route will serve a randomly generated epithet.
    - bind a view function called vocabulary to '/vocabulary'. This route will serve the vocabulary used to generate 
    epithets.
3. Have these functions return a JSON representation of {"epithets": []} and {"vocabulary": {}} respectively.


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