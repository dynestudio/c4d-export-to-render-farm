"""
Export to Render Farm Update Team Server Paths - C4D script 0.1
Thanks for download - for commercial and personal uses.
Export to Render Farm granted shall not be copied, distributed, or-sold, offered for resale, transferred in whole or in part except that you may make one copy for archive purposes only.

http://dyne.studio/
Writen by: Carlos Dordelly
Special thanks: Pancho Contreras, Terry Williams & Roberto Gonzalez.

Export to Render Farm provides a alternative way to collect a c4d file with additional features.
Date start: 13/feb/2018
Date version: 09/jun/2018
Date end: --
Written and tested in Cinema 4D R19 / R18 / R17 / R16.

Export to Render Farm belongs to Dyne Tools (group of digital tools from dyne).

"""

import c4d
from c4d import gui

#global render engines ids
ARNOLD_RENDERER    = 1029988
ARNOLD_DRIVER      = 1030141
OCTANE_RENDERER    = 1029525
REDSHIFT_RENDERER  = 1036219
PRO_RENDERER       = 1037639
PHYSICAL_RENDERER  = 1023342
STANDARD_RENDERER  = 0

#driver types
C4DAIN_DRIVER_EXR      = 9504161
C4DAIN_DRIVER_DEEPEXR  = 1058716317
C4DAIN_DRIVER_JPEG     = 313466666
C4DAIN_DRIVER_PNG      = 9492523
C4DAIN_DRIVER_TIFF     = 313114887
C4DAIN_DRIVER_DISPLAY  = 1927516736

#drivers file names
C4DAIP_DRIVER_EXR_FILENAME      = 1285755954
C4DAIP_DRIVER_JPEG_FILENAME     = 766183461
C4DAIP_DRIVER_DEEPEXR_FILENAME  = 1429220916
C4DAIP_DRIVER_PNG_FILENAME      = 1807654404
C4DAIP_DRIVER_TIFF_FILENAME     = 1913388456

#render data global ids
renderdata   = doc.GetActiveRenderData()
rdata        = renderdata.GetData()
Beauty_path  = "./$prj/$prj_Beauty"
MP_path      = "./users/admin/$prj/results/$prj_MP"

#document global ids
doc=c4d.documents.GetActiveDocument()
docname=doc.GetDocumentName()
docpath=doc.GetDocumentPath()

#get all objects with children
def get_all_objects(op, filter, output):
    while op:
        if filter(op):
            output.append(op)
        get_all_objects(op.GetDown(), filter, output)
        op = op.GetNext()
    return output

#octane renderer set path
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
    octane_mp_path = docpath + "/" + docname[:-4] + MP_path[-8:]
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

def main(): #export_to_renderfarm update paths main function
    render_engine = active_render_engine_string()
    print render_engine + " detected" #render engine from the scene
    render_engine = rdata[c4d.RDATA_RENDERENGINE]

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
            driver_custom_path = "./$prj/$prj_" + driver_name + padding_space + padding + driver_format
              
            if not driver_type == C4DAIN_DRIVER_DISPLAY:
                driver.SetParameter(path_id, driver_custom_path, c4d.DESCFLAGS_SET_0)
            else:
                None

    renderdata[c4d.RDATA_PATH] = Beauty_path #beauty export is not necessary with C4DtoA and Redshift

    if render_engine == OCTANE_RENDERER:
        renderdata[c4d.RDATA_MULTIPASS_FILENAME] = ""
        Octane_Safety_Checks(docpath,docname)
    else:
        renderdata[c4d.RDATA_MULTIPASS_FILENAME] = MP_path #MP = Multipass  

    #Update the scene
    c4d.EventAdd()

    gui.MessageDialog("The render paths was successfully updated!\nSee the console and log for more details.")


if __name__=='__main__':
    main()