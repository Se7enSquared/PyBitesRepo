from collections import namedtuple
from telnetlib import SE

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

class UserNoPermission(Exception):
    def __init__(self):
        self.message = 'Insufficient permissions'
        super().__init__(self.message)

class UserAccessExpired(Exception):
    def __init__(self):
        self.message = 'access expired'
        super().__init__(self.message)

class UserDoesNotExist(Exception):
    def __init__(self):
        self.message = 'User does not exist'
        super().__init__(self.message)

def _get_user(username):
    users = {user.name: user for user in USERS}
    return users.get(username)

def get_secret_token(username):
    user = _get_user(username)
    if not user:
        raise UserDoesNotExist()
    if user.expired:
        raise UserAccessExpired()
    if user.role != ADMIN:
        raise UserNoPermission()

    return SECRET
