<h1>N-Queen Problem Solver using Genetic Algorithm</h1>
<p>This Python script aims to solve the classic N-Queen problem using a Genetic Algorithm (GA). The N-Queen problem involves placing N chess queens on an N×N chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. Genetic Algorithm is a metaheuristic inspired by the process of natural selection.</p>

**Overview**  
This script comprises two classes: agent and GeneticAlgorithm.

`agent:` Represents an individual solution (board configuration) in the N-Queen problem. It holds the board configuration, fitness value, and functions for initializing, evaluating fitness, and printing the board.

`GeneticAlgorithm:` Controls the genetic algorithm's steps, including initializing the population, running the genetic algorithm loop, sorting the population, creating a new generation, implementing mutation, crossover, and defining stopping criteria.

**Usage**  
`Initialization:` Input the size of the chessboard (N) when prompted.

`Genetic Algorithm Execution:` The script initializes the GA with a predefined population size and runs the algorithm until a stopping criterion is met (all agents reach the maximum fitness value, i.e., a solution).
