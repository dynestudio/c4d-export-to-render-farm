import c4d
from c4d import gui

#global render engines ids
#arnold ids
ARNOLD_RENDERER                   = 1029988
ARNOLD_RENDERER_COMMAND           = 1039333
ARNOLD_DUMMYFORMAT                = 1035823
ARNOLD_DRIVER                     = 1030141
C4DAIP_DRIVER_EXR_HALF_PRECISION  = 317968755

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

#octane ids
OCTANE_RENDERER    = 1029525
OCTANE_LIVEPLUGIN  = 1029499

#other render engines ids
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
doc        = c4d.documents.GetActiveDocument()
docname    = doc.GetDocumentName()
docpath    = doc.GetDocumentPath()
docfolder  = docname[:-4]

#get all objects with children
def get_all_objects(op, filter, output):
    while op:
        if filter(op):
            output.append(op)
        get_all_objects(op.GetDown(), filter, output)
        op = op.GetNext()
    return output

def Arnold_Safety_Checks():

        # drivers safety checks
        objectsList = get_all_objects(doc.GetFirstObject(), lambda x: x.CheckType(ARNOLD_DRIVER), [])
        for obj in objectsList:
            obj[c4d.C4DAI_DRIVER_ENABLE_AOVS] = True
            obj[c4d.C4DAI_DRIVER_MERGE_AOVS] = True

            driver_name = obj[c4d.ID_BASELIST_NAME]
            driver_type = obj[c4d.C4DAI_DRIVER_TYPE]
            if driver_type == C4DAIN_DRIVER_EXR:
                if not driver_name == "crypto":
                    obj[C4DAIP_DRIVER_EXR_HALF_PRECISION] = True
                else:
                    obj[C4DAIP_DRIVER_EXR_HALF_PRECISION] = False
            else:
                None

        c4d.EventAdd()

Arnold_Safety_Checks()