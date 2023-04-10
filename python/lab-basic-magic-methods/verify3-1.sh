cd /home/labex/project
python -c 'from person import Person;p = Person("Alice", 30);del p'
cat person.py | grep -E "__del__"
