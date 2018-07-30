import c4d
from c4d import gui


def get_targetPath():
    
    targetPath = c4d.storage.SaveDialog()

    if targetPath[-4:] == ".c4d":
        targetPath = targetPath[:-4]
    else:
        None   

    return targetPath     

def saveProject():

    
    doc=c4d.documents.GetActiveDocument()
    docpath=doc.GetDocumentPath()
    
    targetPath = get_targetPath()
    print targetPath
    if targetPath == None:
        gui.MessageDialog('The scene has not been collected.') 
        return False
    else:
        None

    assets = []
    missingAssets = []
    print missingAssets
    
    #You will need c4d R15.057 for this function
    saveProject_flags = c4d.SAVEPROJECT_ASSETS | c4d.SAVEPROJECT_SCENEFILE | c4d.SAVEPROJECT_DONTFAILONMISSINGASSETS | c4d.SAVEPROJECT_ADDTORECENTLIST | c4d.SAVEPROJECT_PROGRESSALLOWED

    res = c4d.documents.SaveProject(doc, saveProject_flags, targetPath, assets, missingAssets)

    print "fase 02"
    print assets
    print "fase 03"
    print missingAssets
        
    c4d.EventAdd()

    if res == False:
        gui.MessageDialog('The scene has not been collected,\ncheck the console for more details.') 
        return False
    else:
        print "The scene has been collected correctly."
        return True
    
if __name__=='__main__':
    saveProject()
