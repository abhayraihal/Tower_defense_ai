import pygame
from enum import Enum

from game.game import Game
from experiment.geneticAlgorithm.parallelGA import ParallelGeneticAlgorithm
from experiment.geneticAlgorithm.serialGA import SerialGeneticAlgorithm

from agent.geneticAgent import GeneticAgent
from constants.gameConstants import *


class MODE(Enum):
    manual           = 0,
    geneticAlgorithm = 1,


GAME_MODE = MODE.geneticAlgorithm  # Select which mode to run the game in
PARALLEL_MODE  = False          # Run a game on each processor core (only when visual_mode is off)
COLLECT_WHOLE_GAME_DATA = False  # Game data collection for the GA
COLLECT_INNER_GAME_DATA = False  # "     "
VISUAL_MODE    = True          # Display Graphics
READ_FILE      = False          # Read model from file and continue training from it
SAVE_TO_DISK   = False          # Collect and store data
PRINT_GRAPHS   = False          # Prints graphs of score averages


# the game expects the following signature:
#      Game(visualMode, towers, gameRecord, collectInnerGameData, deepQagent)

def main():
    ''' Entry point for game '''

    #Setup Game
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.display.set_caption("AI Tower Defense")

    displaySettings()

    # Determine game mode
    if GAME_MODE == MODE.manual:
        game = Game(True, [], None, False, None)
        game.run()
    else:
        # we only use genetic algorithm
        if PARALLEL_MODE:
            gaAlgo = ParallelGeneticAlgorithm(VISUAL_MODE, READ_FILE, SAVE_TO_DISK, PRINT_GRAPHS, COLLECT_WHOLE_GAME_DATA, COLLECT_INNER_GAME_DATA)
        else:
            gaAlgo = SerialGeneticAlgorithm(VISUAL_MODE, READ_FILE, SAVE_TO_DISK, PRINT_GRAPHS, COLLECT_WHOLE_GAME_DATA, COLLECT_INNER_GAME_DATA)
        gaAlgo.run()

    pygame.quit()

def displaySettings():
    ''' Displays the current game settings '''
    print(f"\n=== AI Tower Defense Settings ===")
    print(f"Game Mode:              {GAME_MODE.name}")
    print(f"Parallel Mode:          {PARALLEL_MODE}")
    print(f"Visual Mode:            {VISUAL_MODE}")
    print(f"Load model from file:   {READ_FILE}")
    print(f"Save model to file:     {SAVE_TO_DISK}")
    print(f"Save graphs:            {PRINT_GRAPHS}\n")


if __name__ == "__main__":
    main()
