# Genetic Algorithm for Mastermind Game

## Overview
This project implements a genetic algorithm to solve the classic Mastermind game, where the goal is to guess a secret sequence of colors. The program simulates the process of natural selection, using crossover and mutation to evolve potential solutions over generations until the code is cracked. A brute-force method is also included for comparison.

## Project Goal
To showcase how genetic algorithms can effectively solve problems involving optimization and pattern matching in a simulated environment.

![Mastermind Solver](https://github.com/user-attachments/assets/bda6e1a4-7102-4140-ae6d-0c3fce4fb26f)

## Features
- **Color Options**: Includes six possible colors represented by emojis: ⬛, 🟥, 🟨, 🟩, 🟪, 🟫.
- **Genetic Algorithm**: Uses population initialization, fitness evaluation, selection, crossover, and mutation to iteratively improve guesses.
- **Brute Force Method**: A baseline approach to guess the code by generating random sequences until a match is found.
- **Comparison**: Outputs the number of attempts required by both the genetic algorithm and brute force method.

## Key Functions
- `generateGene()`: Creates a random guess.
- `checkFitness()`: Evaluates the fitness of a guess based on its similarity to the target code.
- `crossover()`: Combines parts of two parent genes to create new child genes.
- `mutate()`: Randomly alters parts of a gene based on a mutation rate.
- `mastermind()`: Main function that runs the genetic algorithm.
- `bruteforce()`: Runs the brute force algorithm.

