"""
Adds the /src/ folder to the path in order to load package

example:
    import context
    from az.cli import az
"""
import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src/')))
