"""Describes objects that appear in this game.

For this example program, a single `Balloon` class is defined.
"""

from sdbg import dprint

import pygame
from pygame import Surface, Rect, Event
from pygame.sprite import Sprite
import random

from pygame_new.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class Balloon(Sprite):
    """A balloon that can be spawned with health points at an arbitrary location.

    # Preconditions

    Before any balloon is drawn, `Balloon.setup_sprites` must be used to globally
    define the sprites for different hp values. If a list of sprites are provided
    and a balloon has some `hp`, the `hp - 1`th (zero-indexed) sprite is used to
    draw the balloon.

    This implies if the balloon is drawn, `hp` must always be greater than zero
    and less than the length of an existing given sprite list.
    """

    # `DRAGBOX` and `HURTBOX` define where, relative to the top left of a balloon,
    # a click will drag or hurt it. That is, they encode an offset and a size.
    # These are currently hardcoded values chosen to accompany the balloon image
    # in `pygame-new/src/assets`.
    _DRAGBOX_OFFSET = (6, 20)
    _DRAGBOX = Rect(0, 0, 4, 19).move(*_DRAGBOX_OFFSET)
    _HURTBOX_OFFSET = (0, 0)
    _HURTBOX = Rect(0, 0, 16, 20).move(*_HURTBOX_OFFSET)

    _SPRITES: list[Surface] | None = None
    """List of sprites to use for drawing different hp values."""

    @staticmethod
    def setup_sprites(sprites: list[Surface]) -> None:
        """Globally defines the sprites for different hp values.

        If a list of sprites are provided and a balloon has some `hp`, the `hp - 1`th
        (zero-indexed) sprite is used to draw the balloon. This implies if the balloon
        is drawn, `hp` must always be greater than zero and less than the length of an
        existing given sprite list.

        Calling the function more than once is allowed and swaps all balloons
        to the new sprite list.
        """
        Balloon._SPRITES = sprites

    def __init__(
        self, hp: int, top: int | None = None, left: int | None = None
    ) -> None:
        """Initialize a Balloon."""
        assert hp > 0

        Sprite.__init__(self)

        self._hp = hp
        """The balloon's current hp. Must never be `<= 0`. If self is drawn, also
        must never be `> len(Balloon._SPRITES)`."""

        if top is None:
            self._top = random.randint(0, WINDOW_HEIGHT - 20)
        else:
            self._top = top

        if left is None:
            self._left = random.randint(0, WINDOW_WIDTH - 20)
        else:
            self._left = left

        self._dragging_offset: tuple[int, int] | None = None
        """Some (x,y) if we are currently dragging and need the sprite to follow
        the mouse by setting the topleft to mouse + (x,y). None if we are not
        dragging."""

    def handle_event(self, e: Event) -> None:
        """Update the Balloon's state, given an event and the current mouse position.

        This function assumes mouse down and up events can only alternate.
        """
        match e:
            case Event(type=pygame.MOUSEBUTTONDOWN, pos=(x, y)):
                dprint("mbd'd (should happen thrice (once per balloon) per click)")

                # if the balloon's hurtbox touches the mouse
                if Balloon._HURTBOX.move(self._left, self._top).collidepoint(x, y):
                    self._hp -= 1
                    if self._hp == 0:
                        self.kill()
                # if the balloon's dragbox touches the mouse
                elif Balloon._DRAGBOX.move(self._left, self._top).collidepoint(x, y):
                    self._dragging_offset = (
                        self._left - x,
                        self._top - y,
                    )
            case Event(type=pygame.MOUSEBUTTONUP):
                self._dragging_offset = None
            case Event(type=pygame.MOUSEMOTION, pos=(x, y)):
                match self._dragging_offset:
                    case (xoffset, yoffset):
                        self._left = xoffset + x
                        self._top = yoffset + y
                    case None:
                        pass
            case _:
                pass

    def draw(self, screen: Surface) -> None:
        """Draw this balloon onto the given screen.

        See preconditions described in `Balloon`.
        """
        assert Balloon._SPRITES is not None
        screen.blit(Balloon._SPRITES[self._hp - 1], dest=(self._left, self._top))
