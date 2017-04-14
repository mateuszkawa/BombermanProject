import time, logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class User:
    def __init__(self, name: str):
        self.name = name
        self.id = id(self)


class UserMessage:
    pass


class Registration:

    def __init__(self, time_window):
        self.users = {}
        self.time_window=time_window
        self.initial_time = time.time()

    def register(self, user: User):
        logging.info(f'registering {user.name}')
        self.actual_time = time.time()
        time_left = self.actual_time - self.initial_time
        if time_left > self.time_window:
            raise "over delta, muddafadda"

        if user.name in self.users:
            logging.info(f'User already registered!! {user.name}')
        else:
            self.users[user.name] = user

        registered_user = self.users[user.name]
        return {
            'user_id' : registered_user.id,
            'time_left' : time_left
        }

    def contain_user_named(self, user_name):
        return user_name in self.users


class ActualState:
    pass


if __name__ == '__main__':
    user = User('user1')
    registration = Registration(3000)
    registration.register(user)

    assert registration.contain_user_named('user1')
    assert registration.users.get('user1').id is not None
