class UserListInterface:
    def size(self):
        raise NotImplementedError("The size method must be implemented for a UserList")

    def get_user(self, index):
        raise NotImplementedError("The get_user method must be implemented for a User")

    def get_all_users(self):
        raise NotImplementedError("The get_all_users method must be implemented for a User")

class MessageListInterface:
    def size(self):
        raise NotImplementedError("The size method must be implemented for a MessageList")

    def get_message(self, index):
        raise NotImplementedError("The get_message method must be implemented for a MessageList")

    def get_all_messages(self):
        raise NotImplementedError("The get_all_messages method must be implemented for a MessageList")