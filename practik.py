class student:

    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self. school =school
    def actions(self):
        return f"{self.name} {self.age} {self.school}"
eliza = student("eliza",16,11)
saku = student("saku" ,17,10)

class supstudent(student):
    pass
    def hobby_spell(self):
        return f"{self.name} {self.age} {self.school} играет волейбол !!!"

madi = supstudent("madi",18,11)
# print(eliza.actions())
# print (madi.actions())
# print(type(eliza))
# print(type(madi))

# print (madi.hobby_spell())
class sportstudent(student):
    def __init__(self,name,age,school,sport):
        super().__init__(self,name,age,school)
        self.sport = sport
Anar=sportstudent("Anar",19,25,"football")
