import glob
import os.path

import fints.parser
import pytest

TEST_MESSAGES = {
    os.path.basename(f).rsplit('.')[0]: open(f, 'rb').read() for f in 
    glob.glob(os.path.join(os.path.dirname(__file__), "messages", "*.bin"))
}

# We will turn off robust mode generally for tests
fints.parser.robust_mode = False
