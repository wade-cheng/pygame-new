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

## Reference

This section provides a reference index for links, keywords, or explanations
that can be helpful for understanding this example project.

### Project management

- virtual environments (venvs) are often used to manage code projects of any language.
  - helpful material that explains this concept:
    - https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/
    - https://realpython.com/python-virtual-environments-a-primer/
  - Python venvs are managed automatically when using the uv package and project manager (https://docs.astral.sh/uv/)
- `pyproject.toml`
  - a configuration file that describes a python project
  - analogous to `Cargo.toml` (Rust) or `package.json` (npm)
  - ours specifies lints, dependencies (i.e. what's in the venv), a build system (to enable pytest), and other metadata

### Linting

We can programatically inspect a codebase for suspicious style.

- helpful material that explains this concept:
  - https://en.wikipedia.org/wiki/Lint_(software)
- ruff is the linter we have configured (https://docs.astral.sh/ruff/)
- mypy is the type checker we have installed (https://mypy-lang.org/)
  - unlike ruff, we have only specified it as a dev dependency---no configurations were added
  - type checking is a subset of linting. But it is different enough from other types of linting that in colloquial speech, linting can be used to mean "linting, except type checking." This leaves type checking its own separate term. <!-- TODO: is this true? Even if it is a teensy bit, this may be redundant. Consider changing to just the first sentence. -->
- other linters you may have heard of are
  - the black formatter (https://github.com/psf/black/)
  - the flake8 linter (https://github.com/PyCQA/flake8/)

### Formatting

We can programatically format the code.

- some motivation for formatting exists at https://github.com/psf/black/
- this can be enabled on save, if desired. left as an exercise to the reader.

### Testing

Programmatically testing a codebase is useful.

- helpful material that explains this concept:
  - https://docs.pytest.org/en/stable/explanation/
  - Unit Testing Principles, Practices, and Patterns (ISBN-13 978-1617296277)
- pytest: the testing framework we use (https://docs.pytest.org/en/stable/)
- doctest: a testing framework we don't use (https://docs.python.org/3/library/doctest.html)
  - this fills a different niche than pytest by testing code in docstrings
  - but pytest is able to run doctest
  - can be helpful---left as an exercise to the reader
- unittest: a testing framework we don't use (https://docs.python.org/3/library/unittest.html)
  - this fills the same niche as pytest
  - pytest can run unittest tests, but if you have a new project, might as well stick to one framework

## Meta

Some other content for this README is planned:

- Why pygame-new?
- Design Decisions
- A guided tour
