from turtle import Turtle

snake_position = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_length = []
        self.create_snake()
        self.head = self.snake_length[0]

    def create_snake(self):
        for position in snake_position:
            self.add_snake_length(position)

    def add_snake_length(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_length.append(snake)

    def reset_snake(self):
        for snake in self.snake_length:
            snake.goto(1000, 1000)
        self.snake_length.clear()
        self.create_snake()
        self.head = self.snake_length[0]

    def grow_snake(self):
        self.add_snake_length(self.snake_length[-1].position())

    def move(self):
        for snake_num in range(len(self.snake_length) - 1, 0, -1):
            x_cor = self.snake_length[snake_num - 1].xcor()
            y_cor = self.snake_length[snake_num - 1].ycor()
            self.snake_length[snake_num].goto(x_cor, y_cor)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
