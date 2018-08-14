import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from flask_migrate import MigrateCommand
from Shopacholic import application

manager = Manager(application)
manager.add_command('db', MigrateCommand)

manager.add_command('server', Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port=5000
))

if __name__ == '__main__':
    manager.run()