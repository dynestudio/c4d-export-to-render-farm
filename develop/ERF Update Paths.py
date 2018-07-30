"""
Export to Render Farm Update Paths - C4D script 0.1 wip 03
Thanks for download - for commercial and personal uses.
Export to Render Farm granted shall not be copied, distributed, or-sold, offered for resale, transferred in whole or in part except that you may make one copy for archive purposes only.

http://dyne.studio/
Writen by: Carlos Dordelly
Special thanks: Pancho Contreras, Terry Williams & Roberto Gonzalez.

Export to Render Farm provides a alternative way to collect a c4d file with additional features.
Date start: 13/feb/2018
Date version: 08/apr/2018
Date end: --
Written and tested in Cinema 4D R19 / R18 / R17 / R16.

Export to Render Farm belongs to Dyne Tools (group of digital tools from dyne).

"""

import c4d
from c4d import gui

#global render engines ids
ARNOLD_RENDERER    = 1029988
OCTANE_RENDERER    = 1029525
REDSHIFT_RENDERER  = 1036219
PRO_RENDERER       = 1037639
PHYSICAL_RENDERER  = 1023342
STANDARD_RENDERER  = 0

#render data global ids
renderdata   = doc.GetActiveRenderData()
rdata        = renderdata.GetData()
Beauty_path  = "./$prj/$prj_Beauty"
MP_path      = "./$prj/$prj_MP"

#document global ids
doc=c4d.documents.GetActiveDocument()
docname=doc.GetDocumentName()
docpath=doc.GetDocumentPath()

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

def main(): #export_to_renderfarm update paths main function
    render_engine = active_render_engine_string()
    print render_engine + " detected" #render engine from the scene
    render_engine = rdata[c4d.RDATA_RENDERENGINE]

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