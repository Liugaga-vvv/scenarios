cd /home/labex/project
python -c 'from person import Person;p1 = Person("Alice", 30);p2 = Person("Bob", 35);p1 == p2;p1 != p2'
cat person.py | grep -E "__eq__|__ne__"
