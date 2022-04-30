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


def get_secret_token(username):
    found = False
    for user in USERS:
        if user.name == username:
            found = True
            if user.expired:
                raise UserAccessExpired()
            if user.role != ADMIN:
                raise UserNoPermission()

    if not found:
        raise UserDoesNotExist()
    return SECRET
