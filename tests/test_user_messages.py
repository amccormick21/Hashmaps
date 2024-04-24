import unittest
from message_table.message_table import UserList, MessageList
from message_table.message_table import DataCache

class TestUserMessages(unittest.TestCase):
    def setUp(self):
        self.data_cache = DataCache(user_list=UserList(), message_list=MessageList())

    def test_user_unique_message(self):
        user_message_first = self.data_cache.get_user_message(0, 0)
        user_message_second = self.data_cache.get_user_message(0, 1)
        self.assertNotEqual(user_message_first, user_message_second)

    def test_all_messages_unique(self):
        unique_messages = set()

        for i in range(0, self.data_cache.users.size()):
            returned_message = self.data_cache.get_user_message(0, i)
            unique_messages.add(returned_message)

        self.assertEqual(len(unique_messages), self.data_cache.users.size())

    def test_all_users_unique(self):
        unique_messages = set()

        for i in range(0, self.data_cache.users.size()):
            returned_message = self.data_cache.get_user_message(i, 0)
            unique_messages.add(returned_message)

        self.assertEqual(len(unique_messages), self.data_cache.users.size())

    def test_print_messages(self):
        # This test will pass if it just completes
        self.data_cache.pretty_print_message_table()

if __name__ == '__main__':
    unittest.main()
