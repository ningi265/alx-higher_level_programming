#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    
    Parameters:
        obj (object): The object whose attributes and methods are to be retrieved.
    
    Returns:
        list: A list containing the names of attributes and methods.
    """
    return dir(obj)
