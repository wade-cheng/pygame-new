from pygame_new import Game
import asyncio


async def main() -> None:
    await Game().run()


if __name__ == "__main__":
    asyncio.run(main())
