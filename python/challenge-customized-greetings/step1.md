# Customized Greetings

## Problem Description

You need to write a Python script called `greet.py` that will take in a name and an optional greeting as command line arguments and print out a customized greeting message.

The script should take in the following arguments:

- `--name` (required): the name of the person to greet
- `--greeting` (optional): a custom greeting message to use instead of the default "Hello"

If the `--greeting` argument is not provided, the script should use the default greeting "Hello". If the `--name` argument is not provided, the script should print an error message and exit.

## Example Usage

```bash
python greet.py --name Alice
```

Output: "Hello, Alice!"

```bash
python greet.py --name Bob --greeting "Hi there"
```

Output: "Hi there, Bob!"

```bash
python greet.py --greeting "Hi there"
```

Output: "Error: name argument is required"

## Constraints

- The script should use the `argparse` module to parse command line arguments.
- The script should have proper error handling for when the `--name` argument is not provided.
- The script should have a docstring explaining its usage and inputs/outputs.
