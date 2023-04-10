# Solution

import argparse

def greet(name: str, greeting: str = "Hello") -> str:
    """
    Generates a customized greeting message.
    
    Args:
    - name: a string representing the name of the person to greet
    - greeting: an optional string representing a custom greeting message
    
    Returns:
    - a string representing the customized greeting message
    """
    return f"{greeting}, {name}!"

def main():
    """
    Parse command line arguments and generate a customized greeting message.
    """
    parser = argparse.ArgumentParser(description='Generate a customized greeting message.')
    parser.add_argument('--name', required=True, help='The name of the person to greet')
    parser.add_argument('--greeting', help='A custom greeting message to use instead of the default "Hello"')
    args = parser.parse_args()
    
    name = args.name
    greeting = args.greeting if args.greeting else "Hello"
    
    print(greet(name, greeting))

if __name__ == '__main__':
    main()