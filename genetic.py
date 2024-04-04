import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Distance matrix representing distances between cities
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Number of cities
num_cities = len(distances)

class TSPSolverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("TCP Problem Application Solver by Genetic Algorithm")
        self.master.iconbitmap("TCP.ico")

        self.population_size_var = tk.IntVar(value=50)
        self.num_generations_var = tk.IntVar(value=1000)
        self.mutation_rate_var = tk.DoubleVar(value=0.01)
        self.theme_var = tk.BooleanVar(value=False)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.master, text="Welcome to the TCP Problem Application Solver", font=('Helvetica', 14)).grid(row=0, columnspan=2, padx=5, pady=5)

        ttk.Label(self.master, text="Population Size:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.master, textvariable=self.population_size_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.master, text="Number of Generations:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.master, textvariable=self.num_generations_var).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.master, text="Mutation Rate:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.master, textvariable=self.mutation_rate_var).grid(row=3, column=1, padx=5, pady=5)

        ttk.Checkbutton(self.master, text="Black and White Theme", variable=self.theme_var, command=self.toggle_theme).grid(row=4, columnspan=2, padx=5, pady=5)

        ttk.Button(self.master, text="Run Solver", command=self.run_solver).grid(row=5, columnspan=2, padx=5, pady=10)

    def toggle_theme(self):
        theme = "winnative" if not self.theme_var.get() else "clam"
        self.master.tk_setPalette(background=theme)

    def calculate_total_distance(self, route):
        total_distance = 0
        for i in range(num_cities - 1):
            total_distance += distances[route[i]][route[i + 1]]
        total_distance += distances[route[-1]][route[0]]  # Return to the starting city
        return total_distance

    def generate_random_route(self):
        return random.sample(range(num_cities), num_cities)

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(0, num_cities - 1)
        child = [-1] * num_cities
        for i in range(crossover_point):
            child[i] = parent1[i]
        for i in range(num_cities):
            if parent2[i] not in child:
                for j in range(num_cities):
                    if child[j] == -1:
                        child[j] = parent2[i]
                        break
        return child

    def mutate(self, route):
        if random.random() < self.mutation_rate_var.get():
            idx1, idx2 = random.sample(range(num_cities), 2)
            route[idx1], route[idx2] = route[idx2], route[idx1]

    def genetic_algorithm(self):
        population_size = self.population_size_var.get()
        num_generations = self.num_generations_var.get()

        population = [self.generate_random_route() for _ in range(population_size)]

        best_distances = []
        best_route = None
        for generation in range(num_generations):
            population = sorted(population, key=lambda x: self.calculate_total_distance(x))
            fittest_route = population[0]
            best_distances.append(self.calculate_total_distance(fittest_route))

            new_population = [fittest_route]  # Keep the fittest route unchanged

            while len(new_population) < population_size:
                parent1, parent2 = random.sample(population, 2)
                child = self.crossover(parent1, parent2)
                self.mutate(child)
                new_population.append(child)

            population = new_population

            if best_route is None or self.calculate_total_distance(fittest_route) < self.calculate_total_distance(best_route):
                best_route = fittest_route

        best_distance = self.calculate_total_distance(best_route)
        messagebox.showinfo("Result", f"Best Route: {best_route}\nBest Distance: {best_distance}")

        # Plot the evolution of the best distance
        plt.figure()
        plt.plot(best_distances)
        plt.xlabel("Generation")
        plt.ylabel("Best Distance")
        plt.title("Evolution of Best Distance")
        plt.show()

    def run_solver(self):
        self.genetic_algorithm()


def main():
    root = tk.Tk()
    app = TSPSolverApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
