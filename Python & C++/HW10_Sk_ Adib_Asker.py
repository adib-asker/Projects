#Sk Adib Asker
#CS 100 2017F Section 103
#HW 10, Nov 22, 2017

class Dog:
    '''This class is to define the dog's name and breed,
       and whether the dog knows how to do some tricks'''
    species = 'Canis familiaris'
    def __init__ (self, dog_name, dog_breed):
        ''' Initialize the variables'''
        self.name = dog_name
        self.breed = dog_breed
        self.tricks = []
        

    def teach(self, dog_str):
        '''This method adds a string to the tricks's list'''
        self.tricks.append(dog_str)
        print(self.name, "knows", dog_str)

    def knows(self, dog_srt1):
        '''This method checks whether the string is part of the tricks's list'''
        if dog_srt1 in self.tricks:
            print('Yes,', self.name, 'knows', dog_str)
            return True
        else:
            print('No,', self.name, 'doesn\'t know', dog_str)
            return False
        
    def morph(self,species):
        Dog.species = species
    #def species(self):
        #print(self.species)
