class User:
    # constructor method to initialize the attributes of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    user1 = User("Alice", 30)
    print(user1)  # Output: <__main__.User object at 0x...>
    print(user1.name)  # Output: Alice
    print(user1.age)   # Output: 30
    #user2 = User()
    #print(user2)  # Output: <__main__.User object at 0x...>


