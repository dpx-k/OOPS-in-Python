class Student:

    college_name = "Presidency University"

    def __init__(self, name, age): 
        self.name = name
        self.age = age
        self.course = coursef

    def print_details(self): 
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", self.college_name, "\n")
    
    @classmethod
    def change_college(cls):
        cls.college_name = "Aerva University"

    @staticmethod
    def is_adult(age): 
       return age >= 18
    
    class Address: 
        def __init__(self, city, state): 
            self.city = city 
            self.state = state
        
        def get_address(self): 
            return self.city, self.state
    
    class Course: 
        def __init__(self, student):
            self.student = student
            
        def get_info(self): 
            self.student.print_details()

student1 = Student("Deepak", 18)
student1.print_details()

student1.change_college()
student1.print_details()

address = Student.Address("Bengaluru", "Karnataka")
print("Address:", address.get_address(), "\n")

course = Student.Course(student1)
print("Course Student Info:", course.get_info())