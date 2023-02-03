import turtle

# Window characteristics
wind = turtle.Screen()                            # Build the window that I'll watch game in it
wind.title("Ping Pong")                           # The title of the window
wind.bgcolor("black")                             # The background color of the window
wind.setup(width=800,height=600)                  # Give the height and width for window
wind.tracer(0)                                    # To prevent the window to update from itself

# Paddle 1
paddle1 = turtle.Turtle()                         # Initialize turtle object
paddle1.speed(0)                                  # Set the speed of the animation 
paddle1.shape("square")                           # Set the shape of the object
paddle1.shapesize(stretch_wid=5,stretch_len=1)    # Stretch the shape to meet the size
paddle1.color("blue")                             # Set the color of the shape
paddle1.penup()                                   # To stop the object from drawing lines
paddle1.goto(-375,0)                              # Set the position of the object

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.color("red")
paddle2.penup()
paddle2.goto(375,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25
ball.dy = 0.25

# Score
score_player1 = 0
score_player2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()                                # To hide turtle object
score.goto(0,260)
score.write("Player 1 : 0   Player 2 : 0" , align="center" , font=("Courier",24,"normal")) # To Write on the window game

#functions to contol moves of paddle 1
def paddle1_up():
    y=paddle1.ycor()                              # Set the y coordinate of paddle 1
    y+= 20                                        # Increase y by 20
    paddle1.sety(y)                               # Set the y of the paddle 1 to the new y coordinate
    
def paddle1_down():
    y=paddle1.ycor()                              
    y-= 20                                        # Decrease y by 20
    paddle1.sety(y)
    
#functions to contol moves of paddle 1
def paddle2_up():
    y=paddle2.ycor()                              
    y+= 20
    paddle2.sety(y)

def paddle2_down():
    y=paddle2.ycor()                              
    y-= 20
    paddle2.sety(y)


#Keyboard bindings of paddle 1
wind.listen()                                     # Tell the window to expect keyboard input
wind.onkeypress(paddle1_up,"w")                   # When press w the function paddle_up invoked
wind.onkeypress(paddle1_down,"s")
    
#Keyboard bindings of paddle 2
wind.listen()
wind.onkeypress(paddle2_up,"Up")    
wind.onkeypress(paddle2_down,"Down") 
   
# Main game loop
while True:
    wind.update()
    
    # Move the ball
    ball.setx(ball.xcor()+ ball.dx)               # Ball starts at 0 and everytime loop is run ==>+0.25 x-axis
    ball.sety(ball.ycor()+ ball.dy)               # Ball starts at 0 and everytime loop is run ==>+0.25 y-axis
    
    # Check the border 
    if ball.ycor() >290:                          # If ball is at Top border
        ball.sety(290)                            # Set y coordinate  290
        ball.dy*=-1                               # Reverse y direction 
    
    if ball.ycor() <-290:                         # If ball is at Bottom border
        ball.sety(-290)                           
        ball.dy*=-1 
    
    if ball.xcor() >390:                          # If ball is at Right border
        ball.goto(0,0)                            # Return ball to center
        ball.dx *=-1                              # Reverse x direction                               
        score_player1 += 1
        score.clear()
        score.write(f"Player 1 : {score_player1}   Player 2 : {score_player2}" , align="center" , font=("Courier",24,"normal"))
        
    if ball.xcor() <-390:                         # If ball is at Left border
        ball.goto(0,0)
        ball.dx *=-1
        score_player2 += 1
        score.clear()                             # To remove previous value
        score.write(f"Player 1 : {score_player1}   Player 2 : {score_player2}" , align="center" , font=("Courier",24,"normal"))
          
    # Ball and paddle collision
    if (ball.xcor() >365 and ball.xcor() < 375) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(365)
        ball.dx*=-1      
    if (ball.xcor() <-365 and ball.xcor() > -375) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-365)
        ball.dx*=-1      

    if score_player1 == 5 :                       
        ball.color("black")
        ball.goto(0,0)
        score.goto(0,0)
        score.write("Player 1 is Winner " , align="center" , font=("Courier",24,"normal"))  
    if score_player2 == 5 :
        ball.color("black")
        score.goto(0,0)
        score.write("Player 2 is Winner " , align="center" , font=("Courier",24,"normal"))
        
