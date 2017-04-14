from unittest import TestCase, skip, main
from engine import fields_where_user_can_be_placed, indestructible

class MyTestCase(TestCase):

    @skip
    def test_generate_board(self):
        self.assertEqual(True, False)

    def test_length_of_fields_where_user_can_be_placed(self):
        fields = fields_where_user_can_be_placed()
        self.assertEquals(len(fields), 25)
        fields = fields_where_user_can_be_placed(100, 100)
        self.assertEquals(len(fields), 2500)
        fields = fields_where_user_can_be_placed(2, 2)
        self.assertEquals(len(fields), 1)
        fields = fields_where_user_can_be_placed(2, 4)
        self.assertEquals(len(fields), 2)
        fields = fields_where_user_can_be_placed(4, 2)
        self.assertEquals(len(fields), 2)

    def test_fields_cannot_be_made_from_too_small_dimensions(self):
        with self.assertRaises(Exception):
            fields_where_user_can_be_placed(1, 1)
        with self.assertRaises(Exception):
            fields_where_user_can_be_placed(0, 0)
        with self.assertRaises(Exception):
            fields_where_user_can_be_placed(1, 10)
        with self.assertRaises(Exception):
            fields_where_user_can_be_placed(10, 0)

    def test_length_of_indestructible_fields(self):
        fields = indestructible()
        self.assertEquals(len(fields), 25)
        fields = indestructible(100, 100)
        self.assertEquals(len(fields), 2500)
        fields = indestructible(2, 2)
        self.assertEquals(len(fields), 1)
        fields = indestructible(2, 4)
        self.assertEquals(len(fields), 2)
        fields = indestructible(4, 2)
        self.assertEquals(len(fields), 2)

    def test_indestructible_fields_cannot_be_made_from_too_small_dimensions(self):
        with self.assertRaises(Exception):
            indestructible(1, 1)
        with self.assertRaises(Exception):
            indestructible(0, 0)
        with self.assertRaises(Exception):
            indestructible(1, 10)
        with self.assertRaises(Exception):
            indestructible(10, 0)

    def test_length_of_destructible_fields(self):
        self.assertEquals(1, 1)

    def get_users(self):
        users = [{'name': 'Luk'}, {'name': 'Marke'}]
        return users

if __name__ == '__main__':
    main()
