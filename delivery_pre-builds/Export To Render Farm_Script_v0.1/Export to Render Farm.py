"""
Export to Render Farm_v04
Thanks for purchasing - for commercial and all uses.

be.net/dyne
Writen by: Carlos Dordelly

Colleect your files and set more easily your render paths
Date: 03/06/2017
Written and tested in Cinema 4D R18 / R17 / R16 - Maybe works in older versions.

"""

import c4d
from c4d import gui

#Global IDs
ARNOLD_RENDERER = 1029988
ARNOLD_RENDERER_COMMAND = 1039333
ARNOLD_DUMMYFORMAT = 1035823
rdata = doc.GetActiveRenderData()
doc=c4d.documents.GetActiveDocument()
docname=doc.GetDocumentName()
docpath=doc.GetDocumentPath()


def GetArnoldRenderSettings():

    # find the active Arnold render settings
    videopost = rdata.GetFirstVideoPost()
    while videopost:
        if videopost.GetType() == ARNOLD_RENDERER:
            return videopost;
        videopost = videopost.GetNext()
     
    # create a new one when does not exist
    if videopost is None:
        c4d.CallCommand(ARNOLD_RENDERER_COMMAND)
         
        videopost = rdata.GetFirstVideoPost()
        while videopost:
            if videopost.GetType() == ARNOLD_RENDERER:
                return videopost;
            videopost = videopost.GetNext()
             
    return None

"""
def get_frames():

    #Active Document
    doc = c4d.documents.GetActiveDocument()
    # Render Data
    renderdata = doc.GetActiveRenderData()
    rdata = renderdata.GetData()
    
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
    
    #print frames sequence
    print "frame from: "+str(framefrom)
    print "frame to: "+str(frameto)
"""

def export_to_renderfarm():

    #Collect start
    save=c4d.CallCommand(12098) # Save

    #function variables
    container = rdata.GetData()

    #Render setting collect name
    rdata[c4d.ID_BASELIST_NAME]= "_"+docname+"_To Render Farm"

    #Output Formats
    if rdata[c4d.RDATA_RENDERENGINE] == ARNOLD_RENDERER:
        BeautyFormat = ARNOLD_DUMMYFORMAT #ArnoldDummy Format
    if not  rdata[c4d.RDATA_RENDERENGINE] == ARNOLD_RENDERER:
        BeautyFormat = c4d.FILTER_JPG #Beauty reference in JPG format
    MPFormat=c4d.FILTER_EXR
    
    container[c4d.RDATA_FORMAT] = BeautyFormat
    container[c4d.RDATA_ALPHACHANNEL]=False
    
    container[c4d.RDATA_MULTIPASS_SAVEFORMAT] = MPFormat
    saveOptions = container.GetContainerInstance(c4d.RDATA_MULTIPASS_SAVEOPTIONS)

    # OpenEXR Compression options
    bc = c4d.BaseContainer()
    bc[0] = 3 # ZIP
    bc[1] = True # clamp to half float
    
    # save OpenEXR options & continer data
    saveOptions.SetContainer(0,bc)
    rdata.SetData(container)

    #set render paths
    rdata[c4d.RDATA_PATH] = "./$prj/$prj_Beauty" #Beauty export is not necessary with some 3rd party renders just like C4DtoA
    rdata[c4d.RDATA_MULTIPASS_FILENAME] = "./$prj/$prj_MP" #MP = Multipass
    
    #Arnold Render Settings Safety check
    if rdata[c4d.RDATA_RENDERENGINE] == ARNOLD_RENDERER:
        #C4DtoA Lines
        # find the Arnold video post data   
        arnoldRenderSettings = GetArnoldRenderSettings()
        if arnoldRenderSettings is None:
            raise BaseException("Failed to find Arnold render settings")
         
        # setup the settings
        arnoldRenderSettings[c4d.C4DAI_OPTIONS_LOCK_SAMPLING_PATTERN] = True
        arnoldRenderSettings[c4d.C4DAI_OPTIONS_USE_TX_TEXTURES] = True
        arnoldRenderSettings[c4d.C4DAI_OPTIONS_DISPLAY_BUCKETS]=0
    if not  rdata[c4d.RDATA_RENDERENGINE] == ARNOLD_RENDERER:
        None

    #Update te scene
    c4d.EventAdd()

    #Collect New File
    c4d.CallCommand(12255, 12255) # Save Project with Assets...
    
    #Write codument with frames and path settings
    #print docname
    #print docpath

    #Close the collected file
    c4d.CallCommand(12664, 12664) # Close collected project
    c4d.CallCommand(52000, 2) # Recent Files
    
    #Collect finish dialog
    gui.MessageDialog('Sucessfully Exported')


if __name__=='__main__':
    export_to_renderfarm()