from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        # self.blocks = [IBlock(), OBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.boms = 10
        self.game_over_sound = pygame.mixer.Sound("Music/gameover.wav")
        self.clear_sound = pygame.mixer.Sound("Music/lineclear.mp3")
        self.rotate_sound = pygame.mixer.Sound("Music/rotate.mp3")
        self.bom_sound = pygame.mixer.Sound("Music/bomsound.mp3")
        pygame.mixer.music.load("Music/runsoundtetris.mp3")
        pygame.mixer.music.play(-1)
        return

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 400
            self.boms += 1
        elif lines_cleared == 3:
            self.score += 900
            self.boms += 1
        elif lines_cleared == 4:
            self.score += 1600
            self.boms += 2
        self.score += move_down_points

    def get_random_block(self):
        if len(self.blocks)==0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
            # self.blocks = [IBlock(), OBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        self.current_block.move(0,-1)
        if self.block_inside() == False or not self.block_fits():
            # self.move_right()
            self.current_block.move(0,1)
        return
    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside() == False  or not self.block_fits():
            # self.move_left()
            self.current_block.move(0,-1)
        return
    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside() == False or not self.block_fits():
            #self.move_up()
            self.current_block.move(-1, 0)
            self.lock_block()
        return

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block

        self.next_block = self.get_random_block()
        if random.randint(1, 5) % 2 == 0:
            self.next_block.id = 9


        # rows_cleared = self.grid.clear_full_rows()
        # if rows_cleared:
        #     self.clear_sound.play()
        # self.update_score(rows_cleared, 0)

        while (self.grid.clear_full_rows()):
            rows_cleared = self.grid.clear_full_rows()
            self.update_score(rows_cleared, 0)
            self.clear_sound.play()

        if self.block_fits() == False:
            self.game_over_sound.play()
            self.game_over = True


    def bom(self, row, column):
        if self.boms>0 and row<19 and column<10:
            print(row, column)
            self.grid.clear_on_point(row, column)
            self.boms -= 1
            self.bom_sound.play()



    def move_up(self):
        self.current_block.move(-1, 0)
        return

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or not self.block_fits():
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()
        return

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)
