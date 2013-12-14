import codecs
import os


CODEC="UTF-8"


class PixelCharException(Exception): pass


class PixelChar(object):
    """ This class holds pixel represantation of the letter in the 'self.lines'
    """
    
    MAX_HEIGHT = 7
    MAX_WIDTH = 7
    
    def __init__(self):
        self.name = ""
        self.lines = []
    
    
    def loadFromFile(self, fname):
        """ It takes 2 assumption:
        - 'fname' is 'self.name' without extension (and therefor it should have only one letter length)
        - all lines of the fname should be the same length.
        """
        name = os.path.basename(fname).split(".")[0]
        if len(name) > 1:
            raise ValueError, "The name of the file is longer than one letter"
        self.name = name
        
        error = None
        fh = None
        prev_length = 0
        try:
            fh = codecs.open(fname, CODEC)
            for line in fh:
                length = len(line)
                if prev_length and prev_length != length:
                    raise ValueError, "Found lines with different size: {0} and {1}".format(
                            prev_length, length)
                prev_length = length
                self.lines.append(line[:-1])
            
            if self.width() > PixelChar.MAX_WIDTH:
                raise ValueError, "One of its lines exceeded the max length '{0}': '{1}'".format(
                        PixelChar.MAX_WIDTH, self.width())
            if self.height() > PixelChar.MAX_HEIGHT:
                raise ValueError, "Exceeded the max height of the char represantation '{0}': '{1}'".format(
                        PixelChar.MAX_HEIGHT, self.height())
        except (OSError, IOError, ValueError), e:
            error = u"Failed to load from '{0}': {1}".format(os.path.basename(fname), unicode(e))
        finally:
            if fh is not None:
                fh.close()
            if error is not None:
                raise PixelCharException, error
    
    
    def width(self):
        """ all lines should have the same size, so we can use any of them to get the char's width
        """
        return len(self.lines[0])
    
    
    def height(self):
        return len(self.lines)
    
    
    def __getitem__(self, i):
        return self.lines[i]
    
    
    def setSpaced(self):
        self.lines = []
        for y in range(PixelChar.MAX_HEIGHT):
            self.lines.append("".join(" " for i in range(PixelChar.MAX_WIDTH)))
