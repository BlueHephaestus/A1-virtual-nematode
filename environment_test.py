from tkinter import *

import disembodiedConnectome
from base import *
from bot import Bot
from config import *


class Environment():
    def __init__(self):
        # Window + Frame
        self.window = Tk()
        self.frame = Frame(self.window, bd=5, relief=SUNKEN)
        self.frame.grid(row=0, column=0)

        # Hard-code choice of resolution for canvas and scroll region as maximum shape of images*resize_factor
        """
    self.canvas = Canvas(self.frame, bg="#000000", width=1366, height=768, scrollregion=(0,0,
      self.dataset.imgs.max_shape()[1]*self.editor_resize_factor, 
      self.dataset.imgs.max_shape()[0]*self.editor_resize_factor))
    """
        self.canvas = Canvas(self.frame, bg="#FFFFFF", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

        # Img + Event listeners
        # self.canvas.image = ImageTk.PhotoImage(Image.fromarray(self.img))#Literally because tkinter can't handle references properly and needs this.
        # self.canvas_image_config = self.canvas.create_image(0, 0, image=self.canvas.image, anchor="nw")#So we can change the image later
        self.canvas.focus_set()
        self.canvas.bind("<Button 1>", self.mouse_click)  # left
        """
    self.canvas.bind("<Button 3>", self.mouse_click)#right
    self.canvas.bind("<B1-Motion>", self.mouse_move)#left
    self.canvas.bind("<B3-Motion>", self.mouse_move)#right
    self.canvas.bind("<ButtonRelease-1>", self.mouse_left_release)
    self.canvas.bind("<ButtonRelease-3>", self.mouse_right_release)
    self.canvas.bind_all("<Button-4>", self.mouse_scroll)#Scrollwheel for entire editor
    self.canvas.bind_all("<Button-5>", self.mouse_scroll)#Scrollwheel for entire editor
    """
        self.canvas.bind("<Left>", self.left_arrow_key_press)
        self.canvas.bind("<Right>", self.right_arrow_key_press)
        self.canvas.bind("<Up>", self.up_arrow_key_press)
        self.canvas.bind("<Down>", self.down_arrow_key_press)
        self.canvas.bind("<Key>", self.key_press)
        self.canvas.bind("<Return>", self.spawn_bot)

        self.canvas.pack(side=LEFT)

        self.t = 0

        self.bot = Bot()
        self.render_bot()
        self.window.mainloop()

    def render_bot(self):
        # Draw the bot on our canvas using it's given position and direction it's facing.
        self.canvas.delete("bot")

        # Draw body
        body_x1, body_y1 = polar_to_cartesian(RENDER_BOT_RADIUS, self.bot.theta + PI / 2)
        body_x2, body_y2 = polar_to_cartesian(RENDER_BOT_RADIUS, self.bot.theta - PI / 2)
        self.canvas.create_line(self.bot.x + body_x1, self.bot.y + body_y1, self.bot.x + body_x2,
                                self.bot.y + body_y2, fill="blue", tags="bot")

        # Draw head to indicate direction bot is facing
        head_x2, head_y2 = polar_to_cartesian(RENDER_HEAD_RADIUS, self.bot.theta)
        self.canvas.create_line(self.bot.x, self.bot.y, self.bot.x + head_x2, self.bot.y + head_y2,
                                fill="red", tags="bot")

        # Draw single dot to track where we've been
        if self.t % TRACKER_DOT_STEP == 0:
            self.canvas.create_line(self.bot.x, self.bot.y, self.bot.x, self.bot.y + 1,
                                    fill="green")
        self.t += 1

    def spawn_bot(self, event):
        # Give it a cage to use for sonar
        self.canvas.create_rectangle(self.bot.x - CANVAS_CAGE_WIDTH,
                                     self.bot.y - CANVAS_CAGE_HEIGHT,
                                     self.bot.x + CANVAS_CAGE_WIDTH,
                                     self.bot.y + CANVAS_CAGE_HEIGHT, outline="black")

        # Spawn a new nematode to inhabit our bot and be it's brain; send movements.
        for left, right in disembodiedConnectome.spawn():
            # Normalize movements to our ranges
            left = (left / 180)
            right = (right / 180)
            # print("LEFT: {}, RIGHT: {}".format(left,right))

            self.bot.update(left, right)
            self.render_bot()
            self.canvas.update()
            # time.sleep(0.01)

    def mouse_click(self, event):
        # self.canvas.create_rectangle(200, 400, 300, 500, fill='', outline="darkRed", width=2, tags="selection")
        # self.canvas.create_rectangle(400, 400, 600, 402, fill='', outline="darkRed", width=2, tags="selection")
        pass

    def q_key_press(self, event):
        # (Quit) We close the editor and prompt them for if they are finished with editing or not. If they're not finished we do nothing.
        self.window.destroy()
        sys.exit("Exiting...")

    ####################################
    # MANUAL CONTROLS
    ####################################
    def key_press(self, event):
        # Hub for all key press events.
        c = event.char.upper()
        if c == "Q":
            self.q_key_press(event)

    def left_arrow_key_press(self, event):
        # Move left wheel, rotate right
        self.bot.update(PI / 8, 0)
        self.render_bot()

    def right_arrow_key_press(self, event):
        # Move right wheel, rotate left
        self.bot.update(0, PI / 8)
        self.render_bot()

    def up_arrow_key_press(self, event):
        self.bot.update(PI / 8, PI / 8)
        self.render_bot()

    def down_arrow_key_press(self, event):
        self.bot.update(-PI / 8, -PI / 8)
        self.render_bot()


Environment()
