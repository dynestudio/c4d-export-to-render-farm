import c4d
from c4d import gui
#Welcome to the world of Python


def main():
    
    doc = c4d.documents.GetActiveDocument()
    docpath= doc.GetDocumentPath()
    MP_path = "./$prj/$prj_MP"
    octane_mp_path = docpath + MP_path[-8:]

    print docpath
    print MP_path[-8:]
    print octane_mp_path
    
if __name__=='__main__':
    main()
