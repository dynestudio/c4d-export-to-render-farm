import c4d


def export_to_renderfarm():


    doc=c4d.documents.GetActiveDocument()
    docname=doc.GetDocumentName()

    rd=doc.GetActiveRenderData()
    container = rd.GetData()

    rd[c4d.ID_BASELIST_NAME]= "_"+docname+"_To Render Farm"
    rd.SetData(container)
    rd[c4d.RDATA_PATH] = "./$prj/$prj_Beauty" #Beauty export is not necessary with some 3rd party renders just like C4DtoA
    rd[c4d.RDATA_MULTIPASS_FILENAME] = "./$prj/$prj_MP" #MP = Multipass
    


    c4d.EventAdd()

if __name__=='__main__':    
    export_to_renderfarm()