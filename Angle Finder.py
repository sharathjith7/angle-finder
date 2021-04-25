import pygame
import sys
import math
from PIL import ImageGrab

####################### SETTINGS ###########################
pygame.init()

WIDTH = 555
HEIGHT = 578

BLACK = (0, 0, 0)
RED = (225, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 255)
GREY = (107, 107, 107)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

FPS = 27

####################### MAIN CLASS ###########################


class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.mouse_clicked = False
        self.dot_positions = []
        self.mouse_pos = (0, 0)
        self.m1 = 0  # for dot_positions[0] and dot_positions[1]
        self.m2 = 0  # for dot_positions[1] and dot_positions[2]
        self.found_m = False
        self.found_angle = False
        self.angle = 0
        self.clipboard_data = ImageGrab.grabclipboard()
        if self.clipboard_data is not None:
            self.clipboard_data.save('screen.png')
            self.clipboard_image = pygame.image.load('screen.png')
            self.w, self.h = self.clipboard_image.get_width(), self.clipboard_image.get_height()
            self.screen = pygame.display.set_mode((self.w, self.h))

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONUP:
                if len(self.dot_positions) < 3:
                    self.mouse_clicked = True
                    self.dot_positions.append(pygame.mouse.get_pos())

        keys = pygame.key.get_pressed()
        print(keys)
        if keys[pygame.KMOD_CTRL]:
            self.clipboard_data = ImageGrab.grabclipboard()

            if self.clipboard_data is not None:
                self.clipboard_data.save('screen.png')
                self.clipboard_image = pygame.image.load('screen.png')
                self.w, self.h = self.clipboard_image.get_width(), self.clipboard_image.get_height()
                self.screen = pygame.display.set_mode((self.w, self.h))

        self.mouse_pos = pygame.mouse.get_pos()

    def update(self):
        if len(self.dot_positions) == 3 and not self.found_angle:
            self.angle = self.find_angle()
            self.found_angle = True
        '''self.take_pic = pyautogui.screenshot()
        self.take_pic.save("screen.png")
        self.display_screen = pygame.image.load('screen.png')'''

    def draw(self):
        self.screen.fill(BLACK)
        if self.clipboard_data is not None and self.clipboard_image is not None:
            #print(self.clipboard_image)
            self.screen.blit(self.clipboard_image, (0,0))
        if self.mouse_clicked:
            if len(self.dot_positions) == 1:
                pygame.draw.circle(self.screen, YELLOW, self.dot_positions[0], 3)
                pygame.draw.line(self.screen, RED, self.dot_positions[0], self.mouse_pos, 1)
            elif len(self.dot_positions) == 2:
                pygame.draw.circle(self.screen, YELLOW, self.dot_positions[0], 3)
                pygame.draw.line(self.screen, RED, self.dot_positions[0], self.dot_positions[1], 1)
                pygame.draw.circle(self.screen, YELLOW, self.dot_positions[1], 3)
                pygame.draw.line(self.screen, RED, self.dot_positions[1], self.mouse_pos, 1)
                print(self.dot_positions[1], self.mouse_pos)
            else:
                pygame.draw.circle(self.screen, YELLOW, self.dot_positions[0], 3)
                pygame.draw.line(self.screen, RED, self.dot_positions[0], self.dot_positions[1], 1)
                pygame.draw.circle(self.screen, YELLOW, self.dot_positions[1], 3)
                pygame.draw.line(self.screen, RED, self.dot_positions[1], self.dot_positions[2], 1)
                pygame.draw.circle(self.screen, YELLOW, self.dot_positions[2], 3)
                print(self.m1, self.m2)
                print(self.angle)
                '''x = self.screen.get_at((100, 100))
                print(x)'''

        pygame.display.update()

    def find_m(self):
        print(self.dot_positions)
        self.m1 = abs((self.dot_positions[0][1] - self.dot_positions[1][1]) / (self.dot_positions[0][0] - self.dot_positions[1][0]))
        self.m2 = abs((self.dot_positions[2][1] - self.dot_positions[1][1]) / (self.dot_positions[2][0] - self.dot_positions[1][0]))
        self.found_m = True

    def find_angle(self):
        x1, y1 = self.dot_positions[0][0], self.dot_positions[0][1]
        x2, y2 = self.dot_positions[1][0], self.dot_positions[1][1]
        x3, y3 = self.dot_positions[2][0], self.dot_positions[2][1]

        angle = math.acos((((x3 - x2) * (x1 - x2)) + ((y3 - y2) * (y1 - y2))) / ((math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)) * (math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))))

        angle = math.degrees(angle)

        return angle

# http://www.webmath.com/_answer.php
# https://www.youtube.com/watch?v=JSEPDJfl8m8
# https://stackoverflow.com/questions/550001/fully-transparent-windows-in-pygame

####################### REAL CODE ###########################

main = Main()
main.run()
