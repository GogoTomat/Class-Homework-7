class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grade:
                lecturer.grade[course] += grade
            else:
                lecturer.grade[course] = grade

    def avg_grade(self):
        my_list = []
        for grade in self.grades.values():
            for mark in grade:
                my_list.append(mark)
        stud_avg = sum(my_list) / len(my_list)
        return stud_avg

    def avg_grade_course(students, course):
        my_list = []
        for student in students:
            if student.grades.get(course) != None:
                for kurs in student.grades.get(course):
                    my_list.append(course)
            else:
                pass
        avg_grade_course = sum(my_list) / len(my_list)
        return avg_grade_course


    def __str__(self):
        print("Name: ", self.name)
        print("Surname: ", self.surname)
        print("Average grade: ", self.avg_grade())
        print("Courses in progress: ", self.courses_in_progress)
        print("Finished courses: ", self.finished_courses)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a student")
        else:
            return self.avg_grade() < other.avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


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
        print("Name: ", self.name)
        print("Surname: ", self.surname)


class Lecturer (Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}

    def lec_avg_grade(self):
        my_list = []
        for grade in self.grades.values():
            for mark in grade:
                my_list.append(mark)
        lec_avg = sum(my_list) / len(my_list)
        return lec_avg

    def __str__(self):
        print("Name: ", self.name)
        print("Surname: ", self.surname)
        print("Average grade: ", self.lec_avg_grade())

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a lecturer.")
        else:
            return self.lec_avg_grade() < other.lec_avg_grade()

    def lec_avg_grade_kurs(lecturers, course):
        my_list = []
        for lecturer in lecturers:
            if lecturer.grades.get(course) != None:
                for kurs in lecturer.grades.get(course):
                    my_list.append(course)
            else:
                pass
            lec_avg_grade_course = sum(my_list) / len(my_list)
            return lec_avg_grade_course


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']


cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
lk = Lecturer("Biba", 'Boba')

print(best_student.grades)
