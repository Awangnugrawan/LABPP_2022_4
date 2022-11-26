inputName=input('Name: ')
inputAge=int(input('Age: '))
inputHobby=input('Hobby:')
inputIsmale=input('Is Male: ')
inputIsmale=inputIsmale.lower()
print()

class person :

    def __init__(self,inputName,inputAge,inputGender) :
        self.name=inputName
        self.gender=inputAge
        self.gender=inputGender

    def setName(self,inputName) :
        self.name=inputName
    def getName(self) :
        print('Name:',self.name)
        
    def setHobby(self,inputHobby) :
        self.hobby=inputHobby
    def getHobby(self) :
        print('Hobby:', self.hobby)


    def setAge(self,inputAge) :
        self.age=inputAge
    def getAge(self) :
        print('Age:', self.age)

    def setGender(self,inputGender) :
        self.gender=inputGender
    def getGender(self) :
        if self.gender == 'true':
            self.gender=True
            if self.gender==True :
                print('Gender: Male')
        elif self.gender == 'false':
            self.gender=False
            if self.gender==False :
                print('Gender: Female')
        else :
            print('Please make sure you put True/False in Is Male.')

person1=person(inputName, inputAge, inputIsmale)
person1.setName(inputName)
person1.getName()
person1.setAge(inputAge)
person1.getAge()
person1.setHobby(inputHobby)
person1.getHobby()
person1.setGender(inputIsmale)
person1.getGender()