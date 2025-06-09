# pygame-new

A minimal pygame example project with

- pygbag support
- a test suite
- code as a library and small main file

This project is managed with the [uv](https://docs.astral.sh/uv/) project manager.
After installation, run this game in your browser with

```
uv run pygbag --icon src/assets/favicon.png src/main.py
```

or traditionally with

```
cd src; uv run main.py; cd ..
```

Run the unit tests with

```
uv run pytest -v
```

or drop the `-v` for less verbosity.
