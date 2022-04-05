from tkinter import *
import tkinter as tk
from random import randint, choice
import tkinter.messagebox


class Field:
    def __init__(self, c, n, m, width, height, master):
        """
       c - canvas instance
       n - number of rows
       m - number of columns
       width - width of game field in pixels
       height - width of game field in pixels
       walls - if True matrix should have 0's surrounded by 1's (walls)
       example
       1 1 1 1
       1 0 0 1
       1 1 1 1
       """
        self.sizem = None
        self.sizen = None
        self.c = c

        self.c.bind('')

        self.a = []
        self.n = n
        self.m = m
        self.width = width
        self.height = height
        self.__snake_body = [(6, 6)]
        self.__food = None
        self.__create_food()

        master.bind('<Key>', self.change_magnitude)

        for i in range(self.n):
            self.a.append([])
            for j in range(self.m):
                self.a[i].append(0)

        self.magnitude = 'left'

        self.draw()

    def step(self):
        head = self.__snake_body[-1]
        full = False

        if head == self.__food:
            self.__create_food()
            full = True

        if head[0] == -1 or head[1] == -1 or head[0] == self.n or head[1] == self.m or head in self.__snake_body[:-1]:
            self.lost()

        if self.magnitude == 'down':
            self.__snake_body.append((head[0] + 1, head[1]))
        elif self.magnitude == 'right':
            self.__snake_body.append((head[0], head[1] + 1))
        elif self.magnitude == 'left':
            self.__snake_body.append((head[0], head[1] - 1))
        else:
            self.__snake_body.append((head[0] - 1, head[1]))

        if not full:
            self.__snake_body = self.__snake_body[1:]
    
    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()

    def draw(self):
        self.c.delete('all')
        self.sizen = self.width // self.n
        self.sizem = self.height // self.m

        for cell in self.__snake_body:
            self.c.create_rectangle(self.__food[1] * self.sizem, self.__food[0] * self.sizem,
                                    (self.__food[1] + 1) * self.sizem, (self.__food[0] + 1) * self.sizen, fill='red')
            self.c.create_rectangle(
                cell[1] * self.sizem,
                cell[0] * self.sizen,
                (cell[1] + 1) * self.sizem,
                (cell[0] + 1) * self.sizen,
                fill='black'
            )


        self.step()
        self.c.after(100, self.draw)

    def change_magnitude(self, event):
        key = event.keysym.lower()
        if key not in ('down', 'right', 'up', 'left'):
            return

        self.magnitude = key

    def __create_food(self):
        self.__food = (randint(5, self.n - 5), randint(5, self.m - 5))

    @staticmethod
    def lost(self):
        tk.messagebox.showinfo(message='You lost')
        raise Exception('You lost')


root = Tk()
root.geometry("800x800")
c = Canvas(root, width=800, height=800)
c.pack()

f = Field(c, 40, 40, 800, 800, root)

root.mainloop()
