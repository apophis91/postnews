import click
from flask_sqlalchemy import SQLAlchemy
from .config import config
from werkzeug.utils import import_string, find_modules
from .utils import ApiFlask

db = SQLAlchemy()

def create_app(config_name=None):
    app = ApiFlask(__name__)
    app.config.from_object(config.get(config_name, config['development']))
    db.init_app(app)
    register_cli(app)
    register_bp(app)
    return app

def register_bp(app):
    """ Register blueprints automatically. """
    for nm in find_modules("postnews.bprints", recursive=True):
        mod = import_string(nm)
        if hasattr(mod, "bp"):            # bp = Blueprint(...)
            app.register_blueprint(mod.bp)
    return None

def register_cli(app):
    @app.cli.command("initdb")
    def initdb():
        from postnews import models
        db.create_all()
        click.echo("Database created.")
