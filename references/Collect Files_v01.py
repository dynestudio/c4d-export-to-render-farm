import c4d
import os

def main():
    current_dir = doc.GetDocumentPath()
    buffer_path = None


    list_obj = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)
    if not list_obj:
        return
    
    new_doc = c4d.documents.IsolateObjects(doc, list_obj)
    c4d.documents.InsertBaseDocument(new_doc)
    if not current_dir:
        return
    buffer_path = os.path.join(current_dir,"file_buffer.c4d")
    c4d.documents.SaveDocument(new_doc, buffer_path, c4d.SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST, c4d.FORMAT_C4DEXPORT)
        
    path = c4d.storage.LoadDialog(flags = c4d.FILESELECT_DIRECTORY)
    if not path:
        return
    
    filename = c4d.gui.InputDialog("Nom du dossier", "Dossier")
    if not filename:
        return
    
    
    assets = list()
    missingAssets = list()
    path = str(os.path.join(path,filename))
    c4d.documents.SaveProject(new_doc, c4d.SAVEPROJECT_SCENEFILE | c4d.SAVEPROJECT_ASSETS | c4d.SAVEPROJECT_PROGRESSALLOWED | c4d.SAVEPROJECT_DIALOGSALLOWED | c4d.SAVEPROJECT_SHOWMISSINGASSETDIALOG, path, assets, missingAssets)
    
    if buffer_path:
        os.remove(buffer_path)
        
    if missingAssets:
        gui.MessageDialog("Missing Asset\n" + str(missingAssets))


    c4d.documents.KillDocument(new_doc)


if __name__=='__main__':
    main()