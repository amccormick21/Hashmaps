import unittest
from message_table.message_table import HashTable, MessageStatus, MessageElement

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(20)

    def test_create_buckets(self):
        self.assertEqual(self.hash_table.size, 20)
        self.assertEqual(len(self.hash_table.hash_table), 20)

    def test_set_val(self):
        self.hash_table.set_val("value1")
        self.assertEqual(self.hash_table.get_val(hash("value1")), "value1")

    def test_get_val(self):
        self.hash_table.set_val("value2")
        self.assertEqual(self.hash_table.get_val("value2"), "value2")

    def test_multiple_val(self):
        self.hash_table.set_val("Message One")
        self.hash_table.set_val("Message Two")
        self.hash_table.set_val("Message One")

        # get the first element of self.hash_table.hash_table which has length 2
        bucket = [b for b in self.hash_table.hash_table if len(b) == 2][0]
        self.assertEqual(len(bucket), 2)
        self.assertEqual(bucket[0].message, "Message One")
        self.assertEqual(bucket[0].state, MessageStatus.READY)
        self.assertEqual(bucket[1].message, "Message One")
        self.assertEqual(bucket[1].state, MessageStatus.READY)

    def test_get_multiple(self):
        self.hash_table.set_val("Message One")
        self.hash_table.set_val("Message Two")
        self.hash_table.set_val("Message One")

        message = self.hash_table.get_val(hash("Message One"))
        self.assertEqual(message, "Message One")

        bucket = [b for b in self.hash_table.hash_table if len(b) == 2][0]
        self.assertEqual(len(bucket), 2)
        self.assertEqual(bucket[0].message, "Message One")
        self.assertEqual(bucket[0].state, MessageStatus.USED)
        self.assertEqual(bucket[1].message, "Message One")
        self.assertEqual(bucket[1].state, MessageStatus.READY)

        message = self.hash_table.get_val(hash("Message One"))
        self.assertEqual(message, "Message One")

        bucket = [b for b in self.hash_table.hash_table if len(b) == 2][0]
        self.assertEqual(len(bucket), 2)
        self.assertEqual(bucket[1].message, "Message One")
        self.assertEqual(bucket[1].state, MessageStatus.USED)

    def test_delete_message(self):
        self.hash_table.set_val("Message One")
        self.hash_table.set_val("Message Two")
        self.hash_table.set_val("Message One")

        message = self.hash_table.get_val(hash("Message One"))
        self.assertEqual(message, "Message One")

        self.hash_table.delete_val(hash("Message One"))
        
        bucket = [b for b in self.hash_table.hash_table if len(b) == 2][0]
        self.assertEqual(len(bucket), 2)
        self.assertEqual(bucket[0].message, "Message One")
        self.assertEqual(bucket[0].state, MessageStatus.EMPTY)


if __name__ == '__main__':
    unittest.main()
