from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectur(self, lectur, course, grade):
        if 0 <= grade <= 10:
            if isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress:
                if course in lectur.grades:
                    lectur.grades[course] += [grade]
                else:
                    lectur.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def mean_grade(self):
        if len(self.grades) != 0:
            return round(sum(mean(grade) for grade in self.grades.values()) / len(self.grades), 1)
        else:
            return 'Нет оценок'

    def __str__(self):
        return f'''
    Имя: {self.name}
    Фамилия: {self.surname}
    Средняя оценка за домашние задания: {self.mean_grade()}
    Курсы в процессе изучения: {' '.join(self.courses_in_progress)}
    Завершенные курсы: {' '.join(self.finished_courses)}
    '''

    def __gt__(self, other):
        return self.mean_grade() > other
    def __lt__(self, other):
        return self.mean_grade() < other
    def __ge__(self, other):
        return self.mean_grade() >= other
    def __le__(self, other):
        return self.mean_grade() <= other
    def __eq__(self, other):
        return self.mean_grade() == other
    def __ne__(self, other):
        return self.mean_grade() != other


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def mean_grade(self):
        if len(self.grades) != 0:
            return round(sum(mean(grade) for grade in self.grades.values()) / len(self.grades), 1)
        else:
            return 'Нет оценок'

    def __str__(self):
        return f'''
   Имя: {self.name}
   Фамилия: {self.surname}
   Средняя оценка за лекции: {self.mean_grade()}
   '''

    def __gt__(self, other):
        return self.mean_grade() > other
    def __lt__(self, other):
        return self.mean_grade() < other
    def __ge__(self, other):
        return self.mean_grade() >= other
    def __le__(self, other):
        return self.mean_grade() <= other
    def __eq__(self, other):
        return self.mean_grade() == other
    def __ne__(self, other):
        return self.mean_grade() != other


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
'''


def calculat_average_grade_for_course(students, name_course):
    total = 0
    mean_grade = 0
    for student in students:
        for course, grade in student.grades.items():
            if course == name_course:
                total += len(grade)
                mean_grade += sum(grade)
    return round(mean_grade / total, 1)

def calculat_average_grade_for_lecture(lectors, name_lecture):
    total = 0
    mean_grade = 0
    for lector in lectors:
        for lecture, grade in lector.grades.items():
            if lecture == name_lecture:
                total = len(grade)
                mean_grade += sum(grade)
    return round(mean_grade / total, 1)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Algebra']

worst_student = Student('Dima', 'Pudlo', 'male')
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Algebra']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Algebra']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Algebra', 10)
cool_mentor.rate_hw(worst_student, 'Algebra', 2)

lestor = Lecturer('Ivan', 'Susanin')
lestor.courses_attached += ['Algebra']
lestor.courses_attached += ['Python']


best_student.rate_lectur(lestor, 'Algebra', 5)
best_student.rate_lectur(lestor, 'Python', 10)
worst_student.rate_lectur(lestor, 'Algebra', 6)
worst_student.rate_lectur(lestor, 'Python', 7)

print(lestor.grades)
print(lestor)
print(best_student)
print(worst_student)
print(best_student > worst_student)

all_student = [best_student, worst_student]
all_lestor = [lestor]

print(lestor.grades)
print(calculat_average_grade_for_course(all_student, 'Algebra'))
print(calculat_average_grade_for_lecture(all_lestor, 'Algebra'))