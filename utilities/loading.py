"""
Used to load key and a few other things

Functions
----------
key:
setup:

"""

def key(
        loc:str='api.key'
    ):
    """
    Load key from location

    Parameters
    ----------
    loc: file location of key

    Return
    ----------
    Returns key from file
    """
    #TODO make better
    return open(loc, "r").read()

def setup():
    #TODO
    return
    