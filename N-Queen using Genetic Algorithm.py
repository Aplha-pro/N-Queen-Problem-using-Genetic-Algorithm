import random  # Importing Library to generate random number to initialize population with random DNA


class agent:  # class of agent in this case it's the board of n queen problem
    def __init__(self, size, c=None):  # c chromosome passed to agent's constructor
        if c is None:  # check if c i None it initializes chromosome value with empty array
            self.chromosome = []
        self.size = size  # size of board (Must be greater than 3)
        self.chromosome = c  # stores all dna in a list
        self.fitness = 0  # Stores fitness value of agent
        if c:  # check if chromosome is passed to constructor it calculates the fitness of the agent based of predefined value of chromosome
            self.set_fitness()

    def init_agent(self):  # initialize chromosome values with random numbers
        for i in range(self.size):
            self.chromosome.append(random.randint(1, self.size))
        self.set_fitness()  # calculate fitness value

    def set_fitness(self):  # calculate the fitness value
        # check the value of current index with all further index (if possible)
        for i in range(self.size):
            for j in range(i, self.size):
                # check if queen is present in same row or in any diagonal way (checking the attacking positions)
                if self.chromosome[i] != self.chromosome[j] and abs(self.chromosome[i] - self.chromosome[j]) != abs(i - j):
                    self.fitness += 1

    def print_agent(self, fitprint=True):  # printing the board and maybe the fitness value
        for i in range(self.size-1, -1, -1):
            print(end="|")
            for j in range(self.size):
                if self.chromosome[j] == (i + 1):
                    print(' Q|', end="")
                else:
                    print("__|", end="")
            print()
        if fitprint:
            print("Fitness Value: ", self.fitness, "\n")


class GeneticAlgorithm:  # Control all the steps of genetic algorithm
    def __init__(self, psize, bsize):  # get population size and board size
        self.population = []
        self.B_SIZE = bsize
        self.P_SIZE = psize
        self.generation = 0
        self.max_fit_val = 0  # stores the maximum possible fitness value or the fitness value of goal state

    def init_population(self):  # initialize the population with defined size having random dna values
        self.max_fit_val = int(((self.B_SIZE - 1) * self.B_SIZE) / 2)
        for i in range(self.P_SIZE):
            board = agent(self.B_SIZE)
            board.chromosome = []
            board.init_agent()
            self.population.append(board)

    def run(self):  # control the processing of genetic algorithm
        print("Initializing Population")
        self.init_population()
        while self.stopping_criteria():
            self.print_generation()
            self.create_new_generation()
        self.sort_population()
        print('Final Result at Generation: ', self.generation)
        ga.population[0].print_agent(False)

    def sort_population(self):  # sorting population according to their fitness value, agent with higer fitness value move towards 0 index
        genes_list = []
        fitness_list = []
        for entity in self.population: # separating fitness value and choromosome list to compare and shift within the list.
            genes_list.append(entity.chromosome)
            fitness_list.append(entity.fitness)

        # comparing the fitness value of one list and sort the chromosome list in population accordingly
        sorted_pop = [x for _, x in sorted(zip(fitness_list, genes_list), reverse=True)]
        self.population = []
        for i in range(self.P_SIZE):
            self.population.append(agent(size=self.B_SIZE, c=sorted_pop[i]))

    def create_new_generation(self):
        self.sort_population()
        new_population = []
        for i in range(0, int(len(self.population) / 2)):  # Choosing top half best performing population for breeding
            new_population.append(self.crossover(self.population[i], self.population[i + 1], 3))
            new_population.append(self.crossover(self.population[i + 1], self.population[i], 3))
        for i in range(len(new_population)):
            if random.randint(0, 4) == 1:  # Setting 1 out of 5 chances for mutation i.e. 20% chance for mutation
                new_population[i] = self.mutation(new_population[i])
        # Clearing old population and replacing with newly generated population
        self.population = []
        for i in range(self.P_SIZE):
            self.population.append(new_population[i])
        self.generation += 1

    def mutation(self, entity):  # Mutation Function
        idx = random.randint(0, self.B_SIZE-1)
        entity.chromosome[idx] = random.randint(1, self.B_SIZE)  # Mutate one gene value using random value between 1 and size of board inclusive
        return entity

    def crossover(self, p1, p2, cutoff):  # breeding function
        # Cutoff define at which index the genes of other parent board attach
        new_agent = []
        for j in range(0, cutoff):  # Takes the genes of one board from starting (0) to cutoff index
            new_agent.append(p1.chromosome[j])
        for k in range(cutoff, self.B_SIZE):  # Takes the genes of one board from cutoff index to the last gene of index
            new_agent.append(p2.chromosome[k])
        return agent(self.B_SIZE, new_agent)  # develop the agent and return

    def stopping_criteria(self):  # Stops the iterations of genetic algorithm when it reaches the goal state
        for entity in self.population:
            if entity.fitness < self.max_fit_val:
                return True
            else:
                return False
        return True

    def print_generation(self):  # Print message about the working of a generation
        print("Generation: ", self.generation)
        for entity in self.population:
            entity.print_agent()


if __name__ == '__main__':
    s = int(input("Enter the size of n (Note: n > 3): "))  # Get value of n from user
    # Creating instance of Genetic Algorithm
    ga = GeneticAlgorithm(8, s)
    ga.run()
