'''
Second task from oop lab 5
'''
from abc import ABC


class Teacher:
    '''
    Represents Teacher class
    '''
    def __init__(self, name, course):
        '''
        Initialize Teacher object

        :param name: str
        :param course: Course
        '''
        if not isinstance(name, str):
            raise ValueError(f'Name cant be represented as {type(name).__name__} type')
        if not isinstance(course, Course):
            raise ValueError(f'Course cant be represented as {type(course).__name__} type')
        self._name = name
        self._course = course
        self.attach_to_course(course)

    @property
    def name(self):
        '''
        :return: str
        '''
        return self._name

    def attach_to_course(self, course):
        '''
        Attaches teacher to created course

        :param course: Course
        :return: None
        '''
        course.teacher.append(self)

    def __str__(self):
        '''
        :return: Teacher info
        '''
        return f'Name: {self._name}\nCourse: {self._course.title}'


class Course(ABC):
    '''
    Represents Course class
    '''
    def __init__(self, title, course_program):
        '''
        Initialize Course object

        :param title: str
        :param course_program: list
        '''
        if not isinstance(title, str):
            raise ValueError(f'Title cant be represented as {type(title).__name__} type')
        if not isinstance(course_program, list):
            raise ValueError(f'Course program cant be represented as {type(course_program).__name__} type')
        self._title = title
        self._course_program = course_program
        self._teacher = []
        self._type = ''

    @property
    def title(self):
        '''
        :return: str
        '''
        return self._title

    @property
    def teacher(self):
        '''
        :return: Teacher
        '''
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        '''

        :param value:
        :return:
        '''
        self._teacher = value

    def __str__(self):
        '''
        :return: Info about course
        '''
        teachers = ''
        for i in self._teacher:
            teachers += i.name+'; '
        return f'Title: {self._title}\nTeachers: {teachers}\nCourse program: {self._course_program}'


class ILocalCourse(Course):
    '''
    Represents ILocalCourse class
    '''
    def __init__(self, title, course_program):
        super().__init__(title, course_program)
        self._type = 'local'

    def __str__(self):
        return f'{super().__str__()}\nType: {self._type}'


class IOffsiteCourse(Course):
    '''
    Represents IOffsiteCourse class
    '''
    def __init__(self, title, course_program):
        super().__init__(title, course_program)
        self._type = 'offsite'

    def __str__(self):
        return f'{super().__str__()}\nType: {self._type}'


class CourseFactory:
    '''
    Factory for creating courses for software academy
    '''
    def __init__(self):
        self._courses_list = []

    @property
    def courses_list(self):
        '''
        All courses of software academy

        :return: list
        '''
        return self._courses_list

    def create_course(self, title, course_program, teacher_names, _type):
        '''
        Creates course for software academy

        :param title: str
        :param course_program: list
        :param teacher_names: list
        :param _type: str
        :return: Course
        '''
        if _type == 'local':
            course = ILocalCourse(title, course_program)
        elif _type == 'offsite':
            course = IOffsiteCourse(title, course_program)
        else:
            raise ValueError('Wrong type')
        teachers = []
        for i in teacher_names:
            teachers.append(Teacher(i, course))
        self._courses_list.append(course)
        return course


if __name__ == '__main__':
    soft_academy1 = CourseFactory()
    soft_academy1.create_course('Math', ['Topic1', 'Topic2', 'Topic3'], ['Teacher Name'], 'local')
    soft_academy1.create_course('OOP', ['Inh', 'Pol', 'Log'], ['T O', 'T S'], 'local')
    soft_academy1.create_course('Comp. Math', ['Linear Programming', 'Duality in LP'],
                                ['Teacher1', 'Teacher2', 'Teacher3', 'Teacher4', 'Teacher5'], 'offsite')

    for i in soft_academy1.courses_list:
        print(i, '\n')

