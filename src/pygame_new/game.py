import pygame
from pygame.sprite import Group
import asyncio
import sys
import platform
import random

from pygame_new.game_objects import Balloon
from pygame_new.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("pygame-new")
        if sys.platform == "emscripten":
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            platform.document.body.style.background = "white"
            platform.document.getElementById(
                "canvas"
            ).style.imageRendering = "pixelated"
        else:
            pygame.display.set_icon(pygame.image.load("assets/favicon.png"))

            self.screen = pygame.display.set_mode(
                (WINDOW_WIDTH, WINDOW_HEIGHT), flags=0, vsync=1
            )

        self.clock = pygame.time.Clock()
        self.running = True

        Balloon.setup_sprites(
            [
                pygame.image.load("assets/red_balloon.png"),
                pygame.image.load("assets/orange_balloon.png"),
                pygame.image.load("assets/yellow_balloon.png"),
            ]
        )

        self.balloons: Group[Balloon] = Group(
            Balloon(hp=3), Balloon(hp=2), Balloon(hp=1)
        )

    async def run(self):
        while self.running:
            self.update()
            self.draw()
            self.clock.tick(FPS)
            await asyncio.sleep(0)

        pygame.quit()

    def update(self):
        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

            for balloon in self.balloons:
                balloon.handle_event(event, x, y)

        if len(self.balloons) != 3:
            self.balloons.add(Balloon(hp=random.randint(1, 3)))

    def draw(self):
        self.screen.fill("white")
        for balloon in self.balloons:
            balloon.draw(self.screen)
        pygame.display.update()
