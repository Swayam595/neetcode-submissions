class Person:
    def __init__(self, lastName: str, age: int, married: bool):
        self.lastName = lastName
        self.age = age
        self.married = married

    def getLastName(self) -> str:
        return self.lastName

    def getAge(self) -> int:
        return self.age

    def isMarried(self) -> bool:
        return self.married

class PersonFilter(Protocol):
    def apply(self, person: Person) -> bool:
        ...

class AdultFilter(PersonFilter):
    # Implement Adult filter
    def apply(self, person: Person) -> bool:
        return 18 <= person.getAge()

class SeniorFilter(PersonFilter):
    # Implement Senior filter
    def apply(self, person: Person) -> bool:
        return 65 <= person.getAge()

class MarriedFilter(PersonFilter):
    # Implement Married filter
    def apply(self, person: Person) -> bool:
        return person.isMarried()

class PeopleCounter:
    def __init__(self):
        self.filter: PersonFilter = None

    def setFilter(self, filter: PersonFilter) -> None:
        self.filter = filter

    def count(self, people: List[Person]) -> int:
        # Implement method here
        numuber_of_person = 0

        for i in range(len(people)):
            person = people[i]

            if self.filter.apply(person):
                numuber_of_person += 1
        
        return numuber_of_person
    
