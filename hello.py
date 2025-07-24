def get_hello_message():
    print('Hello friends how are you')
    return "Hello, World!"

def print_hello():
    message = get_hello_message()
    print(message)

if __name__ == "__main__":
    print_hello()