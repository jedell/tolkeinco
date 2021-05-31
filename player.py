import sys
import pygame as pg
from pygame.math import Vector2

pg.init()

class Player(pg.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pg.image.load("player_standing.png")
        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0, 0)
        # Store the actual position as another vector because
        # rect coordinates can only be integers.
        self.pos = Vector2(pos)
        self.max_speed = 3.5
        self.goal = Vector2(pos)
        self.goal_radius = 40
        self.stopped = True

    def update(self):
        self.pos += self.vel  # Update the position vector first.
        self.rect.center = self.pos  # Update the rect afterwards.

        # This vector points to the goal.
        heading = self.goal - self.pos
        distance = heading.length()
        # Normalize it, so that we can scale it to the desired length/speed below.
        if heading:  # Can't normalize a zero vector.
            heading.normalize_ip()
            self.stopped = False

        if distance > self.goal_radius:
            # Move with maximum speed.
            self.vel = heading * self.max_speed
            self.stopped = False
        elif self.goal_radius > distance  > 1:
            # Slow down when we're approaching the goal.
            self.vel = heading * (distance/self.goal_radius * self.max_speed)
            self.stopped = False
        else:
            self.vel = Vector2(0, 0)
            self.stopped = True

            #print("stopped")
