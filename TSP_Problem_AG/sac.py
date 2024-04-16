import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
from customtkinter import CTkFrame

class KnapsackApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Knapsack Problem Solver")
        self.master.attributes("-fullscreen", True)
        self.dark_mode = False  # Default: Light Mode
        self.selected_items=[]
        self.master.configure(bg="white")
        # self.background_image = background_image

        self.item_name_mapping = {
            (5, 10): "Bottle",
            (15, 30): "Headphones",
            (30, 50): "Laptop",
            (10, 20): "Phone",
            (20, 25): "Snacks"
        }

        # Create name_by_weight_value dictionary
        self.name_by_weight_value = {k: v for k, v in self.item_name_mapping.items()}

        # Initialize background image if needed
        # self.background_image2 = None

        self.items = []  # Example items (weight, value)
        self.max_weight = 50

        self.create_widgets()
        self.create_panel()

    def create_panel(self):
        # Create a frame for buttons
        self.button_frame = ttk.Frame(self.master)
        self.button_frame.pack(side=tk.TOP, fill=tk.X, padx=30, pady=15)

        # Add solve button
        self.solve_button = ttk.Button(self.button_frame, text="Solve", command=self.solve_knapsack, style="Custom.TButton")
        self.solve_button.pack(side=tk.RIGHT, padx=10)

        # Add remove item button
        self.remove_item_button = ttk.Button(self.button_frame, text="Remove Item", command=self.remove_item, style="Custom.TButton")
        self.remove_item_button.pack(side=tk.RIGHT, padx=10)

        # Add exit button
        self.exit_button = ttk.Button(self.button_frame, text="Exit", command=self.exit_app, style="Custom.TButton")
        self.exit_button.pack(side=tk.RIGHT, padx=10)

        # Add return button
        self.return_button = ttk.Button(self.button_frame, text="Return to Main App", command=self.return_to_main_app, style="Custom.TButton")
        self.return_button.pack(side=tk.LEFT, padx=10)
        # Add return button
        self.return_button = ttk.Button(self.button_frame, text="Dark Mode", command=self.activate_dark_mode, style="Custom.TButton")
        self.return_button.pack(side=tk.LEFT, padx=10)

        # Create the canvas for the graph
        self.graph_canvas = tk.Canvas(self.master)
        self.graph_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        

    def create_widgets(self):
        self.title_label = ttk.Label(self.master, text="Knapsack Problem Solved By Genetic Algorithm", font=("Helvetica", 20, "bold"))
        self.title_label.pack(side=tk.TOP, padx=20, pady=10)


        
        self.item_frame = ttk.Frame(self.master, padding="20 10")
        self.item_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a frame for buttons at the top
        # Create a frame for buttons at the top
        self.button_frame_top = ttk.Frame(self.master, padding="20")
        self.button_frame_top.place(relx=0.5, y=10, anchor=tk.CENTER)


        # Create a frame for buttons at the top
        self.button_frame_top = ttk.Frame(self.master, padding="20")
        self.button_frame_top.pack(side=tk.TOP, fill=tk.X)

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

        # # Create a frame for buttons
        # self.button_frame = ttk.Frame(self.master, padding="20")
        # self.button_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Define icons for objects
        self.bottle_image = Image.open("sac_images/Bottle.png")
        self.bottle_image = self.bottle_image.resize((50, 50), Image.LANCZOS)
        self.bottle = ImageTk.PhotoImage(self.bottle_image)

        self.headphones_image = Image.open("sac_images/Headphones.png")
        self.headphones_image = self.headphones_image.resize((50, 50), Image.LANCZOS)
        self.headphones = ImageTk.PhotoImage(self.headphones_image)

        self.laptop_image = Image.open("sac_images/Laptop.png")
        self.laptop_image = self.laptop_image.resize((50, 50), Image.LANCZOS)
        self.laptop = ImageTk.PhotoImage(self.laptop_image)

        self.phone_image = Image.open("sac_images/Phone.png")
        self.phone_image = self.phone_image.resize((50, 50), Image.LANCZOS)
        self.phone = ImageTk.PhotoImage(self.phone_image)

        self.snacks_image = Image.open("sac_images/Snacks.png")
        self.snacks_image = self.snacks_image.resize((50, 50), Image.LANCZOS)
        self.snacks = ImageTk.PhotoImage(self.snacks_image)

         # Add buttons for objects at the top
        buttons = [
            ("Bottle", self.bottle),
            ("Headphones", self.headphones),
            ("Laptop", self.laptop),
            ("Phone", self.phone),
            ("Snacks", self.snacks)
        ]

        for i, (item_name, image) in enumerate(buttons):
            button = ttk.Button(self.button_frame_top, text=item_name, image=image, compound=tk.LEFT,
                                command=lambda name=item_name: self.add_item(name), style="Custom.TButton")
            button.grid(row=0, column=i, padx=5, pady=5, sticky="ew")

        # Configure column weights to make buttons center-aligned
        for i in range(len(buttons)):
            self.button_frame_top.grid_columnconfigure(i, weight=1)



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

        # Add the selected item to the list of selected items
        self.selected_items.append(self.items[-1])

        # Update item labels
        self.update_item_labels()
    def return_to_main_app(self):
            # Destroy the current window (KnapsackApp window)
            self.master.destroy()


    def activate_dark_mode(self):
            # Toggle dark mode
            self.dark_mode = not self.dark_mode

            # Change the appearance based on the mode
            if self.dark_mode:
                # Dark mode settings
                self.master.configure(bg="black")
                # Update other widget configurations for dark mode
            else:
                # Light mode settings
                self.master.configure(bg="white")
                # Update other widget configurations for light mode 



    def remove_item(self):
        # Remove the last item
        if self.selected_items:
            self.selected_items.pop()
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
            selected_items = [self.selected_items[i] for i, selected in enumerate(solution) if selected]

            if selected_items:
                # Calculate the total weight and value of selected items
                total_weight = sum(item[0] for item in selected_items)
                total_value = sum(item[1] for item in selected_items)

                # Calculate fitness (total value divided by total weight)
                fitness = total_value / total_weight if total_weight != 0 else 0

                item_names = ', '.join([f"Item {i+1} (Weight={item[0]}, Value={item[1]})" for i, item in enumerate(selected_items)])
                self.solution_label.config(text=f"Best Solution: {item_names}, Total Weight: {total_weight}, Total Value: {total_value}, Fitness: {fitness}")

                # Display images of selected items and fitness in a popup
                popup = tk.Toplevel(self.master)
                popup.title("Selected Items")

                # Calculate the center position for the popup window
                screen_width = self.master.winfo_screenwidth()
                screen_height = self.master.winfo_screenheight()
                popup_width = 500  # Adjust as needed
                popup_height = 500  # Adjust as needed
                x_position = (screen_width - popup_width) // 2
                y_position = (screen_height - popup_height) // 2
                popup.geometry(f"{popup_width}x{popup_height}+{x_position}+{y_position}")

                # Add title label
                title_label = ttk.Label(popup, text="Solution Of the Knapsack problem", font=("Helvetica", 16, "bold"))
                title_label.pack(side=tk.TOP, padx=10, pady=5)

                # Add fitness label
                fitness_label = ttk.Label(popup, text=f"Fitness: {fitness}", font=("Helvetica", 14, "bold"))
                fitness_label.pack(side=tk.TOP, padx=10, pady=5)

                # Create a frame to hold the items
                item_frame = ttk.Frame(popup)
                item_frame.pack(side=tk.TOP, padx=10, pady=5)

                for i, (weight, value) in enumerate(selected_items):
                    try:
                        item_name = self.name_by_weight_value.get((weight, value))
                        if item_name:
                            # Load item image
                            item_image_path = f"sac_images/{item_name}.png"  # Assuming images are named after item names
                            item_image = Image.open(item_image_path)
                            item_image = item_image.resize((100, 100), Image.LANCZOS)
                            item_photo = ImageTk.PhotoImage(item_image)

                            # Create label with item image and information
                            item_label = ttk.Label(item_frame, image=item_photo, text=f"Name: {item_name}\nWeight: {weight}\nValue: {value}", compound=tk.TOP)
                            item_label.image = item_photo
                            item_label.grid(row=0, column=i, padx=10, pady=5, sticky="w")
                        else:
                            # If item name is not found, display an error message
                            messagebox.showerror("Error", f"Item with weight={weight} and value={value} not found")
                    except (FileNotFoundError, OSError) as e:
                        # Catch exceptions related to file not found or errors in opening the image
                        messagebox.showerror("Error", f"Error loading image for item with weight={weight} and value={value}: {e}")

                # Add a hide button to close the popup
                hide_button = ttk.Button(popup, text="Hide", command=popup.destroy)
                hide_button.pack(side=tk.BOTTOM, padx=10, pady=10)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for parameters. Please enter valid numbers.")



    def fitness(self, individual):
        total_weight = sum(self.selected_items[i][0] for i, selected in enumerate(individual) if selected)
        total_value = sum(self.selected_items[i][1] for i, selected in enumerate(individual) if selected)
        if total_weight > self.max_weight:
            return 0  # Penalize solutions exceeding the weight limit
        return total_value

    def genetic_algorithm(self, pop_size, num_generations, mutation_rate):
        # Generate individuals based on selected items
        population = []
        for _ in range(pop_size):
            individual = [random.choice([0, 1]) for _ in range(len(self.selected_items))]
            population.append(individual)

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

# root = tk.Tk()
# app = KnapsackApp(root)
# root.mainloop()
