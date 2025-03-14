print("__name__ is", __name__)
DEV = True # True for development with hot reload, False for production with no hot reload

import sys
import asyncio
from nicegui import ui 
# NOTE: no less amount of import compared to importing just the ui_run function, check by len(sys.modules)
# TODO: can we enhance the speed of `from nicegui.ui_run import run as ui_run`? 

def debug_loop_type():
    return f"{__name__} - {asyncio.get_event_loop_policy()}"

def attach_winloop_if_needed():
    print(f"Platform: {sys.platform}")
    if sys.platform in ('win32', 'cygwin', 'cli'):
        import winloop
        winloop.install()

def attach_and_debug(name):
    print(f"Trying to attach winloop for {name}...")
    attach_winloop_if_needed()
    print(f"{name} code:", debug_loop_type())

attach_and_debug("main code")

if not DEV or not __name__ == "__main__":
    # === PUT YOUR CODE HERE ===
    from nicegui import app

    @ui.page("/")
    def index():
        ui.label("Hello, world! Is this fast?")
        ui.label(debug_loop_type())

    # === END OF YOUR CODE ===

    def handle_startup():
        attach_and_debug("startup code")

    app.on_startup(handle_startup)

ui.run(reload=DEV, port=7777)