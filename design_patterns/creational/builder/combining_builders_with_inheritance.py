class Person:
    def __init__(self):
        self.name: str | None = None
        self.date_of_birth: str | None = None
        self.profession: str | None = None

    def __str__(self):
        return f"Name: {self.name}\nDate of birth: {self.date_of_birth}\nEmployed as a {self.profession}"

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person: Person = Person()

    def build(self):
        return self.person


class PersonNameBuilder(PersonBuilder):
    def called(self, name: str):
        self.person.name = name
        return self


class PersonProfessionBuilder(PersonNameBuilder):
    def works_as_a(self, profession: str):
        self.person.profession = profession
        return self


class PersonDateOfBirthBuilder(PersonProfessionBuilder):
    def born_on(self, date_of_birth: str):
        self.person.date_of_birth = date_of_birth
        return self


person_builder = PersonDateOfBirthBuilder()


def main():
    person = person_builder.called("Jane Smith").works_as_a("Accountant").born_on("01/01/1999").build()
    print(person)


if __name__ == "__main__":
    main()
    # output:
    # Name: Jane Smith
    # Date of birth: 01/01/1999
    # Employed as a Accountant
