import time

class User:
    def __init__(self, name: str):
        self.name = name
        self.id = id(self)


class Registration:

    def __init__(self, time_window):
        self.users = {}
        self.time_window=time_window
        self.initial_time = time.time()

    def register(self, user: User):
        self.actual_time = time.time()
        diff = self.actual_time - self.initial_time
        if diff > self.time_window:
            raise "over delta, muddafadda"
        self.users[user.name] = user
        return {
            'user_name' : user.name,
            'time_left' : diff
        }

    def contain_user_named(self, user_name):
        return user_name in self.users




if __name__ == '__main__':
    user = User('user1')
    registration = Registration(3000)
    registration.register(user)

    assert registration.contain_user_named('user1')
    assert registration.users.get('user1').id is not None
