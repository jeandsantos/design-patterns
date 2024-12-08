import copy


class Address:
    def __init__(self, street_address: str, floor: int, country: str):
        self.street_address = street_address
        self.floor = floor
        self.country = country

    def __str__(self):
        return f"{self.street_address}, Floor {self.floor}, {self.country}"


class Employee:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} works at {self.address}"


class EmployeeFactory:
    main_office_employee = Employee("", Address("123 London Road", 0, "UK"))
    branch_office_employee = Employee("", Address("456 Baker Street", 0, "UK"))

    @staticmethod
    def __new_employee(prototype: Employee, name: str, floor: int) -> Employee:
        new_employee = copy.deepcopy(prototype)
        new_employee.name = name
        new_employee.address.floor = floor
        return new_employee

    @staticmethod
    def new_main_office_employee(name: str, floor: int) -> Employee:
        return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee, name, floor)

    @staticmethod
    def new_branch_office_employee(name: str, floor: int) -> Employee:
        return EmployeeFactory.__new_employee(EmployeeFactory.branch_office_employee, name, floor)


def main():
    john = EmployeeFactory.new_main_office_employee("John", 3)
    jane = EmployeeFactory.new_branch_office_employee("Jane", 10)

    print(john)
    print(jane)


if __name__ == "__main__":
    main()
    # output:
    # John works at 123 London Road, Floor 3, UK
    # Jane works at 456 Baker Street, Floor 10, UK
