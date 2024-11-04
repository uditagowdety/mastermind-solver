import math
import random
colours=['⬛','🟥','🟨','🟩','🟪','🟫']#allowed colours
POPSIZE=8
MUTATION_RATE=.1

def generateGene():
    return tuple([random.choice(colours) for x in range(4)])

def generatePopulation():
    Population=[]
    for i in range(POPSIZE):
        Population.append(generateGene())
    return Population

def checkFitness(gene,CODE):
    codeCopy=CODE.copy()#to not alter original code
    fitness=0.0
    for index,colour in enumerate(gene):
        if colour in codeCopy:
            if CODE[index]==colour:
                fitness+=1
            else:
                fitness+=.5
            codeCopy.remove(colour)
    return fitness
                
def populationFitness(Population,CODE):
    fitnessDict={gene:0 for gene in Population}
    for gene in Population:
        fitnessDict[gene]=checkFitness(gene,CODE)
    
    #sorting by fitness
    sortedFit= sorted(fitnessDict.items(), key=lambda x:x[1], reverse=True)
    fitnessDict=dict(sortedFit)
    return fitnessDict

def crossover(c1,c2):
    cross = random.randint(1,3)
    
    # Perform crossover
    offspring1 = c1[:cross] + c2[cross:]
    offspring2 = c2[:cross] + c1[cross:]

    if(FIRST_ITER):
        print(f"Parent 1:{c1}   Parent 2:{c2}")
        print(f"Crossover Point={cross}")
        print(f"Child 1: {offspring1}, Child 2:{offspring2}\n")



    
    return mutate(offspring1),mutate(offspring2)
    

def mutate(gene):
    mutated_gene = []

    for codon in gene:
        if random.random() < MUTATION_RATE:
            mutated_gene.append(random.choice(colours))
        else:
            mutated_gene.append(codon)
    
    return tuple(mutated_gene)

def select(population, fitness_values):
    return population[0],population[1]

def printPopulation(populationDict):
    for gene in populationDict:
        gene_string="".join(gene)
        print(f"{gene_string}:{populationDict[gene]}\n")

def mastermind(CODE):
    population=generatePopulation()
    populationDict=populationFitness(population,CODE)
    GOAL =tuple(CODE)
    gen=0
    global FIRST_ITER
    FIRST_ITER=True

    fitness_values=list(populationDict.values())
    population=list(populationDict.keys())

    while GOAL not in populationDict:
        #selection
        if FIRST_ITER:
            print(f"\n Intitial Randomly Generated Population:")
            printPopulation(populationDict)
            print(f'\n')
        parent1,parent2=select(population,fitness_values)
        #crossover,mutation
        child1,child2=crossover(parent1,parent2)
        if FIRST_ITER:
            print(f"Mutated Child 1:{child1}")
            print(f"Mutated Child 2:{child2}\n")
            FIRST_ITER=False

        population.extend([child1,child2])
        populationDict=populationFitness(population,CODE)

        fitness_values=list(populationDict.values())
        population=list(populationDict.keys())
        print(f"Generation {gen}, Best: {fitness_values[0]}, Sequence: {population[0]}")
        gen+=1
    return gen
def bruteforce(CODE):
    match= False
    number_gueses=0
    while not match:
        guess=generateGene()
        if checkFitness(guess,CODE)==4:
            match=True
        number_gueses+=1
    return number_gueses

if __name__=='__main__':
    print("Allowed Colours:⬛, 🟥, 🟨, 🟩, 🟪, 🟫")
    CODE=list(input("Enter A Code"))
    print(f"Code to Crack={CODE}")
    tries_AI=mastermind(CODE)*2+10
    tries_brute_force=bruteforce(CODE)
    print(f"Tries Taken By Brute Force: {tries_brute_force}")
    print(f"Tries Taken By Genetic Algorithm: {tries_AI}")