```python
# TODO: Add and parse the arguments.
group.add_argument('-a', '--add', nargs=2, type=int, metavar=('NUM1', 'NUM2'), help='add NUM1 and NUM2')
group.add_argument('-s', '--subtract', nargs=2, type=int, metavar=('NUM1', 'NUM2'), help='subtract NUM2 from NUM1')
group.add_argument('-m', '--multiply', nargs=2, type=int, metavar=('NUM1', 'NUM2'), help='multiply NUM1 and NUM2')
group.add_argument('-d', '--divide', nargs=2, type=int, metavar=('NUM1', 'NUM2'), help='divide NUM1 by NUM2')
args = parser.parse_args()
```
