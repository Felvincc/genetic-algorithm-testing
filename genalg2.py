
import random

def rand_chromosome():
    rand_chromo_list=[]

    for _ in range(8):

        rand_char = random.choice('01')

        rand_int=int(rand_char)

        rand_chromo_list.append(rand_int)
        
    rand_chromo_tuple = tuple(rand_chromo_list)

    return rand_chromo_tuple
    
def one(x):

    dict = {
        1: 200,
        2: 150,
        3: 10,
        4: 80,
        5: 400,
        6: 50,
        7: 20,
        8: 30,
    }

    if x == 0:

        return 200
    
    elif x == 1:

        return 150
    
    elif x == 2:

        return 10
    
    elif x == 3:

        return 80
    
    elif x == 4:

        return 400
    
    elif x == 5:
       
       return 50
    
    elif x == 6:

        return 20
    
    elif x == 7:

        return 30

def fitness(conv_chromo):

    total = 0

    for x in conv_chromo:

        total += x

    if total > 500:

        conv_chromo_tuple = tuple(conv_chromo)

        chromo_and_fitness=(0, conv_chromo_tuple)

        return chromo_and_fitness
    
    else:

        conv_chromo_tuple = tuple(conv_chromo)

        chromo_and_fitness=(total, conv_chromo_tuple)

        return chromo_and_fitness
    
def evaluator(chromo):

    conv_chromo=[]

    for x in range(len(chromo)):

        gene = chromo[x]

        if gene == 1:
            temp = one(x)
            conv_chromo.append(temp)
        else:
            conv_chromo.append(0)


    fitness_score = fitness(conv_chromo)

    return fitness_score


def create_population():

    list_population =[]

    for _ in range(20):

        initial = rand_chromosome()

        processed=evaluator(initial)

        list_population.append(processed)
    
    list_population.sort()
    list_population.reverse()

    tuple_population = tuple(list_population)

    return tuple_population


initial_generation = create_population()




'''

    a = rand_chromosome()

    #a = (1,0,0,0,0,0,1,1)

    print(a)

    fitness_score = evaluator(a)

    print(fitness_score)

'''
