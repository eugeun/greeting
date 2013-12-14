import os
from charcontainer import CharContainer

CHARSET_DIR = "chars"

def main():
    motd = CharContainer()
    workdir = "."
    motd.loadCharSet(os.path.join(workdir, CHARSET_DIR))
    text = "Hello world"
    motd.showMessage(text)


main()
