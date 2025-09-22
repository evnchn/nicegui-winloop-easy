# NiceGUI + Winloop — easy integration

A minimal, known-working way to use Winloop (@Vizonex/Winloop) — a Windows-focused drop-in asyncio event loop implementation similar in spirit to uvloop — with a NiceGUI project.

This repository contains a tiny example showing how to install and enable Winloop so NiceGUI runs on Winloop's event loop policy. Users report observable improvements in page load times. When the server is terminated you should see Winloop-related messages in the console confirming the loop was in use.

## Requirements
- Windows (Winloop is a Windows-specific loop implementation)
- Python (use a reasonably recent Python 3.x supported by Winloop and NiceGUI)

## Installation

1. Install dependencies:

```
pip install nicegui winloop
```

2. Save the example below to example.py and run it with Python.

## Example (example.py)

```python
import asyncio
import winloop

# Install Winloop's event loop policy before importing/starting NiceGUI
asyncio.set_event_loop_policy(winloop.EventLoopPolicy())

from nicegui import ui

@ui.page('/')
def index():
    ui.label('Hello NiceGUI + Winloop!')

if __name__ == '__main__':
    ui.run(title='NiceGUI + Winloop', host='0.0.0.0', port=8080)
```

## Run

```
python example.py
```

Open http://localhost:8080 — you should notice snappier page loads in many cases.

## Verify Winloop is active

- When shutting down the server, check the console output. Winloop prints messages on start/stop; seeing those messages is a good indicator the Winloop policy was used.

## Notes

- This repo is intentionally minimal: its goal is to be a simple drop-in example for NiceGUI + Winloop integration.
- Results will vary depending on your application and environment; benchmarks are encouraged for any production use.

## License

No license file is included in this repository.