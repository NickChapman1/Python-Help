from turtle import Turtle, Screen
from Ball import Balls
from Create_Pong_Pieces import Pong
from Scoreboard import Scoreboard
from scoreboard2 import Scoreboard2
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("Grey")
screen.title("Pong")
screen.tracer(0) ##when you turn off the animation you need to manually refresh it each time.
#Adding in a while loop with screen.update() to fix this
#paddle1 = Pong()
r_paddle = Pong((350,0))
l_paddle = Pong((-350,0))
main_ball = Balls((0,0))
#r_score = Scoreboard( x_pos = 70, y_pos= 260)
#l_score = Scoreboard(x_pos = -70, y_pos=260)
new_scoreboard = Scoreboard2()

#top_paddle = Pong((100,100)) #Can just create as many paddles as you want with ease now.

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(main_ball.move_speed)
    screen.update() #will make it so the tracer being off works becasue animation is off,
    main_ball.move()
    print(main_ball.xcor(),main_ball.ycor())
#bounce x
    if main_ball.ycor() > 280 or main_ball.ycor() < -280:
        main_ball.bounce_y_axis()      #Make the ball bounce
        #main_ball.increase_ball_speed() #ended up not using this method of class
#bounce Y
    if main_ball.distance(r_paddle) < 50 and main_ball.xcor() > 320 or \
    main_ball.distance(l_paddle) < 50 and main_ball.xcor() < -320:
        main_ball.bounce_x_axis()
    # if main_ball.xcor() > 388 or main_ball.ycor() > 288 or main_ball.xcor() < -288 or main_ball.ycor() < -288:
    #     game_is_on = False
    #     print("game over")

    #detect when right paddle missesl. Note the y cor doesn't matter it alreAdy bounces if it hits the walls
    if main_ball.xcor() > 380 or main_ball.ycor() > 290 or main_ball.ycor() < -290:
        main_ball.reset_ball()
     #   l_score.increase_score()
        new_scoreboard.l_point_add()

    #left paddle
    if main_ball.xcor() < -380:
        main_ball.reset_ball()
       # r_score.increase_score()
        new_scoreboard.r_point_add()

    # if main_ball.ycor() < -320 or main_ball.ycor() < 320 and main_ball.xcor() < -360 or main_ball.xcor() > 360:
    #     main_ball.teleport(0,0)
screen.exitonclick()