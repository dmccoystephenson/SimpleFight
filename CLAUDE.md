# CLAUDE.md

## Project overview

SimpleFight: a console fight in which you and your enemy (100 health each) trade punches for 1 to 10 damage a round until one drops below 1 health. There is no input; every run is a new random fight. It is one of Daniel McCoy Stephenson's first programs, revived in 2026 as part of the "First Programs" collection at https://danielstephenson.dev/play, and it is playable in a browser at https://simplefight.play.danielstephenson.dev.

## Technology stack

- Python, a single script (`program5.py`) with no dependencies beyond the standard library.
- It runs under both Python 3 and Python 2 (it was written for Python 2).
- Browser build: [tak](https://github.com/Stephenson-Software/tak)'s console runtime (Python via Pyodide), pinned in `.github/workflows/browser.yml` to commit `9b539d8760e2c02cc262a7dcff6d0c541572ab71`.
- Deployment: GitHub Actions + `Stephenson-Software/arcade-deploy@v1` to arcade (slug `simplefight`).

## Build and run commands

```bash
# Run it in a terminal
python3 program5.py
python2 program5.py   # still works

# Build the browser bundle (needs tak installed; Python 3.12 in CI)
pip install "tak @ git+https://github.com/Stephenson-Software/tak@9b539d8760e2c02cc262a7dcff6d0c541572ab71"
python3 web/build_zip.py          # writes web/index.html and web/game.zip

# Serve it locally, cross-origin isolated
python3 -c "from tak.web.serve import main; main(root='.', title='SimpleFight')"
```

## Test commands

There is no test suite. The only automated check is the `Browser build` workflow (`.github/workflows/browser.yml`), which runs on every pull request: it builds the bundle and asserts that `web/game.zip` contains `program5.py` plus tak's `console-worker.js` and `boot.js`, and that `web/index.html` calls `TakConsole.start(` with `program5.py`. To check a change locally, run the script under `python3` (and `python2`) and run `python3 web/build_zip.py`.

## Repository layout

```
program5.py                    The program (the browser entry point too)
version.txt                    Version (0.1.0); the deploy version is this plus the commit SHA
web/build_zip.py               Builds web/index.html and web/game.zip with tak
.github/workflows/browser.yml  PR build check; deploys to arcade on push to master
```

`web/index.html`, `web/game.zip` and `web/version.txt` are build output and are gitignored.

## Coding conventions

- Tabs for indentation in the program, as originally written.
- `print(...)` calls only, so the output is identical under Python 2 and Python 3. Avoid Python-3-only syntax (f-strings, etc.) unless Python 2 support is deliberately dropped and the README updated.

## Do / Don't

**Do:**
- Keep the program's behaviour and output as it was originally written; this is a preserved early program, and the README lists every change made for the browser build.
- Keep `program5.py` as the entry point and keep its name in sync across `web/build_zip.py`, the workflow's bundle assertion and the README.
- Update the README when a change alters what the program does or how it runs.

**Don't:**
- Don't commit `web/index.html`, `web/game.zip` or `web/version.txt`.
- Don't change the pinned tak commit, the arcade slug (`simplefight`) or the deploy step without a reason; a push to master deploys a new arcade version.
- Don't add input prompts or dependencies without checking they work under tak's console runtime in the browser.
