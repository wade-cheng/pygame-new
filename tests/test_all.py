from pygame import Event, MOUSEBUTTONDOWN, MOUSEBUTTONUP

from pygame_new.game_objects import Balloon


class TestBalloonHitboxes:
    def test_a_clicked_balloon_should_pop(self) -> None:
        # arrange
        b = Balloon(top=0, left=0, hp=3)

        # act
        b.handle_event(Event(MOUSEBUTTONDOWN), mousex=1, mousey=1)

        # assert
        assert b._hp == 2

    def test_balloons_move_when_dragged_by_string(self) -> None:
        # arrange
        b = Balloon(top=0, left=0, hp=3)
        dx, dy = 3, 1
        startx, starty = Balloon._DRAGBOX_OFFSET
        endx, endy = Balloon._DRAGBOX_OFFSET[0] + dx, Balloon._DRAGBOX_OFFSET[1] + dy

        # act
        b.handle_event(Event(MOUSEBUTTONDOWN), mousex=startx, mousey=starty)
        b.handle_event(Event(MOUSEBUTTONUP), mousex=endx, mousey=endy)

        # assert
        assert b._top == 1
        assert b._left == 3
