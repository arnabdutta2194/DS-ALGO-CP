class animalShelter:
    def __init__(self) :
        self.cats = []
        self.dogs = []
    
    def enqueue(self,animal,type):
        if type == "cat":
            self.cats.append(animal)
        else: self.dogs.append(animal)
    
    def dequeueCat(self):
        if len(self.cats) == 0: return None
        else:
            return self.cats.pop(0)
    
    def dequeueDog(self):
        if len(self.dogs) == 0: return None
        else:
            return self.dogs.pop(0)
    
    def dequeueAny(self):
        if len(self.cats) == 0: return self.dogs.pop(0)
        elif len(self.cats) == 0: return self.cats.pop(0)
        
customQueue = animalShelter()
customQueue.enqueue('Cat1','cat')
customQueue.enqueue('Cat2','cat')
customQueue.enqueue('Dog1','dog')
customQueue.enqueue('Cat3','cat')
customQueue.enqueue('Cat4','cat')
customQueue.enqueue('Dog2','dog')
print(customQueue.dequeueDog())
print(customQueue.dequeueCat())