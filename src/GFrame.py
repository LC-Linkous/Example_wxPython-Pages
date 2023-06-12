##------------------\
#   MultiPageExample
#   'GFrame.py'
#   Class for GUI layout and functionality
#   Author(s): Lauren Linkous
#   August 1, 2022
##------------------/


import wx #pip install wxpython
import wx.lib.newevent
import wx.lib.mixins.inspection as wit
import os

#default frame/panel sizes
WIDTH = 850
HEIGHT = 700

class GFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent=parent, title=title, size=(WIDTH, HEIGHT))
        #setting up the toolbar + other panel defaults
        self.panel_setup = SetupPage(self)
        self.panel_home = HomePage(self)
        self.panel_help = HelpPage(self)
        self.panel_setup.Hide()
        self.panel_home.Show() #shown by default
        self.panel_help.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_setup, 1, wx.EXPAND)
        self.sizer.Add(self.panel_home, 1, wx.EXPAND)
        self.sizer.Add(self.panel_help, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        menubar = wx.MenuBar()
        self.setupMenu = wx.Menu()
        self.homeMenu = wx.Menu()
        self.helpMenu = wx.Menu()

        menubar.Append(self.setupMenu, '&Settings')
        menubar.Append(self.homeMenu, '&Home')
        menubar.Append(self.helpMenu, '&Help')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU_OPEN, self.onMenuClick)
        self.Bind(wx.EVT_CLOSE, self.onClose)

    def onMenuClick(self, event):
        # not the prettiest, but avoids the dropdown sub-menus
        #alt to toolbar because wx toolbar uses bitmaps instead of text

        if event.GetMenu() == self.setupMenu:
            self.panel_setup.Show()
            self.panel_home.Hide()
            self.panel_help.Hide()
        elif event.GetMenu() == self.homeMenu:
            self.panel_setup.Hide()
            self.panel_home.Show()
            self.panel_help.Hide()
        elif event.GetMenu() == self.helpMenu:
            self.panel_setup.Hide()
            self.panel_home.Hide()
            self.panel_help.Show()
        self.Layout() #may need to refresh on some systems

    def onClose(self, event):
        self.Destroy()


class SetupPage(wx.Panel):
    #page for general run information
    #also for specifying user information and other notes

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        # current program loc as default. def here because used in setup panel
        self.parent = parent
        self.sPanelLeft = SetupSettingsPanel(self)
        self.sPanelRight = SetupSettingsPanel(self)

        # update button
        self.updateBtn = wx.Button(self, wx.ID_ANY, label='UPDATE', name='UPDATE_BUTTON')
        self.updateBtn.Bind(wx.EVT_BUTTON, self.updatePageOnClick)

        #layout using nested spacers
        # the main sizer for the panel
        root_sizer = wx.BoxSizer(wx.VERTICAL) 
        # the horizontal spacer holding the settings panels
        # this example uses two of the same panels to show reusability 
        settings_sizer = wx.BoxSizer(wx.HORIZONTAL)
        settings_sizer.Add(self.sPanelLeft)
        settings_sizer.AddSpacer(10) #10 px spacer
        settings_sizer.Add(self.sPanelRight)

        root_sizer.Add(settings_sizer)
        root_sizer.AddSpacer(10)
        root_sizer.Add(self.updateBtn) 
        self.SetSizer(root_sizer)


    def updatePageOnClick(self, event):
        print ("button clicked")

class HomePage(wx.Panel):
     def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.parent= parent
        self.SetBackgroundColour('PURPLE')

        self.sPanel = HomeSettingsPanel(self)

        root_sizer = wx.BoxSizer(wx.VERTICAL)
        root_sizer.Add(self.sPanel, 3) #, wx.EXPAND)
        self.SetSizer(root_sizer)


class HelpPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        #uses a static position, not a spaccer
        wx.StaticText(self, label="Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ut fringilla est, \n"
                                  "quis tincidunt ex. Duis lorem risus, tincidunt et ante sed, porta sollicitudin \n"
                                  "neque. Nulla faucibus pulvinar justo sit amet varius. Phasellus vel maximus sem. \n"
                                  "Ut porttitor nisi nunc, ac auctor lorem hendrerit eget. Ut dapibus orci vitae nisl \n"
                                  "pretium, in pulvinar metus tincidunt. In rhoncus non leo malesuada lacinia. Proin \n"
                                  "cursus ac elit non laoreet. Nam mauris turpis, condimentum sit amet justo vel, \n"
                                  "sagittis sodales nisl. Sed nec augue eget nisl rhoncus auctor quis efficitur felis.\n"
                                  " Curabitur placerat, dolor id accumsan porttitor, est odio fringilla ligula, ac \n"
                                  "tincidunt diam augue ac nisl. Nullam et hendrerit nulla, a pulvinar nulla. Duis orci \n"
                                  " nulla, hendrerit et porttitor quis, ultrices nec sapien. ", pos=(5, 35))

##### reusable GUI Panel classes #####
class SetupSettingsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent) #, size=(500, 425))
        BOX_WIDTH = 350
        FIELD_WIDTH = 300
        #
        self.parent = parent
        #text example
        self.lblBox = wx.StaticBox(self, wx.ID_ANY, 'Example group box', size=(BOX_WIDTH, 40))
        self.lblTxtbx = wx.TextCtrl(self.lblBox, size=(FIELD_WIDTH, 20), pos=(5, 15))


        # use a box sizer to lay out widgets
        sizer_v_left = wx.BoxSizer(wx.VERTICAL)
        sizer_v_left.Add((0, 10), proportion=0, flag=wx.EXPAND)
        sizer_v_left.Add(self.lblBox, 0, flag=wx.LEFT, border=5)

        sizer_final = wx.BoxSizer(wx.HORIZONTAL)
        sizer_final.Add(sizer_v_left, 0, flag=wx.LEFT, border=5)
        sizer_final.Add((0, 10), proportion=0, flag=wx.EXPAND)

        self.SetSizer(sizer_final)

class HomeSettingsPanel(wx.Panel):
    #parent is HomePage class
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent) #, size=(250, 425))
        self.parent = parent




if __name__ == "__main__":
    ## way #1 to test
    # app = wx.App()
    # frame = GFrame(None, title='MultiPage GUI Example')
    # frame.Show()
    # app.MainLoop()

    ## way #2 to test
    app = wit.InspectableApp()
    GUIFrame = GFrame(None, title='MultiPage GUI Example')
    GUIFrame.Show()
    app.MainLoop()



