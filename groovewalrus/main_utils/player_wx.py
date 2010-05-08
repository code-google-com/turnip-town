# -*- coding: utf-8 -*-
"""
GrooveWalrus: wx media player
Copyright (C) 2010
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

import wx
import wx.media

########################################################################
class Player(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
       
        self.parent = parent
        #self.mediaPlayer = self.parent.mediaPlayer
        self.mediaPlayer = wx.media.MediaCtrl(self.parent, style=wx.SIMPLE_BORDER, szBackend=wx.media.MEDIABACKEND_WMP10)
        self.parent.Bind(wx.media.EVT_MEDIA_LOADED, self.PlayWxMedia)
        
        self.paused = False
        
    #----------------------------------------------------------------------
                  
    def PlayWxMedia(self, event):
        print 'foon'
        self.mediaPlayer.Play()
        
    def play(self, file_name):
        print file_name
        self.mediaPlayer.Load(file_name)
        
    def stop_play(self):
        self.mediaPlayer.Stop()
                
    def toggle_pause(self):
        if self.paused == False:
            self.mediaPlayer.Pause()
            self.paused = True
        else:
            self.mediaPlayer.Play()
            self.paused = False

        
