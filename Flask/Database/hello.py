from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' %self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager = Manager(app)
manager.add_command("shell", Shell(make_context=make_shell_context))

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
#
# db.drop_all()
# db.create_all()
#
# admin_role = Role(name='Admin')
# mode_role = Role(name='Moderator')
# user_role = Role(name='User')
#
# user_john = User(username='john', role=admin_role)
# user_susan = User(username='susan', role=user_role)
# user_david = User(username='david', role=user_role)
#
# db.session.add_all([admin_role, mode_role, user_role, user_john, user_susan, user_david])
#
# db.session.commit()

# print(user_role.id)

if __name__ == '__main__':
    manager.run()

