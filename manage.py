from flask_script import Commands
from flask_migrate import Migrate, MigrateCommand

from app import app
from models import db

migrate = Migrate(app, db)
manager = Commands(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()