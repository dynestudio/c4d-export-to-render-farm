import c4d

def arnold_param():
    doc=c4d.documents.GetActiveDocument()
    rDat=doc.GetActiveRenderData()
    rDat[c4d.RDATA_RENDERENGINE] = 1029988
    print rDat[c4d.RDATA_RENDERENGINE] #C4DtoA ID code
    
    ArnoldRenderer = rDat[c4d.RDATA_RENDERENGINE]
    ArnoldRenderer[c4d.C4DAI_OPTIONS_LOCK_SAMPLING_PATTERN]=True
    c4d.EventAdd()

arnold_param()