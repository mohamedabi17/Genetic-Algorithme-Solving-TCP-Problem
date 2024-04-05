import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from customtkinter import CTkFrame
import numpy as np
from deap import creator, base, tools, algorithms
import random
import ctypes
from PIL import Image, ImageTk
# from GENETIC import main

import random  # Add this import statement at the beginning of your script

class GraphConverterApp:
    def __init__(self, master, background_image):
        self.master = master
        self.master.title("TSP Solver with Genetic Algorithm")
        self.master.attributes("-fullscreen", True)
        # self.master.attributes("-zoomed", True)
        self.master.configure(bg="white")
        self.dark_mode = False  # Default: Light Mode

        self.background_image = background_image

        self.points = []
        self.distances = None

        self.node_colors = ['blue', 'black', 'blue', 'black', 'blue', 'black','blue', 'black', 'blue', 'black', 'blue', 'black']

        self.button_frame = CTkFrame(self.master, fg_color="white")
        self.button_frame.pack(side=tk.TOP, pady=5)
        
        self.graph_canvas = tk.Canvas(self.master, bg="white", width=600, height=400)
        self.graph_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.graph_canvas.bind("<MouseWheel>", self.on_mousewheel)
        self.graph_canvas.bind("<Shift-MouseWheel>", self.on_shift_mousewheel)  
        
        self.graph_canvas.bind("<MouseWheel>", self.zoom)      
        
        self.result_text = tk.Text(self.master, height=10, width=50)
        self.result_text.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=10, pady=10)


        self.dark_mode_icon = ImageTk.PhotoImage(Image.open("images/dark_mode_icon.png").resize((15, 15)))
        self.draw_node_icon = ImageTk.PhotoImage(Image.open("images/draw_node_icon.png").resize((15, 15)))
        self.convert_icon = ImageTk.PhotoImage(Image.open("images/connect.jpg").resize((15, 15)))
        self.solve_icon = ImageTk.PhotoImage(Image.open("images/solve-complex-problems.jpg").resize((15, 15)))
        self.clear_icon = ImageTk.PhotoImage(Image.open("images/clear_icon.ico").resize((15, 15)))
        self.home_icon = ImageTk.PhotoImage(Image.open("images/home.ico").resize((15, 15)))
        self.exit_icon = ImageTk.PhotoImage(Image.open("images/exit.jpg").resize((15, 15)))
        self.random_distance_icon = ImageTk.PhotoImage(Image.open("images/random_distance_icon.jpg").resize((15, 15)))
        # Add an icon for the button




        self.dark_mode_button = ttk.Button(self.button_frame, text="Dark Mode", image=self.dark_mode_icon, compound=tk.LEFT, command=self.toggle_dark_mode, takefocus=0, style='CustomButton.TButton')
        self.dark_mode_button.pack(side=tk.TOP, padx=5, pady=5)

        padding_y = 5

        self.draw_node_button = ttk.Button(self.button_frame, text="Draw Node", image=self.draw_node_icon, compound=tk.LEFT, command=self.draw_node, takefocus=0, style='CustomButton.TButton')
        self.draw_node_button.pack(side=tk.TOP, padx=5, pady=padding_y)

        self.convert_button = ttk.Button(self.button_frame, text="Connect Nodes", image=self.convert_icon, compound=tk.LEFT, command=self.convert_to_matrix, takefocus=0, style='CustomButton.TButton')
        self.convert_button.pack(side=tk.TOP, padx=5, pady=padding_y)

        self.solve_button = ttk.Button(self.button_frame, text="Solve TSP", image=self.solve_icon, compound=tk.LEFT, command=self.solve_tsp, takefocus=0, style='CustomButton.TButton')
        self.solve_button.pack(side=tk.TOP, padx=5, pady=padding_y)

        self.clear_button = ttk.Button(self.button_frame, text="Clear Graph", image=self.clear_icon, compound=tk.LEFT, command=self.clear_graph, takefocus=0, style='CustomButton.TButton')
        self.clear_button.pack(side=tk.TOP, padx=5, pady=padding_y)

        self.home_button = ttk.Button(self.button_frame, text="Home", image=self.home_icon, compound=tk.LEFT, command=self.go_home, takefocus=0, style='CustomButton.TButton')
        self.home_button.pack(side=tk.TOP, padx=5, pady=padding_y)


        self.random_distance_button = ttk.Button(self.button_frame, text="Random Distances", image=self.random_distance_icon, compound=tk.LEFT, command=self.generate_random_distances, takefocus=0, style='CustomButton.TButton')
        self.random_distance_button.pack(side=tk.TOP, padx=5, pady=padding_y)
        
        self.exit_button = ttk.Button(self.button_frame, text="Exit", image=self.exit_icon, compound=tk.LEFT, command=self.exit_app, takefocus=0, style='CustomButton.TButton')
        self.exit_button.pack(side=tk.TOP, padx=5, pady=padding_y)

        self.button_frame.pack(side=tk.RIGHT, fill=tk.Y)

        style = ttk.Style()
        style.configure('CustomButton.TButton', foreground='blue', background='white', font=('Time new romain', 9, 'bold'))
        style.configure('Dark.TButton', foreground='black', background='black', font=('Time new romain', 9, 'bold'))

        self.node_count = 0
        self.connecting_nodes = False

    def generate_random_distances(self):
        if len(self.points) == 0:
            messagebox.showerror("Error", "Please create nodes first.")
            return

        if self.distances is not None:
            messagebox.showwarning("Warning", "Distances already converted to matrix.")
            return

        self.distances = np.zeros((len(self.points), len(self.points)))

        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                # Check if the distance is already set
                if self.distances[i][j] == 0:
                    # If not set, generate a random distance
                    distance = random.uniform(1, 100)  # Adjust the range according to your requirements
                    self.distances[i][j] = self.distances[j][i] = distance
                    # Update the canvas with the distance
                    self.graph_canvas.create_line(self.points[i][0], self.points[i][1], self.points[j][0], self.points[j][1], fill="black", width=2, tags="line")
                    self.graph_canvas.create_text((self.points[i][0] + self.points[j][0]) / 2, (self.points[i][1] + self.points[j][1]) / 2, text=str(distance), fill="black", font=("Time new romain", 12, "bold"), tags="text")
    
    def on_mousewheel(self, event):
        self.graph_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_shift_mousewheel(self, event):
        self.graph_canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")
    
    def zoom(self, event):
        scale_factor = 1.1  
        if event.delta > 0:  
            self.graph_canvas.scale("all", event.x, event.y, scale_factor, scale_factor)
        elif event.delta < 0:  
            self.graph_canvas.scale("all", event.x, event.y, 1 / scale_factor, 1 / scale_factor)
    

    def exit_app(self):
        self.master.destroy()
    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.master.config(bg="black")
            self.graph_canvas.config(bg="gray10")
            self.result_text.config(bg="gray10", fg="lightgreen")
            self.button_frame.configure(foreground="black")  
            for button in [self.dark_mode_button, self.draw_node_button, self.convert_button, self.solve_button, self.clear_button]:
                button.config(style='Dark.TButton')
            self.dark_mode_button.config(text="Light Mode")
            self.graph_canvas.itemconfig("line", fill="white")
            self.graph_canvas.itemconfig("text", fill="white")
        else:
            self.master.config(bg="white")
            self.graph_canvas.config(bg="white")
            self.result_text.config(bg="white", fg="blue")
            self.button_frame.configure(foreground="white")  
            for button in [self.dark_mode_button, self.draw_node_button, self.convert_button, self.solve_button, self.clear_button]:
                button.config(style='CustomButton.TButton')
            self.dark_mode_button.config(text="Dark Mode")
            self.graph_canvas.itemconfig("line", fill="black")
            self.graph_canvas.itemconfig("text", fill="black")

    def draw_node(self):
        if self.node_count >= len(self.node_colors) or self.node_count >= 12: 
            messagebox.showwarning("Warning", "Maximum number of nodes reached.")
            return

        self.graph_canvas.bind("<Button-1>", self.add_node)

    def add_node(self, event):
        x, y = event.x, event.y
        node_size = 20  
        self.points.append((x, y, self.node_count))
        self.graph_canvas.create_oval(x - node_size, y - node_size, x + node_size, y + node_size, fill=self.node_colors[self.node_count], outline=self.node_colors[self.node_count])
        self.graph_canvas.create_text(x, y, text=str(self.node_count + 1), fill="white", anchor=tk.CENTER, font=("Time new romain", 15, "bold"))
        self.node_count += 1
        self.graph_canvas.unbind("<Button-1>")

    def connect_nodes(self):
        if self.node_count < 2:
            messagebox.showerror("Error", "Please create at least 2 nodes.")
            return

        if self.connecting_nodes:
            self.connecting_nodes = False
            self.graph_canvas.unbind("<Button-1>")
            self.convert_button.config(state=tk.NORMAL)
        else:
            self.connecting_nodes = True
            self.convert_button.config(state=tk.DISABLED)
            self.graph_canvas.bind("<Button-1>", self.add_connection)
    
    

    def convert_to_matrix(self):
        if len(self.points) == 0:
            messagebox.showerror("Error", "Please create nodes first.")
            return

        if self.distances is not None:
            messagebox.showwarning("Warning", "Distances already converted to matrix.")
            return

        self.distances = np.zeros((len(self.points), len(self.points)))

        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                distance = simpledialog.askfloat("Distance", f"Enter distance between nodes {i + 1} and {j + 1}:")
                self.distances[i][j] = self.distances[j][i] = distance
                self.graph_canvas.create_line(self.points[i][0], self.points[i][1], self.points[j][0], self.points[j][1], fill="black", width=2, tags="line")
                self.graph_canvas.create_text((self.points[i][0] + self.points[j][0]) / 2, (self.points[i][1] + self.points[j][1]) / 2, text=str(distance), fill="black", font=("Time new romain", 12, "bold"), tags="text")

        self.result_text.insert(tk.END, "Distance Matrix:\n")
        for row in self.distances:
            self.result_text.insert(tk.END, ' '.join(map(str, row)) + '\n')
        self.result_text.insert(tk.END, '\n')

    def solve_tsp(self):
        if self.distances is None:
            messagebox.showerror("Error", "Please convert graph to matrix first.")
            return

        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        toolbox = base.Toolbox()
        toolbox.register("indices", random.sample, range(len(self.distances)), len(self.distances))
        toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        def evalTSP(individual):
            return sum(self.distances[individual[i - 1]][individual[i]] for i in range(len(individual))),

        toolbox.register("evaluate", evalTSP)
        toolbox.register("mate", tools.cxOrdered)
        toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
        toolbox.register("select", tools.selTournament, tournsize=3)

        pop = toolbox.population(n=50)

        result = algorithms.eaSimple(pop, toolbox, cxpb=0.8, mutpb=0.001, ngen=50, verbose=False)

        best_individual = tools.selBest(pop, k=1)[0]
        result_text = f'Best individual: {best_individual}\nFitness: {evalTSP(best_individual)}'
        self.result_text.insert(tk.END, result_text + '\n\n')
        self.result_text.see(tk.END)  

        messagebox.showinfo("Result", result_text)

    def clear_graph(self):
        self.graph_canvas.delete("all")
        self.points = []
        self.distances = None
        
        self.node_count = 0
        self.connecting_nodes = False
        self.convert_button.config(state=tk.NORMAL)
        self.solve_button.config(state=tk.NORMAL)
        self.result_text.delete('1.0', tk.END)

    def go_home(self):
        self.master.destroy()  
        # main()  



