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

# 5. Shared Warm-Up Method
class Athlete:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def warm_up(self):
        print(f"{self.name} is warming up.")    
class Gymnast(Athlete):
    def __init__(self, name, age,apparatus):
        super().__init__(name, age)       
        self.apparatus =apparatus
    def compete(self):
        print(f"{self.name} competes on the {self.apparatus}")    
class Swimmer(Athlete):
    def __init__(self, name, age,stroke):
        super().__init__(name, age)
        self.stroke =stroke
    def compete(self):
        print(f"{self.name} competes in {self.stroke}") 
ana = Gymnast("Ana", 19, "rings")
ana.warm_up()
ana.compete()
ben = Swimmer("Ben", 21, "butterfly")
ben.warm_up()
ben.compete()  

# 6. Constructor Chaining with super()
class Athlete:
    def __init__(self,name, age, years_active):
        self.years_active =years_active
        self.name =name
        self.age =age
    def experience(self):
        print(f"{self.name} has been active for {self.years_active} years.")
class TeamSportPlayer(Athlete):
    def __init__(self, name, age, years_active,team_name):
        super().__init__(name, age, years_active)    
        self.team_name =team_name
    def team_info(self):
        print(f"{self.name} plays for {self.team_name}.")    
gal = TeamSportPlayer("Gal", 28, 10, "Maccabi") 
gal.experience()
gal.team_info() 

# 7. Personal Best Tracking
class Athlete:
    def __init__(self,name, sport):
        self.name =name
        self.sport =sport
        self.personal_best = None    
    def set_record(self,value):
        self.personal_best = value
    def has_record(self):
        return True if self.personal_best != None else False
class Sprinter(Athlete):
    def __init__(self, name):
        super().__init__(name, sport = "100m Sprint")        
usain = Sprinter("Usain")
print(usain.__dict__)
print(usain.has_record())
usain.set_record(10.8)
print(usain.has_record())
print(usain.personal_best)

# 8. Training Session Counter
class Athlete:
    def __init__(self,name, age):
        self.name =name
        self.age =age
        self.sessions_completed = 0
    def train(self):
        self.sessions_completed +=1
    def sessions_needed(self,target):
        if target - self.sessions_completed < 0:
            return 0
        else:
            return target - self.sessions_completed
class Triathlete(Athlete):
    def __init__(self, name, age,dcisipline):
        super().__init__(name, age)         
        self.dcisipline =dcisipline
    def describe(self):
        print(f"Triathlete {self.name}, age: {self.age}, discipline: {self.dcisipline}")
dan = Triathlete("Dan", 26, "cycling")
dan.describe()
dan.train()            
dan.train()            
dan.train()            
dan.train()            
dan.train()
print(f"{dan.sessions_completed} sessions completed")            
print(f"{dan.sessions_needed(10)} more needed")

# 9. Basketball Player Card
class Athlete:
    def __init__(self,name, age, position):
        self.name =name
        self.age = age
        self.position =position
    def player_card(self):
        print(f"name is: {self.name} | age is: {self.age} | position is: {self.position}")
class BasketballPlayer(Athlete):
    def __init__(self, name, age, position,jersey_number):
        super().__init__(name, age, position)
        self.jersey_number =jersey_number
    def full_profile(self):
        self.player_card()
        print(f"Jersey: #{self.jersey_number}")
mia = BasketballPlayer("Mia", 24, "guard", 7)
mia.full_profile()
messi = BasketballPlayer("messi", 39, "playmeyker", 10)
messi.full_profile()
lamin = BasketballPlayer("lamin", 19, "cf", 19)
lamin.full_profile()

# 10. Three-Level Inheritance Chain
class Person:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def greet(self):
        print(f"Hi, I am {self.name}.")
class Athlete(Person):
    def __init__(self, name, age,sport):
        super().__init__(name, age)        
        self.sport =sport
    def train(self):
        print(f"{self.name} is training for {self.sport}.")
class ProfessionalAthlete(Athlete):
    def __init__(self, name, age, sport,sponsor):
        super().__init__(name, age, sport)  
        self.sponsor =sponsor
    def sponsor_info(self):
        print(f"{self.name} is sponsored by {self.sponsor}.")
messi = ProfessionalAthlete("messi", 39, "football", "Nike")
messi.greet()
messi.train()
messi.sponsor_info()

# self learn: singleton
# practice:
# 1. Same Logger Object
class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
            print("gad")
        return cls._instance
gad = Logger()
gad = Logger()

# 2. Shared Settings
class AppSettings:
    _instance = None
    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
            cls.theme = "dark"
        return cls._instance
app1 = AppSettings()
app2 = AppSettings()
print(app1.theme)
print(app2.theme)

app1.theme = "gad"
print(app2.theme)

