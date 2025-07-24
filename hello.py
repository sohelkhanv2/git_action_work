def get_hello_message():
    return "Hello, World!"

def print_hello():
    message = get_hello_message()
    print(message)

if __name__ == "__main__":
    print_hello()