Linux Mouse Jiggler
A simple GUI application that prevents your computer from going to sleep by periodically moving the mouse cursor slightly. Perfect for keeping your system active during presentations, downloads, or remote work sessions.
Features

GUI Interface: Easy-to-use graphical interface built with Tkinter
Adjustable Interval: Set jiggle interval from 1 to 300 seconds using slider or text input
Non-Intrusive: Moves mouse 1 pixel right then back to original position
Start/Stop Control: Toggle the jiggler on/off with a single button
Status Indicator: Visual feedback showing current running state
Lightweight: Minimal resource usage, runs in background thread

Requirements

Python 3.x
tkinter (usually included with Python)
pynput library

Installation
Step 1: Install Python Dependencies
On CachyOS/Arch Linux, you'll encounter the "externally-managed-environment" error when trying to install pynput with pip. Here's how to fix it:
bash# Option 1: Override the restriction (simplest)
pip install pynput --break-system-packages

# Option 2: Use pipx (recommended for applications)
sudo pacman -S python-pipx
pipx install pynput

# Option 3: Use virtual environment (cleanest)
python -m venv mouse_jiggler_env
source mouse_jiggler_env/bin/activate
pip install pynput
Step 2: Download the Script
Save the Python code as mouse_jiggler.py in your desired location.
Usage
Running the Application
bash# If you used Option 1 (--break-system-packages)
python mouse_jiggler.py

# If you used Option 2 (pipx)
python mouse_jiggler.py

# If you used Option 3 (virtual environment)
source mouse_jiggler_env/bin/activate
python mouse_jiggler.py
Using the Interface

Set Interval: Use the slider or type directly in the text field to set how often the mouse should jiggle (1-300 seconds)
Start Jiggling: Click the "Start" button to begin mouse jiggling
Stop Jiggling: Click the "Stop" button to halt the process
Monitor Status: The status label shows whether the jiggler is running or stopped

How It Works
The application uses the pynput library to:

Get the current mouse position
Move the cursor 1 pixel to the right
Wait 0.1 seconds
Move the cursor back to its original position
Wait for the specified interval before repeating

This minimal movement is enough to prevent screen savers and sleep mode while being virtually unnoticeable during normal computer use.
Troubleshooting
"ModuleNotFoundError: No module named 'pynput'"
This means pynput isn't installed. Follow the installation steps above.
"externally-managed-environment" error
Modern Linux distributions prevent global pip installations. Use one of the three options provided in the installation section.
Permission Issues
If you encounter permission errors, ensure your user has access to control input devices. You may need to add your user to the input group:
bashsudo usermod -a -G input $USER
Then log out and back in.
GUI Not Appearing
Make sure you have a display server running (X11 or Wayland) and that tkinter is properly installed:
bashsudo pacman -S tk
Technical Details

Language: Python 3
GUI Framework: Tkinter (built-in)
Input Control: pynput library
Threading: Uses daemon threads for non-blocking operation
Platform: Linux (tested on CachyOS/Arch)

Why This Solution?
Many mouse jiggler solutions are either:

Command-line only (not user-friendly)
Windows-specific
Require complex setup
Use excessive system resources

This application provides a simple, lightweight, cross-platform solution with an intuitive GUI that anyone can use.
License
This is a simple utility script - feel free to modify and distribute as needed.
