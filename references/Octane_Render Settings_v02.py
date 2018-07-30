import c4d
from c4d import gui

OCTANE_LIVEPLUGIN = 1029499
OCTANE_CAMERATAG = 1029524
OCTANE_RENDERER = 1029525
OCTANE_VIDEOPOST = 1005172
#thanks to the octane user mpazera for the base code

def Octane_Log_Data():

    sBC = doc.GetDataInstance();
    data = sBC.GetContainerInstance(OCTANE_LIVEPLUGIN)
        
    rdata = doc.GetActiveRenderData()
    octane = rdata.GetFirstVideoPost()

    kernelRS = octane[3001]
    kernelLV = int(data.GetReal(3001)) 

    #Transfer Data From LV Settings
    if rdata[c4d.RDATA_RENDERENGINE] != OCTANE_RENDERER:
        rdata[c4d.RDATA_RENDERENGINE] = OCTANE_RENDERER
    else:
        None
    
    octane[3001] = int(data.GetReal(3001))

    #Info Kernel
    if kernelLV == 0 :

        render_kernel = "Render Kernel: Infochannels"

        max_samples = octane[c4d.SET_INFOCHAN_MAXSAMPLES] = int(data.GetReal(c4d.SET_INFOCHAN_MAXSAMPLES))
        max_samples = "Max. Samples = " + str(max_samples)
        info_type = octane[c4d.SET_INFOCHAN_TYPE] = int(data.GetReal(c4d.SET_INFOCHAN_TYPE))
        if info_type == 0:
            info_type = "Geometric normals"
        elif info_type == 1:
            info_type = "Shading normals"
        elif info_type == 2:
            info_type = "Position"
        elif info_type == 3:
            info_type = "Z-depth"
        elif info_type == 4:
            info_type = "Material ID"
        elif info_type == 5:
            info_type = "Texture coordinates"
        elif info_type == 6:
            info_type = "Tangent"
        elif info_type == 7:
            info_type = "Wireframe"
        elif info_type == 8:
            info_type = "Vertex normal"
        elif info_type == 9:
            info_type = "Object layer ID"
        elif info_type == 10:
            info_type = "Ambient occlussion"
        elif info_type == 11:
            info_type = "Motion vector"
        elif info_type == 12:
            info_type = "Render layer ID"
        elif info_type == 13:
            info_type = "Render layer mask"
        elif info_type == 14:
            info_type = "Light pass ID"
        elif info_type == 15:
            info_type = "Tangent normal"
        elif info_type == 16:
            info_type = "Opacity"
        elif info_type == 17:
            info_type = "Baking group ID"
        elif info_type == 18:
            info_type = "Roughness"
        elif info_type == 19:
            info_type = "IOR"
        elif info_type == 20:
            info_type = "Diffuse filter"
        elif info_type == 21:
            info_type = "Reflection filter"
        elif info_type == 22:
            info_type = "Refraction filter"
        elif info_type == 23:
            info_type = "Transmission filter"
        else:
            info_type = "Object layer color"
        info_type = "Type = " + info_type
        ray_distr = octane[c4d.SET_INFOCHAN_RAYDISTR] = int(data.GetBool(c4d.SET_INFOCHAN_RAYDISTR))
        if ray_distr == 0:
            ray_distr = "Distributed rays"
        elif ray_distr == 1:
            ray_distr = "Non-distributed with pixel filtering"
        else:
            ray_distr = "Non-distributed without pixel filtering"
        ray_distr = "Sampling mode = " + ray_distr
        ray_epsilon = octane[c4d.SET_INFOCHAN_RAYEPSILON] = float(data.GetReal(c4d.SET_INFOCHAN_RAYEPSILON))
        ray_epsilon = "Ray epsilon = " + str(ray_epsilon)
        Filter = octane[c4d.SET_INFOCHAN_FILTERSIZE] = float(data.GetReal(c4d.SET_INFOCHAN_FILTERSIZE))
        Filter = "Filter size = " + str(Filter)
        AO_dist = octane[c4d.SET_INFOCHAN_AODIST] = int(data.GetReal(c4d.SET_INFOCHAN_AODIST))
        AO_dist = "AO distance = " + str(AO_dist)
        AO_alphashd = octane[c4d.SET_INFOCHAN_AO_ALPHASHD] = bool(data.GetBool(c4d.SET_INFOCHAN_AO_ALPHASHD))
        if AO_alphashd == True:
            AO_alphashd = "AO alpha shadows = Enabled"
        else: 
            AO_alphashd = "AO alpha shadows = Disabled"
        opac_thresh = octane[c4d.SET_INFOCHAN_OPAC_THRESH] = float(data.GetReal(c4d.SET_INFOCHAN_OPAC_THRESH))
        opac_thresh = "Opacity threshold = " + str(opac_thresh)
        zdepthmax = octane[c4d.SET_INFOCHAN_ZDEPTHMAX] = float(data.GetReal(c4d.SET_INFOCHAN_ZDEPTHMAX))
        zdepthmax = "Z-depth max = " + str(zdepthmax)
        uvmax = octane[c4d.SET_INFOCHAN_UVMAX] = float(data.GetReal(c4d.SET_INFOCHAN_UVMAX))
        uvmax = "UV max = " + str(uvmax)
        uvset = octane[c4d.SET_INFOCHAN_UVSET] = float(data.GetReal(c4d.SET_INFOCHAN_UVSET))
        uvset = "UV coord. selection = " + str(uvset)
        maxspeed = octane[c4d.SET_INFOCHAN_MAXSPEED] = float(data.GetReal(c4d.SET_INFOCHAN_MAXSPEED))
        maxspeed = "Max speed = " + str(maxspeed)
        bumpnormal = octane[c4d.SET_INFOCHAN_BUMPNORMAL] = bool(data.GetBool(c4d.SET_INFOCHAN_BUMPNORMAL))
        if bumpnormal == True:
            bumpnormal = "Bump and normal mapping = " + "Enabled"
        else:
            bumpnormal = "Bump and normal mapping = " + "Disabled"
        wirebacklight = octane[c4d.SET_INFOCHAN_WIREBACKLGHT] = bool(data.GetBool(c4d.SET_INFOCHAN_WIREBACKLGHT))
        if wirebacklight == True:
            wirebacklight = "Wireframe backaface highlighting = " + "Enabled"
        else:
            wirebacklight = "Wireframe backaface highlighting = " + "Disabled"
        alphachan = octane[c4d.SET_INFOCHAN_ALPHACHAN] = bool(data.GetBool(c4d.SET_INFOCHAN_ALPHACHAN))
        if alphachan == True:
            alphachan = "Alpha channel = " + "Enabled"
        else:
            alphachan = "Alpha channel = " + "Disabled"
        par_samples = octane[c4d.SET_INFOCHAN_PAR_SAMPLES] = float(data.GetReal(c4d.SET_INFOCHAN_PAR_SAMPLES))
        par_samples = "Parallel samples = " + str(par_samples) 
        maxtile_samp = octane[c4d.SET_INFOCHAN_MAXTILE_SAMP] = float(data.GetReal(c4d.SET_INFOCHAN_MAXTILE_SAMP))
        maxtile_samp = "Max tile samples = " + str(maxtile_samp)
        min_net_traffic = octane[c4d.SET_INFOCHAN_MIN_NET_TRAFFIC] = bool(data.GetBool(c4d.SET_INFOCHAN_MIN_NET_TRAFFIC))
        if min_net_traffic == True:
            min_net_traffic = "Min net traffic = " + "Enabled"
        else:
            min_net_traffic = "Min net traffic = " + "Disabled"
    
        c4d.EventAdd(1)

        octane_kernelsettings_list = [render_kernel, "", max_samples, info_type, ray_distr, ray_epsilon, Filter, AO_dist, AO_alphashd, opac_thresh, zdepthmax, uvmax, uvset, maxspeed, bumpnormal, wirebacklight, alphachan, par_samples, maxtile_samp, min_net_traffic]

    #Direct Lighting  
    if kernelLV == 1 :
        
        render_kernel = "Render Kernel: Direct Lighting"

        max_samples = octane[c4d.SET_DIRECT_MAXSAMPLES] = int(data.GetReal(c4d.SET_DIRECT_MAXSAMPLES))
        max_samples = "Max. Samples = " + str(max_samples)
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

        octane_kernelsettings_list = [render_kernel, "", ]
        
    #Path Tracing
    if kernelLV == 2 :

    	render_kernel = "Render Kernel: Path Tracing"

        max_samples = octane[c4d.SET_PATHTRACE_MAXSAMPLES] = int(data.GetReal(c4d.SET_PATHTRACE_MAXSAMPLES))
        max_samples = "Max. Samples = " + str(max_samples)
        diffuse_depth = octane[c4d.SET_PATHTRACE_DIFDEPTH] = int(data.GetReal(c4d.SET_PATHTRACE_DIFDEPTH))
        diffuse_depth = "Diffuse Depth = " + str(diffuse_depth)
        specular_depth = octane[c4d.SET_PATHTRACE_GLOSSYDEPTH] = int(data.GetReal(c4d.SET_PATHTRACE_GLOSSYDEPTH))
        specular_depth = "Specular Depth = " + str(specular_depth)
        ray_epsilon = octane[c4d.SET_PATHTRACE_RAYEPS] = float(data.GetReal(c4d.SET_PATHTRACE_RAYEPS))
        ray_epsilon = "Ray epsilon = " + str(ray_epsilon)
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

        octane_kernelsettings_list = [render_kernel, "", ]
    
    #PMC
    if kernelLV == 3 :
        
        render_kernel = "Render Kernel: PMC"

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
        
        c4d.CallCommand(1031195)
        c4d.EventAdd(1)

        octane_kernelsettings_list = [render_kernel, "", ]

    print octane_kernelsettings_list #for developing purposes

    octane_log_list = []

    for i in octane_kernelsettings_list:
        octane_log_list.append(i)

if __name__=='__main__':
    Octane_Log_Data()