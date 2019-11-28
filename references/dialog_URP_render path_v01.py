import c4d
from c4d import gui

IDC_LABELNAME     = 10000
IDC_LIST          = 10002
IDC_USERINPUT_00  = 10003
IDC_USERINPUT_01  = 10004
IDC_USERINPUT_02  = 10005
IDC_POINTS        = 10007
IDC_POINTSOP01    = 10008
IDC_POINTSOP02    = 10009

class OptionsDialog(gui.GeDialog):
    def CreateLayout(self):
        # title
        self.SetTitle('Update Render Path')

        # statics text - description UI
        self.AddStaticText(IDC_LABELNAME, c4d.BFH_LEFT, name = 'Select render path type:') 

        # combo box UI - render type
        self.AddComboBox(IDC_POINTS, c4d.BFH_CENTER, initw = 100, inith = 10, specialalign = True)
        self.AddChild(IDC_POINTS, IDC_POINTSOP01, "Still")
        self.AddChild(IDC_POINTS, IDC_POINTSOP02, "Animation")

        # combo box UI - path type
        self.AddComboBox(IDC_LIST, c4d.BFH_CENTER, initw = 100, inith = 10, specialalign = True)
        self.AddChild(IDC_LIST, IDC_USERINPUT_00, "Drive Path")
        self.AddChild(IDC_LIST, IDC_USERINPUT_01, "Project Path")
        self.AddChild(IDC_LIST, IDC_USERINPUT_02, "Team Server Path")

        # Ok/Cancel buttons
        self.AddDlgGroup(c4d.DLG_OK|c4d.DLG_CANCEL)
        self.ok = False

        # set dialog default values
        self.SetInt32(IDC_LIST , IDC_USERINPUT_00)
        self.SetInt32(IDC_POINTS, IDC_POINTSOP01)

        return True

    def Command(self, id, msg):
        if id == c4d.IDC_OK:
            self.ok = True
            self.findCName = self.GetInt32(IDC_LIST)
            self.Close()

        elif id == c4d.IDC_CANCEL:
            self.Close()
            

        return True

def main():
    # Open the options dialog to let users choose their options.
    dlg = OptionsDialog()
    dlg.Open(c4d.DLG_TYPE_MODAL, defaultw = 300, defaulth = 50)
    if not dlg.ok:
        return

    '''dialog = dlg.findCName
    pdialog = dlg.findPName

    if pdialog == IDC_POINTSOP01:
        pdialog = True
    else:
        pdialog = False

    print dialog
    print pdialog '''

if __name__=='__main__':
 main()