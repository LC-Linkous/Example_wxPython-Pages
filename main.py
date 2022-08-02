##------------------\
#   MultiPageExample
#   'main.py'
#   Main class for project
#   Author(s): Lauren Linkous
#   August 1, 2022
##------------------/

from GFrame import GFrame
import wx #pip install wxpython
import wx.lib.newevent
import wx.lib.mixins.inspection as wit

def main():

    app = wit.InspectableApp()
    GUIFrame = GFrame(None, title='MultiPage GUI Example')
    GUIFrame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
