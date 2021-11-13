import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
# setting up the screen for the game
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # turns off the screen updates

# snake head
head = turtle.Turtle()
head.speed(0)  # This is the animation speed
head.shape("square")
head.color("red")
head.penup()  # Make sure the segment doesn't draw on the screen
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Function
def go_up():
    if head.direction != "down":  # preventing the snake to get into its own body
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_left, "Left")
# main game loop
while True:
    wn.update()

    # Check for the collosion with the boundaries
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segment lis
        for segment in segments:
            segment.goto(1000, 1000)
        # clear the segment lis
        segments.clear()

        # Reset the score
        score = 0
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

        #Reset the delay
        delay=0.1
    # Check for the collosion with the food
    if head.distance(food) < 20:
        # Move food to another random spot
        x = random.randint(-290, 290)
        # because our center is (0,0)and height and the widtdh of the window is 600
        # so we have 300 to the left and 300 to the right and -290 and 290 is taken so
        # that the movement is within the boundaries
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay-=0.001

        # Incresase the Score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the send segments first in the reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for the collosing with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide the segment list
            for segment in segments:
                segment.goto(1000, 1000)
            # clear the segment lis
            segments.clear()

            # Reset the score
            score = 0
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
            #Reset the delay
            delay=0.1
    time.sleep(delay)

wn.mainloop()
