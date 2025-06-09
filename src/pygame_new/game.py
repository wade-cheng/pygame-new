"""Define the game.

This module contains one class, `Game`, which is used to play the pygame-new example.

    >>> Game().run()
"""

from typing import Any
import pygame
from pygame.sprite import Group
import asyncio
import sys
import platform
import random

from pygame_new.game_objects import Balloon
from pygame_new.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS


class Game:
    """A simple pygame example game.

    It spawns three balloons on a blank screen. They can be popped by clicking on the
    balloon body, or dragged by their strings. When a balloon is popped, it will
    respawn at a random location.
    """

    def __init__(self) -> None:
        """Set up the game."""
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

        # This must be type annotated `Any` for now, because of current issues
        # in pygame-ce's type hinting. This is being fixed in the future.
        #
        # In an ideal world, we would use `Group[Balloon]` to provide better
        # editor integration.
        self.balloons: Group[Any] = Group(Balloon(hp=3), Balloon(hp=2), Balloon(hp=1))

    async def run(self) -> None:
        """Run the game.

        This contains a game loop that would block if it were not async. It is made
        async to be web-compatible with pygbag.

        The game loop is a simple update -> draw -> wait cycle. No delta time system
        for framerate independence is included. We lock the framerate to the specified
        constant.
        """
        while self.running:
            self.update()
            self.draw()
            self.clock.tick(FPS)
            await asyncio.sleep(0)

        pygame.quit()

    def update(self) -> None:
        """Run the update step of the game loop."""
        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

            for balloon in self.balloons:
                balloon.handle_event(event, x, y)

        if len(self.balloons) != 3:
            self.balloons.add(Balloon(hp=random.randint(1, 3)))

    def draw(self) -> None:
        """Run the draw step of the game loop."""
        self.screen.fill("white")
        for balloon in self.balloons:
            balloon.draw(self.screen)
        pygame.display.update()
