"""Runs the example game."""

from pygame_new import Game
import asyncio


async def main() -> None:
    """Use `Game` to start playing."""
    await Game().run()


if __name__ == "__main__":
    asyncio.run(main())
