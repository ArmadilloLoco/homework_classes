class Student:
    def __init__(self, name: str, surname: str, gender: str):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_mentor(self, mentor: object, course: str, grade: int): # rate lecturer
        if isinstance(mentor, Lecturer) and course in mentor.courses_attached and course in self.courses_in_progress:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self): # average grade
        total_grades = list()
        for grades in self.grades.values():
            total_grades.append(grades)
        return sum(grades) / len(grades)
    
    def __str__(self): # student info
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg_grade()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, other): # compare students
        if isinstance(other, Student):
            return self.avg_grade() == other.avg_grade()


class Mentor:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self): # average grade
        total_grades = list()
        for grades in self.grades.values():
            total_grades.append(grades)
        return sum(grades) / len(grades)
    
    def __str__(self):  # lecturer info
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_grade()}'
    
    def __eq__(self, other): # compare lecturers
        if isinstance(other, Lecturer):
            return self.avg_grade() == other.avg_grade()
            
class Reviewer(Mentor): 
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)

    def rate_hw(self, student: object, course: str, grade: int): # rate student
        print(type(student), type(course), type(grade))
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self): # reviewer info
        return f'Имя: {self.name} \nФамилия: {self.surname}'


def avg_total(person_list: list, course: str): # average grades for students and lecturers
    grades = list()
    for person in person_list:
        if course in person.grades:
            grades += person.grades[course]
    return sum(grades) / len(grades)
    

student_1 = Student('Ruoy', 'Eman', 'm')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']
student_1.grades = {"Python": [10, 9, 8]}

student_2 = Student('Ivan', 'Ivanov', 'm')
student_2.courses_in_progress += ['Python']
student_2.grades = {"Python": [7, 6, 5]}
 
lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']
lecturer_1.grades = {"Python": [10, 9, 8]}

lecturer_2 = Lecturer('Petr', 'Petrov')
lecturer_2.courses_attached += ['Python']
lecturer_2.grades = {"Python": [10, 9, 8]}
 
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_2 = Reviewer('Petr', 'Petrov')

# Информация о студентах и лекторах
print(f'ПРОВЕРЯЮЩИЙ \n{reviewer_1}') 
print(f'ЛЕКТОР \n{lecturer_1}')
print(f'СТУДЕНТ \n{student_1}')

# Сравнение студентов и лекторов по среднему балу
print(student_1.avg_grade() < student_2.avg_grade())
print(lecturer_1.avg_grade() == lecturer_2.avg_grade())

# Подсчет средней оценки студентов по курсу Python
print(avg_total([student_1, student_2], 'Python'))
print(avg_total([lecturer_1, lecturer_2], 'Python'))
