#import libarary
import turtle

# ^^^^^^^^^^^^^^^^^^^^^^^ windows setup ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
window = turtle.Screen()
window.title('ping pong game')
window.setup(width=800 , height=600)
window.tracer(0)
window.bgcolor(.1,.1,.1)

#=====================objects

#ball
ball= turtle.Turtle()
ball.speed(0)# defult range from 1 to 10     0 or 10 means that is fast
ball.shape("circle")
ball.color('white')
ball.shapesize(stretch_len=1 , stretch_wid=1)
ball.goto(0,0) #start position
ball.penup()
ball_dx, ball_dy = 1, 1
ball_speed = .5



#center_line
center_line=turtle.Turtle()
center_line.speed(0)# defult range from 1 to 10     0 or 10 means that is fast
center_line.shape("square")
center_line.color('blue')
center_line.shapesize(stretch_len=.1 , stretch_wid=20)
center_line.goto(x=0 , y=0)  #start position
center_line.penup()


# player1
player1=turtle.Turtle()
player1.speed(0)# defult range from 1 to 10     0 or 10 means that is fast
player1.shape("square")
player1.color('red')
player1.shapesize(stretch_len=1 , stretch_wid=5)
player1.penup()
player1.goto(-350, 0)  #start position  ( x = (-450, 450))

# player2
player2=turtle.Turtle()
player2.speed(0)# defult range from 1 to 10     0 or 10 means that is fast
player2.shape("square")
player2.color('yellow')
player2.shapesize(stretch_len=1 , stretch_wid=5)
player2.penup()
player2.goto(350, 0)  #start position  ( x = (-450, 450))


# score_title
score_title=turtle.Turtle()
score_title.speed(0)# defult range from 1 to 10     0 or 10 means that is fast
score_title.shape("square")
score_title.color('white')
score_title.shapesize(stretch_len=1 , stretch_wid=5)
score_title.penup()
score_title.goto(0,260)  #start position  ( x = (-450, 450))
score_title.hideturtle() # we hide the object because we only want to see the text
score_title.write('palyer1  0 , player2  0 ' , align='center' ,font=('courier',14,'normal'))

p1_score, p2_score = 0, 0  # variables to hold player 1 & player 2 scores

#============================== player movement

# functions of players movement
player_speed =20
# player1
def p1_move_up():
    player1.sety(player1.ycor()+player_speed) # from start(this) position + 20

def p1_move_down():
    player1.sety(player1.ycor() - player_speed) # from start(this) position - 20

# player2
def p2_move_up():
    player2.sety(player2.ycor()+player_speed) # from start(this) position + 20

def p2_move_down():
    player2.sety(player2.ycor() - player_speed) # from start(this) position - 20

# Get users inputs (Key Bindings)

window.listen()              # tell the window to expect user inputs
window.onkeypress(p1_move_down,"a") # p1_move_down   not p1_move_down()
window.onkeypress(p1_move_up,"q")

window.onkeypress(p2_move_up, "Up")
window.onkeypress(p2_move_down, "Down")




# game loop ==========================
while True:
    window.update()

    # ball movement
    ball.setx(ball.xcor() + (ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))

    # ball & borders collisions
    if(ball.ycor() > 290):   # 290 => 300(top border) - 10(half ball size)
        ball.sety(290)
        ball_dy *= -1     # invert Y direction

    if(ball.ycor() < -290):   # 290 => 300(top border) - 10(half ball size)
        ball.sety(-290)
        ball_dy *= -1  # invert Y direction

    # ball & players collisions =====================


    # collision with player 1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (player1.ycor()-60) and ball.ycor() < (player1.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1

    # collision with player 2
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (player2.ycor()-60) and ball.ycor() < (player2.ycor()+60):
        ball.setx(340)
        ball_dx *= -1

    # score handling
    if(ball.xcor() > 390):
        ball.goto(0, 0)
        ball_dx *= -1  # invert X direction
        score_title.clear()
        p1_score += 1
        score_title.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",
                    font=("Courier", 14, "normal"))

    if(ball.xcor() < -390):
        ball.goto(0, 0)
        ball_dx *= -1  # invert X direction
        score_title.clear()
        p2_score += 1
        score_title.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",
                    font=("Courier", 14, "normal"))

    # the border of players
    if (player1.ycor() > 290 or player1.ycor() < -290):
        player1.sety(290)

    if (player2.ycor() > 290 or player2.ycor() < -290):
        player2.sety(290)
