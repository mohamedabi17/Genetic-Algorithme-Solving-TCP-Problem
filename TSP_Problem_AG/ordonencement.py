import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random

class TaskScheduler:
    def __init__(self, tasks=None, num_resources=None, pop_size=100, num_generations=1000, mutation_rate=0.01):
        self.tasks = tasks
        self.num_resources = num_resources
        self.pop_size = pop_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate

    def input_tasks(self, tasks):
        self.tasks = tasks

    def input_num_resources(self, num_resources):
        self.num_resources = num_resources

    def input_parameters(self, pop_size, num_generations, mutation_rate):
        self.pop_size = pop_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate

    def create_initial_population(self):
        if self.tasks is None:
            raise ValueError("Tasks not provided")
        if self.num_resources is None:
            raise ValueError("Number of resources not provided")
        
        print("Generating initial population...")
        initial_population = [random.sample(range(len(self.tasks)), len(self.tasks)) for _ in range(self.pop_size)]
        print("Initial population generated:", initial_population)
        
        return initial_population


    def evaluate_fitness(self, schedule):
        total_duration = sum(self.tasks[task]["duration"] for task in schedule)
        print(f"Fitness of schedule {schedule}: {total_duration}")
        return -total_duration


    def selection(self, population):
        sorted_population = sorted(population, key=self.evaluate_fitness)
        selected_parents = sorted_population[:len(population)//2]
        print("Selected parents:", selected_parents)
        return selected_parents


    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        print("Crossover:")
        print("Parent 1:", parent1)
        print("Parent 2:", parent2)
        print("Child 1:", child1)
        print("Child 2:", child2)
        return child1, child2


    def mutate(self, schedule):
        print("Mutation:")
        print("Before mutation:", schedule)
        for i in range(len(schedule)):
            if random.random() < self.mutation_rate:
                schedule[i] = random.randint(0, len(self.tasks) - 1)
        print("After mutation:", schedule)
        return schedule
    def optimize(self):
        if self.tasks is None or len(self.tasks) == 0:
            print("No tasks provided. Please add tasks.")
            return None

        if self.num_resources is None or self.num_resources == 0:
            print("No resources provided. Please add resources.")
            return None

        population = self.create_initial_population()
        if not population:
            print("Initial population is empty. Please check your inputs.")
            return None

        for gen in range(self.num_generations):
            parents = self.selection(population)
            next_population = []
            for parent1, parent2 in zip(parents[::2], parents[1::2]):
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                next_population.extend([child1, child2])
            population = next_population

        if not population:
            print("Population is empty after generations. No solution found.")
            return None

        best_schedule = min(population, key=self.evaluate_fitness)
        return best_schedule




class TaskSchedulerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Scheduler")  # Set the title of the main window
        
        self.title_label = ttk.Label(self.master, text="Task Scheduler Solved By Genetic Algorithm", font=("Helvetica", 20, "bold"))
        self.title_label.pack(side=tk.TOP, padx=20, pady=10)
        #         # Add title label
        # self.title_label = ttk.Label(self.master, text="Task Scheduler", font=("Helvetica", 24, "bold"))
        # self.title_label.pack(pady=20)  # Adjust padding as needed
        
         # Initialize tasks, resources, and other parameters
        self.tasks = {}
        self.resources = {}
        self.pop_size = 100
        self.num_generations = 1000
        self.mutation_rate = 0.01

        self.create_widgets()

    def create_widgets(self):
        # Task input frame
        self.task_frame = ttk.Frame(self.master, padding="20")
        self.task_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.task_label = ttk.Label(self.task_frame, text="Enter number of tasks:")
        self.task_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.num_tasks_entry = ttk.Entry(self.task_frame, width=10)
        self.num_tasks_entry.grid(row=0, column=1, padx=5, pady=5)

        self.add_tasks_button = ttk.Button(self.task_frame, text="Add Tasks", command=self.add_tasks)
        self.add_tasks_button.grid(row=0, column=2, padx=5, pady=5)

        # Resource input frame
        self.resource_frame = ttk.Frame(self.master, padding="20")
        self.resource_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.resource_label = ttk.Label(self.resource_frame, text="Enter number of resources:")
        self.resource_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.num_resources_entry = ttk.Entry(self.resource_frame, width=10)
        self.num_resources_entry.grid(row=0, column=1, padx=5, pady=5)

        self.add_resources_button = ttk.Button(self.resource_frame, text="Add Resources", command=self.add_resources)
        self.add_resources_button.grid(row=0, column=2, padx=5, pady=5)

        # Parameter input frame
        self.param_frame = ttk.Frame(self.master, padding="20")
        self.param_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.pop_size_label = ttk.Label(self.param_frame, text="Population Size:")
        self.pop_size_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.pop_size_entry = ttk.Entry(self.param_frame, width=10)
        self.pop_size_entry.grid(row=0, column=1, padx=5, pady=5)
        self.pop_size_entry.insert(0, "100")


        self.num_generations_label = ttk.Label(self.param_frame, text="Number of Generations:")
        self.num_generations_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.num_generations_entry = ttk.Entry(self.param_frame, width=10)
        self.num_generations_entry.grid(row=1, column=1, padx=5, pady=5)
        self.num_generations_entry.insert(0, "1000")

        self.mutation_rate_label = ttk.Label(self.param_frame, text="Mutation Rate:")
        self.mutation_rate_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.mutation_rate_entry = ttk.Entry(self.param_frame, width=10)
        self.mutation_rate_entry.grid(row=2, column=1, padx=5, pady=5)
        self.mutation_rate_entry.insert(0, "0.01")

        self.optimize_button = ttk.Button(self.param_frame, text="Optimize", command=self.optimize)
        self.optimize_button.grid(row=3, columnspan=2, padx=5, pady=10)

    def add_tasks(self):
        try:
            num_tasks = int(self.num_tasks_entry.get())
            tasks = {}
            for i in range(num_tasks):
                while True:
                    duration = simpledialog.askinteger("Task Duration", f"Enter duration for task {i+1}:")
                    if duration is None:
                        messagebox.showwarning("Warning", "Task duration cannot be empty. Please try again.")
                    else:
                        tasks[i] = {"duration": duration}
                        break  # Break out of the loop if duration is provided
            self.tasks = tasks
            messagebox.showinfo("Success", "Tasks added successfully.")
            print("Tasks:", self.tasks)  # Add this line to print tasks
            # Add code to display tasks in the GUI if needed
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of tasks.")

    def add_resources(self):
        try:
            num_resources = int(self.num_resources_entry.get())
            self.num_resources = num_resources  # Update the number of resources
            resources = {}
            for i in range(num_resources):
                duration = simpledialog.askinteger("Resource Duration", f"Enter duration for resource {i+1}:")
                if duration is not None:
                    resources[i] = {"duration": duration}
                else:
                    messagebox.showwarning("Warning", "Resource duration cannot be empty. Please try again.")
                    return
            self.resources = resources  # Store resources in self.resources
            messagebox.showinfo("Success", "Resources added successfully.")
            print("Resources:", self.resources)  # Add this line to print resources
            # Add code to display resources in the GUI if needed
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of resources.")
    def optimize(self):
        pop_size = int(self.pop_size_entry.get())
        num_generations = int(self.num_generations_entry.get())
        mutation_rate = float(self.mutation_rate_entry.get())

        if pop_size <= 0 or num_generations <= 0 or mutation_rate <= 0:
            messagebox.showerror("Error", "Please enter positive values for parameters.")
            return

        scheduler = TaskScheduler()
        scheduler.input_tasks(self.tasks)
        scheduler.input_num_resources(len(self.resources))
        scheduler.input_parameters(pop_size, num_generations, mutation_rate)
        best_schedule = scheduler.optimize()
        if best_schedule:
            messagebox.showinfo("Optimization Result", f"Best schedule: {best_schedule}")
        else:
            messagebox.showerror("Error", "No solution found. Please check your inputs.")
