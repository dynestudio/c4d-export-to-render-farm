import c4d
from c4d import gui

# update render path dialog
class OptionsDialog(gui.GeDialog):
    IDC_GROUP_01         = 10000
    IDC_LABELNAME_01     = 10010
    IDC_LABELNAME_02     = 10020
    IDC_LIST_01          = 10030
    IDC_LIST_01_INPUT01  = 10040
    IDC_LIST_01_INPUT02  = 10050
    IDC_LIST_02          = 10060
    IDC_LIST_02_INPUT01  = 10070
    IDC_LIST_02_INPUT02  = 10080
    IDC_LIST_02_INPUT03  = 10090
    STR_RENDER_TYPE01    = "Still"
    STR_RENDER_TYPE02    = "Animation"
    STR_PATH_TYPE01      = "Drive Path"
    STR_PATH_TYPE02      = "Relative Project Path"
    STR_PATH_TYPE03      = "Team Server Path"

    def CreateLayout(self):
        # title
        self.SetTitle('Update Render Path')

        # group colums
        self.GroupBegin(self.IDC_GROUP_01, c4d.BFH_CENTER, 2, 2, "Main Group", 0, 100, 10)

        # statics text - description UI
        self.AddStaticText(self.IDC_LABELNAME_01, c4d.BFH_LEFT, name = 'Select render type . . . .') 
        # combo box UI - render type
        self.AddComboBox(self.IDC_LIST_01, c4d.BFH_CENTER, initw = 200, inith = 12, specialalign = False)
        self.AddChild(self.IDC_LIST_01, self.IDC_LIST_01_INPUT01, self.STR_RENDER_TYPE01)
        self.AddChild(self.IDC_LIST_01, self.IDC_LIST_01_INPUT02, self.STR_RENDER_TYPE02)
        
        # statics text - description UI
        self.AddStaticText(self.IDC_LABELNAME_02, c4d.BFH_LEFT, name = 'Select path type . . . . . .') 
        # combo box UI - path type
        self.AddComboBox(self.IDC_LIST_02, c4d.BFH_CENTER, initw = 200, inith = 11, specialalign = False)
        self.AddChild(self.IDC_LIST_02, self.IDC_LIST_02_INPUT01, self.STR_PATH_TYPE01)
        self.AddChild(self.IDC_LIST_02, self.IDC_LIST_02_INPUT02, self.STR_PATH_TYPE02)
        self.AddChild(self.IDC_LIST_02, self.IDC_LIST_02_INPUT03, self.STR_PATH_TYPE03)
        
        # close group
        self.GroupEnd()

        # Ok/Cancel buttons
        self.AddDlgGroup(c4d.DLG_OK|c4d.DLG_CANCEL)
        self.ok = False

        # set dialog default values
        self.SetInt32(self.IDC_LIST_01 , self.IDC_LIST_01_INPUT01)
        self.SetInt32(self.IDC_LIST_02 , self.IDC_LIST_02_INPUT01)

        return True

    def Command(self, id, msg):
        if id == c4d.IDC_OK:
            self.ok = True
            self.FIND_RENDER_TYPE = self.GetInt32(self.IDC_LIST_01)
            self.FIND_RENDER_PATH = self.GetInt32(self.IDC_LIST_02)
            self.Close()
        elif id == c4d.IDC_CANCEL:
            self.Close()      

        return True

def main():
    # open the options dialog to let users choose their options.
    dlg = OptionsDialog()
    dlg.Open(c4d.DLG_TYPE_MODAL, defaultw = 300, defaulth = 50)
    if not dlg.ok:
        return

    dlg_render_type = dlg.FIND_RENDER_TYPE
    dlg_render_path = dlg.FIND_RENDER_PATH

    # ------------------------------------

    print dlg_render_type
    print dlg_render_path
    print dlg.IDC_LIST_01_INPUT02

if __name__=='__main__':
 main()