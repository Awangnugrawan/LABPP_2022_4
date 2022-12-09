class Person :
    def __init__ (self, name, age, isMale, goals) :
        self.name = name   
        self.age = age    
        self.isMale = isMale
        self.goals = goals
    def setName (self, name) :
        self.name = name 
    def setAge (self, age) :
        self.age = age 
    def setGender (self, gender) :
        if gender == "Male":
            self.isMale = True
        else:
            self.isMale = False
    def getName (self) :
        return self.name 
    def getAge (self) :
        return self.age
    def getGender (self) :
        if self.isMale == True : 
            self.gender = "Male"
            return self.gender
        else: 
            self.gender = "Female"
            return self.gender
    def getGoals (self):
        return self.goals
    def setGoals (self, goals):
        self.goals = goals

name = input()
age = int(input())
isMale = input().upper()
if isMale == "TRUE":
    isMale = bool(True)
else:
    isMale = bool(False)
goals = input()

human = Person(name, age, isMale, goals)
human.setName(name)
print("Nama saya:",human.getName())
print("Umur saya:",human.getAge())
print("Gender:",human.getGender())
print("Cita-cita:",human.getGoals())


