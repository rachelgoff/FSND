import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend/src')))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend/src')))
print("test")

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from .database.models import db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()