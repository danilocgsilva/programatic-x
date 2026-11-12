# programatic-x

A cross-platform Python library for programmatically clicking the OS Start button. It detects the current operating system at runtime and applies the most appropriate strategy — image recognition on Windows, or a keyboard shortcut on Linux.

## Overview

`programatic-x` abstracts away platform differences behind a single factory call. On Windows, it uses screenshot-based template matching (via `pyautogui` and `opencv`) to locate and click the Start button. On Linux and other platforms, it sends the Super key combination via `ydotool`.

## Installation

Install from the local source with pip:

```bash
pip install -e .
```

**Runtime dependencies** (installed automatically via `pyproject.toml`):

| Package | Purpose |
|---|---|
| `pyautogui` | Screen capture, image location, mouse click simulation |
| `pillow` | Image I/O, required by pyautogui |
| `opencv-python` | Enables confidence-based fuzzy template matching |

**System dependency (Linux only):**

- [`ydotool`](https://github.com/ReimuNotMoe/ydotool) — a Wayland-compatible input injection tool. Install it through your distribution's package manager (e.g., `sudo apt install ydotool`). It is not available via pip.

## Quick Start

```python
from programatic_x import ButtonStartFactory

button = ButtonStartFactory.create_button_start()
button.click()
```

That is the entire public API. The factory returns the correct implementation for the current OS, and `click()` performs the action.

## Usage Example

```python
from programatic_x import ButtonStartFactory
from programatic_x.exceptions.CouldNotLocateStartButton import CouldNotLocateStartButton

button = ButtonStartFactory.create_button_start()

try:
    button.click()
    print("Start button clicked successfully.")
except CouldNotLocateStartButton as e:
    print(f"Could not find the Start button on screen: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

> **Note:** Scripts must be run from the repository root directory. The Windows image assets are resolved relative to the working directory (`assets/<image>.png`).

## Architecture

```
ButtonStartFactory
    │
    ├── Windows  →  WindowsButtonStart   (image recognition via pyautogui)
    │                   └── Tries 3 reference assets in assets/ at 0.8 confidence
    │                   └── Raises CouldNotLocateStartButton if all fail
    │
    └── Other    →  MainStartKey         (Super key via ydotool, Linux/Wayland)
```

The design uses three patterns:

- **Factory** — `ButtonStartFactory` encapsulates OS detection and instantiation.
- **Strategy / Interface** — `ButtonStartInterface` enforces a uniform `click()` contract across all implementations.
- **Template assets** — reference PNG screenshots in `assets/` drive Windows image matching.

## API Reference

### `ButtonStartFactory`

The main entry point. Exposed directly from the package root.

```python
from programatic_x import ButtonStartFactory
```

#### `ButtonStartFactory.create_button_start() -> ButtonStartInterface`

Detects the current OS via `platform.system()` and returns the appropriate implementation.

| OS | Returns |
|---|---|
| Windows | `WindowsButtonStart` |
| Linux / other | `MainStartKey` |

---

### `ButtonStartInterface`

Abstract base class. All concrete implementations inherit from this.

```python
from programatic_x.interfaces.ButtonStartInterface import ButtonStartInterface
```

#### `click() -> None`

Performs the platform-specific action to open the Start menu. May raise exceptions on failure (see below).

---

### `WindowsButtonStart`

Windows implementation. Uses image recognition to find and click the Start button.

```python
from programatic_x.WindowsButtonStart import WindowsButtonStart
```

#### `click() -> None`

Iterates over three bundled reference images in order, attempting each at 0.8 confidence:

1. `windows11_start_menu_100_dark.png` — dark theme, 100% DPI scaling
2. `windows11_start_menu_100_light.png` — light theme, 100% DPI scaling
3. `windows11_start_menu_150_light.png` — light theme, 150% DPI scaling

Clicks the center of the first successful match and returns. If all three fail, raises `CouldNotLocateStartButton`.

---

### `MainStartKey`

Linux/other implementation. Uses `ydotool` to send a Super key combination.

```python
from programatic_x.MainStartKey import MainStartKey
```

#### `click() -> None`

Waits 3 seconds, then executes:

```bash
ydotool key 125:1 31:1 31:0 125:0
```

This simulates pressing and releasing the Super (Win) key, which opens the application launcher on most Linux desktop environments.

> The 3-second delay is hardcoded to allow time for the desktop to be in focus before the key event is sent.

---

### `Image`

Internal utility for locating images on screen. Used by `WindowsButtonStart`.

```python
from programatic_x.Image import Image
```

#### `Image.get_image_path(image_name: str) -> str`

Resolves an image filename to `assets/<image_name>` relative to the working directory.

#### `Image.get_center(image_name: str, confidence: float = 0.6) -> tuple`

Locates `image_name` on the screen using `pyautogui.locateOnScreen` and returns the center coordinate of the matched region. Raises an `Exception` if the image is not found.

---

### `CouldNotLocateStartButton`

Custom exception raised by `WindowsButtonStart` when no reference image matches the screen.

```python
from programatic_x.exceptions.CouldNotLocateStartButton import CouldNotLocateStartButton
```

Inherits from the built-in `Exception`. Catch it to handle the "button not found" case gracefully.

---

## Assets

The `assets/` directory contains reference screenshots of the Windows 11 Start button used for template matching:

| File | Theme | DPI Scaling |
|---|---|---|
| `windows11_start_menu_100_dark.png` | Dark | 100% |
| `windows11_start_menu_100_light.png` | Light | 100% |
| `windows11_start_menu_150_light.png` | Light | 150% |

If your environment uses a different theme or DPI setting not covered by these assets, add a matching screenshot to `assets/` and register it in the `image_configs` list inside `WindowsButtonStart.click()`.

## Running the Smoke Test

A manual test script is included in `active_tests/`:

```bash
python active_tests/start.py
```

This runs the full factory → click flow and prints the result. It is excluded from the installable package.

## Known Limitations

- **Windows 10 not supported** — the bundled assets only cover Windows 11. Add your own screenshots for Windows 10 compatibility.
- **Linux requires `ydotool`** — the system package must be installed separately. If it is not present, `click()` will fail silently or raise a subprocess error.
- **Working directory sensitive** — asset paths are resolved relative to `assets/` in the current working directory. Always run scripts from the repository root.
- **Linux delay is not configurable** — `MainStartKey` always waits 3 seconds before sending keys.
- **No X11 image recognition** — on Linux, there is no image-based fallback; `ydotool` is always used regardless of the display server.
