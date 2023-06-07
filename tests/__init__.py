import os
import sys
from typing import Literal

INSERT_POSITION: Literal[0] = 0

cwd: str = os.getcwd()
sys.path.insert(INSERT_POSITION, cwd)
