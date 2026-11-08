import turtle
import random
import math
import time

screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.title("Happy Birthday, Tichho 💖")
screen.bgcolor("#040303")
screen.tracer(0)

message = turtle.Turtle(visible=False)
message.penup()
message.color("#ffdf6c")                      
message.goto(0, 250)
message.write("HAPPY BIRTHDAY!, Tichho", align="center",
              font=("Century School Book", 30, "bold","italic"))

subtitle = turtle.Turtle(visible=False)
subtitle.penup()
subtitle.color("#ff9ed8")
subtitle.goto(0, 210)
subtitle.write("To the sweetest sister in the world 💖",
               align="center", font=("Century School Book", 17, "bold", "italic"))

shayari = turtle.Turtle(visible=False)
shayari.penup()
shayari.color("#ffe6f2")

shayari.goto(0, 150)
shayari.write(
    "तेरी मुस्कान से रोशन मेरी हर शाम रहे।",
    align="center",
    font=("Century School Book", 14, "italic")
)

shayari.goto(0, 120)
shayari.write(
    "तेरी जिंदगी में खुशियों का पैगाम रहे।",
    align="center",
    font=("Century School Book", 14, "italic")
)

shayari.goto(0, 90)
shayari.write(
    "हर ख़्वाब तेरा हक़ीक़त बन जाए,",
    align="center",
    font=("Century School Book", 14, "italic")
)

shayari.goto(0, 60)
shayari.write(
    "Happy Birthday Tichho, आपका हर दिन खास रहे ! 💖",
    align="center",
    font=("Century School Book", 14, "bold", "italic")
)

cake = turtle.Turtle(visible=False)
cake.speed(0)
cake.pensize(3)

def filled_rect(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.color(color)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.penup()

cake.color("#f4f0ff")
cake.penup()
cake.goto(-170, -180)
cake.pendown()
cake.setheading(0)
cake.begin_fill()
cake.fillcolor("#f4f0ff")
cake.forward(340)
cake.left(90)
cake.forward(14)
cake.left(90)
cake.forward(340)
cake.left(90)
cake.forward(14)
cake.left(90)
cake.end_fill()
cake.penup()

filled_rect(cake, -145, -166, 290, 75, "#ff79ad")
filled_rect(cake, -125, -91, 250, 65, "#ffc5df")

for x in range(-125, 126, 25):
    cake.goto(x, -103)
    cake.dot(9, "#fff6fb")
for x in range(-145, 146, 29):
    cake.goto(x, -150)
    cake.dot(8, "#fff6fb")

candle_colors = ["#71e6ff", "#ffe36e", "#b9ff9a", "#c9a0ff", "#ff9c72"]
candle_x = [-90, -45, 0, 45, 90]
for x, color in zip(candle_x, candle_colors):
    filled_rect(cake, x - 6, -26, 12, 45, color)

flames = []
for x in candle_x:
    flame = turtle.Turtle(visible=True)
    flame.penup()
    flame.goto(x, 27)
    flame.shape("circle")
    flame.shapesize(0.65, 0.42)
    flame.color("#ffb52e")
    flame.showturtle()
    flames.append(flame)


confetti_colors = [
    "#ff6bcb", "#ffe66d", "#6be7ff", "#a7ff83",
    "#c8a2ff", "#ff9671", "#ffffff"
]
confetti = []
for _ in range(90):
    piece = turtle.Turtle(visible=False)
    piece.penup()
    piece.shape(random.choice(["circle", "square", "triangle"]))
    piece.color(random.choice(confetti_colors))
    piece.shapesize(random.uniform(0.25, 0.65))
    piece.goto(random.randint(-430, 430), random.randint(-320, 340))
    piece.showturtle()
    confetti.append({
        "turtle": piece,
        "speed": random.uniform(1.5, 5),
        "drift": random.uniform(-1.4, 1.4)
    })

decorations = []
for _ in range(18):
    d = turtle.Turtle(visible=False)
    d.penup()
    d.color(random.choice(["#ff77aa", "#ffdf6c", "#bca7ff", "#ffffff"]))
    d.goto(random.randint(-420, 420), random.randint(-120, 180))
    d.write(random.choice(["♥", "★", "✦"]), align="center",
            font=("Century School Book", random.randint(12, 23), "bold", "italic"))
    decorations.append(d)

wish = turtle.Turtle(visible=False)
wish.penup()
wish.color("#ffffff")
wish.goto(0, -245)
wish.write("May your day be filled with love, laughter & magic!",
           align="center", font=("Century School Book", 14, "normal"))

wish2 = turtle.Turtle(visible=False)
wish2.penup()
wish2.color("#ff9ed8")
wish2.goto(0, -278)
wish2.write("Lots of love, always! 💕",
            align="center", font=("Century School Book", 16, "bold"))

frame = 0
try:
    while True:
        screen.update()
        frame += 1

        for item in confetti:
            piece = item["turtle"]
            x, y = piece.position()
            piece.goto(x + item["drift"], y - item["speed"])
            if y < -340:
                piece.goto(random.randint(-430, 430), 350)
                piece.color(random.choice(confetti_colors))

        for i, flame in enumerate(flames):
            flame.shapesize(
                random.uniform(0.45, 0.8),
                random.uniform(0.36, 0.5)
            )
            flame.color(random.choice(["#ffb52e", "#ffe66d", "#ff784f"]))

        message.color("#ffdf6c" if frame % 20 < 10 else "#9effca")

        time.sleep(0.035)

except turtle.Terminator:
    pass
