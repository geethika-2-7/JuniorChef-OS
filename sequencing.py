import tkinter as tk
import random

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


class SequencingGame:
    def __init__(self, parent, recipe_name, on_complete):
        self.parent = parent
        self.recipe_name = recipe_name
        self.on_complete = on_complete

        self.steps = RECIPES[recipe_name]["steps"]
        self.correct_order = list(range(len(self.steps)))
        self.selected_order = []
        self.buttons = []

        self.game_window = tk.Toplevel(parent)
        self.game_window.title("🍳 JuniorChef - Cooking Sequence")
        self.game_window.geometry("700x650")
        self.game_window.configure(bg="#FFF4E6")

        self.build_screen()

    def clear_screen(self):
        for widget in self.game_window.winfo_children():
            widget.destroy()

    def build_screen(self):
        self.clear_screen()

        self.selected_order = []
        self.buttons = []

        title = tk.Label(
            self.game_window,
            text="🧩 COOKING SEQUENCE",
            font=("Arial", 24, "bold"),
            bg="#FFF4E6",
            fg="#7A3E22"
        )
        title.pack(pady=20)

        instruction = tk.Label(
            self.game_window,
            text=f"Arrange the {self.recipe_name} steps in the correct order!",
            font=("Arial", 14),
            bg="#FFF4E6",
            fg="#8B6B58"
        )
        instruction.pack(pady=10)

        self.order_label = tk.Label(
            self.game_window,
            text="Selected steps: 0",
            font=("Arial", 12, "bold"),
            bg="#FFF4E6",
            fg="#7A3E22"
        )
        self.order_label.pack(pady=10)

        shuffled_steps = list(range(len(self.steps)))
        random.shuffle(shuffled_steps)

        for step_number in shuffled_steps:
            button = tk.Button(
                self.game_window,
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
            self.game_window,
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

    def select_step(self, step_number):
        if step_number in self.selected_order:
            return

        self.selected_order.append(step_number)

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

    def check_sequence(self):
        if len(self.selected_order) < len(self.steps):
            self.order_label.config(
                text=f"Please select all {len(self.steps)} steps first!",
                fg="#C0392B"
            )
            return

        if self.selected_order == self.correct_order:
            self.show_result(True)
        else:
            self.show_result(False)

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
            self.game_window,
            text=title_text,
            font=("Arial", 24, "bold"),
            bg="#FFF4E6",
            fg=result_color
        )
        title.pack(pady=30)

        result = tk.Label(
            self.game_window,
            text=result_text,
            font=("Arial", 14),
            bg="#FFF4E6",
            fg="#7A3E22",
            justify="center"
        )
        result.pack(pady=20)

        retry_button = tk.Button(
            self.game_window,
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
            self.game_window,
            text="⭐ CONTINUE",
            font=("Arial", 12, "bold"),
            bg="#72C472",
            fg="white",
            activebackground="#5EAD5E",
            padx=20,
            pady=8,
            command=lambda: self.finish(correct)
        )
        continue_button.pack(pady=10)

    def retry(self):
        self.build_screen()

    def finish(self, correct):
        self.game_window.destroy()
        self.on_complete(correct)


def start_sequencing(parent, recipe_name, on_complete):
    if recipe_name not in RECIPES:
        print(f"Unknown recipe: {recipe_name}")
        return

    SequencingGame(parent, recipe_name, on_complete)