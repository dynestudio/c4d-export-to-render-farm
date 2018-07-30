import c4d
from c4d import gui


def get_targetPath():
    
    targetPath = c4d.storage.SaveDialog()
    if targetPath == None:
        print "A path was not selected."
        return None
    else:
        None

    if targetPath[-4:] == ".c4d":
        targetPath = targetPath[:-4]
    else:
        None   

    return targetPath     

def saveProject():

    #lists for assets
    assets = []
    missingAssets = []
    missingAssets_log = []

    doc=c4d.documents.GetActiveDocument()
    docpath=doc.GetDocumentPath()
    
    #get the collect path
    targetPath = get_targetPath()
    if targetPath == None:
        gui.MessageDialog('You have canceled the collect.') 
        return False
    else:
        None

    #execute the collect files
    #if int(C4DR_ver) <= 15:
        #gui.MessageDialog('\n\nWARNING - You are using' + C4D_version_log + '\nThis script is for Cinema 4D R15.057 and above, sorry :(.')
    #else:
        #None

    #collect properties
    saveProject_flags = c4d.SAVEPROJECT_ASSETS | c4d.SAVEPROJECT_SCENEFILE | c4d.SAVEPROJECT_DONTFAILONMISSINGASSETS | c4d.SAVEPROJECT_ADDTORECENTLIST | c4d.SAVEPROJECT_PROGRESSALLOWED
    #execute save project with assets
    res = c4d.documents.SaveProject(doc, saveProject_flags, targetPath, assets, missingAssets)        
    c4d.EventAdd()

    #missing assets operations
    if len(missingAssets) >= 1:
        missingAssets_log.append("WARNING - there are missing assets in this scene:\n")

        for a in missingAssets:
            missingAssets_log.append(a['filename'])

        if len(missingAssets_log) > 5:
            missingAssets_log_gui = missingAssets_log[:6]
        else:
            missingAssets_log_gui = missingAssets_log

        missingAssets_log_guisplit = str('\n'.join(missingAssets_log_gui))
        
        if len(missingAssets_log) > 6:
            missingAssets_log_gui = missingAssets_log_guisplit + '\n-And more.'
        else:
            missingAssets_log_gui = missingAssets_log_guisplit

        gui.MessageDialog(missingAssets_log_gui+'\n\nCheck the log file to view the missing assets list.')
    else:
        missingAssets_log.append("There are not missing assets in this scene :).")

    #return conditions from collect function 
    if res == True:
        print "The scene has been collected correctly."
        return [True,missingAssets_log]
    else:
        gui.MessageDialog('The scene has not been collected, an error has occurred :(,\ncheck the console for more details.')
        print "If the error is here in the console, please contact us: info@dynetv.com"
        return [False,missingAssets_log]
    
if __name__=='__main__':
    saveProject()
