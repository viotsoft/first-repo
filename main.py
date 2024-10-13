class Cat():
    def __init__(self, name):
        self.name = name
    def say(self):
        print(f"{self.name} tell mau")

my_cat = Cat('Murchick')
print(f"{my_cat.name} cute cat")
my_cat.say()

class HouseCat(Cat):
    def __init__(self, name):
        super().__init__(name)
    
    def play(self):
        print(f"{self.name} play")

my_house_cat = HouseCat('Murch')
print(f"{my_cat.name} home cat")
my_house_cat.say()
my_house_cat.play()

