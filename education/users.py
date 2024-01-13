class Human:
    def __init__(self, name, familyname, age, gender, nationality):
        self.name = name
        self.familyname = familyname
        self.age = age
        self.gender = gender
        self.nationality = nationality

    def set_name(self, name):
        self.name = name

    def set_family(self, familyname):
        self.familyname = familyname

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_nationality(self, nationality):
        self.nationality = nationality

    def get_info(self):
        return {
            'Name': self.name,
            'Family Name': self.familyname,
            'Age': self.age,
            'Gender': self.gender,
            'Nationality': self.nationality
        }

class Student(Human):
    def __init__(self, name, familyname, age, gender, nationality):
        super().__init__(name, familyname, age, gender, nationality)
        self.school_name = None
        self.subjects_taken = []

    def set_school(self, school_name):
        self.school_name = school_name

    def add_subject(self, subject):
        self.subjects_taken.append(subject)

class Teacher(Human):
    def __init__(self, name, familyname, age, gender, nationality):
        super().__init__(name, familyname, age, gender, nationality)
        self.school_name = None
        self.subjects_taught = []

    def set_school(self, school_name):
        self.school_name = school_name

    def add_subject(self, subject):
        self.subjects_taught.append(subject)
