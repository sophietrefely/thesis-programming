list1 = [['orange',"['horse', 'cat', 'dog']", 'pear'], ['lemon', "['cow', 'sheep']", 'orange']]

##for element in list1:
##    animals = element[1]
##    animals_strip = animals.strip('[]')
##    animals_list = animals_strip.split(',')
##    for animal in animals_list:
##        animal_strip = animal.strip()
##        print(animal_strip)
    
for element in list1:
    animals = eval(element[1])
    for animal in animals:
        print(animal)
    
