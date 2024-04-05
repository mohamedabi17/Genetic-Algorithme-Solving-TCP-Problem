import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from sac import KnapsackApp
from tsp_problem_algorithm_genitic import GraphConverterApp

def main():
    root = tk.Tk()
    root.title("TSP Solver with Genetic Algorithm")
    root.geometry("1200x800")
    root.configure(bg="white")
    root.resizable(False, False)  

    # Load background image
    image_path = 'images/background.jpg'
    img = Image.open(image_path).resize((1200, 800), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(img)
    image_path2 = 'images/background_red.jpg'
    img2 = Image.open(image_path2).resize((1200, 800), Image.LANCZOS)
    background_image2 = ImageTk.PhotoImage(img2)

    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def open_first_interface():
        button1.place_forget()  # Hide the TCP PROBLEM button
        button2.place_forget()  # Hide the Knapsack Problem button
        app = GraphConverterApp(root, background_image)  

    def open_second_interface():
            button1.place_forget()  # Hide the TCP PROBLEM button
            button2.place_forget()  # Hide the Knapsack Problem button
            app = KnapsackApp(root, background_image2)

    # Adjust the width and height to your preference
    button_width = 200
    button_height = 50

    # Modern button style
    button_style = ttk.Style()
    button_style.theme_use('clam')  # Choose a modern theme (e.g., 'clam', 'alt', 'default')

    button1 = ttk.Button(
        root,
        text="TCP PROBLEM",
        command=open_first_interface,
        style='Modern.TButton'
    )
    button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the button

    button2 = ttk.Button(
        root,
        text="Knapsack Problem",
        command=open_second_interface,
        style='Modern.TButton'
    )
    button2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)  # Center the button

    # Define modern button style
    button_style.configure('Modern.TButton', font=('Arial', 12, 'bold'), foreground='white', background='#4CAF50', width=button_width, height=button_height)

    root.mainloop()

if __name__ == "__main__":
    main()
