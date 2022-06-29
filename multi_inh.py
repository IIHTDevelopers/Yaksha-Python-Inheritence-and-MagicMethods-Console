class Student:
    def set_details(self,id,name):
        self.id=id
        self.name=name
    def get_details(self):
        pass

class Marks(Student):
    def set_marks(self,subject1,subject2,subject3,subject4,subject5):
        self.subject1=subject1
        self.subject2=subject2
        self.subject3=subject3
        self.subject4=subject4
        self.subject5=subject5
    def get_marks(self):
        pass

class Result(Marks):
    def get_result(self):
        pass

if __name__=="__main__":
    obj=Result()
    id=int(input("Enter id"))
    name=input("Enter name")
    obj.set_details(id,name)
    subject1,subject2,subject3,subject4,subject5=[eval(x) for x in input("Enter 5 subjects marks").split()]
    obj.set_marks(subject1,subject2,subject3,subject4,subject5)
    details=obj.get_details()
    print(' '.join(str(x) for x in details))
    marks=obj.get_marks()
    print(' '.join(str(x) for x in marks))
    result=obj.get_result()
    print(' '.join(str(x) for x in result))
