'''
Middle test
'''

from abc import ABC, abstractmethod
import uuid


class DuplicateError(Exception):
    pass


class Factory:
    '''
    Represents Factory class
    '''
    def __init__(self):
        self.employee_list = []

    def sort_employee(self):
        '''
        Sorts employee list by descending month salary

        :return: list
        '''
        return self.employee_list.sort(key=lambda x: x.month_salary, reverse=True)

    def new_employee(self, func):
        '''
        Adds new employee to Factory list

        :param func: employee type(Hourly, Fixed)
        :return: employee
        '''
        if not isinstance(func, (Hourly, Fixed)):
            raise TypeError(f"'{type(func).__name__}' cannot be interpreted as Employee object")
        for i in self.employee_list:
            if func.Id == i.Id:
                raise DuplicateError('Duplicate id')
        self.employee_list.append(func)
        return func

    def __str__(self):
        '''
        :return: Factory employees
        '''
        lst = ''
        for i in self.employee_list:
            lst += f'{str(i)}\n\n'
        return lst


class Employee(ABC):
    '''
    Represents Employee object
    '''
    def __init__(self, name, surname, phone, salary):
        '''
        Initialize Employee object

        :param name: str
        :param surname: str
        :param phone: str
        :param salary: int, float
        '''
        if not isinstance(name, str):
            raise TypeError(f"'{type(name).__name__}' object cannot be interpreted as a name of employee")
        if not isinstance(surname, str):
            raise TypeError(f"'{type(surname).__name__}' object cannot be interpreted as a surname of employee")
        if not isinstance(phone, str):
            raise TypeError(f"'{type(phone).__name__}' object cannot be interpreted as a phone-number of employee")
        if not isinstance(salary, (int, float)):
            raise TypeError(f"'{type(salary).__name__}' object cannot be interpreted as a salary of employee")

        if not name:
            raise ValueError(f'Employee cannot be without name')
        if not surname:
            raise ValueError(f'Employee cannot be without surname')
        if not phone:
            raise ValueError(f'Employee cannot be without phone-number')
        if not salary or salary <= 0:
            raise ValueError(f'Employee`s salary can only be a positive number')

        self.name = name
        self.surname = surname
        self.Id = uuid.uuid4()
        self.phone = phone
        self.salary = salary
        self.month_salary = self.average_month_salary()

    @abstractmethod
    def average_month_salary(self):
        '''
        :return: float, int
        '''
        pass

    def __str__(self):
        '''
        :return: Employee info
        '''
        return f'Fullname: {self.name+" "+self.surname}\nID: {self.Id}\nPhone: {self.phone}\nSalary: {self.month_salary}'


class Hourly(Employee):
    '''
    Represents Hourly-payed type of Employee
    '''
    def average_month_salary(self):
        return 20.8 * 8 * self.salary


class Fixed(Employee):
    '''
    Represents Monthly-payed type of Employee
    '''
    def average_month_salary(self):
        return self.salary


if __name__ == '__main__':
    Factory1 = Factory()

    Factory1.new_employee(Hourly('emp1', 'emp1', '095', 15))
    Factory1.new_employee(Fixed('emp2', 'emp2', '095', 1500))
    Factory1.new_employee(Hourly('emp3', 'emp3', '095', 17))
    Factory1.new_employee(Fixed('emp4', 'emp4', '095', 2000))
    Factory1.new_employee(Hourly('emp5', 'emp5', '095', 16))
    Factory1.new_employee(Fixed('emp6', 'emp6', '095', 1600))

    Factory1.sort_employee()
    print(Factory1)