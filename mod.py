import pygame
import math

class colRect:
    def __init__(self, rect, win):
        self.rect = rect
        self.keys = pygame.key.get_pressed()
        self.win = win

    def isMouseOn(self):
        return pygame.mouse.get_pos()[0] > self.rect[0] and pygame.mouse.get_pos()[0] < self.rect[0] + self.rect[2] and pygame.mouse.get_pos()[1] - self.rect[3] < self.rect[1] and pygame.mouse.get_pos()[1] > self.rect[1]

    def isPressed(self):
        m = pygame.mouse.get_pressed()
        if (pygame.mouse.get_pos()[0] > self.rect[0] and pygame.mouse.get_pos()[0] < self.rect[0] + self.rect[2] and
                pygame.mouse.get_pos()[1] - self.rect[3] < self.rect[1] and pygame.mouse.get_pos()[1] > self.rect[1] and
                m[0]):
            return True
        else:
            return False

    def colide(self, object):
        if (object.rect[0] - self.rect[2] < self.rect[0] and object.rect[0] + self.rect[2] > self.rect[0] and
                object.rect[1] - self.rect[3] < self.rect[1] and object.rect[1] + self.rect[3] > self.rect[1]):
            return True
        else:
            return False

    def pixelSimetry(self, object):
        if (object.rect[0] == self.rect[0] and object.rect[1] == self.rect[1]):
            return True
        else:
            return False

    def distance(self, target):
        return math.hypot(self.rect[0] - target[0], self.rect[1] - target[1])

    def angle(self, target):
        return math.sin(math.atan2(target[1] - self.rect[1], target[0] - self.rect[0]))

def distance(self, target):
    return math.hypot(self[0] - target[0], self[1] - target[1])

def angle(self, target):
    return math.atan2(target[1] - self[1], target[0] - self[0])

def text(surface, font, text, rect, color):
    surface.blit(font.render(text, True, color), rect)


def linearing(selftr, targettr, speed):
    if (selftr[0] < targettr[0]):
        selftr[0] += speed
    if (selftr[0] > targettr[0]):
        selftr[0] -= speed
    if (selftr[1] < targettr[1]):
        selftr[1] += speed
    if (selftr[1] > targettr[1]):
        selftr[1] -= speed


def displace(selftr, targettr, speed):
    if (selftr[1] > targettr[1]):
        # selftr[1] -= speed
        if (selftr[0] < targettr[0]):
            selftr[0] -= speed
        elif (selftr[0] > targettr[0]):
            selftr[0] += speed
    elif (selftr[1] < targettr[1]):
        selftr[1] -= speed
    return selftr

def isMouseOn(self):
    return pygame.mouse.get_pos()[0] > self[0] and pygame.mouse.get_pos()[0] < self[0] + self[2] and pygame.mouse.get_pos()[1] - self[3] < self[1] and pygame.mouse.get_pos()[1] > self[1]

def isPressed(self):
    m = pygame.mouse.get_pressed()
    if (pygame.mouse.get_pos()[0] > self[0] and pygame.mouse.get_pos()[0] < self[0] + self[2] and
            pygame.mouse.get_pos()[1] - self[3] < self[1] and pygame.mouse.get_pos()[1] > self[1] and
            m[0]):
        return True
    else:
        return False

def colideNS(self, object):
    if (object[0] - self[2] < self[0] and object[0] + self[2] > self[0] and object[1] - self[3] < self[1] and object[
        1] + self[3] > self[1]):
        return True
    else:
        return False