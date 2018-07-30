import c4d
from c4d import gui

def collect():
	doc=c4d.documents.GetActiveDocument()
	docname=doc.GetDocumentName()
	docpath=doc.GetDocumentPath()

	assets=c4d.documents.GetAllAssets(doc, True, docpath)
	missingAssets=c4d.documents.GetAllMissingAssets(doc, True, docpath)
	#c4d.documents.GetAllAssets(doc,True,"")
	#IsInSearchPath()

	SaveProject=c4d.documents.SaveProject(doc, c4d.SAVEPROJECT_SCENEFILE, docpath, assets, missingAssets)


if __name__=='__main__':
	collect()