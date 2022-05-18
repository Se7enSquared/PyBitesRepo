known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    def wrapper(user):
        if user in known_users:
            if user in loggedin_users:
                return func(user)
            else:
                return 'please login'
        else:
            return 'please create an account'
    wrapper.__doc__ = func.__doc__
    return wrapper


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'

print(welcome('sue'))