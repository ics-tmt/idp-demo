#!/usr/bin/env python3
"""
Python script to display the current local date and time.
"""
from datetime import datetime

def get_current_time():
    """
    Return the current local datetime.
    """
    return datetime.now()

if __name__ == "__main__":
    now = get_current_time()
    print("Current time:", now)