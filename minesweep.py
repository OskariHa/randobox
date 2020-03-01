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
        self.num_of_bombs = 10
        # for counter on toolbar
        self.bomb_counter = StringVar()
        self.bomb_counter.set(str(self.num_of_bombs))

        # empty grid
        self.playing_grid = self.grid()
        # create bombs
        self.bomb_positions = self.create_bombs()
        self.add_bombs()

        self.buttons = self.draw_grid()

        self.clicked = "f"
        self.btn_pos = None

        self.running = True

        # timer variables
        self.t = StringVar()
        self.t.set("1000")
        self.d = str(self.t.get())

        self.create_timer()

        restart = Button(toolbar, text="restart", command=self.restart)
        restart.grid(row=0, column=1, padx=90, pady=(2, 1))
        self.bomb_counter_lbl = Label(toolbar, textvariable=self.bomb_counter,
                                      bg="BLACK", fg="RED", width=10, font=36)
        self.bomb_counter_lbl.grid(row=0, column=2, padx=90)

        self.wonned = Label(root, text="YOU WON!!", fg="GREEN")

    # *************** ONCLICK FUNCTIONS ******************

    def onclick_left(self, pos, image_pos, event):

        if self.running:

            if pos in self.bomb_positions:
                self.bomb_hit(pos)

            else:
                self.nearby_bombs(pos)

    def onclick_right(self, pos, image_pos, event):
        if self.running:
            # add flag count
            if image_pos == 1:
                temp_string = str(self.bomb_counter.get())
                temp_int = int(temp_string)
                temp_int += 1
                temp_string = temp_int
                self.bomb_counter.set(temp_string)

            if image_pos != 2:
                image_pos += 1
            else:
                image_pos = 0

            # remove flag count
            if image_pos == 1:
                temp_string = str(self.bomb_counter.get())
                temp_int = int(temp_string)
                temp_int -= 1
                temp_string = temp_int
                self.bomb_counter.set(temp_string)

            if pos in range(0, 10):
                self.buttons[0][pos].configure(image=self.right_images[image_pos])
                # print(self.playing_grid[0][pos])
                self.buttons[0][pos].bind("<Button-3>", partial(self.onclick_right, pos,
                                                                image_pos))
            else:
                temp_string = str(pos)
                row = int(temp_string[0])
                col = int(temp_string[1])
                # print(self.playing_grid[row][col])
                self.buttons[row][col].configure(image=self.right_images[image_pos])
                self.buttons[row][col].bind("<Button-3>", partial(self.onclick_right, pos,
                                                                  image_pos))

    # ********** NEARBY BOMBS **************

    def nearby_bombs(self, pos):
        # 55 hit /// 44,45,46,54,56,64,65,66
        checked_positions = self.checked_positions(pos)

        image_pos = 0
        no_bombs = True
        temp = []

        if pos in range(0, 10):
            row = 0
            col = pos
        else:
            temp_string = str(pos)
            row = int(temp_string[0])
            col = int(temp_string[1])
        for i in checked_positions:
            if -1 < i < 100:
                if i in self.bomb_positions:
                    image_pos += 1
                    no_bombs = False
                else:
                    if -1 < i <= 9:
                        temp_string = str(i)
                        row2 = 0
                        col2 = int(temp_string[0])
                    else:
                        temp_string = str(i)

                        row2 = int(temp_string[0])
                        col2 = int(temp_string[1])

                    if col2 != -1:
                        if self.playing_grid[row2][col2] != 2:
                            temp.append(i)

        self.buttons[row][col].grid_forget()
        self.playing_grid[row][col] = 2
        pic = Label(self.root, image=self.left_images[image_pos])
        pic.grid(row=row, column=col)
        if no_bombs:
            # print(temp)
            self.multi_clear(temp)

        no_closed_spots = True
        for i in self.playing_grid:
            for t in i:
                if t == 0:
                    no_closed_spots = False

        if no_closed_spots:
            self.wonned.grid(row=self.grid_size + 1, columnspan=10)
            self.end_game()

    def multi_clear(self, adjacent):
        for i in adjacent:
            self.nearby_bombs(i)

    def checked_positions(self, pos):
        on_left = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        on_right = [9, 19, 29, 39, 49, 59, 69, 79, 89]
        # on_top = [1, 2, 3, 4, 5, 6, 7, 8]

        if pos == 0:
            positions = [pos + 1, pos + 10, pos + 11]
        elif pos == 99:
            positions = [pos - 1, pos - 10, pos - 11]
        # elif pos in on_top:
        # positions = [pos + 1, pos + 9, pos + 10, pos + 11]
        elif pos in on_left:
            positions = [pos - 10, pos - 9, pos + 1, pos + 10, pos + 11]
        elif pos in on_right:
            positions = [pos - 11, pos - 10, pos - 1, pos + 9, pos + 10]
        else:
            positions = [pos - 11, pos - 10, pos - 9, pos - 1, pos + 1,
                         pos + 9, pos + 10, pos + 11]

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
                    self.end_game()
                else:
                    temp_string = str(b)
                    row = int(temp_string[0])
                    col = int(temp_string[1])
                    self.buttons[row][col].configure(image=self.bomb_images[1])
                    self.end_game()

    # ***************** END GAME AND RESTART *************
    def end_game(self):
        self.running = False

    def restart(self):
        # empty grid
        self.playing_grid = self.grid()
        # create bombs
        self.bomb_positions = self.create_bombs()
        self.add_bombs()

        self.buttons = self.draw_grid()

        self.clicked = "f"
        self.btn_pos = None
        self.bomb_counter.set(str(self.num_of_bombs))

        self.running = True

        self.reset_timer()
        self.start_timer()

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

    # ********************** TIMER *************
    def create_timer(self):
        timer_lbl = Label(self.toolbar, textvariable=self.t, bg="BLACK", fg="RED",
                          width=10, font=36)
        timer_lbl.grid(row=0, column=0, padx=90)
        self.start_timer()

    def reset_timer(self):
        self.t.set("1000")

    def start_timer(self):
        timer = self.t
        self.timer()

    def stop(self):
        self.end_game()

    def timer(self):
        if self.running:
            self.d = str(self.t.get())
            s = int(self.d)
            if s == 0:
                self.stop()
            else:
                s -= 1
            self.d = s
            self.t.set(self.d)
            if self.running:
                self.root.after(1000, self.start_timer)
