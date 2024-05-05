class Colors:

    dark_grey = (0, 120, 0)
    green = (0, 240, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 100, 247)
    cyan = (21, 204, 209)
    blue = (255, 94, 255)
    dark_blue = (44, 44, 127)
    white = (255, 255, 255)
    light_blue = (59, 85, 162)
    break_color = (255, 255, 204)
    black = (10, 10, 0)

    @classmethod
    def get_cell_colors(cls):
        return (cls.dark_grey, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue, cls.green, cls.break_color, cls.black)