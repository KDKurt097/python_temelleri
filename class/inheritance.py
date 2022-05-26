
# İnheritance (Kalıtım): Miras alma # Örneğin animal classının özellikleri olucak ve bu özellikler aynı şekilde dog ve cat classında da olucak ama bu classların ayrı bir şekilde kendilerine hal özellikleri de olacak

class Person():
    def __init__(self):
        print("Person created.")

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        print("Student created.") 

s1 = Student()
        



