import c4d
from c4d import gui


def get_targetPath():
    
    targetPath = c4d.storage.SaveDialog()

    if not targetPath[-4:] == ".c4d":
        targetPath = targetPath+".c4d"
    else:
        None   

    return targetPath     

def main():

    
    doc=c4d.documents.GetActiveDocument()
    docpath=doc.GetDocumentPath()
    
    targetPath = "/Users/Carlos/Desktop/Test 03"

    #You will need c4d R15.057 for this function
    assets=c4d.documents.GetAllAssets(doc, True, docpath)
    
    missingAssets = None
    
    saveProject_flags = c4d.SAVEPROJECT_ASSETS | c4d.SAVEPROJECT_SCENEFILE | c4d.SAVEPROJECT_PROGRESSALLOWED | c4d.SAVEPROJECT_ADDTORECENTLIST
    
    collect_file = c4d.documents.SaveProject(doc, saveProject_flags, targetPath, assets, missingAssets)
        
    c4d.EventAdd()

    if collect_file == False:
        gui.MessageDialog('The scene has not been collected,\ncheck the console for more details.') print "the scene has not been collected."
        return
    else:
        print "the scene has been collected correctly."
    
if __name__=='__main__':
    main()
