from abc import ABC, abstractmethod
import uuid


class Person(ABC):
    def __init__(self, name, surname, date_of_birthday, patronymic_name='', *args, **kwargs):
        self.__name = ''
        self.__surname = ''
        self.__patronymic_name = ''
        self.__date_of_birthday = None


class Student(Person):
    def __init__(self, name, surname, date_of_birthday, patronymic_name='', *args, **kwargs):
        super().__init__(name, surname, date_of_birthday, patronymic_name='', *args, **kwargs)
        self.id = uuid.uuid4()

    def __str__(self):
        pass


class Teacher(Person):
    def __init__(self, name, surname, date_of_birthday, patronymic_name='', *args, **kwargs):
        super().__init__(name, surname, date_of_birthday, patronymic_name='', *args, **kwargs)
        self.id = uuid.uuid4()


class Course:
    def __init__(self, title, ed_program, credits, lectures=0, practices=0, labs=0, ind_works=0, *args, **kwargs):
        if credits*30 != lectures + practices + labs + ind_works:
            pass

        self.__title = title
        self.__credits = 0
        self.__lectures = 0
        self.__practices = 0
        self.__labs = 0
        self.__ind_works = 0
        self.__teachers = {}
        self.id = uuid.uuid4()
        self.__ed_program = None

    @property
    def title(self):
        return self.__title

    def append_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            pass
        self.__teachers[teacher.id] = teacher


class StudentPlan:
    def __init__(self, student):
        self.__student = student
        self.__courses = {}

    def course_append(self, course, semester, progress=-1):
        self.__courses[course.id] = (course, semester, progress)

    def __str__(self):
        res = ''
        for i in self.__courses:
            course, semester, progress = self.__courses[i]
            res += f'{course.title}, semester: {semester}, {progress}\n'
        return res



if __name__ == '__main__':
    student1 = Student('NAME', 'SURNAME', '12.12.2000')
    student2 = Student('NAME1', 'SURNAME2', '12.12.1000')

    teacher = Teacher('N1', 'S1', '12.10.1980')

    course1 = Course('OOP', 'CS', 5, 30, 30, 30, 60)
    course1.append_teacher(teacher)

    course2 = Course('OOP2', 'CS2', 5, 30, 30, 30, 60)
    course2.append_teacher(teacher)

    student_plan1 = StudentPlan(student1)
    student_plan1.course_append(course1, 1, 90)

    print(student_plan1)