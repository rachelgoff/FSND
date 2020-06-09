from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from backend.src.app import app as application
from backend.src.database.models import db

migrate = Migrate(applicaiton, db)
manager = Manager(application)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()