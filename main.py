import tkinter as tk
from sequencing import start_sequencing
score = 0
current_recipe = ""
ingredient_frame = None
answer_frame = None
progress_label = None
score_label = None
pancake_button = None

def go_home():
    lesson_frame.pack(pady=10)

    title.config(text="🍳 JUNIORCHEF OS")
    welcome.config(text="Learn • Cook • Play!")

    start_button.config(
        text="🍪 START COOKING",
        command=start_cooking
    )
    start_button.pack(pady=30)

def start_cooking():
    global score ,pancake_button
    score = 0
    lesson_frame.pack_forget()

    title.config(text="🍳 CHOOSE YOUR RECIPE")
    welcome.config(text="Pick a recipe to start cooking!")

    start_button.config(
        text="🍪 CHOCOLATE COOKIES",
        command=choose_cookie
    )
    start_button.pack(pady=10)
    if pancake_button is not None:
        pancake_button.destroy()
        pancake_button = None
    pancake_button = tk.Button(
        window,
        text="🥞 PANCAKES",
        font=("Arial", 16, "bold"),
        width=20,
        bg="#E87945",
        fg="white",
        activebackground="#D96532",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=choose_pancake
    )
    pancake_button.pack(pady=10)
def choose_pancake():
    global pancake_button
    global current_recipe
    current_recipe = "Pancake"
    if pancake_button is not None:
        pancake_button.destroy()
        pancake_button = None

    title.config(text="🥞 PANCAKES")
    welcome.config(
        text="Let's make some fluffy pancakes! 🥞\n\n"
             "We'll measure the ingredients carefully."
    )

    start_button.config(
        text="🥣 START MEASURING",
        command=start_pancake_measuring
    )
    start_button.pack(pady=30)
def start_pancake_measuring():
    start_button.pack_forget()

    title.config(text="🥞 PANCAKE INGREDIENTS")
    welcome.config(
        text="Measure each ingredient carefully! 🥣"
    )

    global ingredient_frame

    ingredient_frame = tk.Frame(
        window,
        bg="#FFE8D1",
        padx=20,
        pady=10
    )
    ingredient_frame.pack(pady=10)

    ingredients_heading = tk.Label(
        ingredient_frame,
        text="🥞 PANCAKE RECIPE",
        font=("Arial", 16, "bold"),
        bg="#FFE8D1",
        fg="#7A3E22"
    )
    ingredients_heading.pack(pady=5)

    ingredients = [
        "🌾  Flour          1 cup",
        "🥛  Milk           1 cup",
        "🍬  Sugar          1/2 cup",
        "🧈  Butter         1/4 cup"
    ]

    for ingredient in ingredients:
        ingredient_label = tk.Label(
            ingredient_frame,
            text=ingredient,
            font=("Arial", 14),
            bg="#FFF4E6",
            fg="#7A3E22"
        )
        ingredient_label.pack(pady=4)

    start_button.config(
        text="🥣 START MEASURING",
        command=pancake_measurement
    )
    start_button.pack(pady=20)
def pancake_measurement():
    ingredient_frame.destroy()
    start_button.pack_forget()

    title.config(text="🥞 MEASUREMENT CHALLENGE")
    welcome.config(
        text="The recipe needs 1 cup of milk.\n"
             "You have a 1/2-cup measuring scoop.\n\n"
             "🥛 How many scoops do you need?"
    )

    global answer_frame

    answer_frame = tk.Frame(
        window,
        bg="#FFF4E6"
    )
    answer_frame.pack(pady=20)

    button1 = tk.Button(
        answer_frame,
        text="1 SCOOP",
        font=("Arial", 14, "bold"),
        width=15,
        command=wrong_pancake_measurement
    )
    button1.pack(pady=5)

    button2 = tk.Button(
        answer_frame,
        text="2 SCOOPS",
        font=("Arial", 14, "bold"),
        width=15,
        command=correct_pancake_measurement
    )
    button2.pack(pady=5)

    button3 = tk.Button(
        answer_frame,
        text="3 SCOOPS",
        font=("Arial", 14, "bold"),
        width=15,
        command=wrong_pancake_measurement
    )
    button3.pack(pady=5)
def wrong_pancake_measurement():
    title.config(text="💭 TRY AGAIN!")
    welcome.config(
        text="Not quite!\n\n"
             "You need 1 cup of milk.\n"
             "Each scoop holds 1/2 cup.\n\n"
             "Try again! 🥛"
    )

def correct_pancake_measurement():
    global score
    score += 1
    score_label.config(text=f"⭐ Score: {score}")
    clear_answers()

    title.config(text="🎉 CORRECT!")
    welcome.config(
        text="Great job!\n"
             "You got the measurement right!\n\n"
             "1/2 cup + 1/2 cup = 1 cup\n"
             "So you need 2 scoops of milk! 🥛"
    )

    start_button.config(
        text="➡️ CONTINUE",
        command=pancake_fraction
    )
    start_button.pack(pady=30)
def pancake_fraction():
    clear_answers()
    start_button.pack_forget()

    title.config(text="🧮 PANCAKE FRACTION CHALLENGE")
    welcome.config(
        text="The recipe needs 1/2 cup of sugar.\n"
             "You already added 1/4 cup.\n\n"
             "🧮 How much more sugar do you need?"
    )

    global answer_frame

    answer_frame = tk.Frame(
        window,
        bg="#FFF4E6"
    )
    answer_frame.pack(pady=20)

    button1 = tk.Button(
        answer_frame,
        text="1/4 CUP",
        font=("Arial", 14, "bold"),
        width=15,
        command=correct_pancake_fraction
    )
    button1.pack(pady=5)

    button2 = tk.Button(
        answer_frame,
        text="1/2 CUP",
        font=("Arial", 14, "bold"),
        width=15,
        command=wrong_pancake_fraction
    )
    button2.pack(pady=5)

    button3 = tk.Button(
        answer_frame,
        text="3/4 CUP",
        font=("Arial", 14, "bold"),
        width=15,
        command=wrong_pancake_fraction
    )
    button3.pack(pady=5)
def wrong_pancake_fraction():
    title.config(text="💭 TRY AGAIN!")
    welcome.config(
        text="Not quite!\n\n"
             "The recipe needs 1/2 cup.\n"
             "You already added 1/4 cup.\n\n"
             "Think: 1/2 - 1/4 = ? 🧮"
    )
def correct_pancake_fraction():
    global score
    score += 1
    score_label.config(text=f"⭐ Score: {score}")
    clear_answers()

    title.config(text="🎉 GREAT JOB!")
    welcome.config(
        text="You got the fraction right!\n\n"
             "1/2 - 1/4 = 1/4\n"
             "You need 1/4 cup more sugar! 🍬"
    )

    start_button.config(
        text="➡️ CONTINUE COOKING",
        command=finish_pancake
    )
    start_button.pack(pady=30)
def finish_pancake():
    clear_answers()
    progress_label.config(text="Step 3 of 3 🧩")

    title.config(text="🧩 COOKING SEQUENCE")
    welcome.config(
        text="Now let's put the pancake cooking steps\n"
             "in the correct order!\n\n"
             "Your next challenge is to arrange the steps."
    )

    start_button.config(
        text="🧩 START SEQUENCING",
        command=start_sequence
    )
    start_button.pack(pady=30)
def choose_cookie():
    global current_recipe, pancake_button
    current_recipe = "Chocolate Cookie"
    if pancake_button is not None:
        pancake_button.destroy()
        pancake_button = None
    progress_label.config(text="Step 1 of 3 🥣")
    score_label.config(text="⭐ Score: 0")
    title.config(text="🍪 CHOCOLATE COOKIES")
    welcome.config(
        text="Let's bake some delicious cookies! 🍪\n\n"
         "First, we'll measure the ingredients carefully."
    )
    global ingredient_frame

    ingredient_frame = tk.Frame(
        window,
        bg="#FFE8D1",
        padx=20,
        pady=10
    )
    ingredient_frame.pack(pady=10)
    recipe_heading = tk.Label(
        ingredient_frame,
        text="🍪 CHOCOLATE COOKIE RECIPE",
        font=("Arial", 16, "bold"),
        bg="#FFE8D1",
        fg="#7A3E22"
    )
    recipe_heading.pack(pady=5)
    recipe_instruction = tk.Label(
        ingredient_frame,
        text="Measure each ingredient carefully! 🥣",
        font=("Arial", 11, "italic"),
        bg="#FFE8D1",
        fg="#8B6B58"
    )
    recipe_instruction.pack(pady=3)
    ingredients_heading = tk.Label(
    ingredient_frame,
    text="🧺 INGREDIENTS",
    font=("Arial", 13, "bold"),
    bg="#FFE8D1",
    fg="#7A3E22"
)
    ingredients_heading.pack(pady=8)
    ingredients = [
        "🌾  Flour              1 cup",
        "🧈  Butter             1/2 cup",
        "🍬  Sugar              1/2 cup",
        "🍫  Chocolate Chips    1/2 cup"
    ]

    for ingredient in ingredients:
        ingredient_label = tk.Label(
            ingredient_frame,
            text=ingredient,
            font=("Arial", 14),
            bg="#FFF4E6",
            fg="#7A3E22"
        )
        ingredient_label.pack(pady=4)

    start_button.config(
        text="🥣 START MEASURING",
        command=start_measuring
)

def clear_answers():
    global answer_frame
    if answer_frame is not None:
        answer_frame.destroy()
        answer_frame = None
def start_measuring():
    ingredient_frame.destroy()
    start_button.pack_forget()

    title.config(text="🥣 MEASUREMENT CHALLENGE")
    welcome.config(
        text="The recipe needs 1 cup of flour.\n"
             "You have a 1/2-cup measuring scoop.\n\n"
             "🥣 MEASURING TIP\n"
            "Two 1/2-cup scoops make 1 whole cup!\n\n"
             "How many scoops do you need?"
    )

    global answer_frame

    answer_frame = tk.Frame(
        window,
        bg="#FFF4E6"
    )
    answer_frame.pack(pady=20)

    button1 = tk.Button(
        answer_frame,
        text="1 SCOOP",
        font=("Arial", 14, "bold"),
        width=15 ,
        command=wrong_measurement
    )
    button1.pack(pady=5)

    button2 = tk.Button(
        answer_frame,
        text="2 SCOOPS",
        font=("Arial", 14, "bold"),
        width=15,
        command=correct_measurement
    )
    button2.pack(pady=5)

    button3 = tk.Button(
        answer_frame,
        text="3 SCOOPS",
        font=("Arial", 14, "bold"),
        width=15 ,
        command=wrong_measurement
    )
    button3.pack(pady=5)
def wrong_measurement():
    title.config(text="💭 TRY AGAIN!")
    welcome.config(
        text="Not quite!\n\n"
             "Remember: you need 1 cup.\n"
             "Each scoop holds 1/2 cup.\n\n"
             "Try choosing another answer!"
    )    
def correct_measurement():
    global score
    score += 1
    score_label.config(text=f"⭐ Score: {score}")
    clear_answers()
    title.config(text="🎉 CORRECT!")
    welcome.config(
        text="Great job!\n"
             "You got the measurement right!\n\n"
             "1/2 cup + 1/2 cup = 1 cup\n"
             "You need 2 scoops of flour! 🥣"
    )
    start_button.config(
        text="➡️ CONTINUE",
        command=next_activity
    )
    start_button.pack(pady=30) 
def next_activity():
    clear_answers()
    start_button.pack_forget()
    progress_label.config(text="Step 2 of 3 🧮")

    title.config(text="🧮 FRACTION CHALLENGE")
    welcome.config(
        text="The recipe needs 1 1/2 cups of milk.\n"
             "You have a 1/2-cup measuring scoop.\n\n"
             "🧮 FRACTION TIP\n"
             "1 1/2 cups = three 1/2-cup scoops!\n\n"
             "How many scoops do you need?"
    )

    global answer_frame

    answer_frame = tk.Frame(
        window,
        bg="#FFF4E6"
    )
    answer_frame.pack(pady=20)

    button1 = tk.Button(
        answer_frame,
        text="2 SCOOPS",
        font=("Arial", 14, "bold"),
        width=15,
        command=wrong_fraction
    )
    button1.pack(pady=5)

    button2 = tk.Button(
        answer_frame,
        text="3 SCOOPS",
        font=("Arial", 14, "bold"),
        width=15,
        command=correct_fraction
    )
    button2.pack(pady=5)

    button3 = tk.Button(
        answer_frame,
        text="4 SCOOPS",
        font=("Arial", 14, "bold"),
        width=15,
        command=wrong_fraction
    )
    button3.pack(pady=5)  
def wrong_fraction():
    title.config(text="💭 TRY AGAIN!")
    welcome.config(
        text="Not quite!\n\n"
             "Remember: 1 1/2 cups means 3 halves.\n"
             "Each scoop is 1/2 cup.\n"
             "So you need 3 scoops! 🧮\n\n"
             "Try again!"
    )
def correct_fraction():
    global score
    score += 1
    score_label.config(text=f"⭐ Score: {score}")
    clear_answers()

    title.config(text="🎉 GREAT JOB!")
    welcome.config(
        text="You got it!\n"
            "You got the fraction right!\n\n"
             "1/2 + 1/2 + 1/2 = 1 1/2 cups\n"
             "That's 3 scoops of milk! 🥛"
    )

    start_button.config(
        text="➡️ CONTINUE COOKING",
        command=finish_math
    )
    start_button.pack(pady=30)
def finish_math():
    clear_answers()
    progress_label.config(text="Step 3 of 3 🧩")
    title.config(text="🧩 COOKING SEQUENCE")
    welcome.config(
        text="Now let's put the cooking steps in the correct order!\n\n"
             "Your next challenge is to arrange the steps."
    )

    start_button.config(
        text="🧩 START SEQUENCING",
        command=start_sequence
    )
    start_button.pack(pady=30)
def start_sequence():
    clear_answers()

    title.config(text="🧩 COOKING SEQUENCE")
    welcome.config(
        text="Arrange the cooking steps in the correct order!\n\n"
             "Choose the steps in the correct sequence."
    )

    start_button.pack_forget()
    progress_label.pack_forget()
    score_label.pack_forget()

    start_sequencing(
        window,
        current_recipe,
        sequencing_finished
    )
def sequencing_finished(correct):
    global score

    if correct:
        score += 1

    show_score()
def show_score():
    clear_answers()
    progress_label.pack_forget()
    score_label.pack_forget()
    title.config(text="⭐ GREAT JOB!")
    welcome.config(
        text=f"You completed the {current_recipe} activity!\n\n"
             "Measurement: ✓\n"
             "Fractions: ✓\n"
             "Sequencing: ✓\n\n"
             f"🏆 YOUR SCORE: {int((score / 3) * 100)}%"
    )
    start_button.config(
        text="🍪 COOK AGAIN",
        command=start_cooking
    )
    start_button.pack(pady=30)
        
# Create the main window
window = tk.Tk()

# Window title
window.title("JuniorChef OS")

# Window size
window.geometry("800x500")
window.configure(bg="#FFF4E6")

# Main title
title = tk.Label(window, text="🍳 JUNIORCHEF OS", font=("Arial", 28, "bold"),bg="#FFF4E6",fg="#7A3E22")
title.pack(pady=40)
progress_label = tk.Label(
    window,
    text="",
    font=("Arial", 12, "bold"),
    bg="#FFF4E6",
    fg="#D96532"
)
progress_label.pack()
score_label = tk.Label(
    window,
    text="",
    font=("Arial", 12, "bold"),
    bg="#FFF4E6",
    fg="#7A3E22"
)
score_label.pack()
welcome = tk.Label(
    window,
    text="Learn • Cook • Play!",
    font=("Arial", 16),
    bg="#FFF4E6",
    fg="#8B6B58"
)
welcome.pack()
lesson_frame = tk.Frame(
    window,
    bg="#FFE8D1",
    padx=20,
    pady=10
)
lesson_frame.pack(pady=10)

lesson_title = tk.Label(
    lesson_frame,
    text="👩‍🍳 TODAY'S LESSON",
    font=("Arial", 14, "bold"),
    bg="#FFE8D1",
    fg="#7A3E22"
)
lesson_title.pack(pady=5)

lesson_text = tk.Label(
    lesson_frame,
    text="🥣 Measurements    🧮 Fractions    🧩 Cooking Steps",
    font=("Arial", 12),
    bg="#FFE8D1",
    fg="#8B6B58"
)
lesson_text.pack()
# Start Cooking button
start_button = tk.Button(
    window,
    text="🍪 START COOKING",
    font=("Arial", 16,"bold"),
    width=20,
    bg="#E87945",
    fg="white",
    activebackground="#D96532",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=start_cooking
)
start_button.pack(pady=30)

# Keep the window open
window.mainloop()