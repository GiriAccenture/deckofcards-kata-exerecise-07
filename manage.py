#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    print("Hello everyone. I had completed kata 07.")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spades.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
