# -*- coding: utf-8 -*-
"""
GrooveWalrus: song
Copyright (C) 2011
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

#song object

########################################################################
class Song:
    """It's a song"""
    #----------------------------------------------------------------------
    def __init__(self, playlist_name=None):
        self.artist = ''
        self.title = ''
        self.album = ''
        self.next_song = None
        self.previous_song = None        
        self.track_time = 0
        self.location = ''
        self.time_played = 0
        self.song_id = 0
        self.rating = None
        
    #----------------------------------------------------------------------
        
    def SetSongTitle(self, song_title):
        #title
        self.title = song_title
        
    def GetSongTime(self, file_location):
        stime = 240
        #if os.path.isfile(file_location):
            #stime = local_songs.GetMp3Length(location)
        return stime
    
    def SetNextsong(self, song):
        self.next_song = song

if __name__ == "__main__":       
    x = Song()
    x.title = 'Some Title'
