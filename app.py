import sys
import os
import ctypes
import time
import webview
import keyboard

def is_admin() -> bool:
    """Check if the current process has administrator rights."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def relaunch_as_admin() -> bool:
    """Relaunch the script with admin rights."""
    if os.name != "nt":
        return False
    params = " ".join([f'"{arg}"' for arg in sys.argv])
    executable = sys.executable
    try:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", executable, params, None, 1
        )
        return True
    except Exception as e:
        print(f"[ERROR] Failed to relaunch as admin: {e}")
        return False

class Api:
    ...

if __name__ == "__main__":
    start_time = time.perf_counter()

    if os.name == "nt" and not is_admin():
        print("[INFO] Relaunching with administrator privileges...")
        if relaunch_as_admin():
            sys.exit(0)
        else:
            sys.exit(1)

    HTML_PATH = os.path.abspath(os.path.join("public", "index.html"))

    api = Api()
    window = webview.create_window(
        title="Hotkeys",
        url=HTML_PATH,
        frameless=False,
        easy_drag=True,
        width=450,
        height=600,
        resizable=False,
        js_api=api,
        on_top=True
    )
    
    end_time = time.perf_counter()
    print(f"[INFO] Application initialized in {end_time - start_time:.4f} seconds")
    webview.start(debug=False)
