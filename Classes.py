#1.
class Dog(object):
    def __init__(self):
	    print("Initiate anyways")
    def speak(self):
        pass

Danny = Dog()
SH = Dog()

#2. 
#이거 하나만 만들어도 몇천개의 캐릭터 생성 가능
#NPC하나 만드는데 각 NPC의 변수를 만들 필요가 없어짐
class Cat(): #self의 의미는 각 instance를 의미함 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [1,2,3,4]
    def speak(self):
        print("my name is ", self.name, self.age)
    def change_age(self,age):
        self.age = age
    def add_weight(self, weight):
        self.weight = weight

Kim = Cat("Danny", 33) #instance variable
Kim.speak()
Park = Cat("SH", 50)
Park.speak()
Park.change_age(11)
Park.speak()

Park.add_weight(123)

print(Park.age, Park.li, Park.weight) #You can access to the attribute of the object by simplly calling it
#print(Kim.weight) #이거는 add_weight 안해서 안됨

#3.
class Mother(): #self의 의미는 각 instance를 의미함 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("my name is ", self.name, self.age, self.color)
    
    def talk(self):
        print("Stop Playing Games!!")

#같은 기능의 클래스를 다른 이름으로 사용하려면 원래는 이렇게 복붙해야하지만,
#inheritance (상속)을 사용하면 그럴 필요 없음
class Son(Mother): #Hum = parent class, animal = child
    def __init__(self, name, age, color):
        #여기서 super()은 위의 Mother Class의 self.name과 self.age에다가 값을 넣어서 
        #사용하겠다는 뜻
        super().__init__(name, age)     
        self.color = color #엄마가 좋아하는 색은 알기 싫고 아들이 원하는 색만 알고 싶을때
    
    def talk(self): #override
        print("I Love to play MineCraft Mommy...")

#엄마의 대한 function을 아들이 가져다가 쓸 수 있는 방법
Kim = Son("youngho", 30, 'Blue')
Kim.speak()
Kim.talk()
    