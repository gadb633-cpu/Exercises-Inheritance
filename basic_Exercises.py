# Main Exercises
# 1. Swimmer Inherits from Athlete
class Athlete:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete.") 
class Swimmer(Athlete):
    def __init__(self,name,age):
        super().__init__(name,age)
tom = Swimmer("Tom", 22)
tom.introduce()    

# 2. Runner with a Fixed Sport
class Athlete:
    def __init__(self,name, age, sport):
        self.name =name
        self.age = age
        self.sport =sport
    def describe(self):
        print(f"{self.name} competes in {self.sport}.")
class Runner(Athlete):
    def __init__(self,name,age):
        super().__init__(name,age,sport="running")
sara = Runner("Sara", 25)
sara.describe()

# 3. Cyclist with Gear Info
class Athlete:
    def __init__(self,name, age):
        self.name =name
        self.age =age
    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete.")
class Cyclist(Athlete):
    def __init__(self,name,age,bike_brand):
        super().__init__(name,age)
        self.bike_brand =bike_brand
    def describe_gear(self):
        print(f"Cyclist {self.name} rides a {self.bike_brand}.")    
mike = Cyclist("Mike", 30, "Trek")
mike.introduce()
mike.describe_gear()

# 4. Three Sports, One Parent
class Athlete:
    def __init__(self,name, country):
        self.name =name
        self.country =country
    def greet(self):
        print(f"{self.name} represents {self.country}.")
class Swimmer(Athlete):
    def __init__(self, name, country,stroke_style):
        super().__init__(name, country)
        self.stroke_style =stroke_style
class Runner(Athlete):
    def __init__(self, name, country,best_distance):
        super().__init__(name, country)        
        self.best_distance =best_distance
class Cyclist(Athlete):
    def __init__(self, name, country,race_type):
        super().__init__(name, country)        
        self.race_type =race_type
lior = Swimmer("Lior", "Israel", "freestyle")
lior.greet()
avi = Runner("Avi", "Kenya", "marathon")
avi.greet()
jan = Cyclist("Jan", "France", "road")
jan.greet()        