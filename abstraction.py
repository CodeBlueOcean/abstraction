# Encapsulation ( 4 pilliars of oop)

# 1 abstraction

class PlayerCharacter:
    def _init_(self, name, age):
        self.name = name 
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('andrei', 100)
#print((1,2,3).count(1))
print(len((1,2,3,1)))


# Another example Encapsulation ( 4 pilliars of oop)

# 1 abstraction

class PlayerCharacter:
    def _init_(self, name, age):
        self.name = name 
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('andrei', 100)
camera.takepicture()
player1.name = '!!!'
player1.speak = "BOOOOOO"

print(player1.speak)
#error message, speak has been modify as a value, not as a funtion 
#print(player1.speak())


