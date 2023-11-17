"""Creating the snake and adding the movements"""

from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Class for the snake"""
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creating the snake"""
        for position in START_POSITION:
            self.add_segment(position)

 
    def extend(self):
        """Extending the snake"""
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        """"Adding segments"""
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("green")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        """Defining the moves"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        """Moving left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Moving right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        """Going up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Going down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
