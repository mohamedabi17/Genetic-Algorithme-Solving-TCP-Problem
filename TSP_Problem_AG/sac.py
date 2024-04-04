import tkinter as tk
from tkinter import ttk, messagebox
import random

class KnapsackApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Knapsack Problem Solver")
        self.master.attributes("-fullscreen", True)
        self.master.configure(bg="white")

        self.items = [(10, 60), (20, 100), (30, 120)]  # Example items (weight, value)
        self.max_weight = 50

        self.create_widgets()

    def create_widgets(self):
        self.item_frame = ttk.Frame(self.master)
        self.item_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.item_labels = []
        for i, (weight, value) in enumerate(self.items):
            label = ttk.Label(self.item_frame, text=f"Item {i+1}: Weight={weight}, Value={value}")
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            self.item_labels.append(label)

        self.solution_label = ttk.Label(self.master, text="Best Solution:")
        self.solution_label.pack(side=tk.TOP, padx=10, pady=10)

        # Add buttons to adjust parameters
        self.param_frame = ttk.Frame(self.master)
        self.param_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.population_label = ttk.Label(self.param_frame, text="Population Size:")
        self.population_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.population_entry = ttk.Entry(self.param_frame, width=10)
        self.population_entry.grid(row=0, column=1, padx=5, pady=5)
        self.population_entry.insert(0, "100")

        self.generations_label = ttk.Label(self.param_frame, text="Number of Generations:")
        self.generations_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.generations_entry = ttk.Entry(self.param_frame, width=10)
        self.generations_entry.grid(row=1, column=1, padx=5, pady=5)
        self.generations_entry.insert(0, "50")

        self.mutation_label = ttk.Label(self.param_frame, text="Mutation Rate:")
        self.mutation_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.mutation_entry = ttk.Entry(self.param_frame, width=10)
        self.mutation_entry.grid(row=2, column=1, padx=5, pady=5)
        self.mutation_entry.insert(0, "0.1")

        # Create a frame for buttons
        self.button_frame = ttk.Frame(self.master)
        self.button_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # Define icons for objects
        self.bottle = tk.PhotoImage(file="sac_images/bottle.png")
        self.bottle = self.bottle.subsample(15)
        self.headphones = tk.PhotoImage(file="sac_images/headphones.png")
        self.headphones = self.headphones.subsample(15)
        self.laptop = tk.PhotoImage(file="sac_images/laptop.png")
        self.laptop = self.laptop.subsample(15)
        self.phone = tk.PhotoImage(file="sac_images/phone.jpeg")
        self.phone = self.phone.subsample(15)
        self.snacks = tk.PhotoImage(file="sac_images/snacks.png")
        self.snacks = self.snacks.subsample(6)

        # Add buttons for objects
        self.bottle_button = ttk.Button(self.button_frame, text="Bottle", image=self.bottle, compound=tk.LEFT, command=lambda: self.add_item("Bottle"))
        self.bottle_button.pack(side=tk.TOP, padx=5, pady=5)

        self.headphones_button = ttk.Button(self.button_frame, text="Headphones", image=self.headphones, compound=tk.LEFT, command=lambda: self.add_item("Headphones"))
        self.headphones_button.pack(side=tk.TOP, padx=5, pady=5)

        self.laptop_button = ttk.Button(self.button_frame, text="Laptop", image=self.laptop, compound=tk.LEFT, command=lambda: self.add_item("Laptop"))
        self.laptop_button.pack(side=tk.TOP, padx=5, pady=5)

        self.phone_button = ttk.Button(self.button_frame, text="Phone", image=self.phone, compound=tk.LEFT, command=lambda: self.add_item("Phone"))
        self.phone_button.pack(side=tk.TOP, padx=5, pady=5)

        self.snacks_button = ttk.Button(self.button_frame, text="Snacks", image=self.snacks, compound=tk.LEFT, command=lambda: self.add_item("Snacks"))
        self.snacks_button.pack(side=tk.TOP, padx=5, pady=5)

        # Add buttons to add or remove items
        self.item_button_frame = ttk.Frame(self.master)
        self.item_button_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.add_item_button = ttk.Button(self.item_button_frame, text="Add Item", command=self.add_item)
        self.add_item_button.pack(side=tk.LEFT, padx=5)

        self.remove_item_button = ttk.Button(self.item_button_frame, text="Remove Item", command=self.remove_item)
        self.remove_item_button.pack(side=tk.LEFT, padx=5)

        # Add solve button
        self.solve_button = ttk.Button(self.master, text="Solve", command=self.solve_knapsack)
        self.solve_button.pack(side=tk.TOP, padx=10, pady=10)

    def add_item(self, item_name):
        # Add the selected item
        if item_name == "Bottle":
            self.items.append((5, 10))  # Example weight and value for Bottle
        elif item_name == "Headphones":
            self.items.append((15, 30))  # Example weight and value for Headphones
        elif item_name == "Laptop":
            self.items.append((30, 50))  # Example weight and value for Laptop
        elif item_name == "Phone":
            self.items.append((10, 20))  # Example weight and value for Phone
        elif item_name == "Snacks":
            self.items.append((20, 25))  # Example weight and value for Snacks

        # Update item labels
        self.update_item_labels()

    def remove_item(self):
        # Remove the last item
        if self.items:
            self.items.pop()

        # Update item labels
        self.update_item_labels()

    def update_item_labels(self):
        # Clear existing labels
        for label in self.item_labels:
            label.destroy()

        # Create new labels
        self.item_labels = []
        for i, (weight, value) in enumerate(self.items):
            label = ttk.Label(self.item_frame, text=f"Item {i+1}: Weight={weight}, Value={value}")
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            self.item_labels.append(label)

    def solve_knapsack(self):
        try:
            population_size = int(self.population_entry.get())
            num_generations = int(self.generations_entry.get())
            mutation_rate = float(self.mutation_entry.get())

            solution = self.genetic_algorithm(population_size, num_generations, mutation_rate)
            self.solution_label.config(text=f"Best Solution: {solution}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for parameters. Please enter valid numbers.")

    def fitness(self, individual):
        total_weight = 0
        total_value = 0
        for i, selected in enumerate(individual):
            if selected:
                total_weight += self.items[i][0]
                total_value += self.items[i][1]
        if total_weight > self.max_weight:
            return 0  # Penalize solutions exceeding the weight limit
        return total_value

    def genetic_algorithm(self, pop_size, num_generations, mutation_rate):
        population = [[random.choice([0, 1]) for _ in range(len(self.items))] for _ in range(pop_size)]

        for _ in range(num_generations):
            population = self.evolve_population(population, mutation_rate)

        best_individual = max(population, key=self.fitness)
        return best_individual

    def evolve_population(self, population, mutation_rate):
        new_population = []
        for _ in range(len(population)):
            parent1 = self.tournament_selection(population)
            parent2 = self.tournament_selection(population)
            child = self.crossover(parent1, parent2)
            child = self.mutate(child, mutation_rate)
            new_population.append(child)
        return new_population

    def tournament_selection(self, population):
        tournament_size = 5
        tournament = random.sample(population, tournament_size)
        return max(tournament, key=self.fitness)

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(0, len(parent1) - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        return child

    def mutate(self, individual, mutation_rate):
        for i in range(len(individual)):
            if random.random() < mutation_rate:
                individual[i] = 1 - individual[i]
        return individual


