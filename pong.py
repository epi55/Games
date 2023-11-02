import turtle as t

# SETUP
t.setup(width=500, height=500)
t.bgcolor("black")

paddle1 = t.Turtle()
paddle1.shape("square")
paddle1.color("red")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy = 0

paddle2 = t.Turtle()
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)
paddle2.dy = 0

ball = t.t()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

game_over = False
winner = None
poinTurtle = {
    "player1": 0,
    "player2": 0
}
game_rules = {
    "max_poinTurtle": 3,
    "ball_speed": 3
}

score_display = t.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideTurtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0  Player 2: 0", align="center", font=("Arial", 24, "normal"))

paddle1.sety(paddle1.ycor() + paddle1.dy)
paddle2.sety(paddle2.ycor() + paddle2.dy)
ball.setx(ball.xcor() + ball.dx)
ball.sety(ball.ycor() + ball.dy)

# Check for game over conditions
if poinTurtle["player1"] == game_rules["max_poinTurtle"]:
    game_over = True
    winner = "player1"
elif poinTurtle["player2"] == game_rules["max_poinTurtle"]:
    game_over = True
    winner = "player2"

# Check for ball collision with paddles
if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2ycor() - 50):
    ball.setx(340)
    ball.dx *= -1
elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
    ball.setx(-340)
    ball.xy *= -1

# Check for ball going off screen
if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
    poinTurtle["player1"] += 1
elif ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    poinTurtle["player2"] += 1

# Check for ball colliding with top or bottom of screen
if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1
elif ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

# Update score display
score_display.clear()
score_display.write("Player 1: {}  Player 2: {}".format(poinTurtle["player1"], poinTurtle["player2"]), align="center", font=("Arial", 24, "normal"))

# Function to move paddles
def paddle1_up():
    paddle1.dy = 10

def paddle1_down():
    paddle1.dy = -10

def paddle2_up():
    paddle2.dy = 10

def paddle2_down():
    paddle2.dy = -10

t.listen()
t.onkeypress(paddle1_up, "w")
t.onkeypress(paddle1_down, "s")
t.onkeypress(paddle2_up, "Up")
t.onkeypress(paddle2_down, "Down")

# Game over screen
game_over_display = t.Turtle()
game_over_display.color("white")
game_over_display.penup()
game_over_display.hideTurtle()
game_over_display.goto(0, 0)
game_over_display.write("Game over! {} wins!".format(winner), align="center", font=("Arial", 36, "normal"))