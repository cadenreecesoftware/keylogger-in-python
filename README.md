# keylogger-in-python
Keylogger built in python with pynput, includes functionality for sending log over email (commented out and filled with placeholder values).
# Keyboard Event Logger — Educational / Ethical Demo

# File: keyboard_logger.py
Purpose: Capture keyboard events on a local machine you own or are authorized to test, write them to keylog.txt, and optionally (commented-out) email the file for demonstration.

# Overview

This small Python project demonstrates how to record keyboard press and release events using pynput and how to attach the resulting keylog.txt file to an email using Python’s smtplib.
It is intended only for learning, development, debugging, or authorized security testing on systems you own or for which you have clear written permission.

# Ethical & Legal Notice

This tool must not be used to capture keystrokes on any device, account, or network you do not own or do not have explicit written authorization to test.

The author (and this repository) is not responsible for any misuse, unlawful monitoring, or privacy violations that arise from improper use.

Unauthorized keylogging can be illegal (criminal or civil liability) in many jurisdictions. Use responsibly and get consent in writing before testing on any other systems.

Make sure you understand and comply with local laws, organizational policies, and ethical guidelines before running this code.

#Features
Logs key presses and releases to keylog.txt.
Stops recording when Escape (Esc) is pressed.
Example (commented out) code to attach keylog.txt and send via SMTP for demonstration purposes only.

# Requirements

Python 3.8+
Python package:
pip install pynput

If you plan to use the email snippet (optional), you will use Python’s standard smtplib — no extra package required. For Gmail, an App Password is recommended (see notes below).

# Installation
Clone or download this repository.
Install dependencies:
pip install pynput
Place the provided keyboard_logger.py in your working directory (or rename as desired).

# Usage — Local, Authorized Testing
Open a terminal in the directory containing keyboard_logger.py.
Run:

python keyboard_logger.py

The program will create/append to keylog.txt and record events.
To stop recording and allow the program to finish, press Esc.

# Inspect keylog.txt:
cat keylog.txt

Important: Only use this on machines you own or are explicitly authorized to test.
