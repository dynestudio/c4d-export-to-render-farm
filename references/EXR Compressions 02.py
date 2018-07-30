import c4d

def main():
        doc=c4d.documents.GetActiveDocument()
        docname=doc.GetDocumentName()

        rd=doc.GetActiveRenderData()
        container = rd.GetData()
        
        rd[c4d.ID_BASELIST_NAME]= "_"+docname+"_To Render Farm"
        
        #formats
        if rd[c4d.RDATA_RENDERENGINE] == 1029988:
            BeautyFormat = 1035823 #ArnoldDummy Format
        if not  rd[c4d.RDATA_RENDERENGINE] == 1029988:
            BeautyFormat = c4d.FILTER_JPG
        MPFormat=c4d.FILTER_EXR
        
        container[c4d.RDATA_FORMAT] = BeautyFormat
        container[c4d.RDATA_ALPHACHANNEL]=False
        
        container[c4d.RDATA_MULTIPASS_SAVEFORMAT] = MPFormat
        saveOptions = container.GetContainerInstance(c4d.RDATA_MULTIPASS_SAVEOPTIONS)
        # OpenEXR options
        bc = c4d.BaseContainer()
        bc[0] = 3 # ZIP
        bc[1] = True # clamp to half float
        
        # save OpenEXR options
        saveOptions.SetContainer(0,bc)
        
        rd[c4d.RDATA_PATH] = "./$prj/$prj_Beauty" #Beauty export is not necessary with some 3rd party renders
        rd[c4d.RDATA_MULTIPASS_FILENAME] = "./$prj/$prj_MP" #MP = Multipass
        
        rd.SetData(container)
        c4d.EventAdd()

if __name__=='__main__':
    main()
