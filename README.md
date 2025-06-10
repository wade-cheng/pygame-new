# pygame-new

A general-purpose minimal pygame example project with

- pygbag support
- a test suite
- code as a library and small main file

This project is managed with the [uv](https://docs.astral.sh/uv/) project manager.
After installation, try out some commands:

```
# run this game in your browser
uv run pygbag --icon src/assets/favicon.png src/main.py

# run this game traditionally
cd src; uv run main.py; cd ..

# run the unit tests
uv run pytest -v
# with less verbosity,
uv run pytest

# lint
uv run ruff check
uv run mypy src tests

# format
uv run ruff format
```
