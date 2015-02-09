list_1 = [['a','cow'], ['b','pig'], ['a','horse'], ['c','dog'], ['b','cat'], ['a','mouse'], ['a','cow']]
##dict_1 = {}
##for entry in list_1:
##     letter = entry[0]
##     animal = entry[1]
##     if letter in dict_1:
##          new_animal = animal
##          old_animal = dict_1[letter]
##          animals = old_animal + new_animal
##          dict_1[letter] = animals
##     else:
##          dict_1[letter] = animal
##print(dict_1)
###output: {'a': 'cowhorsemousecow', 'c': 'dog', 'b': 'pigcat'}

#try making a list within

dict_1 = {}
for entry in list_1:
     letter = entry[0]
     animal = entry[1]
     if letter in dict_1: 
        new_animal = animal
        old_animal = dict_1[letter]
        animals_list = old_animal
        if new_animal in old_animal: 
           dict_1[letter] = old_animal
        else:
            animals_list.append(new_animal)
            dict_1[letter] = animals_list
     else:
          dict_1[letter] = [animal]
print(dict_1)

#successful result! = {'b': ['pig', 'cat'], 'a': ['cow', 'horse', 'mouse'], 'c': ['dog']}
