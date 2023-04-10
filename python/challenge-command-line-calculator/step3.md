# Output Management

After the last step, you have a working calculator. However, the output is not very user-friendly. You need to improve the output management.

## TODO

- Improve the output management.

## Requirements

- Use the `print()` function to print the result.
- If the user uses the `--add` argument, print the result in the following format:
  `{arg1} + {arg2} = {result}`.
- If the user uses the `--subtract` argument, print the result in the following format:
  `{arg1} - {arg2} = {result}`.
- If the user uses the `--multiply` argument, print the result in the following format:
  `{arg1} * {arg2} = {result}`.
- If the user uses the `--divide` argument, print the result in the following format:
  `{arg1} / {arg2} = {result}`.
- The `arg1`, `arg2`, and `result` should be replaced with the actual values and there should be sapces before and after the `+` , `-` , `*` , `/` and `=` signs.

## Tests

You can test your calculator by running the following commands:

```bash
python3 calculator.py -a 1 2
python3 calculator.py -s 1 2
python3 calculator.py -m 1 2
python3 calculator.py -d 1 2
```

The output should be:

```bash
1 + 2 = 3
1 - 2 = -1
1 * 2 = 2
1 / 2 = 0.5
```

## Hints

- The `-a` , `-s` , `-m` , and `-d` arguments are the arguments that you added in the previous step.You can replace them with `--add` , `--subtract` , `--multiply` , and `--divide` arguments.
- The `1` and `2` are the operands that you want to use in the calculation. You can replace them with any numbers.There should be a space between the arguments and the operands.
