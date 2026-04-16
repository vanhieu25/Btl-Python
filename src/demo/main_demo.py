#!/usr/bin/env python3
"""
Entry point cho Demo Dashboard
Chạy: python main_demo.py
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main_window_demo import main

if __name__ == "__main__":
    main()