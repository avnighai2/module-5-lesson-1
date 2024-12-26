class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

blue = Parrot("blue", 10)
Woo = Parrot("Woo", 15)

print("Blue is a {} ".format( blue.species ))
print("Woo is also a {} ".format( Woo.species ))

print("{} is {} years old".format( blue.name, blue.age ))
print("{} is {} years old".format(Woo.name ,Woo.age ))