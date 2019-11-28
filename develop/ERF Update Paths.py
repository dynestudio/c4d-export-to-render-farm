"""
Export to Render Farm Update Paths - C4D script
Thanks for download - for commercial and personal uses.
Export to Render Farm granted shall not be copied, distributed, or-sold, offered for resale, transferred in whole or in part except that you may make one copy for archive purposes only.

http://dyne.studio/

Export to Render Farm provides a alternative way to collect a c4d file with additional features.
Written and tested in Cinema 4D R21 / R20 / R19 - Maybe work in other versions.

Export to Render Farm belongs to Dyne Tools (group of digital tools from dyne).

"""

import c4d
from c4d import gui

# global render engines ids
ARNOLD_RENDERER    = 1029988
ARNOLD_DRIVER      = 1030141
OCTANE_RENDERER    = 1029525
REDSHIFT_RENDERER  = 1036219
PRO_RENDERER       = 1037639
PHYSICAL_RENDERER  = 1023342
STANDARD_RENDERER  = 0

# driver types
C4DAIN_DRIVER_EXR      = 9504161
C4DAIN_DRIVER_DEEPEXR  = 1058716317
C4DAIN_DRIVER_JPEG     = 313466666
C4DAIN_DRIVER_PNG      = 9492523
C4DAIN_DRIVER_TIFF     = 313114887
C4DAIN_DRIVER_DISPLAY  = 1927516736

# drivers file names
C4DAIP_DRIVER_EXR_FILENAME      = 1285755954
C4DAIP_DRIVER_JPEG_FILENAME     = 766183461
C4DAIP_DRIVER_DEEPEXR_FILENAME  = 1429220916
C4DAIP_DRIVER_PNG_FILENAME      = 1807654404
C4DAIP_DRIVER_TIFF_FILENAME     = 1913388456

# render data global ids
renderdata   = doc.GetActiveRenderData()
rdata        = renderdata.GetData()
render_beauty_path  = ".\\$prj\\$prj_proxy"
render_mp_path      = ".\\$prj\\$prj_mp"  
team_server_path    = ".\\users\\admin\\$prj\\results\\$prj_"

# document global ids
doc      = c4d.documents.GetActiveDocument()
docname  = doc.GetDocumentName()
docpath  = doc.GetDocumentPath()

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

# set still of animation folder path
def path_type(folder_render_type, file_type):
    # define render folder type
    if folder_render_type:
        folder_render_type = "\\01_Styleframes"
    else:
        folder_render_type = "\\02_Animation"

    # clear c4d folder path
    docpath_list = docpath.split("\\")
    docpath_main = docpath_list[:-3]

    # set new path
    path = ""
    path_drive_render = "07_Render\\01_Render_3D"

    for i in docpath_main:
        path = path + i + "\\"

    path = path + path_drive_render + folder_render_type + file_type[1:]
    return path

# get all objects with children
def get_all_objects(op, filter, output):
    while op:
        if filter(op):
            output.append(op)
        get_all_objects(op.GetDown(), filter, output)
        op = op.GetNext()
    return output

# octane renderer set path
def GetOctaneRenderSettings():
    # find the active Octane render settings
    videopost = renderdata.GetFirstVideoPost()
    while videopost:
        if videopost.GetType() == OCTANE_RENDERER:
            return videopost;
        videopost = videopost.GetNext()
             
    return None

def Octane_Safety_Checks(docpath,docname):
    # find the Octane video post data   
    octaneRenderSettings = GetOctaneRenderSettings()
    if octaneRenderSettings is None:
        raise BaseException("Failed to find Octane render settings")
     
    # setup mp path
    docname = docname.replace(" ","_")
    octane_mp_path = docpath + "/" + docname[:-4] + mp_path[-8:]
    octaneRenderSettings[c4d.SET_PASSES_SAVEPATH] = octane_mp_path

def active_render_engine_string():
    render_engine = rdata[c4d.RDATA_RENDERENGINE]
    if render_engine == ARNOLD_RENDERER:
        render_engine = "Arnold Renderer"
    elif render_engine == REDSHIFT_RENDERER:    
        render_engine = "Redshift Renderer"
    elif render_engine == OCTANE_RENDERER:
        render_engine = "Octane Renderer"
    elif render_engine == PHYSICAL_RENDERER:
        render_engine = "Physical Renderer"
    elif render_engine == STANDARD_RENDERER:
        render_engine = "Standard Renderer"
    else:
        render_engine = "Unrecognizable Render Engine: " + str(rdata[c4d.RDATA_RENDERENGINE])

    return render_engine

def get_frames():
    #Get Frames info
    if rdata[c4d.RDATA_FRAMESEQUENCE] == c4d.RDATA_FRAMESEQUENCE_ALLFRAMES:
        framefrom = doc[c4d.DOCUMENT_MINTIME].GetFrame(doc.GetFps())
        frameto = doc[c4d.DOCUMENT_MAXTIME].GetFrame(doc.GetFps())
    elif rdata[c4d.RDATA_FRAMESEQUENCE] == c4d.RDATA_FRAMESEQUENCE_CURRENTFRAME:
        framefrom = doc[c4d.DOCUMENT_TIME].GetFrame(doc.GetFps())
        frameto = framefrom
    elif rdata[c4d.RDATA_FRAMESEQUENCE] == c4d.RDATA_FRAMESEQUENCE_PREVIEWRANGE:
        framefrom = doc[c4d.DOCUMENT_LOOPMINTIME].GetFrame(doc.GetFps())
        frameto = doc[c4d.DOCUMENT_LOOPMAXTIME].GetFrame(doc.GetFps())
    else:
        framefrom = rdata[c4d.RDATA_FRAMEFROM].GetFrame(doc.GetFps())
        frameto = rdata[c4d.RDATA_FRAMETO].GetFrame(doc.GetFps())

    frames_log = str(framefrom) + "-" + str(frameto)
    
    return [frames_log, frameto]

def main(): # export_to_renderfarm update paths main function
    render_engine = active_render_engine_string()
    print render_engine + " detected" # render engine from the scene
    render_engine = rdata[c4d.RDATA_RENDERENGINE]

    # render path ops
    # open the options dialog to let users choose their options.
    dlg = OptionsDialog()
    dlg.Open(c4d.DLG_TYPE_MODAL, defaultw = 300, defaulth = 50)
    if not dlg.ok:
        return
    # get dialog user inputs
    dlg_render_type = dlg.FIND_RENDER_TYPE
    dlg_render_path = dlg.FIND_RENDER_PATH

    # ------------------------------------
    # main output paths
    beauty_path = render_beauty_path
    mp_path     = render_mp_path

    if dlg_render_path == dlg.IDC_LIST_02_INPUT01:  # drive path
        # get folder type data
        if dlg_render_type == dlg.IDC_LIST_01_INPUT01:
            folder_render_still = True
        else: 
            folder_render_still = False
        # define new output paths
        beauty_path = path_type(folder_render_still, beauty_path)
        mp_path     = path_type(folder_render_still, mp_path)

    elif dlg_render_path == dlg.IDC_LIST_02_INPUT03:  # team server path
        beauty_path = team_server_path + "proxy_"
        mp_path     = team_server_path + "mp_"

    else:
        None

    # ------------------------------------

    if render_engine == ARNOLD_RENDERER:
        padding = get_frames()
        padding = padding[1]
        print padding
        padding = len(str(padding))

        #padding ops
        if padding == 1:
            padding = 0
        elif padding == 2:
            padding = 3
        else:
            padding = padding
        #padding underscore
        if padding == 0:
            padding_space = ""
        else:
            padding_space = "_"

        padding = "#"*padding

        #drivers list
        driversList = get_all_objects(doc.GetFirstObject(), lambda x: x.CheckType(ARNOLD_DRIVER), [])
        for driver in driversList:
            driver_name = driver[c4d.ID_BASELIST_NAME]
            driver_type = driver[c4d.C4DAI_DRIVER_TYPE]

            if driver_type == C4DAIN_DRIVER_EXR:
                driver_filename = C4DAIP_DRIVER_EXR_FILENAME
            elif driver_type == C4DAIN_DRIVER_DEEPEXR:
                driver_filename = C4DAIP_DRIVER_DEEPEXR_FILENAME
            elif driver_type == C4DAIN_DRIVER_TIFF:
                driver_filename = C4DAIP_DRIVER_TIFF_FILENAME
            elif driver_type == C4DAIN_DRIVER_PNG:
                driver_filename = C4DAIP_DRIVER_PNG_FILENAME
            elif driver_type == C4DAIN_DRIVER_JPEG:
                driver_filename = C4DAIP_DRIVER_JPEG_FILENAME
            else:
                driver_filename = 0

            if driver_type == C4DAIN_DRIVER_EXR:
                driver_format = ".exr"
            elif driver_type == C4DAIN_DRIVER_DEEPEXR:
                driver_format = ".exr"
            elif driver_type == C4DAIN_DRIVER_TIFF:
                driver_format = ".tiff"
            elif driver_type == C4DAIN_DRIVER_PNG:
                driver_format = ".png"
            elif driver_type == C4DAIN_DRIVER_JPEG:
                driver_format = ".jpg"
            else:
                driver_format = ""

            path_id = c4d.DescID(c4d.DescLevel(driver_filename), c4d.DescLevel(1))
            driver_name = driver_name.replace(" ","_")
            # team server path ops
            if dlg_render_path == dlg.IDC_LIST_02_INPUT03:
                arnold_path = team_server_path
            else:
                arnold_path = "./$prj/$prj_"
            # set drivers paths
            driver_custom_path = arnold_path + driver_name + padding_space + padding + driver_format
              
            if not driver_type == C4DAIN_DRIVER_DISPLAY:
                driver.SetParameter(path_id, driver_custom_path, c4d.DESCFLAGS_SET_0)
            else:
                None

    renderdata[c4d.RDATA_PATH] = beauty_path # beauty export is not necessary with C4DtoA and Redshift

    if render_engine == OCTANE_RENDERER:
        renderdata[c4d.RDATA_MULTIPASS_FILENAME] = ""
        Octane_Safety_Checks(docpath,docname)
    else:
        renderdata[c4d.RDATA_MULTIPASS_FILENAME] = mp_path #MP = Multipass  

    # ------------------------------------

    # update the scene
    c4d.EventAdd()

    gui.MessageDialog("The render paths was successfully updated!\nSee the console and log for more details.")


if __name__=='__main__':
    main()