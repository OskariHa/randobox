from tkinter import *
from random import randint
from functools import partial


class MineSweep:

    def __init__(self, root, toolbar):
        self.root = root
        self.toolbar = toolbar

        self.left_images = self.load_left_images()
        self.right_images = self.load_right_images()
        self.bomb_images = self.load_bomb_hit()

        # grid size
        self.grid_size = 10
        # bombs
        self.num_of_bombs = 20

        # empty grid
        self.playing_grid = self.grid()
        # create bombs
        self.bomb_positions = self.create_bombs()
        self.add_bombs()

        self.buttons = self.draw_grid()

        self.clicked = "f"
        self.btn_pos = None

    # *************** ONCLICK FUNCTIONS ******************

    def onclick_left(self, pos, image_pos, event):
        print("left")
        print(pos)

        if pos in self.bomb_positions:
            self.bomb_hit(pos)

        else:
            self.nearby_bombs(pos)

    def onclick_right(self, pos, image_pos, event):
        print("right")
        print(pos)
        if image_pos != 2:
            image_pos += 1
        else:
            image_pos = 0

        if pos in range(0, 10):
            self.buttons[0][pos].configure(image=self.right_images[image_pos])
            self.buttons[0][pos].bind("<Button-3>", partial(self.onclick_right, pos, image_pos))
        else:
            temp_string = str(pos)
            row = int(temp_string[0])
            col = int(temp_string[1])
            self.buttons[row][col].configure(image=self.right_images[image_pos])
            self.buttons[row][col].bind("<Button-3>", partial(self.onclick_right, pos, image_pos))

        print(pos)

    # ********** NEARBY BOMBS **************

    def nearby_bombs(self, pos):
        # 55 hit /// 44,45,46,54,56,64,65,66
        checked_positions = self.checked_positions(pos)

        image_pos = 0
        temp = []
        for i in checked_positions:
            if -1 < i < 100:
                if i in self.bomb_positions:
                    image_pos += 1
                else:
                    temp.append(i)

        if temp:
            self.multi_clear(temp)

        if pos in range(0, 10):
            self.buttons[0][pos].configure(image=self.left_images[image_pos])
        else:
            temp_string = str(pos)
            row = int(temp_string[0])
            col = int(temp_string[1])
            self.buttons[row][col].configure(image=self.left_images[image_pos])

    def multi_clear(self, temp):
        for pos in temp:
            checked_positions = self.checked_positions(pos)
            image_pos = 0
            for i in checked_positions:
                if i in self.bomb_positions:
                    image_pos += 1
            if pos in range(0, 10):
                self.buttons[0][pos].configure(image=self.left_images[image_pos])
            else:
                temp_string = str(pos)
                row = int(temp_string[0])
                col = int(temp_string[1])
                self.buttons[row][col].configure(image=self.left_images[image_pos])

    def checked_positions(self, pos):
        on_left = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        on_right = [9, 19, 29, 39, 49, 59, 69, 79, 89]

        if pos in on_left:
            positions = [pos - 10, pos - 9, pos + 1, pos + 10, pos + 11]
        elif pos in on_right:
            positions = [pos - 11, pos - 10, pos - 1, pos + 9, pos + 10]
        else:
            positions = [pos - 11, pos - 10, pos - 9, pos - 1, pos + 1,
                         pos + 9, pos + 10, pos + 11]

        val = -12
        while val < 0:
            positions = [value for value in positions if value != val]
            val += 1

        val = 112
        while val > 99:
            positions = [value for value in positions if value != val]
            val -= 1

        return positions

    # ************ BOMB HIT *****************

    def bomb_hit(self, pos):

        if pos in range(0, 10):
            self.buttons[0][pos].configure(image=self.bomb_images[0])
        else:
            temp_string = str(pos)
            row = int(temp_string[0])
            col = int(temp_string[1])
            self.buttons[row][col].configure(image=self.bomb_images[0])
        for b in self.bomb_positions:
            if b == pos:
                pass
            else:
                if b in range(0, 10):
                    self.buttons[0][b].configure(image=self.bomb_images[1])
                else:
                    temp_string = str(b)
                    row = int(temp_string[0])
                    col = int(temp_string[1])
                    self.buttons[row][col].configure(image=self.bomb_images[1])

    # ****************** Setup ***************************

    def draw_grid(self):
        button_list = []
        for r in range(0, self.grid_size):
            row = []
            for c in range(0, self.grid_size):
                pos = r * 10 + c
                image_pos = 0
                button = Button(self.root, image=self.right_images[image_pos])
                button.grid(row=r, column=c)
                button.bind("<Button-1>", partial(self.onclick_left, pos, image_pos))
                button.bind("<Button-3>", partial(self.onclick_right, pos, image_pos))
                row.append(button)
            button_list.append(row)
        return button_list

    def add_bombs(self):
        for i in self.bomb_positions:
            if i in range(0, 10):
                self.playing_grid[0][i] = 1
            else:
                temp_string = str(i)
                row = int(temp_string[0])
                col = int(temp_string[1])
                self.playing_grid[row][col] = 1

    def create_bombs(self):
        bomb_list = []
        available_positions = self.grid_size ** 2 - 1
        for r in range(0, self.num_of_bombs):
            added = False
            while not added:
                position = randint(0, available_positions)
                if position in bomb_list:
                    position = randint(0, available_positions)
                else:
                    bomb_list.append(position)
                    added = True
        bomb_list.sort()
        return bomb_list

    # create empty grid
    def grid(self):
        grid_list = []
        for i in range(0, self.grid_size):
            row = []
            for r in range(0, self.grid_size):
                row.append(0)
            grid_list.append(row)
        return grid_list

    # ************** IMAGES *******************

    def load_right_images(self):
        none_img = PhotoImage(file=r"images/minesweep/right/minesweep_none.png")
        none_img = none_img.zoom(2)
        none_img = none_img.subsample(22)
        flag_img = PhotoImage(file=r"images/minesweep/right/minesweep_flag.png")
        flag_img = flag_img.zoom(2)
        flag_img = flag_img.subsample(22)
        questionmark_img = PhotoImage(file=r"images/minesweep/right/minesweep_questionmark.png")
        questionmark_img = questionmark_img.zoom(2)
        questionmark_img = questionmark_img.subsample(76)

        return [none_img, flag_img, questionmark_img]

    def load_left_images(self):

        empty_img = PhotoImage(file=r"images/minesweep/left/minesweep_empty.png")
        empty_img = empty_img.zoom(2)
        empty_img = empty_img.subsample(22)
        one_img = PhotoImage(file=r"images/minesweep/left/minesweep_one.png")
        one_img = one_img.zoom(2)
        one_img = one_img.subsample(22)
        two_img = PhotoImage(file=r"images/minesweep/left/minesweep_two.png")
        two_img = two_img.zoom(2)
        two_img = two_img.subsample(22)
        three_img = PhotoImage(file=r"images/minesweep/left/minesweep_three.png")
        three_img = three_img.zoom(2)
        three_img = three_img.subsample(22)
        four_img = PhotoImage(file=r"images/minesweep/left/minesweep_four.png")
        four_img = four_img.zoom(2)
        four_img = four_img.subsample(22)
        five_img = PhotoImage(file=r"images/minesweep/left/minesweep_five.png")
        five_img = five_img.zoom(2)
        five_img = five_img.subsample(22)
        six_img = PhotoImage(file=r"images/minesweep/left/minesweep_six.png")
        six_img = six_img.zoom(2)
        six_img = six_img.subsample(22)
        seven_img = PhotoImage(file=r"images/minesweep/left/minesweep_seven.png")
        seven_img = seven_img.zoom(2)
        seven_img = seven_img.subsample(22)
        eight_img = PhotoImage(file=r"images/minesweep/left/minesweep_eight.png")
        eight_img = eight_img.zoom(2)
        eight_img = eight_img.subsample(22)

        left_images = [empty_img, one_img, two_img, three_img, four_img, five_img, six_img,
                       seven_img, eight_img]

        return left_images

    def load_bomb_hit(self):
        bomb_img = PhotoImage(file=r"images/minesweep/left/minesweep_bomb.png")
        bomb_img = bomb_img.zoom(2)
        bomb_img = bomb_img.subsample(22)
        explosion_img = PhotoImage(file=r"images/minesweep/left/minesweep_explosion.png")
        explosion_img = explosion_img.zoom(2)
        explosion_img = explosion_img.subsample(22)

        return [explosion_img, bomb_img]


root = Tk()
tolbar = 2
MineSweep(root, tolbar)
root.mainloop()
