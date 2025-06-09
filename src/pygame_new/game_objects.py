from pygame import Surface, Rect, Event, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame.sprite import Sprite
import random

from pygame_new.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class Balloon(Sprite):
    """
    A balloon that can be spawned with health points at an arbitrary location.

    # Preconditions

    Before any balloon is drawn, `Balloon.setup_sprites` must be used to globally
    define the sprites for different hp values. If a list of sprites are provided
    and a balloon has some `hp`, the `hp - 1`th (zero-indexed) sprite is used.
    """

    # `DRAGBOX` and `HURTBOX` define where, relative to the top left of a balloon,
    # a click will drag or hurt it. That is, they encode an offset and a size.
    _HURTBOX_OFFSET = (0, 0)
    _HURTBOX = Rect(0, 0, 16, 20).move(*_HURTBOX_OFFSET)
    _DRAGBOX_OFFSET = (6, 20)
    _DRAGBOX = Rect(0, 0, 4, 19).move(*_DRAGBOX_OFFSET)

    # list of sprites to use for drawing different hp values.
    _SPRITES: list[Surface] | None = None

    @staticmethod
    def setup_sprites(sprites: list[Surface]):
        Balloon._SPRITES = sprites

    def __init__(self, hp: int, top: int | None = None, left: int | None = None):
        assert hp > 0

        super().__init__()

        self._hp = hp

        if top is None:
            self._top = random.randint(0, WINDOW_HEIGHT - 20)
        else:
            self._top = top

        if left is None:
            self._left = random.randint(0, WINDOW_WIDTH - 20)
        else:
            self._left = left

        # Some (x,y) if we are currently dragging and need the sprite to follow
        # the mouse by setting the topleft to mouse + (x,y). None if we are not
        # dragging.
        self._dragging_offset: tuple[int, int] | None = None

    def handle_event(self, e: Event, mousex: int, mousey: int):
        """We assume mouse down and up events can only alternate."""
        if e.type == MOUSEBUTTONDOWN:
            # if the balloon's hurtbox touches the mouse
            if Balloon._HURTBOX.move(self._left, self._top).collidepoint(
                mousex, mousey
            ):
                self._hp -= 1
                if self._hp == 0:
                    self.kill()
            # if the balloon's dragbox touches the mouse
            elif Balloon._DRAGBOX.move(self._left, self._top).collidepoint(
                mousex, mousey
            ):
                self._dragging_offset = (
                    self._left - mousex,
                    self._top - mousey,
                )

        match self._dragging_offset:
            case (xoffset, yoffset):
                self._left = xoffset + mousex
                self._top = yoffset + mousey
            case _:
                pass

        if e.type == MOUSEBUTTONUP:
            self._dragging_offset = None

    def draw(self, screen: Surface):
        assert Balloon._SPRITES is not None
        screen.blit(Balloon._SPRITES[self._hp - 1], dest=(self._left, self._top))
