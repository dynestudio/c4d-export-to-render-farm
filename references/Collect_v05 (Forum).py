import c4d


def get_targetPath():
    
    targetPath = c4d.storage.SaveDialog()

    if targetPath[-4:] == ".c4d":
        targetPath = targetPath[:-4]
    else:
        None   

    return targetPath     

def saveProject():

    doc=c4d.documents.GetActiveDocument()
    docpath=doc.GetDocumentPath() #this would be the last path of the get assets function?
    
    targetPath = get_targetPath()

    assets=c4d.documents.GetAllAssets(doc, True, docpath) #list of assets to copy
        
    missingAssets = None #list of missing assets
    
    flags = c4d.SAVEPROJECT_ASSETS | c4d.SAVEPROJECT_SCENEFILE | c4d.SAVEPROJECT_DIALOGSALLOWED #collect flags
    
    c4d.documents.SaveProject(doc, flags, targetPath, assets, missingAssets) #do collect, what i need to put in missing assets?
        
    c4d.EventAdd()
    
if __name__=='__main__':
    saveProject()
