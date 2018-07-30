import c4d

def collect():
    collect=c4d.CallCommand(12255, 12255)
    if collect == 1:
        print 2
        print collect
    elif collect == None:
        print 1
        print collect

collect()



doc=c4d.documents.GetActiveDocument()
docname=BaseDocument.GetDocumentName()
docpath=BaseDocument.GetDocumentPath()

c4d.documents.GetAllAssets(doc,True,"")

IsInSearchPath()