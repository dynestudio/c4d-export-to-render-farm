import c4d
from c4d import gui


def Export_to_RenderFarm():
    save=c4d.CallCommand(12098) # Save
    if c4d.CallCommand(12255, 12255) == None:
        gui.MessageDialog('Export Cancelled')
        return 0 

    if not c4d.CallCommand(12255, 12255) == None:
        doc=c4d.documents.GetActiveDocument()
        docname=doc.GetDocumentName()

        rDat=doc.GetActiveRenderData()
        rDat[c4d.ID_BASELIST_NAME]= "_"+docname+"_To Render Farm"
        if rDat[c4d.RDATA_RENDERENGINE] == 1029988:
            BeautyFormat = 1035823 #ArnoldDummy Format
        if not  rDat[c4d.RDATA_RENDERENGINE] == 1029988:
            BeautyFormat = c4d.FILTER_JPG
        MPFormat==c4d.FILTER_EXR
        
        rDat[c4d.RDATA_FORMAT] = BeautyFormat
        rDat[c4d.RDATA_MULTIPASS_SAVEFORMAT] = MPFormat
        rDat[c4d.RDATA_PATH] = "./$prj/$prj_Beauty" #Beauty export is not necessary with c4dtoa
        rDat[c4d.RDATA_MULTIPASS_FILENAME] = "./$prj/$prj_MP" #MP = Multipass
        
        #ArnoldRenderer = rDat[c4d.RDATA_RENDERENGINE]
        #ArnoldRenderer[c4d.C4DAI_OPTIONS_LOCK_SAMPLING_PATTERN]=True
        #ArnoldRenderer[c4d.C4DAI_OPTIONS_USE_TX_TEXTURES]=True
        
        save=c4d.CallCommand(12098) # Save all changes in source project
        c4d.EventAdd()
        c4d.CallCommand(12255, 12255) # Save Project with Assets...
        c4d.CallCommand(12664, 12664) # Close collected project
        c4d.CallCommand(52000, 2) # Recent Files
        gui.MessageDialog('Sucessfully Exported')

if __name__=='__main__':
    Export_to_RenderFarm()