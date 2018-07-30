import c4d

def get_c4d_ver():
    
    C4D_ver = str(c4d.GetC4DVersion())
    C4D_ver = C4D_ver[:2] + "." + C4D_ver[2:]
    version_to_log = "Cinema 4D R" + C4D_ver
    C4DR_ver = C4D_ver[:2]
    
    ver_list = [version_to_log,C4DR_ver]

    return ver_list

C4D_version = get_c4d_ver()
C4D_version_log = C4D_version[0]
C4DR_ver = C4D_version[1]

print C4DR_ver

if int(C4DR_ver) == 18:
    print "Release 18"
else:
    print "Not Release 18"