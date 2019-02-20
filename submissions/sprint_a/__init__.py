def configure_app():
    """configuring application"""
    import os
    import dotenv
    from flask import Flask
    app = Flask(__name__)

    PROJECT_ROOT = os.path.dirname(os.getcwd())
    dotenv_path = os.path.join(PROJECT_ROOT, '.env')

    dotenv.load_dotenv(dotenv_path)

    return app


app = configure_app()
 