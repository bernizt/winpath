#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gets the corresponding Bash Ubuntu path of a windows file/folder.

This script has been written for "Bash on Ubuntu on Windows".
"""

__author__ = "Bernat Zaragoza Travieso"
__license__ = "MIT"
__version__ = "0.1"

def get_linuxpath(winpath):
    """Transforms a windows path into its equivalent Bash Ubuntu path.
    
    Args:
        winpath: The file/folder path, as obtained when it is dragged and
            dropped into a Windows command line or bash Ubuntu window.
            
    Returns:
        The mounted path of the file/folder in the Ubuntu file system.
    """
    if "\\" in winpath:
        return ''.join(['/mnt/', winpath[0].lower(),
                         winpath.replace('\\', '/')[2:]])
    else:
        raise ValueError("'\\' not found in '{}'.\nMake sure to double-quote "\
                         "the provided path or the backslashes"\
                         " will be omitted".format(winpath))