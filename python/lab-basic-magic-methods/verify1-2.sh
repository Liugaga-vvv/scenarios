cd /home/labex/project
python -c 'from person import Person;p=Person("Alice", 30);print(p)'
cat person.py | grep "__str__"
