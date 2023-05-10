array1= [1,2,3,4,5,6,7,8,9]
array2=[]
for i in range(len(array1)):
    if (array1[i]%2==1):
        print(array1[i])

class Dog():
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print("name is " + self.name)

doggo = Dog(name="tommy",breed="labrador")
doggo.bark()