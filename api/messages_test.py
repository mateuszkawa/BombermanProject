import unittest
import messages
import time


class MyTestCase(unittest.TestCase):
    def test_user_gets_some_id(self):
        user_1 = messages.User(name='some_name')
        self.assertIsNotNone(user_1.id)

    def test_rises_bad_registration(self):
        register = messages.Registration(time_window=-100)
        with self.assertRaises(Exception):
            register.register(messages.User('some_name'))

    def test_registration_givenTheSameUserAgain_returnsTheSameUser(self):
        user_1 = messages.User(name='userName')
        register = messages.Registration(time_window=100)
        user_1st = register.register(user_1)
        user_2nd = register.register(user_1)
        self.assertEquals(user_1st['user_id'], user_2nd['user_id'])

    def test_registration_givenTheDifferentUser_returnsDifferent_ids(self):
        register = messages.Registration(time_window=100)
        user_1st = register.register(messages.User(name='userName'))
        user_2nd = register.register(messages.User(name='userName2'))
        self.assertNotEquals(user_1st['user_id'], user_2nd['user_id'])

    def test_registration_givenUserLogsAfterTimeWindow_givesException(self):
        register = messages.Registration(time_window=2)
        time.sleep(3)
        with self.assertRaises(Exception):
            register.register(messages.User('some_name'))

    def test_registration_givenTheDifferentUser_returnsDifferent_times(self):
        register = messages.Registration(time_window=100)
        user_1st = register.register(messages.User(name='userName'))
        time.sleep(1)
        user_2nd = register.register(messages.User(name='userName2'))
        self.assertNotEquals(user_1st['time_left'], user_2nd['time_left'])


if __name__ == '__main__':
    unittest.main()
