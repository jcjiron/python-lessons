# python-lessons

A tutorial on programming styles in Python, using a single anchor project
(**Order System**) rewritten under 11 different approaches.

## Anchor project

A small system that: receives an order's items, applies discount/coupon
rules, checks available stock, and produces a receipt with the total.
Enough meat for every style to feel different, small enough to stay
readable.

## Lesson roadmap

| # | Style | Folder |
|---|-------|--------|
| 1 | Ad-hoc / Code-First | `lessons/01_ad_hoc/` |
| 2 | TDD | `lessons/02_tdd/` |
| 3 | BDD | `lessons/03_bdd/` |
| 4 | ATDD | `lessons/04_atdd/` |
| 5 | Outside-In | `lessons/05_outside_in/` |
| 6 | Inside-Out | `lessons/06_inside_out/` |
| 7 | DDD | `lessons/07_ddd/` |
| 8 | Functional-first | `lessons/08_functional/` |
| 9 | Data/Pipeline-driven | `lessons/09_pipeline/` |
| 10 | Event-driven | `lessons/10_event_driven/` |
| 11 | Exploratory/Spike | `lessons/11_exploratory/` |

Each folder has its own `README.md` explaining the style and the code that
illustrates it.

## Setup

### Install Python 3

- **Windows:** download the installer from
  [python.org/downloads](https://www.python.org/downloads/). During setup,
  check **"Add python.exe to PATH"** before clicking Install.
- **macOS:** download the installer from
  [python.org/downloads](https://www.python.org/downloads/), or install via
  [Homebrew](https://brew.sh/): `brew install python3`.

### Verify the install

```bash
python3 --version
```
(On Windows, if `python3` isn't recognized, try `python --version` instead.)
You should see `Python 3.x.x`.

### Run the tests

Each lesson's tests run with the standard library's `unittest` — no extra
installs needed. From inside a lesson's folder:

```bash
cd lessons/02_tdd
python3 -m unittest discover -s . -p "test_*.py" -v
```

(Some lessons may need an extra step of their own — check that lesson's
`README.md` if so.)
