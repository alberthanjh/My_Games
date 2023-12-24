__author__ = 'marble_xu'

from . import tool
from . import constants as c
from .state import mainmenu, screen, level
import pygame

def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()



def main():
    file = "D:\\PythonPlantsVsZombies-master\\sounds\\grasswalk.mp3"
    play_music(file)

    game = tool.Control()
    state_dict = {c.MAIN_MENU: mainmenu.Menu(),
                  c.GAME_VICTORY: screen.GameVictoryScreen(),
                  c.GAME_LOSE: screen.GameLoseScreen(),
                  c.LEVEL: level.Level()}
    game.setup_states(state_dict, c.MAIN_MENU)
    game.main()