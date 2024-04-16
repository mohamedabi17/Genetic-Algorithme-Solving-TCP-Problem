import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from sac import KnapsackApp
from tsp_problem_algorithm_genitic import GraphConverterApp
from ordonencement import TaskSchedulerGUI

def main():
    root = tk.Tk()
    root.title("Knapsack Problem Solved By Genetic Algorithm")
    root.attributes("-fullscreen", True)  # Set to fullscreen
    root.resizable(True, True)  
     

    # Add title label
    # title_label = ttk.Label(root, text="Genetic Algorithm", font=("Helvetica", 28, "bold"))
    # title_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


    # Load background image
    # image_path = 'images/background.jpg'
    # img = Image.open(image_path).resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    # background_image = ImageTk.PhotoImage(img)

    # image_path2 = 'images/background_red.jpg'
    # img2 = Image.open(image_path2).resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    # background_image2 = ImageTk.PhotoImage(img2)

    background_label = tk.Label(root)
    background_label.place(x=0, y=0)

    def open_first_interface():
        button1.place_forget()  # Hide the TCP PROBLEM button
        button2.place_forget()  # Hide the Knapsack Problem button
        app = GraphConverterApp(root)  

    def open_second_interface():
        button1.place_forget()  # Hide the TCP PROBLEM button
        button2.place_forget()  # Hide the Knapsack Problem button
        app = KnapsackApp(root)

    def open_third_interface():
        button1.place_forget()  # Hide the TCP PROBLEM button
        button2.place_forget()  # Hide the Knapsack Problem button
        button3.place_forget()  # Hide the Knapsack Problem button
        root.title("Task Scheduler")  # Set the window title
        app = TaskSchedulerGUI(root)  # Create an instance of TaskSchedulerGUI

    # Define button width and height
    button_width = root.winfo_screenwidth() // 5  # 20% of screen width
    button_height = 50

    # Define modern button style
    button_style = ttk.Style()
    button_style.theme_use('clam')  # Choose a modern theme (e.g., 'clam', 'alt', 'default')
    button_style.configure('Modern.TButton', font=('Arial', 12, 'bold'), foreground='black', width=button_width, height=button_height)

    # Load and resize button icons
    button_icons = [
        Image.open("images/tcp.jpg").resize((button_height, button_height), Image.LANCZOS),
        Image.open("images/sac.png").resize((button_height, button_height), Image.LANCZOS),
        Image.open("images/callendat.png").resize((button_height, button_height), Image.LANCZOS)
    ]
    button_icons = [ImageTk.PhotoImage(icon) for icon in button_icons]
    
        # title_label = ttk.Label(root, text="Genetic Algorithm", font=("Helvetica", 28, "bold"))
    # title_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
   # Add title label
    title_label = ttk.Label(
        root,
        text="Genetic Algorithm Problem Solver",
        font=("Helvetica", 28, "bold"),
        style='Modern.Label'
    )
    title_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)   # Center the label horizontally and position it vertically

    # Create buttons with icons
    button1 = ttk.Button(
        root,
        text="TCP PROBLEM",
        command=open_first_interface,
        image=button_icons[0],
        compound=tk.LEFT,
        style='Modern.TButton'
    )
    button1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)  # Center the button vertically

    button2 = ttk.Button(
        root,
        text="Knapsack Problem",
        command=open_second_interface,
        image=button_icons[1],
        compound=tk.LEFT,
        style='Modern.TButton'
    )
    button2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)  # Center the button vertically

    button3 = ttk.Button(
        root,
        text="Scheduling Problem",
        command=open_third_interface,
        image=button_icons[2],
        compound=tk.LEFT,
        style='Modern.TButton'
    )
    button3.place(relx=0.5, rely=0.8, anchor=tk.CENTER)  # Center the button vertically
    
    # Create a frame to hold the hide and return buttons
    button_frame = ttk.Frame(root)
    button_frame.place(relx=1, rely=0, anchor=tk.NE)  # Place the frame in the top-right corner

    # Add hide button
    hide_button = ttk.Button(
        button_frame,
        text="Hide",
        command=root.iconify,  # Minimize the window
        style='Modern.TButton'
    )
    hide_button.pack(side=tk.TOP, padx=10, pady=5)

    # Add return button
    return_button = ttk.Button(
        button_frame,
        text="Return",
        command=root.destroy,  # Close the window
        style='Modern.TButton'
    )
    return_button.pack(side=tk.TOP, padx=10, pady=5)
    root.mainloop()

if __name__ == "__main__":
    main()

