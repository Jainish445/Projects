import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Pac-Man setup
pacman = turtle.Turtle()
pacman.shape("circle")
pacman.color("yellow")
pacman.penup()
pacman.speed(0)

# Score setup
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-280, 260)
score_display.write(f"Score: {score}", align="left", font=("Arial", 14, "normal"))

# Maze walls
walls = []
def create_wall(x, y, width, height):
    wall = turtle.Turtle()
    wall.shape("square")
    wall.color("blue")
    wall.shapesize(stretch_wid=height/20, stretch_len=width/20)
    wall.penup()
    wall.goto(x, y)
    walls.append(wall)

# Defining the maze structure
maze = [
    (-200, 200, 400, 20), (200, 200, 20, 400), (200, -200, 400, 20), (-200, -200, 20, 400),
    (-100, 150, 200, 20), (100, 100, 20, 100), (-100, 50, 200, 20), (-100, -50, 200, 20),
    (0, -100, 20, 100), (-100, -150, 200, 20)
]

for wall in maze:
    create_wall(*wall)

# Food setup
foods = []
def create_food(x, y):
    food = turtle.Turtle()
    food.shape("circle")
    food.color("white")
    food.penup()
    food.goto(x, y)
    foods.append(food)

# Generating multiple food items
for _ in range(10):
    x = random.randint(-180, 180)
    y = random.randint(-180, 180)
    create_food(x, y)

def reset_game():
    global score
    pacman.goto(0, 0)  # Reset Pac-Man's position
    score = 0
    score_display.clear()
    score_display.write(f"Score: {score}", align="left", font=("Arial", 14, "normal"))
    for food in foods:
        food.goto(random.randint(-180, 180), random.randint(-180, 180))

# Movement setup
def move(x, y):
    global score
    new_x, new_y = pacman.xcor() + x, pacman.ycor() + y
    for wall in walls:
        if wall.distance(new_x, new_y) < 20:
            reset_game()
            return  # Restart game if colliding with a wall
    pacman.goto(new_x, new_y)
    
    # Check for food collision
    for food in foods:
        if pacman.distance(food) < 15:
            food.goto(1000, 1000)  # Move food off-screen
            foods.remove(food)
            score += 10
            score_display.clear()
            score_display.write(f"Score: {score}", align="left", font=("Arial", 14, "normal"))

# Controls
screen.listen()
screen.onkey(lambda: move(0, 20), "Up")
screen.onkey(lambda: move(0, -20), "Down")
screen.onkey(lambda: move(-20, 0), "Left")
screen.onkey(lambda: move(20, 0), "Right")

# Start game loop
while True:
    screen.update()