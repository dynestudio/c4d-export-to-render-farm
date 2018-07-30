import c4d

#global render engines ids
#arnold ids
ARNOLD_RENDERER          = 1029988
ARNOLD_RENDERER_COMMAND  = 1039333
ARNOLD_DUMMYFORMAT       = 1035823
ARNOLD_DRIVER            = 1030141
 
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

def update_driversPath():

     #drivers objects list
     objectsList = get_all_objects(doc.GetFirstObject(), lambda x: x.CheckType(ARNOLD_DRIVER), [])

     for obj in objectsList:
          driver_name = obj[c4d.ID_BASELIST_NAME]
          driver_type = obj[c4d.C4DAI_DRIVER_TYPE]

          if driver_type == C4DAIN_DRIVER_EXR:
               driver_filename = C4DAIP_DRIVER_EXR_FILENAME
          elif driver_type == C4DAIN_DRIVER_DEEPEXR:
               driver_filename = C4DAIP_DRIVER_DEEPEXR_FILENAME
          elif driver_type == C4DAIN_DRIVER_TIFF:
               driver_filename = C4DAIP_DRIVER_TIFF_FILENAME
          elif driver_type == C4DAIN_DRIVER_PNG:
               driver_filename = C4DAIP_DRIVER_PNG_FILENAME
          elif driver_type == C4DAIN_DRIVER_JPEG:
               driver_filename = C4DAIP_DRIVER_JPEG_FILENAME
          else:
               driver_filename = 0

          if driver_type == C4DAIN_DRIVER_EXR:
               driver_format = ".exr"
          elif driver_type == C4DAIN_DRIVER_DEEPEXR:
               driver_format = ".exr"
          elif driver_type == C4DAIN_DRIVER_TIFF:
               driver_format = ".tiff"
          elif driver_type == C4DAIN_DRIVER_PNG:
               driver_format = ".png"
          elif driver_type == C4DAIN_DRIVER_JPEG:
               driver_format = ".jpg"
          else:
               driver_format = ""

          path_id = c4d.DescID(c4d.DescLevel(driver_filename), c4d.DescLevel(1))
          driver_name = driver_name.replace(" ","_")
          driver_custom_path = "./$prj/$prj_" + driver_name + driver_format
          
          if not driver_type == C4DAIN_DRIVER_DISPLAY:
               obj.SetParameter(path_id, driver_custom_path, c4d.DESCFLAGS_SET_0)
          else:
               None
          
     c4d.EventAdd()

update_driversPath()