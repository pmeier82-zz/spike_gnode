#!/usr/bin/env python

import os
import sys

## MAIN

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spike_gnode.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

## EOF
