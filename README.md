# SimpleFight

[![Play in your browser](https://img.shields.io/badge/Play-in%20your%20browser-2ea44f)](https://danielstephenson.dev/play/simplefight)

A console fight: you and your enemy trade punches, each taking 1 to 10 damage a round, until one of you drops below 1 health. There is no input; every run is a new fight.

Written by Daniel McCoy Stephenson in December 2016, as one of his first programs. It is part of the "First Programs" collection on [danielstephenson.dev/play](https://danielstephenson.dev/play).

## Running it
```
python3 program5.py
```
It also still runs under Python 2 (`python2 program5.py`), which it was written for.

## Play in your browser
The program runs in a browser tab under [tak](https://github.com/Stephenson-Software/tak)'s console runtime (Python via Pyodide): https://simplefight.play.danielstephenson.dev, listed with the rest at [danielstephenson.dev/play](https://danielstephenson.dev/play).

The only change made for this was turning its Python 2 `print` statements into `print(...)` calls, which print the same text under both Python 2 and Python 3. To build and serve it locally (needs `tak` installed):
```
python3 web/build_zip.py
python3 -c "from tak.web.serve import main; main(root='.', title='SimpleFight')"
```
Pushes to `master` deploy it to [arcade](https://github.com/Stephenson-Software/arcade) (`.github/workflows/browser.yml`).
