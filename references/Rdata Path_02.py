import c4d
from c4d import gui


def Export_to_RenderFarm():
    doc=c4d.documents.GetActiveDocument()
    docname=doc.GetDocumentName()
    
    rDat=doc.GetActiveRenderData()
    rDat[c4d.ID_BASELIST_NAME]= "_"+docname+"_To Render Farm"
    BeautyFormat = 1035823 #ArnoldDummy Format
    MPFormat=1016606 #EXR format
    rDat[c4d.RDATA_FORMAT] = BeautyFormat
    rDat[c4d.RDATA_MULTIPASS_SAVEFORMAT] = MPFormat
    rDat[c4d.RDATA_PATH] = "./$prj/$prj_Beauty" #Beauty export is not necessary with c4dtoa
    rDat[c4d.RDATA_MULTIPASS_FILENAME] = "./$prj/$prj_MP" #MP = Multipass

    c4d.EventAdd()


if __name__=='__main__':
    Export_to_RenderFarm()