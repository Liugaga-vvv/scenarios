from faker import Faker

from person import Person


def fake_person_list(number_of_person) -> list:
    fake = Faker()
    people = [Person(fake.name(), fake.random_int(min=1, max=100), fake.email()) for _ in range(5)]
    # Sort people by age
    people.sort(key=lambda person: person.getAge())
    return people
