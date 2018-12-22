import random

class Chromosome:
    # Chromosome class constructor
    # Actual functionality is to set up an array called genes.
    # If boolean flag fillGenes is set to True, genes must be
    # filled with random values between 0 and 1, otherwise
    # it must be filled with 0.
    # Length of array genes must be equal to length 
    # constructor parameter.
    # Also initializes local variable mutationRate
    # with corresponding parameter.
    def __init__(self, length, mutationRate, fillGenes=False):
        self.length = length
        self.mutationRate = mutationRate
        self.genes = []

        for _ in range(length):
            if fillGenes:
                self.genes.append(random.random())
            else:
                self.genes.append(0)
        
    # Creates two offspring children using a single crossover point.
    # The basic idea is to first pick a random position, create two 
    # children and then swap their genes starting from the randomly 
    # picked position point.
    # Children genes must be different from both of parents.
    # 
    # Returning type: (Chromosome, Chromosome)
    def Crossover(self, another):
        pos = random.randint(1, self.length - 1)

        first = Chromosome(self.length, self.mutationRate, False)
        second = Chromosome(self.length, self.mutationRate, False)
        first.genes = self.genes[pos:] + another.genes[:pos]
        second.gens = another.genes[pos:] + self.genes[:pos]

        return (first, second)

    # Mutates the chromosome genes in place by randomly switching them
    # depending on mutationRate. More precisely, mutation
    # of i-th gene happens with probability of mutationRate.
    def Mutate(self):
        for index in range(len(self.genes)):
            if random.random() < self.mutationRate:
                self.genes[index] = random.random()