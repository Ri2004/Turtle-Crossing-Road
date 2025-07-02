import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle_player = Player()
carTurtle = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=turtle_player.move_up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carTurtle.create_car()
    carTurtle.move_cars()

    # Detect when player turtle collide with any car
    for car in carTurtle.all_cars:
        if turtle_player.distance(car) < 20:
            game_is_on = False

    # Detect successful crossing
    if turtle_player.is_at_finish_line():
        scoreboard.update_scoreboard()
        turtle_player.go_to_start()
        carTurtle.level_up()


screen.exitonclick()