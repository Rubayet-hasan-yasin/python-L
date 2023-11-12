class Person:
    def __init__(self, name:str, DOB, ht:int):
        self.__name = name
        self.DOB = DOB
        self.height = ht


    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        if(self.__has_any_number(new_name)):
            print("sorry person name can't have number")
            return
        self.__name = new_name

    def __has_any_number(self, string):
        return "0" in string
    
    def get_summary(self):
        return f"name {self.__name}, DateOfBirth: {self.DOB}, height: {self.height}"


person_1 =Person(8, "07/05/2020", "9")
print(person_1.get_summary())
person_1.set_name("Rubayet")
print(person_1.get_summary()) 

# print(person_1.name) #access by the veriable name



# student class 
class Student(Person):
    def __init__(self, name: str, DOB, ht: int, email):
        super().__init__(name, DOB, ht)
        self.email = email
        self.ht= ht

    def get_summary(self):
        return f"name: {self.get_name()} email: {self.email} height: {self.ht}"
    

s = Student("kashem", 2000, 7, "kashem@gamil.com")

print(s.get_summary())