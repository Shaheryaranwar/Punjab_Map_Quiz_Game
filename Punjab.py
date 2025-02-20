import turtle
import pandas as pd
import time

# 🏁 Setup Screen
screen = turtle.Screen()
screen.title("My Quiz Punjab State Game")
image = "punjab.gif"
screen.bgcolor("Black")
screen.addshape(image)
turtle.shape(image)

# 📂 Load State Data
df = pd.read_csv("punjab_1.csv")
all_state = df.state.to_list()

# 🎯 Game Variables
guess_answer = []
start_time = time.time()  # 🕒 Start the timer

# 🎮 Game Loop
while len(guess_answer) < 35:
    input_state = screen.textinput(
        title=f"{len(guess_answer)}/35 Guess the State",
        prompt="What is another state name?"
    )

    if not input_state:
        continue  # Ignore empty input

    input_state = input_state.title()

    if input_state in all_state and input_state not in guess_answer:
        guess_answer.append(input_state)

        # 📍 Place Text on Map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == input_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(input_state)

# ⏳ Calculate Total Time Taken
total_time = round(time.time() - start_time, 2)  # Convert to seconds

# 🎉 Show Final Message
turtle.textinput("Quiz Completed 🎉", f"✅ You passed the quiz in {total_time} seconds!")

screen.exitonclick()
