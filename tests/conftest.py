import pytest, glob, os.path

TEST_MESSAGES = {
    os.path.basename(f).rsplit('.')[0]: open(f, 'rb').read() for f in 
    glob.glob(os.path.join(os.path.dirname(__file__), "messages", "*.bin"))
}
