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
        self.found_angle = False
        self.angle = 0
        self.clipboard_data = ImageGrab.grabclipboard()
        if self.clipboard_data is not None:
            self.clipboard_data.save('Screen.png')
            self.clipboard_image = pygame.image.load('Screen.png')
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    self.clipboard_data = ImageGrab.grabclipboard()

                    if self.clipboard_data is not None:
                        self.clipboard_data.save('Screen.png')
                        self.clipboard_image = pygame.image.load('Screen.png')
                        self.w, self.h = self.clipboard_image.get_width(), self.clipboard_image.get_height()
                        self.screen = pygame.display.set_mode((self.w, self.h))

        self.mouse_pos = pygame.mouse.get_pos()

    def update(self):
        if len(self.dot_positions) == 3 and not self.found_angle:
            self.angle = self.find_angle()
            self.found_angle = True

    def draw(self):
        self.screen.fill(BLACK)
        if self.clipboard_data is not None and self.clipboard_image is not None:
            self.screen.blit(self.clipboard_image, (0, 0))
        else:
            self.draw_text('Press v to paste', self.screen, (205, HEIGHT / 2 - 27), 27, GREY, 'times new roman')
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
                print(self.angle)

        pygame.display.update()

    def find_angle(self):
        x1, y1 = self.dot_positions[0][0], self.dot_positions[0][1]
        x2, y2 = self.dot_positions[1][0], self.dot_positions[1][1]
        x3, y3 = self.dot_positions[2][0], self.dot_positions[2][1]

        angle = math.acos((((x3 - x2) * (x1 - x2)) + ((y3 - y2) * (y1 - y2))) / (
                (math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)) * (math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))))

        angle = math.degrees(angle)

        return angle

####################### REAL CODE ###########################

    def draw_text(self, words, screen, pos, size, colour, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, 0, colour)
        text_size = text.get_size()
        screen.blit(text, pos)


####################### REAL CODE ###########################


main = Main()
main.run()
