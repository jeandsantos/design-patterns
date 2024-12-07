class Person:
    def __init__(self, name: str | None = None):
        if name is None:
            name = "Unknown"
        self.name: str | None = name

        self.street_address: str | None = None
        self.post_code: str | None = None
        self.city: str | None = None

        self.company_name: str | None = None
        self.position: str | None = None
        self.annual_income: int | None = None

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Address: {self.street_address}, {self.post_code}, {self.city}\n"
            + f"Employed at {self.company_name} as a {self.position} earning {self.annual_income}"
        )

    def __repr__(self):
        return f"Person({self.name!r})"


class PersonBuilder:
    def __init__(self, person: Person = Person()):
        self.person: Person = person

    @property
    def known(self):
        return PersonDetailsBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonDetailsBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    def by(self, name: str):
        self.person.name = name
        return self


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    def at(self, company_name: str):
        self.person.company_name = company_name
        return self

    def as_a(self, position: str):
        self.person.position = position
        return self

    def earning(self, annual_income: int):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    def at(self, street_address: str):
        self.person.street_address = street_address
        return self

    def with_post_code(self, post_code: str):
        self.person.post_code = post_code
        return self

    def in_city(self, city: int):
        self.person.city = city
        return self


def main():
    person_builder = PersonBuilder()
    person = (
        person_builder.known.by("Jane Smith")
        .lives.at("123 London Road")
        .with_post_code("SW1 1GB")
        .in_city("London")
        .works.at("Fabrikam")
        .as_a("Engineer")
        .earning(123_000)
        .build()
    )
    print(repr(person))
    print(person)


if __name__ == "__main__":
    main()
