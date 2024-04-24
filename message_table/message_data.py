from message_table.message_interfaces import UserListInterface, MessageListInterface

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email
    
    def get_hash(self):
        return hash(self.name)

    def __str__(self):
        return f'{self.name} <{self.email}>'

class UserList(UserListInterface):
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        with open('data/users.txt', 'r') as file:
            user_data = file.read().splitlines()
        users = []
        for data in user_data:
            name, email = data.split(',')
            user = User(name, email)
            users.append(user)
        return users

    def get_all_users(self):
        return self.users

    def get_user(self, index):
        if 0 <= index < len(self.users):
            return self.users[index]
        else:
            return None

    def size(self):
        return len(self.users)

class Message:
    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message
    
    def get_hash(self):
        return hash(self.message)

    def __str__(self):
        return self.get_message()

class MessageList(MessageListInterface):
    def __init__(self):
        self.messages = self.load_messages()

    def load_messages(self):
        with open('data/messages.txt', 'r') as file:
            messages = [Message(line.rstrip()) for line in file]
        return messages

    def get_all_messages(self):
        return self.messages

    def get_message(self, index):
        if 0 <= index < len(self.messages):
            return self.messages[index]
        else:
            return None

    def size(self):
        return len(self.messages)