import tkinter as tk
from tkinter import messagebox

class CandyDispenser:
    def __init__(self, root):
        self.root = root
        self.root.title("Candy Dispenser Stack :)")
        
        # Stack for candies
        self.stack = []
        self.max_candies = 7  # Maximum capacity of the stack
        
        # Canvas for displaying candies and spring
        self.canvas = tk.Canvas(self.root, width=200, height=600, bg="white")
        self.canvas.pack(side=tk.LEFT, padx=20, pady=20)
        
        # Frame for buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.RIGHT, padx=20, pady=20)
        
        # Buttons
        tk.Button(self.button_frame, text="Push", bg="blue", fg="white", command=self.push_candy).pack(fill=tk.X, pady=5)
        tk.Button(self.button_frame, text="Pop", bg="red", fg="white", command=self.pop_candy).pack(fill=tk.X, pady=5)
        tk.Button(self.button_frame, text="Peek", bg="purple", fg="white", command=self.peek_candy).pack(fill=tk.X, pady=5)
        tk.Button(self.button_frame, text="Is Empty", bg="orange", fg="white", command=self.is_empty).pack(fill=tk.X, pady=5)
        tk.Button(self.button_frame, text="Len", bg="green", fg="white", command=self.show_length).pack(fill=tk.X, pady=5)
        
        # Candy colors
        self.candy_colors = ["pink", "red", "blue", "cyan", "orange", "purple", "green"]
        
        # Draw initial state
        self.update_canvas()

    def update_canvas(self):
        """Update the canvas to show the current stack and spring."""
        self.canvas.delete("all")
        
        # Calculate spring height based on stack size
        max_spring_height = 500  # Fully expanded spring
        min_spring_height = 200  # Fully compressed spring
        spring_height = min_spring_height + (len(self.stack) * 40)  # Dynamically change the size of the spring depending on pop or push

        
        # Draw spring coils
        base_y = 550  # Base of the spring
        top_y = spring_height  # Top of the spring
        coil_count = 10  # Number of coils
        coil_spacing = (base_y - top_y) / coil_count
        
        for i in range(coil_count + 1):
            y = base_y - i * coil_spacing
            if i % 2 == 0:
                self.canvas.create_line(80, y, 120, y, fill="blue")
            else:
                self.canvas.create_line(120, y, 80, y, fill="blue")
            
            # Draw diagonal lines to connect the coils
            if i < coil_count:
                next_y = base_y - (i + 1) * coil_spacing
                if i % 2 == 0:
                    self.canvas.create_line(120, y, 80, next_y, fill="blue")
                else:
                    self.canvas.create_line(80, y, 120, next_y, fill="blue")
        
        # Draw candies
        x1, y1 = 75, spring_height - 60  # Start above the spring
        for candy in self.stack:
            self.canvas.create_oval(x1, y1, x1 + 50, y1 + 50, fill=candy, outline="")
            y1 -= 60  # Adjust for the next candy

    def push_candy(self):
        """Push a candy onto the stack."""
        if len(self.stack) < self.max_candies:
            candy_color = self.candy_colors[len(self.stack)]  
            self.stack.append(candy_color)
            self.update_canvas()
        else:
            messagebox.showerror("Error", "Stack is full!")

    def pop_candy(self):
        """Pop a candy from the stack."""
        if self.stack:
            self.stack.pop()
            self.update_canvas()
        else:
            messagebox.showerror("Error", "Stack is empty!")

    def peek_candy(self):
        """Peek at the top candy."""
        if self.stack:
            messagebox.showinfo("Peek", f"Top candy color: {self.stack[-1]}")
        else:
            messagebox.showinfo("Peek", "Stack is empty!")

    def is_empty(self):
        """Check if the stack is empty."""
        messagebox.showinfo("Is Empty", f"Stack is empty: {len(self.stack) == 0}")

    def show_length(self):
        """Show the current length of the stack."""
        messagebox.showinfo("Length", f"Current stack length: {len(self.stack)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CandyDispenser(root)
    root.mainloop()
