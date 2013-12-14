import os
import fnmatch
from char import PixelChar

class CharContainer(object):
    """ Main class that controls the text output to the screen with SCREEN_WIDTH and TAB_WIDTH
    """
    
    SCREEN_WIDTH = 80
    TAB_WIDTH = 4
    CHAR_DIR = "chars"
    
    def __init__(self):
        self.allChars = {}
        self.chars_height = 0
        self.preamble = ""
    
    
    def loadCharSet(self, dirname):
        """ Load char set with assumption that each char has the same height.
        """
        def all_files(root):
             for path, subdirs, files in os.walk(root):
                 files.sort( )
                 for name in files:
                    yield os.path.join(path, name)
        
        for fname in all_files(os.path.join(dirname, CharContainer.CHAR_DIR)):
            char = PixelChar()
            char.loadFromFile(fname)
            if self.chars_height and char.height() > self.chars_height:
                raise ValueError, "Found char '{0}' with different height '{1}' (previous was '{2}')".format(
                        char.name, char.height(), self.chars_height)
            self.chars_height = char.height()
            self.allChars[char.name] = char
        
        spaceChar = PixelChar()
        spaceChar.setSpaced()
        self.allChars[" "] = spaceChar
    
    
    def showMessage(self, text):
        for letter in text:
            if not letter in self.allChars:
                raise ValueError, "Letter '{0}' not found in the loaded char set".format(letter)
        
        # It will output line by line.
        for num_line in range(self.chars_height):
            line = ""
            for letter in text:
                line = " ".join((line, self.allChars[letter][num_line]))
            print(line)

if __name__ == "__main__":
    motd = CharContainer()
    motd.loadCharSet("resources")
    motd.showMessage("spoc spoc")
