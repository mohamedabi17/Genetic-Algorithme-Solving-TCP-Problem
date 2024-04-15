import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
from customtkinter import CTkFrame
class KnapsackApp:
    def __init__(self, master, background_image2):
        self.master = master
        self.master.title("Knapsack Problem Solver")
        self.master.attributes("-fullscreen", True)
        # self.master.attributes("-zoomed", True)
        self.dark_mode = False  # Default: Light Mode

        # background_label2 = tk.Label(master, image=background_image2)
        # background_label2.place(x=0, y=0, relwidth=1, relheight=1)

        self.background_image2 = None
        self.items = [(10, 60), (20, 100), (30, 120)]  # Example items (weight, value)
        self.max_weight = 50

        self.create_widgets()
        self.create_pannel()

    def create_pannel(self):
        self.button_frame = CTkFrame(self.master)
        self.button_frame.pack(side=tk.TOP, pady=5)
        
        self.graph_canvas = tk.Canvas(self.master)
        self.graph_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.result_text = tk.Text(self.master, height=10, width=50)
        self.result_text.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=10, pady=10)
        
        self.add_item_button = ttk.Button(self.button_frame, text="Add Item", command=self.add_item, style="Custom.TButton")
        self.add_item_button.pack(side=tk.RIGHT, padx=5)

        self.remove_item_button = ttk.Button(self.button_frame, text="Remove Item", command=self.remove_item, style="Custom.TButton")
        self.remove_item_button.pack(side=tk.RIGHT, padx=5)

        self.exit_button = ttk.Button(self.button_frame, text="Exit ", command=self.exit_app, style="Custom.TButton")
        self.exit_button.pack(side=tk.RIGHT, padx=5)

        # Add solve button
        self.solve_button = ttk.Button(self.button_frame, text="Solve", command=self.solve_knapsack, style="Custom.TButton")
        self.solve_button.pack(side=tk.RIGHT, padx=5)




    def create_widgets(self):
        self.item_frame = ttk.Frame(self.master, padding="20 10")
        self.item_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.item_labels = []
        for i, (weight, value) in enumerate(self.items):
            label = ttk.Label(self.item_frame, text=f"Item {i+1}: Weight={weight}, Value={value}", font=("Helvetica", 14))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            self.item_labels.append(label)

        self.solution_label = ttk.Label(self.master, text="Best Solution:", font=("Helvetica", 16, "bold"))
        self.solution_label.pack(side=tk.TOP, padx=20, pady=10)

        # Add buttons to adjust parameters
        self.param_frame = ttk.Frame(self.master, padding="20")
        self.param_frame.pack(side=tk.TOP, fill=tk.X)

        self.population_label = ttk.Label(self.param_frame, text="Population Size:", font=("Helvetica", 14))
        self.population_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.population_entry = ttk.Entry(self.param_frame, width=10, font=("Helvetica", 14))
        self.population_entry.grid(row=0, column=1, padx=5, pady=5)
        self.population_entry.insert(0, "100")

        self.generations_label = ttk.Label(self.param_frame, text="Number of Generations:", font=("Helvetica", 14))
        self.generations_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.generations_entry = ttk.Entry(self.param_frame, width=10, font=("Helvetica", 14))
        self.generations_entry.grid(row=1, column=1, padx=5, pady=5)
        self.generations_entry.insert(0, "50")

        self.mutation_label = ttk.Label(self.param_frame, text="Mutation Rate:", font=("Helvetica", 14))
        self.mutation_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.mutation_entry = ttk.Entry(self.param_frame, width=10, font=("Helvetica", 14))
        self.mutation_entry.grid(row=2, column=1, padx=5, pady=5)
        self.mutation_entry.insert(0, "0.1")

        # Create a frame for buttons
        self.button_frame = ttk.Frame(self.master, padding="20")
        self.button_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Define icons for objects
        self.bottle_image = Image.open("sac_images/1.png")
        self.bottle_image = self.bottle_image.resize((50, 50),Image.Resampling.LANCZOS)
        self.bottle = ImageTk.PhotoImage(self.bottle_image)

        self.headphones_image = Image.open("sac_images/2.png")
        self.headphones_image = self.headphones_image.resize((50, 50),Image.Resampling.LANCZOS)
        self.headphones = ImageTk.PhotoImage(self.headphones_image)

        self.laptop_image = Image.open("sac_images/3.png")
        self.laptop_image = self.laptop_image.resize((50, 50),Image.Resampling.LANCZOS)
        self.laptop = ImageTk.PhotoImage(self.laptop_image)

        self.phone_image = Image.open("sac_images/4.png")
        self.phone_image = self.phone_image.resize((50, 50),Image.Resampling.LANCZOS)
        self.phone = ImageTk.PhotoImage(self.phone_image)

        self.snacks_image = Image.open("sac_images/5.png")
        self.snacks_image = self.snacks_image.resize((50, 50),Image.Resampling.LANCZOS)
        self.snacks = ImageTk.PhotoImage(self.snacks_image)

        # Add buttons for objects
        self.bottle_button = ttk.Button(self.button_frame, text="Bottle", image=self.bottle, compound=tk.LEFT, command=lambda: self.add_item("Bottle"), style="Custom.TButton")
        self.bottle_button.pack(side=tk.TOP, padx=5, pady=5)

        self.headphones_button = ttk.Button(self.button_frame, text="Headphones", image=self.headphones, compound=tk.LEFT, command=lambda: self.add_item("Headphones"), style="Custom.TButton")
        self.headphones_button.pack(side=tk.TOP, padx=5, pady=5)

        self.laptop_button = ttk.Button(self.button_frame, text="Laptop", image=self.laptop, compound=tk.LEFT, command=lambda: self.add_item("Laptop"), style="Custom.TButton")
        self.laptop_button.pack(side=tk.TOP, padx=5, pady=5)

        self.phone_button = ttk.Button(self.button_frame, text="Phone", image=self.phone, compound=tk.LEFT, command=lambda: self.add_item("Phone"), style="Custom.TButton")
        self.phone_button.pack(side=tk.TOP, padx=5, pady=5)

        self.snacks_button = ttk.Button(self.button_frame, text="Snacks", image=self.snacks, compound=tk.LEFT, command=lambda: self.add_item("Snacks"), style="Custom.TButton")
        self.snacks_button.pack(side=tk.TOP, padx=5, pady=5)



    def exit_app(self):
        self.master.destroy()

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
            label = ttk.Label(self.item_frame, text=f"Item {i+1}: Weight={weight}, Value={value}", font=("Helvetica", 14))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            self.item_labels.append(label)

    def solve_knapsack(self):
        try:
            population_size = int(self.population_entry.get())
            num_generations = int(self.generations_entry.get())
            mutation_rate = float(self.mutation_entry.get())

            solution = self.genetic_algorithm(population_size, num_generations, mutation_rate)
            selected_items = [self.items[i] for i, selected in enumerate(solution) if selected]

            if selected_items:
                item_names = ', '.join([f"Item {i+1} (Weight={item[0]}, Value={item[1]})" for i, item in enumerate(selected_items)])
                self.solution_label.config(text=f"Best Solution: {item_names}")

                # Display images of selected items in a popup
                popup = tk.Toplevel(self.master)
                popup.title("Selected Items")

                for i, (weight, value) in enumerate(selected_items):
                    item_image_path = f"sac_images/{i+1}.png"  # Assuming images are named item_1.png, item_2.png, etc.
                    item_image = Image.open(item_image_path)
                    item_image = item_image.resize((100, 100), Image.LANCZOS)
                    item_photo = ImageTk.PhotoImage(item_image)
                    item_label = ttk.Label(popup, image=item_photo)
                    item_label.image = item_photo
                    item_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            else:
                self.solution_label.config(text="No items selected in the solution")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for parameters. Please enter valid numbers.")

    # def fitness(self, individual):
    #     total_weight = 0
    #     total_value = 0
    #     for i, selected in enumerate(individual):
    #         if selected:
    #             total_weight += self.items[i][0]
    #             total_value += self.items[i][1]
    #     if total_weight > self.max_weight:
    #         return 0  # Penalize solutions exceeding the weight limit
    #     return total_value
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

