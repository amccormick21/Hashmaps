
from enum import Enum
from message_table.message_interfaces import UserListInterface, MessageListInterface
from message_table.message_data import UserList, MessageList

class UserMessage:
    def __init__(self, user, message):
        self.user = user
        self.message = message

class MessageStatus(Enum):
    READY = 1
    USED = 2
    EMPTY = 3

class MessageElement:
    def __init__(self, message, state: MessageStatus):
        self.message = message
        self.state = state

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]
    
    def convert_hashed_key(self, key):
        # If the key is a string, hash it and mod by the size
        # If the key is an int, mod by the size
        if isinstance(key, str):
            return hash(key) % self.size
        elif isinstance(key, int):
            return key % self.size
        else:
            raise ValueError("Invalid key type")

    def set_val(self, val):
        hashed_key = hash(val) % self.size
        bucket = self.hash_table[hashed_key]
        
        # If the bucket is empty, append the value to the hash table
        if not bucket:
            bucket.append(MessageElement(val, MessageStatus.READY))
            return
        
        # If the bucket contains a value
        for record in bucket:
            if record.state == MessageStatus.EMPTY:
                record.message = val
                record.state = MessageStatus.READY
                found_key = True
                return

        # If we get to here then the bucket does not have any empty slots
        bucket.append(MessageElement(val, MessageStatus.READY))

    def get_val(self, key):
        hashed_key = self.convert_hashed_key(key)
        starting_key = hashed_key
        bucket = self.hash_table[hashed_key]

        while hashed_key != starting_key - 1:
            for record in bucket:
                if record.state == MessageStatus.READY:
                    record.state = MessageStatus.USED
                    return record.message
            hashed_key = (hashed_key + 1) % self.size
            bucket = self.hash_table[hashed_key]
            
        raise KeyError("Could not return a message as there are none left in the bucket")

    def delete_val(self, key):
        hashed_key = self.convert_hashed_key(key)
        bucket = self.hash_table[hashed_key]
        for record in bucket:
            if record.state != MessageStatus.READY:
                record.state = MessageStatus.EMPTY
                return
            
class DataCache:
    def __init__(self, user_list: UserListInterface, message_list: MessageListInterface):
        self.users = user_list
        self.messages = message_list
        self.message_hash_table = HashTable(self.messages.size())
        self.hash_messages()

    def hash_messages(self):
        [self.message_hash_table.set_val(m) for m in self.messages.get_all_messages()]

    def get_user_message(self, nUserId, nMessage):
        user = self.users.get_user(nUserId)
        nUserMessageId = (user.get_hash() + nMessage)
        return UserMessage(user, self.message_hash_table.get_val(nUserMessageId))
    
    def get_message_table(self):
        # The number of weeks we can run is the size of the messages divided by the size of the users, rounded down
        nWeeks = self.messages.size() // self.users.size()
        
        # For each week, evaluate the messages for the users
        messages = [[] for _ in range(0, self.users.size())]
        for nUser in range(0, self.users.size()):
            messages[nUser] = [self.get_user_message(nUser, nWeek) for nWeek in range(0, nWeeks)]

        return messages
    
    def pretty_print_message_table(self):
        """ Print a table with the user names as rows, and the weeks as columns. The cells represent the message[nUser][nWeek]
        which will be allocated to the user at this week"""
        messages = self.get_message_table()
        message_widths = []
        # Find the maximum width of a message in the nth week
        for iWeek in range(0, len(messages[0])):
            message_widths.append(max([len(str(message[iWeek].message)) for message in messages]))
        name_widths = [len(str(user)) for user in self.users.get_all_users()]

        print()
        print()

        for nUser in range(0, self.users.size()):
            print(self.users.get_user(nUser), end=" " * (max(name_widths) - len(str(self.users.get_user(nUser))) + 2))
            for nWeek in range(0, len(messages[nUser])):
                print(messages[nUser][nWeek].message, end=" " * (max(message_widths) - len(str(messages[nUser][nWeek].message)) + 2))
            print()

if __name__ == "__main__":
    data = DataCache(UserList(), MessageList())
    data.pretty_print_message_table()