from char import PixelChar

class CharContainer(object):
    """ Main class that controls the text output to the screen with SCREEN_WIDTH and TAB_WIDTH
    """
    
    SCREEN_WIDTH = 80
    TAB_WIDTH = 80
    
    def __init__(self):
        self.allChars = {}
        self.preamble = ""
    
    
    def loadCharSet(self, dirname):
        """ Load char set with assumption that each char has the same height.
        """
        return
    
    def showMessage(self, text):
        return
