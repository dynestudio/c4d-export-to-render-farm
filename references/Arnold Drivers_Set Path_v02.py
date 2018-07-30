import c4d

#global render engines ids
#arnold ids
ARNOLD_RENDERER = 1029988
ARNOLD_RENDERER_COMMAND = 1039333
ARNOLD_DUMMYFORMAT = 1035823
ARNOLD_DRIVER = 1030141

# From plugins/C4DtoA/res/description/ainode_driver_exr.h
C4DAIP_DRIVER_EXR_FILENAME  = 1285755954
 
# From plugins/C4DtoA/res/description/arnold_driver.h
C4DAI_DRIVER_TYPE           = 101
 
# From plugins/C4DtoA/api/include/util/NodeIds.h
C4DAIN_DRIVER_EXR      = 9504161
C4DAIN_DRIVER_DEEPEXR  = 1058716317
C4DAIN_DRIVER_JPEG     = 313466666
C4DAIN_DRIVER_PNG      = 9492523
C4DAIN_DRIVER_TIFF     = 313114887

#document global ids
doc=c4d.documents.GetActiveDocument()
docname=doc.GetDocumentName()
docpath=doc.GetDocumentPath()
docfolder=docname[:-4]

#get all objects with children
def get_all_objects(op, filter, output):
    while op:
        if filter(op):
            output.append(op)
        get_all_objects(op.GetDown(), filter, output)
        op = op.GetNext()
    return output

def update_drivers():

     #drivers objects list
     objectsList = get_all_objects(doc.GetFirstObject(), lambda x: x.CheckType(ARNOLD_DRIVER), [])
     path_id = c4d.DescID(c4d.DescLevel(C4DAIP_DRIVER_EXR_FILENAME), c4d.DescLevel(1))

     for obj in objectsList:
          driver_name = obj[c4d.ID_BASELIST_NAME]
          print driver_name
          if not driver_name == "<display driver>":
               obj.SetParameter(path_id, "c:\\my\\new\\path", c4d.DESCFLAGS_SET_0)
          else:
               None
          

update_drivers()