"""
GrooveWalrus: File Cache
Copyright (C) 2009, 2010
11y3y3y3y43@gmail.com
http://groove-walrus.turnip-town.net
-----
This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc., 59 Temple
Place, Suite 330, Boston, MA 02111-1307 USA
"""


import hashlib
import os

# max number of cached files
CACHE_LIMIT = 30
ENCODING = 'utf-8'

def CreateCachedFilename(cache_path, file_string):
    """ Checks if file exists, returns new file name if it doesn't. """
    
    # lets make file names as hex strings for something to do
    
    charset = 'utf-8'
    ufile_string = file_string.encode(charset)
    
    hex_file_name = hashlib.md5(ufile_string).hexdigest()
    full_file_path = cache_path.replace("\\", os.sep) + os.sep + hex_file_name + '.mp3'
    if os.path.isfile(full_file_path):
        return (full_file_path, True)
    else:
        return (full_file_path, False)

def CheckCache(cache_path):
    """ Checks if cache limit has been reached, removes oldest if it has. """
    
    file_path = cache_path.replace("\\", os.sep)
    file_list = os.listdir(file_path)
    
    while len(file_list) > CACHE_LIMIT:
    # keep removing files until we're down to the cache limit
        oldest_file = ''
        first_modified = 2000000000
        
        for file_name in file_list:
        # find oldest file
            full_file_path = file_path + os.sep + file_name
            # use created time, modifed time is not what we want            
            modified = os.path.getctime(full_file_path)
            if modified < first_modified:
                    first_modified = modified
                    oldest_file = full_file_path
        
        # remove oldest file
        os.remove(oldest_file)
        #print oldest_file
        file_list = os.listdir(file_path)

        
def CreateCachedImage(cache_path, file_string, extension):
    """ Checks if file exists, returns new file name if it doesn't. """
    
    # lets make file names as hex strings for something to do
    
    charset = 'utf-8'
    file_string = file_string.lower()
    ufile_string = file_string.encode(charset)
    
    hex_file_name = hashlib.md5(ufile_string).hexdigest()
    full_file_path = cache_path.replace("\\", os.sep) + hex_file_name + extension
    if os.path.isfile(full_file_path):
        return (hex_file_name + extension, True)
    else:
        return (hex_file_name + extension, False)