import c4d

def get_frames():

    #Active Document
    doc = c4d.documents.GetActiveDocument()
    # Render Data
    renderdata = doc.GetActiveRenderData()
    rd = renderdata.GetData()
    
    #Get Frames info
    if rd[c4d.RDATA_FRAMESEQUENCE] == c4d.RDATA_FRAMESEQUENCE_ALLFRAMES:
        framefrom = doc[c4d.DOCUMENT_MINTIME].GetFrame(doc.GetFps())
        frameto = doc[c4d.DOCUMENT_MAXTIME].GetFrame(doc.GetFps())
    elif rd[c4d.RDATA_FRAMESEQUENCE] == c4d.RDATA_FRAMESEQUENCE_CURRENTFRAME:
        framefrom = doc[c4d.DOCUMENT_TIME].GetFrame(doc.GetFps())
        frameto = framefrom
    elif rd[c4d.RDATA_FRAMESEQUENCE] == c4d.RDATA_FRAMESEQUENCE_PREVIEWRANGE:
        framefrom = doc[c4d.DOCUMENT_LOOPMINTIME].GetFrame(doc.GetFps())
        frameto = doc[c4d.DOCUMENT_LOOPMAXTIME].GetFrame(doc.GetFps())
    else:
        framefrom = rd[c4d.RDATA_FRAMEFROM].GetFrame(doc.GetFps())
        frameto = rd[c4d.RDATA_FRAMETO].GetFrame(doc.GetFps())
    
    #print frames sequence
    print "frame from: "+str(framefrom)
    print "frame to: "+str(frameto)

get_frames()