import c4d
from c4d import gui

ID_OCTANE_LIVEPLUGIN = 1029499
ID_OCTANE_CAMERATAG = 1029524
ID_OCTANE_VIDEOPOST_RENDERER = 1029525
ID_OCTANE_VIDEOPOST = 1005172

def main():

    sBC = doc.GetDataInstance();
    data = sBC.GetContainerInstance(ID_OCTANE_LIVEPLUGIN)
        
    rdata = doc.GetActiveRenderData()
    octane = rdata.GetFirstVideoPost()

    kernelRS = octane[3001]
    kernelLV = int(data.GetReal(3001)) 

    bc = c4d.BaseContainer()
    if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD,c4d.BFM_INPUT_CHANNEL,bc):
            shift = bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QSHIFT
    
    if shift == 0:

    #========================== Transfer Data From LV Settings ==========================
        if rdata[c4d.RDATA_RENDERENGINE] != 1029525:
            rdata[c4d.RDATA_RENDERENGINE] = 1029525
        
        octane[3001] = int(data.GetReal(3001))
    
    #------------------------------------ Info Kernel -------------------------------------
    
        if kernelLV == 0 :
            octane[c4d.SET_INFOCHAN_MAXSAMPLES] = int(data.GetReal(c4d.SET_INFOCHAN_MAXSAMPLES))
            print int(data.GetReal(c4d.SET_INFOCHAN_MAXSAMPLES))
            octane[c4d.SET_INFOCHAN_TYPE] = int(data.GetReal(c4d.SET_INFOCHAN_TYPE))
            octane[c4d.SET_INFOCHAN_RAYDISTR] = int(data.GetBool(c4d.SET_INFOCHAN_RAYDISTR))
            octane[c4d.SET_INFOCHAN_RAYEPSILON] = float(data.GetReal(c4d.SET_INFOCHAN_RAYEPSILON))
            octane[c4d.SET_INFOCHAN_FILTERSIZE] = float(data.GetReal(c4d.SET_INFOCHAN_FILTERSIZE))
            octane[c4d.SET_INFOCHAN_AODIST] = int(data.GetReal(c4d.SET_INFOCHAN_AODIST))
            octane[c4d.SET_INFOCHAN_AO_ALPHASHD] = int(data.GetBool(c4d.SET_INFOCHAN_AO_ALPHASHD))
            octane[c4d.SET_INFOCHAN_OPAC_THRESH] = float(data.GetReal(c4d.SET_INFOCHAN_OPAC_THRESH))
            octane[c4d.SET_INFOCHAN_ZDEPTHMAX] = float(data.GetReal(c4d.SET_INFOCHAN_ZDEPTHMAX))
            octane[c4d.SET_INFOCHAN_UVMAX] = float(data.GetReal(c4d.SET_INFOCHAN_UVMAX))
            octane[c4d.SET_INFOCHAN_UVSET] = float(data.GetReal(c4d.SET_INFOCHAN_UVSET))
            octane[c4d.SET_INFOCHAN_MAXSPEED] = float(data.GetReal(c4d.SET_INFOCHAN_MAXSPEED))
            octane[c4d.SET_INFOCHAN_BUMPNORMAL] = bool(data.GetBool(c4d.SET_INFOCHAN_BUMPNORMAL))
            octane[c4d.SET_INFOCHAN_WIREBACKLGHT] = bool(data.GetBool(c4d.SET_INFOCHAN_WIREBACKLGHT))
            octane[c4d.SET_INFOCHAN_ALPHACHAN] = bool(data.GetBool(c4d.SET_INFOCHAN_ALPHACHAN))
            octane[c4d.SET_INFOCHAN_PAR_SAMPLES] = float(data.GetReal(c4d.SET_INFOCHAN_PAR_SAMPLES))
            octane[c4d.SET_INFOCHAN_MAXTILE_SAMP] = float(data.GetReal(c4d.SET_INFOCHAN_MAXTILE_SAMP))
            octane[c4d.SET_INFOCHAN_MIN_NET_TRAFFIC] = bool(data.GetBool(c4d.SET_INFOCHAN_MIN_NET_TRAFFIC))
        
            c4d.EventAdd(1)
        
    #------------------------------------ Direct Lighting -------------------------------------    
        if kernelLV == 1 :
            octane[c4d.SET_DIRECT_MAXSAMPLES] = int(data.GetReal(c4d.SET_DIRECT_MAXSAMPLES))
            octane[c4d.SET_DIRECT_GIMOD] = int(data.GetReal(c4d.SET_DIRECT_GIMOD))
            octane[c4d.SET_DIRECT_SPECDEPTH] = int(data.GetReal(c4d.SET_DIRECT_SPECDEPTH))
            octane[c4d.SET_DIRECT_GLOSDEPTH] = int(data.GetReal(c4d.SET_DIRECT_GLOSDEPTH))
            octane[c4d.SET_DIRECT_DIFDEPTH] = int(data.GetReal(c4d.SET_DIRECT_DIFDEPTH))
            octane[c4d.SET_DIRECT_RAYEPS] = float(data.GetReal(c4d.SET_DIRECT_RAYEPS))
            octane[c4d.SET_DIRECT_FSIZE] = float(data.GetReal(c4d.SET_DIRECT_FSIZE))
            octane[c4d.SET_DIRECT_AODIST] = int(data.GetReal(c4d.SET_DIRECT_AODIST))
            octane[c4d.SET_DIRECT_ALPHASHADOW] = bool(data.GetReal(c4d.SET_DIRECT_ALPHASHADOW))
            octane[c4d.SET_DIRECT_ALPHACHAN] = bool(data.GetReal(c4d.SET_DIRECT_ALPHACHAN))
            octane[c4d.SET_DIRECT_KEEPENV] = bool(data.GetReal(c4d.SET_DIRECT_KEEPENV))
            octane[c4d.SET_DIRECT_PTERMPOWER] = float(data.GetReal(c4d.SET_DIRECT_PTERMPOWER))
            octane[c4d.SET_DIRECT_COHERENTRATIO] = float(data.GetReal(c4d.SET_DIRECT_COHERENTRATIO))
            octane[c4d.SET_DIRECT_STAT_NOISE] = bool(data.GetReal(c4d.SET_DIRECT_STAT_NOISE))
            octane[c4d.SET_DIRECT_PAR_SAMPLES] = int(data.GetReal(c4d.SET_DIRECT_PAR_SAMPLES))
            octane[c4d.SET_DIRECT_MAXTILE_SAMP] = int(data.GetReal(c4d.SET_DIRECT_MAXTILE_SAMP))
            octane[c4d.SET_DIRECT_MIN_NET_TRAFFIC] = bool(data.GetReal(c4d.SET_DIRECT_MIN_NET_TRAFFIC))
            
            octane[c4d.SET_DIRECT_ADAPTIVE_SAMPLING] = bool(data.GetReal(c4d.SET_DIRECT_ADAPTIVE_SAMPLING))
            octane[c4d.SET_DIRECT_ASAMP_NOISE_THRESH] = float(data.GetReal(c4d.SET_DIRECT_ASAMP_NOISE_THRESH))
            octane[c4d.SET_DIRECT_ASAMP_MIN_SAMPLES] = int(data.GetReal(c4d.SET_DIRECT_ASAMP_MIN_SAMPLES))
            octane[c4d.SET_DIRECT_ASAMP_EXP_EXPOSURE] = float(data.GetReal(c4d.SET_DIRECT_ASAMP_EXP_EXPOSURE))
            octane[c4d.SET_DIRECT_ASAMP_GRP_PIXELS] = int(data.GetReal(c4d.SET_DIRECT_ASAMP_GRP_PIXELS))
            
            c4d.EventAdd(1)
            
    #------------------------------------ Path Tracing ------------------------------------- 
        if kernelLV == 2 :
            octane[c4d.SET_PATHTRACE_MAXSAMPLES] = int(data.GetReal(c4d.SET_PATHTRACE_MAXSAMPLES))
            print int(data.GetReal(c4d.SET_PATHTRACE_MAXSAMPLES))
            octane[c4d.SET_PATHTRACE_DIFDEPTH] = int(data.GetReal(c4d.SET_PATHTRACE_DIFDEPTH))
            octane[c4d.SET_PATHTRACE_GLOSSYDEPTH] = int(data.GetReal(c4d.SET_PATHTRACE_GLOSSYDEPTH))
            octane[c4d.SET_PATHTRACE_RAYEPS] = float(data.GetReal(c4d.SET_PATHTRACE_RAYEPS))
            octane[c4d.SET_PATHTRACE_FSIZE] = float(data.GetReal(c4d.SET_PATHTRACE_FSIZE))
            octane[c4d.SET_PATHTRACE_ASHADOW] = bool(data.GetReal(c4d.SET_PATHTRACE_ASHADOW))
            octane[c4d.SET_PATHTRACE_CAUSTICBLUR] = float(data.GetReal(c4d.SET_PATHTRACE_CAUSTICBLUR))
            octane[c4d.SET_PATHTRACE_GICLAMP] = float(data.GetReal(c4d.SET_PATHTRACE_GICLAMP))
            octane[c4d.SET_PATHTRACE_ACHAN] = bool(data.GetReal(c4d.SET_PATHTRACE_ACHAN))
            octane[c4d.SET_PATHTRACE_KEEPENV] = bool(data.GetReal(c4d.SET_PATHTRACE_KEEPENV))
            octane[c4d.SET_PATHTRACE_PTERMPOWER] = float(data.GetReal(c4d.SET_PATHTRACE_PTERMPOWER))
            octane[c4d.SET_PATHTRACE_COHERENTRATIO] = float(data.GetReal(c4d.SET_PATHTRACE_COHERENTRATIO))
            octane[c4d.SET_PATHTRACE_STAT_NOISE] = bool(data.GetReal(c4d.SET_PATHTRACE_STAT_NOISE))
            octane[c4d.SET_PATHTRACE_PAR_SAMPLES] = int(data.GetReal(c4d.SET_PATHTRACE_PAR_SAMPLES))
            octane[c4d.SET_PATHTRACE_MAXTILE_SAMP] = int(data.GetReal(c4d.SET_PATHTRACE_MAXTILE_SAMP))
            octane[c4d.SET_PATHTRACE_MIN_NET_TRAFFIC] = bool(data.GetReal(c4d.SET_PATHTRACE_MIN_NET_TRAFFIC))
            
            octane[c4d.SET_PATHTRACE_ADAPTIVE_SAMPLING] = bool(data.GetReal(c4d.SET_PATHTRACE_ADAPTIVE_SAMPLING))
            octane[c4d.SET_PATHTRACE_ASAMP_NOISE_THRESH] = float(data.GetReal(c4d.SET_PATHTRACE_ASAMP_NOISE_THRESH))
            octane[c4d.SET_PATHTRACE_ASAMP_MIN_SAMPLES] = int(data.GetReal(c4d.SET_PATHTRACE_ASAMP_MIN_SAMPLES))
            octane[c4d.SET_PATHTRACE_ASAMP_EXP_EXPOSURE] = float(data.GetReal(c4d.SET_PATHTRACE_ASAMP_EXP_EXPOSURE))
            octane[c4d.SET_PATHTRACE_ASAMP_GRP_PIXELS] = int(data.GetReal(c4d.SET_PATHTRACE_ASAMP_GRP_PIXELS))
            
            c4d.EventAdd(1)
        
    #----------------------------------------- PMC --------------------------------------- 
        if kernelLV == 3 :
            octane[c4d.SET_PMC_MAXSAMPLES] = int(data.GetReal(c4d.SET_PMC_MAXSAMPLES))
            octane[c4d.SET_PMC_DIFDEPTH] = int(data.GetReal(c4d.SET_PMC_DIFDEPTH))
            octane[c4d.SET_PMC_GLOSSYDEPTH] = int(data.GetReal(c4d.SET_PMC_GLOSSYDEPTH))
            octane[c4d.SET_PMC_RAYEPS] = float(data.GetReal(c4d.SET_PMC_RAYEPS))
            octane[c4d.SET_PMC_FSIZE] = float(data.GetReal(c4d.SET_PMC_FSIZE))
            octane[c4d.SET_PMC_ASHADOWS] = bool(data.GetReal(c4d.SET_PMC_ASHADOWS))
            octane[c4d.SET_PMC_CAUSTICBLUR] = float(data.GetReal(c4d.SET_PMC_CAUSTICBLUR))
            octane[c4d.SET_PMC_GICLAMP] = float(data.GetReal(c4d.SET_PMC_GICLAMP))
            octane[c4d.SET_PMC_ACHANNEL] = bool(data.GetReal(c4d.SET_PMC_ACHANNEL))
            octane[c4d.SET_PMC_KEEPENV] = bool(data.GetReal(c4d.SET_PMC_KEEPENV))
            octane[c4d.SET_PMC_PTERMPOWER] = float(data.GetReal(c4d.SET_PMC_PTERMPOWER))
            octane[c4d.SET_PMC_EXPLOSTRENGTH] = float(data.GetReal(c4d.SET_PMC_EXPLOSTRENGTH))
            octane[c4d.SET_PMC_DLIMPORTANCE] = float(data.GetReal(c4d.SET_PMC_DLIMPORTANCE))
            octane[c4d.SET_PMC_MAXREJECTS] = int(data.GetReal(c4d.SET_PMC_MAXREJECTS))
            octane[c4d.SET_PMC_PARALLELISM] = int(data.GetReal(c4d.SET_PMC_PARALLELISM))
            octane[c4d.SET_PMC_WORK_CHUNK_SIZE] = int(data.GetReal(c4d.SET_PMC_WORK_CHUNK_SIZE))    
            
            c4d.EventAdd(1)
        
    else:
        print "SHIFT"
    #========================== Transfer Data From Render Settings ==========================
        data.SetReal(3001, kernelRS)

    #------------------------------------ Info Kernel -------------------------------------
        if kernelRS == 0:
            data.SetReal(c4d.SET_INFOCHAN_MAXSAMPLES, octane[c4d.SET_INFOCHAN_MAXSAMPLES])
            data.SetReal(c4d.SET_INFOCHAN_TYPE, octane[c4d.SET_INFOCHAN_TYPE])
            data.SetReal(c4d.SET_INFOCHAN_RAYEPSILON, octane[c4d.SET_INFOCHAN_RAYEPSILON])
            data.SetReal(c4d.SET_INFOCHAN_FILTERSIZE, octane[c4d.SET_INFOCHAN_FILTERSIZE])
            data.SetFloat(c4d.SET_INFOCHAN_AODIST, int(octane[c4d.SET_INFOCHAN_AODIST]))
            data.SetReal(c4d.SET_INFOCHAN_AO_ALPHASHD, octane[c4d.SET_INFOCHAN_AO_ALPHASHD])
            data.SetReal(c4d.SET_INFOCHAN_OPAC_THRESH, octane[c4d.SET_INFOCHAN_OPAC_THRESH])
            data.SetReal(c4d.SET_INFOCHAN_ZDEPTHMAX, octane[c4d.SET_INFOCHAN_ZDEPTHMAX])
            data.SetReal(c4d.SET_INFOCHAN_UVMAX, octane[c4d.SET_INFOCHAN_UVMAX])
            data.SetReal(c4d.SET_INFOCHAN_UVSET, octane[c4d.SET_INFOCHAN_UVSET])
            data.SetReal(c4d.SET_INFOCHAN_MAXSPEED, octane[c4d.SET_INFOCHAN_MAXSPEED])
            data.SetReal(c4d.SET_INFOCHAN_RAYDISTR, octane[c4d.SET_INFOCHAN_RAYDISTR])
            data.SetReal(c4d.SET_INFOCHAN_BUMPNORMAL, octane[c4d.SET_INFOCHAN_BUMPNORMAL])
            data.SetReal(c4d.SET_INFOCHAN_WIREBACKLGHT, octane[c4d.SET_INFOCHAN_WIREBACKLGHT])
            data.SetReal(c4d.SET_INFOCHAN_ALPHACHAN, octane[c4d.SET_INFOCHAN_ALPHACHAN])
            data.SetReal(c4d.SET_INFOCHAN_PAR_SAMPLES, int(octane[c4d.SET_INFOCHAN_PAR_SAMPLES]))
            data.SetReal(c4d.SET_INFOCHAN_MAXTILE_SAMP, octane[c4d.SET_INFOCHAN_MAXTILE_SAMP])
            data.SetReal(c4d.SET_INFOCHAN_MIN_NET_TRAFFIC, octane[c4d.SET_INFOCHAN_MIN_NET_TRAFFIC])

    #------------------------------------ Direct Lighting -------------------------------------
        
        if kernelRS == 1:
            data.SetReal(c4d.SET_DIRECT_MAXSAMPLES, octane[c4d.SET_DIRECT_MAXSAMPLES])
            data.SetReal(c4d.SET_DIRECT_GIMOD, octane[c4d.SET_DIRECT_GIMOD])
            data.SetReal(c4d.SET_DIRECT_SPECDEPTH, octane[c4d.SET_DIRECT_SPECDEPTH])
            data.SetReal(c4d.SET_DIRECT_GLOSDEPTH, octane[c4d.SET_DIRECT_GLOSDEPTH])
            data.SetReal(c4d.SET_DIRECT_DIFDEPTH, octane[c4d.SET_DIRECT_DIFDEPTH])
            data.SetReal(c4d.SET_DIRECT_RAYEPS, octane[c4d.SET_DIRECT_RAYEPS])
            data.SetReal(c4d.SET_DIRECT_FSIZE, octane[c4d.SET_DIRECT_FSIZE])
            data.SetReal(c4d.SET_DIRECT_AODIST, octane[c4d.SET_DIRECT_AODIST])
            data.SetReal(c4d.SET_DIRECT_ALPHASHADOW, octane[c4d.SET_DIRECT_ALPHASHADOW])
            data.SetReal(c4d.SET_DIRECT_ALPHACHAN, octane[c4d.SET_DIRECT_ALPHACHAN])
            data.SetReal(c4d.SET_DIRECT_KEEPENV, octane[c4d.SET_DIRECT_KEEPENV])
            data.SetReal(c4d.SET_DIRECT_PTERMPOWER, octane[c4d.SET_DIRECT_PTERMPOWER])
            data.SetReal(c4d.SET_DIRECT_COHERENTRATIO, octane[c4d.SET_DIRECT_COHERENTRATIO])
            data.SetReal(c4d.SET_DIRECT_STAT_NOISE, octane[c4d.SET_DIRECT_STAT_NOISE])
            data.SetReal(c4d.SET_DIRECT_PAR_SAMPLES, octane[c4d.SET_DIRECT_PAR_SAMPLES])
            data.SetReal(c4d.SET_DIRECT_MAXTILE_SAMP, octane[c4d.SET_DIRECT_MAXTILE_SAMP])
            data.SetReal(c4d.SET_DIRECT_MIN_NET_TRAFFIC, octane[c4d.SET_DIRECT_MIN_NET_TRAFFIC])
            data.SetReal(c4d.SET_DIRECT_ADAPTIVE_SAMPLING, octane[c4d.SET_DIRECT_ADAPTIVE_SAMPLING])
            data.SetReal(c4d.SET_DIRECT_ASAMP_NOISE_THRESH, octane[c4d.SET_DIRECT_ASAMP_NOISE_THRESH])
            data.SetReal(c4d.SET_DIRECT_ASAMP_MIN_SAMPLES, octane[c4d.SET_DIRECT_ASAMP_MIN_SAMPLES])
            data.SetReal(c4d.SET_DIRECT_ASAMP_EXP_EXPOSURE, octane[c4d.SET_DIRECT_ASAMP_EXP_EXPOSURE])
            data.SetReal(c4d.SET_DIRECT_ASAMP_GRP_PIXELS, octane[c4d.SET_DIRECT_ASAMP_GRP_PIXELS])
            
    #------------------------------------ Path Tracing -------------------------------------        
        if kernelRS == 2:
            data.SetReal(c4d.SET_PATHTRACE_MAXSAMPLES, octane[c4d.SET_PATHTRACE_MAXSAMPLES])
            data.SetReal(c4d.SET_PATHTRACE_DIFDEPTH, octane[c4d.SET_PATHTRACE_DIFDEPTH])
            data.SetReal(c4d.SET_PATHTRACE_GLOSSYDEPTH, octane[c4d.SET_PATHTRACE_GLOSSYDEPTH])
            data.SetReal(c4d.SET_PATHTRACE_RAYEPS, octane[c4d.SET_PATHTRACE_RAYEPS])
            data.SetReal(c4d.SET_PATHTRACE_FSIZE, octane[c4d.SET_PATHTRACE_FSIZE])
            data.SetReal(c4d.SET_PATHTRACE_ASHADOW, octane[c4d.SET_PATHTRACE_ASHADOW])
            data.SetReal(c4d.SET_PATHTRACE_CAUSTICBLUR, octane[c4d.SET_PATHTRACE_CAUSTICBLUR])
            data.SetReal(c4d.SET_PATHTRACE_GICLAMP, octane[c4d.SET_PATHTRACE_GICLAMP])
            data.SetReal(c4d.SET_PATHTRACE_ACHAN, octane[c4d.SET_PATHTRACE_ACHAN])
            data.SetReal(c4d.SET_PATHTRACE_KEEPENV, octane[c4d.SET_PATHTRACE_KEEPENV])
            data.SetReal(c4d.SET_PATHTRACE_PTERMPOWER, octane[c4d.SET_PATHTRACE_PTERMPOWER])
            data.SetReal(c4d.SET_PATHTRACE_COHERENTRATIO, octane[c4d.SET_PATHTRACE_COHERENTRATIO])
            data.SetReal(c4d.SET_PATHTRACE_STAT_NOISE, octane[c4d.SET_PATHTRACE_STAT_NOISE])
            data.SetReal(c4d.SET_PATHTRACE_PAR_SAMPLES, octane[c4d.SET_PATHTRACE_PAR_SAMPLES])
            data.SetReal(c4d.SET_PATHTRACE_MAXTILE_SAMP, octane[c4d.SET_PATHTRACE_MAXTILE_SAMP])
            data.SetReal(c4d.SET_PATHTRACE_MIN_NET_TRAFFIC, octane[c4d.SET_PATHTRACE_MIN_NET_TRAFFIC])
            data.SetReal(c4d.SET_PATHTRACE_ADAPTIVE_SAMPLING, octane[c4d.SET_PATHTRACE_ADAPTIVE_SAMPLING])
            data.SetReal(c4d.SET_PATHTRACE_ASAMP_NOISE_THRESH, octane[c4d.SET_PATHTRACE_ASAMP_NOISE_THRESH])
            data.SetReal(c4d.SET_PATHTRACE_ASAMP_MIN_SAMPLES, octane[c4d.SET_PATHTRACE_ASAMP_MIN_SAMPLES])
            data.SetReal(c4d.SET_PATHTRACE_ASAMP_EXP_EXPOSURE, octane[c4d.SET_PATHTRACE_ASAMP_EXP_EXPOSURE])
            data.SetReal(c4d.SET_PATHTRACE_ASAMP_GRP_PIXELS, octane[c4d.SET_PATHTRACE_ASAMP_GRP_PIXELS])
            
    #------------------------------------ PMC -------------------------------------   
        if kernelRS == 3:
            data.SetReal(c4d.SET_PMC_MAXSAMPLES, octane[c4d.SET_PMC_MAXSAMPLES])
            data.SetReal(c4d.SET_PMC_DIFDEPTH, octane[c4d.SET_PMC_DIFDEPTH])
            data.SetReal(c4d.SET_PMC_GLOSSYDEPTH, octane[c4d.SET_PMC_GLOSSYDEPTH])
            data.SetReal(c4d.SET_PMC_RAYEPS, octane[c4d.SET_PMC_RAYEPS])
            data.SetReal(c4d.SET_PMC_FSIZE, octane[c4d.SET_PMC_FSIZE])
            data.SetReal(c4d.SET_PMC_ASHADOWS, octane[c4d.SET_PMC_ASHADOWS])
            data.SetReal(c4d.SET_PMC_CAUSTICBLUR, octane[c4d.SET_PMC_CAUSTICBLUR])
            data.SetReal(c4d.SET_PMC_GICLAMP, octane[c4d.SET_PMC_GICLAMP])
            data.SetReal(c4d.SET_PMC_ACHANNEL, octane[c4d.SET_PMC_ACHANNEL])
            data.SetReal(c4d.SET_PMC_KEEPENV, octane[c4d.SET_PMC_KEEPENV])
            data.SetReal(c4d.SET_PMC_PTERMPOWER, octane[c4d.SET_PMC_PTERMPOWER])
            data.SetReal(c4d.SET_PMC_EXPLOSTRENGTH, octane[c4d.SET_PMC_EXPLOSTRENGTH])
            data.SetReal(c4d.SET_PMC_DLIMPORTANCE, octane[c4d.SET_PMC_DLIMPORTANCE])
            data.SetReal(c4d.SET_PMC_MAXREJECTS, octane[c4d.SET_PMC_MAXREJECTS])
            data.SetReal(c4d.SET_PMC_PARALLELISM, octane[c4d.SET_PMC_PARALLELISM])
            data.SetReal(c4d.SET_PMC_WORK_CHUNK_SIZE, octane[c4d.SET_PMC_WORK_CHUNK_SIZE])       
                
        c4d.CallCommand(1031195)
        c4d.EventAdd(1)  

if __name__=='__main__':
    main()