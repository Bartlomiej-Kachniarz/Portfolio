import os
import sys

import pytest

# This is a bypass to import a decorator from another module:

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from counting_partitions import count_partitions  # noqa: E402


def test_count_partitions():
    assert count_partitions(340) == "No of partitions: 8\n"
