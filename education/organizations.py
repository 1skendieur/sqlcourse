import csv

class School:
    def __init__(self, name, address, phone, num_stud, num_teachers):
        self.name = name
        self.address = address
        self.phone = phone
        self.num_stud = num_stud
        self.num_teachers = num_teachers
        self.students = []
        self.teachers = []

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone

    def set_num_stud(self, num_stud):
        self.num_stud = num_stud

    def set_num_teachers(self, num_teachers):
        self.num_teachers = num_teachers

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def get_info(self):
        return {
            'Name': self.name,
            'Address': self.address,
            'Phone': self.phone,
            'Number of Students': self.num_stud,
            'Number of Teachers': self.num_teachers
        }

    def get_report(self):
        with open('school_report.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['School Info'])
            writer.writerow(['Name', 'Address', 'Phone', 'Number of Students', 'Number of Teachers'])
            writer.writerow([self.name, self.address, self.phone, self.num_stud, self.num_teachers])
            writer.writerow([''])
            writer.writerow(['Students'])
            writer.writerow(['Name', 'Family Name', 'Age', 'Gender', 'Nationality', 'Subjects Taken'])
            for student in self.students:
                writer.writerow([student.name, student.familyname, student.age, student.gender, student.nationality, ', '.join(student.subjects_taken)])
            writer.writerow([''])
            writer.writerow(['Teachers'])
            writer.writerow(['Name', 'Family Name', 'Age', 'Gender', 'Nationality', 'Subjects Taught'])
            for teacher in self.teachers:
                writer.writerow([teacher.name, teacher.familyname, teacher.age, teacher.gender, teacher.nationality, ', '.join(teacher.subjects_taught)])
