#C
from typing import Literal

import pygame

COLOR_PINK = (255, 174, 201)
COLOR_WHITE= (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GRAY = (128, 128, 128)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_BROWN = (255, 102, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 2,
    'Level1Bg2' : 4,
    'Player1' : 3,
    'Player1Shot' : 3,
    'Player2' : 3,
    'Player2Shot' : 3,
    'Enemy1' : 2,
    'Enemy1Shot' : 5,
    'Enemy2' : 1,
    'Enemy2Shot' : 5,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_SIZE = {
    'Player1' : 0.5,
    'Player2' : 0.176,
    'Enemy1' : 0.5,
    'Enemy2' : 0.5,
    'Player1Shot' : 0.2,
    'Player2Shot' : 0.0222,
    'Enemy1Shot' : 0.2,
    'Enemy2Shot' : 0.22,
}

ENTITY_SHOT_DELAY = {
    'Player1' : 20,
    'Player2' : 15,
    'Enemy1': 100,
    'Enemy2': 200,

}

#M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

#P
PLAYER_KEY_UP = {'Player2': pygame.K_UP,
                 'Player1': pygame.K_w}

PLAYER_KEY_DOWN = {'Player2': pygame.K_DOWN,
                   'Player1': pygame.K_s}

PLAYER_KEY_LEFT = {'Player2': pygame.K_LEFT,
                   'Player1': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player2': pygame.K_RIGHT,
                    'Player1': pygame.K_d}

PLAYER_KEY_SHOOT = {'Player2': pygame.K_RCTRL,
                    'Player1': pygame.K_LCTRL}


# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 1600
WIN_HEIGHT = 900

