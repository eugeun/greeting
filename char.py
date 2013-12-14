class PixelChar(object):
    """ This class holds pixel represantation of the letter in the 'self.lines'
    """
    
    MAX_HEIGHT = 7
    MAX_WIDTH = 7
    
    def __init__(self):
        self.name = ""
        self.height = 0
        self.width = 0
        self.lines = []
    
    
    def loadFromFile(self, fname):
        """ Load char line by line with assumption that each line has the same width.
        """
        return
    
    
    def __getitem__(self, i):
        return self.lines[i]
