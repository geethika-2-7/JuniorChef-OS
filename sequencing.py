import tkinter as tk
import random


# --------------------------------------------------
# RECIPE DATA
# --------------------------------------------------

RECIPES = {
    "Chocolate Cookie": {
        "steps": [
            "Measure all the ingredients",
            "Mix flour and sugar",
            "Add butter",
            "Add milk and chocolate chips",
            "Mix to form the dough",
            "Shape the cookies",
            "Bake the cookies",
            "Serve and enjoy!"
        ]
    },

    "Pancake": {
        "steps": [
            "Measure all the ingredients",
            "Mix flour and sugar",
            "Add milk",
            "Add melted butter",
            "Mix to form the batter",
            "Heat the pan",
            "Cook the pancake",
            "Serve and enjoy!"
        ]
    }
}


# --------------------------------------------------
# SEQUENCING GAME
# --------------------------------------------------

class SequencingGame:

    def __init__(self, parent, recipe_name, on_complete):
        """
        parent      -> the main JuniorChef window
        recipe_name -> Chocolate Cookie or Pancake
        on_complete -> function called after the game finishes
        """

        self.parent = parent
        self.recipe_name = recipe_name
        self.on_complete = on_complete

        self.steps = RECIPES[recipe_name]["steps"]

        self.correct_order = list(range(len(self.steps)))
        self.selected_order = []

        self.buttons = []
        self.order_label = None

        self.build_screen()

    # --------------------------------------------------
    # CLEAR SCREEN
    # --------------------------------------------------

    def clear_screen(self):
        for widget in self.parent.winfo_children():
            widget.destroy()

    # --------------------------------------------------
    # CREATE GAME SCREEN
    # --------------------------------------------------

    def build_screen(self):

        self.clear_screen()

        self.parent.title("🍳 JuniorChef OS")
        self.parent.configure(bg="#FFF4E6")

        title = tk.Label(
            self.parent,
            text="🧩 COOKING SEQUENCE",
            font=("Arial", 24, "bold"),
            bg="#FFF4E6",
            fg="#7A3E22"
        )
        title.pack(pady=20)

        instruction = tk.Label(
            self.parent,
            text=(
                f"Arrange the {self.recipe_name} steps "
                "in the correct order!"
            ),
            font=("Arial", 14),
            bg="#FFF4E6",
            fg="#8B6B58"
        )
        instruction.pack(pady=10)

        self.order_label = tk.Label(
            self.parent,
            text="Selected steps: 0",
            font=("Arial", 12, "bold"),
            bg="#FFF4E6",
            fg="#7A3E22"
        )
        self.order_label.pack(pady=10)

        # Shuffle the step numbers
        shuffled_steps = list(range(len(self.steps)))
        random.shuffle(shuffled_steps)

        for step_number in shuffled_steps:

            button = tk.Button(
                self.parent,
                text=self.steps[step_number],
                font=("Arial", 11),
                width=45,
                bg="#FFE0CC",
                fg="#3B2418",
                activebackground="#FFD1B3",
                relief="raised",
                command=lambda n=step_number: self.select_step(n)
            )

            button.pack(pady=4)

            self.buttons.append(button)

        check_button = tk.Button(
            self.parent,
            text="✅ CHECK ORDER",
            font=("Arial", 13, "bold"),
            bg="#E87945",
            fg="white",
            activebackground="#D96532",
            padx=20,
            pady=8,
            command=self.check_sequence
        )
        check_button.pack(pady=20)

    # --------------------------------------------------
    # SELECT A STEP
    # --------------------------------------------------

    def select_step(self, step_number):

        # Prevent selecting the same step twice
        if step_number in self.selected_order:
            return

        self.selected_order.append(step_number)

        # Disable the selected button
        for button in self.buttons:

            if button["text"] == self.steps[step_number]:
                button.config(
                    state="disabled",
                    bg="#D8F3DC"
                )
                break

        self.order_label.config(
            text=f"Selected steps: {len(self.selected_order)}",
            fg="#7A3E22"
        )

    # --------------------------------------------------
    # CHECK ANSWER
    # --------------------------------------------------

    def check_sequence(self):

        # User has not selected every step
        if len(self.selected_order) < len(self.steps):

            self.order_label.config(
                text=(
                    f"Please select all {len(self.steps)} "
                    "steps first!"
                ),
                fg="#C0392B"
            )

            return

        # Check whether the order is correct
        if self.selected_order == self.correct_order:
            self.show_result(True)

        else:
            self.show_result(False)

    # --------------------------------------------------
    # RESULT
    # --------------------------------------------------

    def show_result(self, correct):

        self.clear_screen()

        if correct:

            title_text = "🎉 GREAT JOB!"

            result_text = (
                f"You completed the {self.recipe_name} "
                "sequence correctly!\n\n"
                "All the cooking steps are in the right order!"
            )

            result_color = "#3A8D40"

        else:

            title_text = "💡 ALMOST THERE!"

            result_text = (
                f"The {self.recipe_name} steps are not "
                "in the correct order yet.\n\n"
                "Don't worry — you can try again!"
            )

            result_color = "#C77700"

        title = tk.Label(
            self.parent,
            text=title_text,
            font=("Arial", 24, "bold"),
            bg="#FFF4E6",
            fg=result_color
        )
        title.pack(pady=30)

        result = tk.Label(
            self.parent,
            text=result_text,
            font=("Arial", 14),
            bg="#FFF4E6",
            fg="#7A3E22",
            justify="center"
        )
        result.pack(pady=20)

        retry_button = tk.Button(
            self.parent,
            text="🔄 TRY AGAIN",
            font=("Arial", 12, "bold"),
            bg="#E87945",
            fg="white",
            activebackground="#D96532",
            padx=20,
            pady=8,
            command=self.retry
        )
        retry_button.pack(pady=10)

        continue_button = tk.Button(
            self.parent,
            text="⭐ CONTINUE",
            font=("Arial", 12, "bold"),
            bg="#72C472",
            fg="white",
            activebackground="#5EAD5E",
            padx=20,
            pady=8,
            command=lambda: self.on_complete(correct)
        )
        continue_button.pack(pady=10)

    # --------------------------------------------------
    # RETRY
    # --------------------------------------------------

    def retry(self):

        self.selected_order = []
        self.buttons = []

        self.build_screen()


# --------------------------------------------------
# FUNCTION USED BY MAIN.PY
# --------------------------------------------------

def start_sequencing(parent, recipe_name, on_complete):
    """
    Starts the sequencing activity.

    parent      -> JuniorChef main window
    recipe_name -> "Chocolate Cookie" or "Pancake"
    on_complete -> function receiving True/False
    """

    if recipe_name not in RECIPES:
        print(f"Unknown recipe: {recipe_name}")
        return

    SequencingGame(
        parent,
        recipe_name,
        on_complete
    )




