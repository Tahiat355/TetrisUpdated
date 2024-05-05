import pygame
from colors import Colors
class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()


    def is_inside(self, row, column):
        if(row >= 0 and row < self.num_rows and column >=0  and column  < self.num_cols):
            return True
        return False


    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 9:
                self.grid[row][column] = 8
            else:
                self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            if not self.grid[row+num_rows][column] >= 8:
                self.grid[row+num_rows][column] = self.grid[row][column]
                self.grid[row][column] = 0

    def reset(self):
        for row in range(0, self.num_rows):
            for column in range(0, self.num_cols):
                self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0 :
                self.move_row_down(row, completed)

        return completed

    def clear_on_point(self, x, y):
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if j < 10 and i < 20:
                    self.grid[i][j] = 0
        self.move_on_radius(x,y)


    def move_on_radius(self, x, y):
        offset = 3
        for i in range(x+1,0, -1):
            for j in range(y-1, y+2):
                if i - offset >= 0 and j - offset >= 0 and i < 20 and j < 10:
                    self.grid[i][j] = self.grid[i - offset][j]
                    self.grid[i - offset][j] = 0






    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):

                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11, self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

