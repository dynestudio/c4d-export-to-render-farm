import c4d

# From plugins/C4DtoA/res/c4dtoa_symbols.h
ARNOLD_DRIVER               = 1030141

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

def main():
 exrDriver = c4d.BaseObject(ARNOLD_DRIVER)
 exrDriver.SetName("myDriver")
 path_id = c4d.DescID(c4d.DescLevel(C4DAIP_DRIVER_EXR_FILENAME), c4d.DescLevel(1))
 type_id = c4d.DescID(c4d.DescLevel(C4DAIP_DRIVER_EXR_FILENAME), c4d.DescLevel(2))
 print "Current path: %s" % exrDriver.GetParameter(path_id, c4d.DESCFLAGS_GET_0)
 print "Current type: %d" % exrDriver.GetParameter(type_id, c4d.DESCFLAGS_GET_0)
 exrDriver.SetParameter(path_id, "c:\\test\\path", c4d.DESCFLAGS_SET_0)
 exrDriver.SetParameter(type_id, 1, c4d.DESCFLAGS_SET_0)
 
 doc.InsertObject(exrDriver)
 c4d.EventAdd() 

if __name__=='__main__':
 main() 