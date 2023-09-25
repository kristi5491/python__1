import time
import random

class Health:
    __health = 100
    __max_health = 100

    def get_health(self):
        return self.__health
    
    def set_health(self, health):
        self.__health = health

    def __init__(self,  max_health=100):
        self.__max_health = max_health
        if(self.__health > self.__max_health):
            self.__health = self.__max_health

    def damage(self, damage):
        self.__health -= damage
        if(self.__health < 0):
            self.__health = 0
    
    def heal(self, heal):
        self.__health += heal
        if(self.__health > self.__max_health):
            self.__health = self.__max_health
class Position:
    __position = [0, 0]
    __move_speed = 1
    def get_position(self):
        return self.__position

    def move(self, x, y):
        if(x > 1):
            x = 1
        elif(x < -1):
            x = -1
        if(y > 1):
            y = 1
        elif(y < -1):
            y = -1

        self.__position[0] += x * self.__move_speed
        self.__position[1] += y * self.__move_speed
    
    def __init__(self, x=0, y=0, move_speed=1):
        self.__position = [x, y]
        self.__move_speed = move_speed
class Attacker:
    __damage = 10

    def get_damage(self):
        return self.__damage
    def attack(self, target:Health):
        target.damage(self.__damage)
    def __init__(self, damage = 20):
        self.__damage = damage
    

class Name:
    __name = "Player"
    __id = 0
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def __init__(self, id = random.randint(0, 100), name=f'plane'):
        if name == 'plane':
            if id <= 30:
                name = f'destroyer [{id}]'
            elif 30 < id <= 60:
                name = f'bomber [{id}]'
            elif  60 < id <= 75:
                name = f'scouter [{id}]'
        else:
            name = f'base [{id}]'
        self.__name = name
        self.__id = id



def generate_plan():
    
    random_value = random.randint(0, 75)

    if (random_value <= 30):
        class Plane(Health, Position, Attacker, Name):
            def move(self, x, y):
                if(self.get_health() > 0):
                    return super().move(x, y)
            def __init__(self, max_health=100, x = 0, y = 0, move_speed = 1, damage=10):
                Health.__init__(self, max_health)
                Position.__init__(self, x, y ,move_speed )
                Name.__init__(self, id=random_value)
                Attacker.__init__(self, damage)
        return Plane
    elif (30 < random_value <= 60):
        class Plane(Health, Position, Attacker, Name):
            def move(self, x, y):
                if(self.get_health() > 0):
                    return super().move(x, y)
            def __init__(self, max_health=100, x = 0, y = 0, move_speed = 1, damage=10):
                Health.__init__(self, max_health)
                Position.__init__(self, x, y ,move_speed )
                Name.__init__(self, id=random_value)
                Attacker.__init__(self, damage)
        return Plane
    else :
        class Plane(Health, Position, Name):
            def move(self, x, y):
                if(self.get_health() > 0):
                    return super().move(x, y)
            def __init__(self, max_health=100, x = 0, y = 0, move_speed = 2):
                Health.__init__(self, max_health)
                Position.__init__(self, x, y ,move_speed )
                Name.__init__(self, id=random_value)
        return Plane
   





def generate_base():
    random_value = random.randint(76, 100)

    class Base(Health, Position,Name):
        def __init__(self, max_health=300):
            Health.__init__(self, max_health)
            Name.__init__(self, id=random_value, name='base')
            Position.__init__(self)
    return Base
    
planes = []
bases = []
for i in range(3):
    def create_base():
        new_base = generate_base()()
        new_base.set_health(300)
        bases.append(new_base)
        time.sleep(0.1)
    create_base()

for i in range(10):
    def create_plane():
        new_plane = generate_plan()()
        for plane in planes:
            if plane.get_id() == new_plane.get_id():
                create_plane()
        new_plane.set_health(100)
        planes.append(new_plane)
        time.sleep(0.1)
    create_plane()
        

while(True):
    for plane in planes:
        plane.move(random.randint(-1, 1), random.randint(-1, 1))
    
    destroyed_planes = []
    destroyed_bases = []

    for plane in planes:
        if plane.get_health() == 0:
            destroyed_planes.append(plane)
    for base in bases:
        if base.get_health() == 0:
            destroyed_bases.append(base)


    for plane in planes:
        plane_id = plane.get_id()
        if (plane_id <= 30):
            target = random.choice(planes)
            plane.attack(target) 
        elif (30 <plane_id <= 60):
            target = random.choice(bases)
            plane.attack(target)


    if len(destroyed_bases) == 3 :
        print("You win!")
        exit()

    print(len(destroyed_planes))
    if len(destroyed_planes) > 8 :
        for plane in planes:
            if(plane.get_health() > 0):
                print(f'{plane.get_name()} : {plane.get_health()} ♥️ : {plane.get_position()} - Plane Won!')
        exit()

    

    
    for base in bases:
        if (base.get_health() ==  0):
            print(f'{base.get_name()} : dead 💀 : {base.get_position()}')
        else:
            print(f'{base.get_name()} : {base.get_health()} ♥️ : Undefined')

    for plane in planes:
        if(plane.get_health() == 0):
            print(f'{plane.get_name()} : dead 💀 : {plane.get_position()}')
        else:
            print(f'{plane.get_name()} : {plane.get_health()} ♥️ : {plane.get_position()}')
    print('------------------------')

    if(input() == 'q'):
        break



           
    

    
            