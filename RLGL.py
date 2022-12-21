import tkinter as tk
import random

class RedLightGreenLight(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the title of the window
        self.title("Red Light Green Light")

        # Set the size of the window
        self.geometry("200x200")

        # Create a frame to hold the light, the button, and the score label
        frame = tk.Frame(self)
        frame.pack()

        # Create a light that will change color
        self.light = tk.Label(frame, text="", bg="red", width=10, height=5)
        self.light.pack()

        # Create a button to start the automatic light change
        self.button = tk.Button(frame, text="Start game", command=self.start_automatic_change)
        self.button.pack()

        # Create a label to display the score
        self.score = tk.IntVar()
        self.score.set(0)  # Initialize the score to 0
        self.score_label = tk.Label(frame, textvariable=self.score)
        self.score_label.pack()

        # Set the focus on the root window so we can catch key events
        self.focus_set()

        # Bind the key press event to the key press handler
        self.bind("<KeyPress>", self.key_press)


    def toggle_light(self):
        # Toggle the light between red and green
        if self.light['bg'] == "red":
            self.light['bg'] = "green"
        else:
            self.light['bg'] = "red"

    def start_automatic_change(self):
        # initialise the button incase of bad times
        self.button.config(state="normal")
        # Generate a random key to press
        self.key_to_press = random.choice(["a", "s", "d", "f", "g", "h", "j", "k", "l"])

        # Update the light and the score label
        self.light.config(text=self.key_to_press)

        # Start the automatic light change
        self.toggle_light()
        self.after(random.randint(1000, 5000), self.start_automatic_change)
        self.button.config(state="disabled")

    def key_press(self, event):
        # Check if the light is red
        if self.light['bg'] == "red":
            # The user loses the game
            self.light.config(text="You lost!")
            self.unbind("<KeyPress>")
        else:
            # Check if the key pressed is the key to press
            if event.char == self.key_to_press:
                # Increment the score and update the score label
                self.score.set(self.score.get() + 1)
                
                # Check if the user has scored 20 points
                if self.score.get() == 20:
                    # The user wins the game
                    self.light.config(text="You won!")
                    self.unbind("<KeyPress>")

# Create the game and start the main loop
game = RedLightGreenLight()
game.mainloop()
