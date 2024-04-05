import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from sac import KnapsackApp
from tsp_problem_algorithm_genitic import GraphConverterApp

def main():
    root = tk.Tk()
    root.title("TSP Solver with Genetic Algorithm")
    root.attributes("-fullscreen", True)  # Set to fullscreen
    root.configure(bg="white")
    root.resizable(False, False)  

    # Load background image
    image_path = 'images/background.jpg'
    img = Image.open(image_path).resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(img)
    image_path2 = 'images/background_red.jpg'
    img2 = Image.open(image_path2).resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    background_image2 = ImageTk.PhotoImage(img2)

    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0)
   

    def open_first_interface():
        button1.place_forget()  # Hide the TCP PROBLEM button
        button2.place_forget()  # Hide the Knapsack Problem button
        app = GraphConverterApp(root, background_image)  

    def open_second_interface():
            button1.place_forget()  # Hide the TCP PROBLEM button
            button2.place_forget()  # Hide the Knapsack Problem button
            app = KnapsackApp(root, background_image2)

    
    # Define button width and height
    button_width = root.winfo_screenwidth() // 5  # 20% of screen width
    button_height = 50

    # Define modern button style
    button_style = ttk.Style()
    button_style.theme_use('clam')  # Choose a modern theme (e.g., 'clam', 'alt', 'default')
    button_style.configure('Modern.TButton', font=('Arial', 12, 'bold'), foreground='white', background='blue', width=button_width, height=button_height)

    # Load and resize button icons
    button_icons = [
        Image.open("images/tcp.jpg").resize((button_height, button_height), Image.LANCZOS),
        Image.open("images/sac.png").resize((button_height, button_height), Image.LANCZOS)
    ]
    button_icons = [ImageTk.PhotoImage(icon) for icon in button_icons]

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

    root.mainloop()

if __name__ == "__main__":
    main()
