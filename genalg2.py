
import random

import time

import os

def rand_chromosome():                                                  #creates random 8 digit binary string, and returns (duh)
    rand_chromo_list=[]
    #'''
    for _ in range(8):

        rand_char = random.choice('01')

        rand_int=int(rand_char)

        rand_chromo_list.append(rand_int)
        
    rand_chromo_tuple = tuple(rand_chromo_list)
    #'''

    #rand_chromo_tuple = (0,0,0,0,0,0,0,0)

    return rand_chromo_tuple
    
def one(x):                                                             #i dont want to talk about it

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

        return 100
    
    elif x == 1:

        return 100
    
    elif x == 2:

        return 100
    
    elif x == 3:

        return 100
    
    elif x == 4:

        return 100
    
    elif x == 5:
       
       return 100
    
    elif x == 6:

        return 100
    
    elif x == 7:

        return 100

def fitness(conv_chromo):                                               #customizable (probably)

    total = 0

    for x in conv_chromo:

        total += x

    if total > 10000:

        conv_chromo_tuple = tuple(conv_chromo)

        chromo_and_fitness=(0, conv_chromo_tuple)

        return chromo_and_fitness
    
    else:

        conv_chromo_tuple = tuple(conv_chromo)

        chromo_and_fitness=(total, conv_chromo_tuple)

        return chromo_and_fitness
    
def evaluator(chromo):                                                  #evaluates the binary string into the values of the chromosone

    conv_chromo=[]

    for x in range(len(chromo)):

        gene = chromo[x]

        if gene == 1:

            temp = one(x)                                               
            conv_chromo.append(temp)

        else:

            conv_chromo.append(0)


    fitness_score = fitness(conv_chromo)                                #this converts the binary string chromosome into the fitness score (higher the number the better)

    return fitness_score

def create_population():                                                #creates population

    list_population =[]

    for _ in range(20):                                                 #creates 20 chromosomes

        initial = rand_chromosome()

        processed=evaluator(initial)                                    #sends chromosomes to evaluator to see fitness

        list_population.append(processed)
    
    list_population.sort()
    list_population.reverse()

    tuple_population = tuple(list_population)

    return tuple_population

def repackage(premutation_next_gen):                                    #repackages the evaluated new generation back to binary string

    packaged_premutation_next_gen=[]

    for x in premutation_next_gen:
        if x == 0:
            packaged_premutation_next_gen.append(0)
        else:
            packaged_premutation_next_gen.append(1)

    return packaged_premutation_next_gen

def mutation(premutation_next_gen):                                     #mutates by randomly picking an int(1,100) and if its below 4 it mutates

    for i in range(len(premutation_next_gen)):
        a = random.randint(1, 100)
        b = random.randint(0, 1)
        
        if a <= 10:  # MUTATION VALUE
            premutation_next_gen[i] = b

    return premutation_next_gen

    pass                                                        #code snippit below does not work properly, figure out why

''' mutated_next_gen=[]

    for x in premutation_next_gen:

        a = random.randint(1,100)
        b = random.randint(0,1)
        
        if a <= 2:                                         #MUTATION VALUEEEEE
            premutation_next_gen[x] = b

        else:
            pass

    mutated_next_gen=premutation_next_gen

    return mutated_next_gen
    '''

def breed(chosen_ones):                                                 # god forbid you have to debug this 
    
    next_generation =[]

    for x in range(5):

        for x in range(len(chosen_ones)):

            overwrite_genes = []
            male_list = list(chosen_ones[x])
            
            random_int = random.randint(0,3)

            if random_int == x:
                random_int = random.randint(0,3)
            else:
                pass

            female_list= list(chosen_ones[random_int])

            male_tail=random.randint(0,len(male_list)-3)
            male_body=male_tail+1
            male_head=male_tail+2

    
            female_tail=random.randint(0,len(male_list)-3)                      #female tail, body, head doesnt serve a purpose anymore
            female_body=female_tail+1
            female_head=female_tail+2


            overwrite_genes = []
            overwrite_genes.append(male_list[male_tail])
            overwrite_genes.append(male_list[male_body])
            overwrite_genes.append(male_list[male_head])

            female_list[male_tail]=male_list[male_tail]
            female_list[male_body]=male_list[male_body]
            female_list[male_head]=male_list[male_head]

            

            premutation_next_gen = female_list

            packaged_premutated_next_gen = repackage(premutation_next_gen)

            mutated_next_gen=mutation(packaged_premutated_next_gen)

            evaluated_next_gen = evaluator(mutated_next_gen)

            next_generation.append(evaluated_next_gen)

            next_generation.sort()
            next_generation.reverse()

    return next_generation
    
def start():

    chosen_ones=[]

    initial_generation = create_population()

    best_solutions = initial_generation[:4]

    for s in best_solutions:

        chosen_ones.append(s[1])

    for x in range(10000):

        chosen_ones_temp = breed(chosen_ones)

        chosen_ones_temp.sort()
        chosen_ones_temp.reverse()

        #os.system('cls')

        print(f"\n=====Generation {x} Best Solutions=====")

        print(chosen_ones_temp[3:])

        print()

        #time.sleep(1)

        next_generation = chosen_ones_temp

        #add a function that saves the highes value of all iterations

    exit()



start()

