import c4d
from c4d import gui


def export_to_renderfarm():
    save=c4d.CallCommand(12098) # Save
    if c4d.CallCommand(12255, 12255) == None:
        gui.MessageDialog('Export Cancelled')
        return

    if not c4d.CallCommand(12255, 12255) == None:
        doc=c4d.documents.GetActiveDocument()
        docname=doc.GetDocumentName()

        rd=doc.GetActiveRenderData()
        container = rd.GetData()

        rd[c4d.ID_BASELIST_NAME]= "_"+docname+"_To Render Farm"

        #Output Formats
        if rd[c4d.RDATA_RENDERENGINE] == 1029988:
            BeautyFormat = 1035823 #ArnoldDummy Format
        if not  rd[c4d.RDATA_RENDERENGINE] == 1029988:
            BeautyFormat = c4d.FILTER_JPG
        MPFormat=c4d.FILTER_EXR
        
        container[c4d.RDATA_FORMAT] = BeautyFormat
        container[c4d.RDATA_ALPHACHANNEL]=False
        
        container[c4d.RDATA_MULTIPASS_SAVEFORMAT] = MPFormat
        saveOptions = container.GetContainerInstance(c4d.RDATA_MULTIPASS_SAVEOPTIONS)
        # OpenEXR Compression options
        bc = c4d.BaseContainer()
        bc[0] = 3 # ZIP
        bc[1] = True # clamp to half float
        
        # save OpenEXR options
        saveOptions.SetContainer(0,bc)
        
        rd[c4d.RDATA_PATH] = "./$prj/$prj_Beauty" #Beauty export is not necessary with some 3rd party renders just like C4DtoA
        rd[c4d.RDATA_MULTIPASS_FILENAME] = "./$prj/$prj_MP" #MP = Multipass
        
        #Need C4D 2.0.2          #ArnoldRenderer = rd[c4d.rdA_RENDERENGINE]
        #Need C4D 2.0.2          #ArnoldRenderer[c4d.C4DAI_OPTIONS_LOCK_SAMPLING_PATTERN]=True
        #Need C4D 2.0.2          #ArnoldRenderer[c4d.C4DAI_OPTIONS_USE_TX_TEXTURES]=True
        
        save=c4d.CallCommand(12098) # Save all changes in source project
        rd.SetData(container)
        c4d.EventAdd()
        c4d.CallCommand(12255, 12255) # Save Project with Assets...
        c4d.CallCommand(12664, 12664) # Close collected project
        c4d.CallCommand(52000, 2) # Recent Files
        gui.MessageDialog('Sucessfully Exported')

if __name__=='__main__':
    export_to_renderfarm()