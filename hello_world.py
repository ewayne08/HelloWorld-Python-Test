class HelloWorld:
    def __init__(self):
        print("HelloWorld object created!")

    def say_hello(self):
        print("Hello, World!")


if __name__ == "__main__":
    hw = HelloWorld()   # Create an instance of HelloWorld
    hw.say_hello()      # Call the method
