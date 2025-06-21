from pygame import Event, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, Vector2

from pygame_new.game_objects import Balloon


class TestBalloonHitboxes:
    def test_a_clicked_balloon_should_pop(self) -> None:
        # arrange
        b = Balloon(top=0, left=0, hp=3)

        # act
        b.handle_event(Event(MOUSEBUTTONDOWN, pos=(1, 1)))

        # assert
        assert b._hp == 2

    def test_balloons_move_when_dragged_by_string(self) -> None:
        # arrange
        DELTA = Vector2(3, 1)
        BALLOON_START = Vector2(1, 0)
        BALLOON_END = BALLOON_START + DELTA
        CLICK_START = BALLOON_START + Balloon._DRAGBOX_OFFSET
        CLICK_END = BALLOON_START + Balloon._DRAGBOX_OFFSET + DELTA

        b = Balloon(top=BALLOON_START[1], left=BALLOON_START[0], hp=3)

        # act
        b.handle_event(Event(MOUSEBUTTONDOWN, pos=tuple(CLICK_START)))
        b.handle_event(Event(MOUSEMOTION, pos=tuple(CLICK_END)))

        # assert
        assert (b._left, b._top) == BALLOON_END

    def test_balloons_stay_when_string_clicked(self) -> None:
        # arrange
        DELTA = Vector2(3, 1)
        BALLOON_START = Vector2(1, 0)
        CLICK_START = BALLOON_START + Balloon._DRAGBOX_OFFSET
        CLICK_END = BALLOON_START + Balloon._DRAGBOX_OFFSET + DELTA

        b = Balloon(top=BALLOON_START[1], left=BALLOON_START[0], hp=3)

        # act
        b.handle_event(Event(MOUSEBUTTONDOWN, pos=tuple(CLICK_START)))
        b.handle_event(Event(MOUSEBUTTONUP, pos=tuple(CLICK_START)))
        b.handle_event(Event(MOUSEMOTION, pos=tuple(CLICK_END)))

        # assert
        assert (b._left, b._top) == BALLOON_START
