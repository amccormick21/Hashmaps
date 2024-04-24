# Hashmaps

## Introduction
Based on highly technical conversations in a pub while watching football, this repo contains a demo and unit tests of an implementation of an algorithm to pair lines of a list together in a way that ensures a one-to-one relationship between elements of the list.

## Requirements
### Data
The data is loaded from two test files for now, located in the `./data` directory.
Data loading is interfaced so that this could be read from a database or other data source if necessary.
For the purposes of this demo, list one is the `users` and list two is the `messages`.

### Processing
We should develop a method which can return a user-message pair based on the index of the user and a note about how many messages they have previously recieved.

### Output
The user and message are returned from a function.

## Implementation
A `User` and `Message` can be read from files by a `UserList` and a `MessageList` respectively.
A `HashMap` is used to hash and store the messages. This is used so that we can directly index the dictionary, while still being able to randomise access to the messages and therefore provide some level of uniqueness between different users.
Values are extracted from the `HashMap` by querying the value at the `nUserMessageId` location. This value is based on the modulo of the hash of the username, plus an offset based on the number of messages that have previously been sent to the user.
The value of the modulo comes from the number of elements in the hash map, which is equal to the number of messages.

### Properties
We guarantee that the user will recieve every message exactly once before they see a repeated message
As long as there are enough unique messages, we guarantee that the `n`th message seen by any given user will be different than the `n`th message seen by every other user.

### Limitations
This is currently implemented using a single-access pattern - once we have accessed an element once, it can no longer be used. This means that a single message can never be sent to multiple users, and we therefore burn through the number of available messages very quickly.
We cannot "release" messages to be sent to other users.
There is not enough depth in the current solution to prevent users from seeing specific messages - namely, their own.

## Running
To run the code, follow the following steps:
1. Clone the repo: `git clone https://github.com/amccormick21/HashMaps`
2. Run `make` in the root of the repository to run the tests. One of these will print out a sample of what the messages would have been for this set of users
