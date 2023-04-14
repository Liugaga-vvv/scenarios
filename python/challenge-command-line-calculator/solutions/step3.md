```python
# TODO: Output management.
if args.add:
    result = add(*args.add)
    print(f"{args.add[0]} + {args.add[1]} = {result}")
elif args.subtract:
    result = subtract(*args.subtract)
    print(f"{args.subtract[0]} - {args.subtract[1]} = {result}")
elif args.multiply:
    result = multiply(*args.multiply)
    print(f"{args.multiply[0]} * {args.multiply[1]} = {result}")
elif args.divide:
    result = divide(*args.divide)
    print(f"{args.divide[0]} / {args.divide[1]} = {result}")
else:
    parser.print_help()
```
