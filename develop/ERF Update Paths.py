"""
Export to Render Farm Update Paths - C4D script 0.1 wip 01
Thanks for download - for commercial and personal uses.
Export to Render Farm granted shall not be copied, distributed, or-sold, offered for resale, transferred in whole or in part except that you may make one copy for archive purposes only.

http://dyne.studio/
Writen by: Carlos Dordelly
Special thanks: Pancho Contreras, Terry Williams & Roberto Gonzalez.

Export to Render Farm provides a alternative way to collect a c4d file with additional features.
Date start: 16/02/2018
date end: --
Written and tested in Cinema 4D R19 / R18 / R17 / R16.

Export to Render Farm belongs to Dyne Tools (group of digital tools from dyne).

"""

import c4d
from c4d import gui

#global render engines ids
#arnold ids
ARNOLD_RENDERER = 1029988
ARNOLD_RENDERER_COMMAND = 1039333
ARNOLD_DUMMYFORMAT = 1035823
ARNOLD_DRIVER = 1030141

#octane ids
OCTANE_RENDERER = 1029525
OCTANE_LIVEPLUGIN = 1029499

#other render engines ids
REDSHIFT_RENDERER = 1036219
PRO_RENDERER = 1037639
PHYSICAL_RENDERER = 1023342
STANDARD_RENDERER = 0

#render data global ids
renderdata = doc.GetActiveRenderData()
rdata = renderdata.GetData()
Beauty_path = "./$prj/$prj_Beauty"
MP_path = "./$prj/$prj_MP"

#document global ids
doc=c4d.documents.GetActiveDocument()
docname=doc.GetDocumentName()
docpath=doc.GetDocumentPath()
docfolder=docname[:-4]

#cinema 4D version
def get_c4d_ver():
    
    C4D_ver = str(c4d.GetC4DVersion())
    C4D_ver = C4D_ver[:2] + "." + C4D_ver[2:]
    version_to_log = "Cinema 4D R" + C4D_ver
    C4DR_ver = C4D_ver[:2]
    
    ver_list = [version_to_log,C4DR_ver]

    return ver_list

C4D_version = get_c4d_ver()
C4D_version_log = C4D_version[0]
C4DR_ver = C4D_version[1]

# ---start render engines settings--- #

#octane renderer
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
         
        # setup the settings
        octaneRenderSettings[c4d.SET_PASSES_ENABLED] = True
        docname = docname.replace(" ","_")
        octane_mp_path = docpath + "/" + docname[:-4] + MP_path[-8:]
        octaneRenderSettings[c4d.SET_PASSES_SAVEPATH] = octane_mp_path
        Pxr24 = 5 #pixar EXR compression
        octaneRenderSettings[c4d.SET_PASSES_EXR_COMPR] = Pxr24
        octaneRenderSettings[c4d.SET_PASSES_SHOWPASSES] = True
        octaneRenderSettings[c4d.SET_PASSES_SAVE_MAINPASS] = True
        octaneRenderSettings[c4d.SET_PASSES_MULTILAYER] = True
        octaneRenderSettings[c4d.SET_PASSES_IMAGECOLORPROFILE] = 1
        octaneRenderSettings[c4d.SET_PASSES_TONEMAPTYPE] = 1

# ---end render engines settings--- #

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
        render_engine = rdata[c4d.RDATA_RENDERENGINE]

    return render_engine

def export_to_renderfarm():

    container = renderdata.GetData()
    render_engine = active_render_engine_string()
    #render engine from the scene
    print render_engine+" detected"
    render_engine = rdata[c4d.RDATA_RENDERENGINE]

    #Output Render File Formats
    #Beauty
    if render_engine == ARNOLD_RENDERER:
        BeautyFormat = ARNOLD_DUMMYFORMAT
    elif render_engine == REDSHIFT_RENDERER:
        BeautyFormat = ARNOLD_DUMMYFORMAT
    elif render_engine == OCTANE_RENDERER:
        BeautyFormat = c4d.FILTER_PNG
    else:
        BeautyFormat = c4d.FILTER_JPG

    #MultiPass
    MPFormat=c4d.FILTER_EXR
    
    container[c4d.RDATA_FORMAT] = BeautyFormat

    #octane set 16bits beauty
    if render_engine == OCTANE_RENDERER:
        container[c4d.RDATA_FORMATDEPTH] = 1
    else:
        None

    #arnold beauty alpha uncheck
    if render_engine == ARNOLD_RENDERER:
        container[c4d.RDATA_ALPHACHANNEL]=False
    else:
        container[c4d.RDATA_ALPHACHANNEL] = True
    
    container[c4d.RDATA_MULTIPASS_SAVEFORMAT] = MPFormat
    saveOptions = container.GetContainerInstance(c4d.RDATA_MULTIPASS_SAVEOPTIONS)

    # OpenEXR Compression options
    bc = c4d.BaseContainer()
    bc[0] = 3 # ZIP
    bc[1] = True # clamp to half float
    
    # save OpenEXR options & container data
    saveOptions.SetContainer(0,bc)
    renderdata.SetData(container)

    #set render outputs
    renderdata[c4d.RDATA_SAVEIMAGE] = True
    renderdata[c4d.RDATA_MULTIPASS_SAVEIMAGE] = True

    #set render paths
    renderdata[c4d.RDATA_PATH] = Beauty_path #beauty export is not necessary with C4DtoA and Redshift

    if render_engine == OCTANE_RENDERER:
        renderdata[c4d.RDATA_MULTIPASS_FILENAME] = ""
    else:
        renderdata[c4d.RDATA_MULTIPASS_FILENAME] = MP_path #MP = Multipass  

    #octane correct multipass path
    if render_engine == OCTANE_RENDERER:
        doc=c4d.documents.GetActiveDocument()
        docname=doc.GetDocumentName()
        docpath=doc.GetDocumentPath()
        Octane_Safety_Checks(docpath,docname)
    else:
        None

    #Update the scene
    c4d.EventAdd()
        
    #Collect finish dialog
    print "The render paths was successfully updated! Happy Rendering ;)"
    if int(C4DR_ver) == 19:
        gui.MessageDialog("The render paths was successfully updated!\nRemember to change the EXR compression to:\nLossy 16-bit float, Zip, blocks of 16 scan lines in the Render Settings.")
    else:
        gui.MessageDialog("The render paths was successfully updated!\nSee the console and log for more details.")


if __name__=='__main__':
    export_to_renderfarm()