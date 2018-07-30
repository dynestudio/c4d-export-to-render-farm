"""
Export to Render Farm_v07
Thanks for download - for commercial and all uses.

be.net/dyne
Writen by: Carlos Dordelly

Colleect your files and set more easily your render paths
Date: 11/11/2017
Written and tested in Cinema 4D R18 / R17 / R16 - Maybe works in older versions.

"""

import c4d
from c4d import gui

#global render engines ids
ARNOLD_RENDERER = 1029988
ARNOLD_RENDERER_COMMAND = 1039333
ARNOLD_DUMMYFORMAT = 1035823

REDSHIFT_RENDERER = 1036219
OCTANE_RENDERER = 1029525
PHYSICAL_RENDERER = 1023342
STANDARD_RENDERER = 0

#render data global ids
renderdata = doc.GetActiveRenderData()
rdata = renderdata.GetData()

#global ids
doc=c4d.documents.GetActiveDocument()
docname=doc.GetDocumentName()
docpath=doc.GetDocumentPath()
docfolder=docname[:-4]



# ---start render engines settings--- #



#arnold renderer
def GetArnoldRenderSettings():

    # find the active Arnold render settings
    videopost = renderdata.GetFirstVideoPost()
    while videopost:
        if videopost.GetType() == ARNOLD_RENDERER:
            return videopost;
        videopost = videopost.GetNext()
     
    # create a new one when does not exist
    if videopost is None:
        c4d.CallCommand(ARNOLD_RENDERER_COMMAND)
         
        videopost = rdata.GetFirstVideoPost()
        while videopost:
            if videopost.GetType() == ARNOLD_RENDERER:
                return videopost;
            videopost = videopost.GetNext()
             
    return None

def Arnold_Safety_Checks():
        # find the Arnold video post data   
        arnoldRenderSettings = GetArnoldRenderSettings()
        if arnoldRenderSettings is None:
            raise BaseException("Failed to find Arnold render settings")
         
        # setup the settings
        arnoldRenderSettings[c4d.C4DAI_OPTIONS_LOCK_SAMPLING_PATTERN] = True
        arnoldRenderSettings[c4d.C4DAI_OPTIONS_USE_TX_TEXTURES] = True
        arnoldRenderSettings[c4d.C4DAI_OPTIONS_AUTO_TX] = True
        arnoldRenderSettings[c4d.C4DAI_OPTIONS_DISPLAY_BUCKETS] = 0


def Arnold_Log_Data():
        # find the Arnold video post data   
        arnoldRenderSettings = GetArnoldRenderSettings()
        if arnoldRenderSettings is None:
            raise BaseException("Failed to find Arnold render settings")
        
        # settings to log
        AA_samples = "AA Samples = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_AA_SAMPLES])
        diffuse_samples = "Diffuse Samples = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_DIFFUSE_SAMPLES])
        specular_samples = "Specular Samples = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_SPECULAR_SAMPLES])
        transmission_samples = "Transmission Samples = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_TRANSMISSION_SAMPLES])
        sss_samples = "SSS Samples = "+ str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_SSS_SAMPLES])
        volume_indirect_samples = "Volume Indirect Samples = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_VOLUME_SAMPLES])

        sampling_pattern = arnoldRenderSettings[c4d.C4DAI_OPTIONS_LOCK_SAMPLING_PATTERN]
        if sampling_pattern == 1:
            sampling_pattern = True
        if not sampling_pattern == 1:
            sampling_pattern = False
        sampling_pattern = "Sampling Pattern = " + str(sampling_pattern)

        depth_total = "Total Depth = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_TOTAL_DEPTH])
        diffuse_depth = "Diffuse Depth = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_DIFFUSE_DEPTH])
        specular_depth = "Specular Depth = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_SPECULAR_DEPTH])
        transmission_depth = "Transmission Depth = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_TRANSMISSION_DEPTH])
        volume_depth = "Volume Depth = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_VOLUME_DEPTH])
        transparency_depth = "Transparency Depth = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_AUTO_TRANSPARENCY_DEPTH])

        #lists to log
        arnold_samples_list = ["C4DtoA Samplings:", "", AA_samples, diffuse_samples, specular_samples, transmission_samples, sss_samples, volume_indirect_samples, sampling_pattern, ""]
        arnold_depth_list = ["C4DtoA Ray Depth:", "", depth_total, diffuse_depth, specular_depth, transmission_depth, volume_depth, transparency_depth, ""]
        arnold_log_list = []

        for i in arnold_samples_list:
            arnold_log_list.append(i)

        for i in arnold_depth_list:
            arnold_log_list.append(i)

        return arnold_log_list

#redshift renderer
def GetRedshiftRenderSettings():

    # find the active Redshift render settings
    videopost = renderdata.GetFirstVideoPost()
    while videopost:
        if videopost.GetType() == REDSHIFT_RENDERER:
            return videopost;
        videopost = videopost.GetNext()
             
    return None

def Redshift_Safety_Checks():
        # find the Redshift video post data   
        redshiftRenderSettings = GetRedshiftRenderSettings()
        if redshiftRenderSettings is None:
            raise BaseException("Failed to find Redshift render settings")
         
        # setup the settings
        None


def Redshift_Log_Data():
        # find the Redshift video post data   
        redshiftRenderSettings = GetRedshiftRenderSettings()
        if redshiftRenderSettings is None:
            raise BaseException("Failed to find Redshift render settings")
        
        # settings to log
        None

        #lists to log
        redshift_samples_list = []
        redshift_depth_list = []
        redshift_log_list = []

        return redshift_log_list

#octane renderer
def GetOctaneRenderSettings():

    # find the active Octane render settings
    videopost = renderdata.GetFirstVideoPost()
    while videopost:
        if videopost.GetType() == OCTANE_RENDERER:
            return videopost;
        videopost = videopost.GetNext()
             
    return None

def Octane_Safety_Checks():
        # find the Octane video post data   
        octaneRenderSettings = GetOctaneRenderSettings()
        if octaneRenderSettings is None:
            raise BaseException("Failed to find Octane render settings")
         
        # setup the settings
        None


def Octane_Log_Data():
        # find the Octane video post data   
        octaneRenderSettings = GetOctaneRenderSettings()
        if octaneRenderSettings is None:
            raise BaseException("Failed to find Octane render settings")
        
        # settings to log
        None

        #lists to log
        octane_samples_list = []
        octane_depth_list = []
        octane_log_list = []

        return redshift_log_list

#physical renderer
def GetPhysicalRenderSettings():
	# find the active Physical render settings
    videopost = renderdata.GetFirstVideoPost()
    while videopost:
        if videopost.GetType() == PHYSICAL_RENDERER:
            return videopost;
        videopost = videopost.GetNext()
             
    return None

def Physical_Safety_Checks():
        # find the Physical video post data   
        physicalRenderSettings = GetPhysicalRenderSettings()
        if physicalRenderSettings is None:
            raise BaseException("Failed to find Physical render settings")
         
        # setup the settings
        physicalRenderSettings[c4d.VP_XMB_RAYTRACING_SAMPLER]=1
        physicalRenderSettings[c4d.VP_XMB_RAYTRACING_SAMPLES_SHADING_TRANS] = True
        renderdata[c4d.RDATA_AAFILTER] = 1

def Physical_Log_Data():
        # find the Physical video post data   
        physicalRenderSettings = GetPhysicalRenderSettings()
        if physicalRenderSettings is None:
            raise BaseException("Failed to find Physical render settings")

        # settings to log
        #basic settings
        sampler = physicalRenderSettings[c4d.VP_XMB_RAYTRACING_SAMPLER]
        if sampler == 1:
            sampler = "Adaptive"
        elif sampler == 0:
            sampler = "Fixed"
        sampler = "Sampler = "+sampler

        sampling_subdiv = "Sampling Subdivisions = " + str(int(physicalRenderSettings[c4d.VP_XMB_RAYTRACING_SAMPLES]))
        shading_subdiv_min = "Shading Subdivisions (Min) = " + str(int(physicalRenderSettings[c4d.VP_XMB_RAYTRACING_SAMPLES_SHADING_MIN]))
        shading_subdiv_max = "Shading Subdivisions (Max) = " + str(int(physicalRenderSettings[c4d.VP_XMB_RAYTRACING_SAMPLES_SHADING_MAX]))
        shading_error_threshold = "Shading Error Threshold = " + str(int(physicalRenderSettings[c4d.VP_XMB_RAYTRACING_SAMPLES_SHADING_ERROR]*100)) + "%"

        shading_transparency_check = physicalRenderSettings[c4d.VP_XMB_RAYTRACING_SAMPLES_SHADING_TRANS]
        if shading_transparency_check == 1:
            shading_transparency_check = True
        if not shading_transparency_check == 1:
            shading_transparency_check = False
        shading_transparency_check = "Shading Transparency Check = "+str(shading_transparency_check)

        blur_subdiv_max = "Blurriness Subdivision (Max) = " + str(int(physicalRenderSettings[c4d.VP_XMB_RAYTRACING_SAMPLES_BLURRY_SHADING]))
        shadow_subdiv_max = "Shadow Subdivision (Max) = " + str(int(physicalRenderSettings[c4d.VP_XMB_RAYTRACING_SAMPLES_BLURRY_LIGHT]))
        ao_subdiv_max = "Ambient Oclusion Subdivision (Max) = " + str(int(physicalRenderSettings[c4d.VP_XMB_RAYTRACING_SAMPLES_BLURRY_AO]))
        sss_subdiv_max = "Subsurface Scattering Subdivision (Max) = " + str(int(physicalRenderSettings[c4d.VP_XMB_RAYTRACING_SAMPLES_BLURRY_SSS]))

        #advanced settings
        raytracing_engine = physicalRenderSettings[c4d.VP_XMB_RAYTRACING_ADVANCED_ENGINE]
        if raytracing_engine == 0:
            raytracing_engine = "Physical"
        elif raytracing_engine == 1:
            raytracing_engine = "Embree (Faster)"
        elif raytracing_engine == 2:
            raytracing_engine = "Embree (Smaller)"
        raytracing_engine = "Raytracing Engine = "+raytracing_engine

        quick_preview = physicalRenderSettings[c4d.VP_XMB_RAYTRACING_ADVANCED_PREVIEW]
        if quick_preview == 0:
            quick_preview = "Never"
        elif quick_preview == 1:
            quick_preview = "Progressive Mode"
        elif quick_preview == 2:
            quick_preview = "All Modes"
        elif quick_preview == 3:
            quick_preview = "Preview Only"
        quick_preview = "Quick Preview = "+quick_preview

        debug_info_level = physicalRenderSettings[c4d.VP_XMB_RAYTRACING_ADVANCED_STATS]
        if debug_info_level == 0:
            debug_info_level = "None"
        elif debug_info_level == 1:
            debug_info_level = "Regular"
        elif debug_info_level == 2:
            debug_info_level = "Detailed"
        debug_info_level = "Debug Information Level = "+debug_info_level

        #AA (antialiasing) settings
        AA_filter = renderdata[c4d.RDATA_AAFILTER]
        if AA_filter == 0:
            AA_filter = "Cubic (Still Image)"
        elif AA_filter == 1:
            AA_filter = "Gauss (Animation)"
        elif AA_filter == 2:
            AA_filter = "Mitchell"
        elif AA_filter == 3:
            AA_filter = "Sinc"
        elif AA_filter == 4:
            AA_filter = "Box"
        elif AA_filter == 5:
            AA_filter = "Triangle"
        elif AA_filter == 6:
            AA_filter = "Catmull"
        elif AA_filter == 7:
            AA_filter = "PAL/NTSC"
        AA_filter = "Quick Preview = "+AA_filter

        mip_scale = "MIP Scale = " + str(int(renderdata[c4d.RDATA_AAMIPGLOBAL]*100)) + "%"

        #lists to log
        physical_basic_list = ["Physical Basic Settings:", "", sampler, sampling_subdiv, shading_subdiv_min, shading_subdiv_max, shading_error_threshold, shading_transparency_check, blur_subdiv_max, shadow_subdiv_max, ao_subdiv_max, sss_subdiv_max, ""]
        physical_AA_list = ["Anti-Aliasing:", "", AA_filter, mip_scale, ""]
        physical_advanced_list = ["Physical Advanced Settings:", "", raytracing_engine, quick_preview, debug_info_level, ""]
        physical_log_list = []

        for i in physical_basic_list:
            physical_log_list.append(i)

        for i in physical_advanced_list:
            physical_log_list.append(i)

        for i in physical_AA_list:
            physical_log_list.append(i)

        return physical_log_list

#standard renderer
def Standard_Safety_Checks():
        # setup the settings
        renderdata[c4d.RDATA_ANTIALIASING] = 2
        renderdata[c4d.RDATA_AAFILTER] = 1
        renderdata[c4d.RDATA_AAOBJECTPROPERTIES] = True
        renderdata[c4d.RDATA_AACONSIDERMULTIPASSES] = True
        renderdata[c4d.RDATA_OPTION_TRANSPARENCY] = True
        renderdata[c4d.RDATA_OPTION_REFRACTION] = True
        renderdata[c4d.RDATA_OPTION_REFLECTION] = True
        renderdata[c4d.RDATA_OPTION_SHADOW] = True
        renderdata[c4d.RDATA_NOISE_LOCK] = True
        renderdata[c4d.RDATA_AUTOLIGHT] = False
        c4d.EventAdd()

def Standard_Log_Data():
        # options to log
        transparency = renderdata[c4d.RDATA_OPTION_TRANSPARENCY]
        if transparency  == 1:
            transparency  = True
        if not transparency  == 1:
            transparency  = False
        transparency  = "Transparency = "+str(transparency)

        refraction = renderdata[c4d.RDATA_OPTION_REFRACTION]
        if refraction  == 1:
            refraction  = True
        if not refraction  == 1:
            refraction  = False
        refraction  = "Refraction = "+str(refraction)

        reflection = renderdata[c4d.RDATA_OPTION_REFLECTION]
        if reflection  == 1:
            reflection  = True
        if not reflection  == 1:
            reflection  = False
        reflection  = "Reflection = "+str(reflection)

        shadow = renderdata[c4d.RDATA_OPTION_SHADOW]
        if shadow  == 1:
            shadow  = True
        if not shadow  == 1:
            shadow  = False
        shadow  = "Shadow = "+str(shadow)

        ray_threshold = "Ray Threshold = " + str(int(renderdata[c4d.RDATA_THRESHOLD]*100)) + "%"
        ray_depth = "Ray Depth = " + str(renderdata[c4d.RDATA_RAYDEPTH])
        reflection_depth = "Reflection Depth = " + str(renderdata[c4d.RDATA_REFLECTIONDEPTH])
        shadow_depth = "Shadow Depth = " + str(renderdata[c4d.RDATA_SHADOWDEPTH])
        level_detail = "Level of Detail = " + str(int(renderdata[c4d.RDATA_LOD]*100)) + "%"

        #AA (antialiasing) settings
        anti_aliasing = renderdata[c4d.RDATA_ANTIALIASING]
        if anti_aliasing == 0:
            anti_aliasing = "None"
        elif anti_aliasing == 1:
            anti_aliasing = "Geometry"
        elif anti_aliasing == 2:
            anti_aliasing = "Best"
        anti_aliasing_log = "Anti-Aliasing Type = "+anti_aliasing

        AA_filter = renderdata[c4d.RDATA_AAFILTER]
        if AA_filter == 0:
            AA_filter = "Cubic (Still Image)"
        elif AA_filter == 1:
            AA_filter = "Gauss (Animation)"
        elif AA_filter == 2:
            AA_filter = "Mitchell"
        elif AA_filter == 3:
            AA_filter = "Sinc"
        elif AA_filter == 4:
            AA_filter = "Box"
        elif AA_filter == 5:
            AA_filter = "Triangle"
        elif AA_filter == 6:
            AA_filter = "Catmull"
        elif AA_filter == 7:
            AA_filter = "PAL/NTSC"
        AA_filter = "Quick Preview = "+AA_filter

        mip_scale = "MIP Scale = " + str(int(renderdata[c4d.RDATA_AAMIPGLOBAL]*100)) + "%"

        #lists to log
        standard_options_list = ["Standard Options:", "", transparency, refraction, reflection, shadow, ray_threshold, ray_depth, reflection_depth, shadow_depth, level_detail, ""]
        standard_AA_list = ["Anti-Aliasing:", "", AA_filter, mip_scale, anti_aliasing_log, ""]
        standard_log_list = []

        if anti_aliasing == "Best":
            AA_min_level = renderdata[c4d.RDATA_AAMINLEVEL]
            if AA_min_level == 0:
                AA_min_level = "Min Level = 1x1"
            elif AA_min_level == 1:
                AA_min_level = "Min Level = 2x2"
            elif AA_min_level == 2:
                AA_min_level = "Min Level = 4x4"
            elif AA_min_level == 3:
                AA_min_level = "Min Level = 8x8"
            elif AA_min_level == 4:
                AA_min_level = "Min Level = 16x16"

            AA_max_level = renderdata[c4d.RDATA_AAMAXLEVEL]
            if AA_max_level == 0:
                AA_max_level = "Max Level = 1x1"
            elif AA_max_level == 1:
                AA_max_level = "Max Level 2x2"
            elif AA_max_level == 2:
                AA_max_level = "Max Level 4x4"
            elif AA_max_level == 3:
                AA_max_level = "Max Level 8x8"
            elif AA_max_level == 4:
                AA_max_level = "Max Level 16x16"

            AA_threshold = "AA Threshold = " + str(int(renderdata[c4d.RDATA_AATHRESHOLD]*100)) + "%"

            AA_best_list = [AA_min_level, AA_max_level, AA_threshold]

        if not anti_aliasing == "Best":
            None

        for i in standard_options_list:
            standard_log_list.append(i)

        if anti_aliasing == "Best":
            for i in AA_best_list:
                standard_AA_list.append(i)
                    
        if not anti_aliasing == "Best":
            None

        for i in standard_AA_list:
            standard_log_list.append(i)

        return standard_log_list



# ---end render engines settings--- #



def get_output_data_format():
    # options to log
    size_unit = renderdata[c4d.RDATA_SIZEUNIT]
    if size_unit == 0:
        size_unit = "Pixels"
    elif size_unit == 1:
        size_unit = "cm"
    elif size_unit == 2:
        size_unit = "mm"
    elif size_unit == 3:
        size_unit = "Inches"
    elif size_unit == 4:
        size_unit = "Points"
    elif size_unit == 5:
        size_unit = "Picas"
    size_unit_log = "Size Unit = "+size_unit

    render_width = "Render Widh: "+str(int(renderdata[c4d.RDATA_XRES_VIRTUAL]))+" "+size_unit
    render_height = "Render Height: "+str(int(renderdata[c4d.RDATA_YRES_VIRTUAL]))+" "+size_unit
    resolution = "Render Resolution: "+str(int(renderdata[c4d.RDATA_PIXELRESOLUTION_VIRTUAL]))+"dpi"
    frame_rate = "Frame Rate: "+str(int(renderdata[c4d.RDATA_FRAMERATE]))

    render_region = renderdata[c4d.RDATA_RENDERREGION]
    if render_region == False:
        render_region = "Render Region: Disabled"
    elif render_region == True:
        render_region = "Render Region: Enabled"
        left_border = "Render Region - Left Border: "+str(int(renderdata[c4d.RDATA_RENDERREGION_LEFT]))
        top_border = "Render Region - Top Border: "+str(int(renderdata[c4d.RDATA_RENDERREGION_TOP]))
        right_border = "Render Region - Right Border: "+str(int(renderdata[c4d.RDATA_RENDERREGION_RIGHT]))
        bottom_border = "Render Region - Bottom Border: "+str(int(renderdata[c4d.RDATA_RENDERREGION_BOTTOM]))
        render_region_list = [left_border, top_border, right_border, bottom_border]

    output_data_list = [render_width, render_height, size_unit_log, resolution, frame_rate, render_region]

    if render_region == "Render Region: Enabled":
        for i in render_region_list:
            output_data_list.append(i)
    if not render_region == "Render Region: Enabled":
        None

    return output_data_list

def active_render_engine_string():
    render_engine = rdata[c4d.RDATA_RENDERENGINE]
    if render_engine == ARNOLD_RENDERER:
        render_engine = "Arnold Renderer"
    elif render_engine == REDSHIFT_RENDERER:    
        render_engine = "Redshift Renderer"
    elif render_engine == OCTANE_RENDERER:
        render_engine = "Octane Renderer"
    elif render_engine == PHYSICAL_RENDERER:
        render_engine = "Physical Renderer"
    elif render_engine == STANDARD_RENDERER:
        render_engine = "Standard Renderer"
    else:
        render_engine = rdata[c4d.RDATA_RENDERENGINE]

    return render_engine

def get_frames():    
    #Get Frames info
    if rdata[c4d.RDATA_FRAMESEQUENCE] == c4d.RDATA_FRAMESEQUENCE_ALLFRAMES:
        framefrom = doc[c4d.DOCUMENT_MINTIME].GetFrame(doc.GetFps())
        frameto = doc[c4d.DOCUMENT_MAXTIME].GetFrame(doc.GetFps())
    elif rdata[c4d.RDATA_FRAMESEQUENCE] == c4d.RDATA_FRAMESEQUENCE_CURRENTFRAME:
        framefrom = doc[c4d.DOCUMENT_TIME].GetFrame(doc.GetFps())
        frameto = framefrom
    elif rdata[c4d.RDATA_FRAMESEQUENCE] == c4d.RDATA_FRAMESEQUENCE_PREVIEWRANGE:
        framefrom = doc[c4d.DOCUMENT_LOOPMINTIME].GetFrame(doc.GetFps())
        frameto = doc[c4d.DOCUMENT_LOOPMAXTIME].GetFrame(doc.GetFps())
    else:
        framefrom = rdata[c4d.RDATA_FRAMEFROM].GetFrame(doc.GetFps())
        frameto = rdata[c4d.RDATA_FRAMETO].GetFrame(doc.GetFps())
    
    return str(framefrom)+"-"+str(frameto)

def write_txt(n_docpath, n_docname, n_docfolder, render_log, output_data_format):

    frames=get_frames()
    fileformat=".txt"

    txtfilename=n_docpath+"/"+n_docfolder+"_frames to render_"+frames+fileformat
    print "Collected log saved in " + txtfilename

    f=open(txtfilename,"w")
    f.write(n_docname+" "+"Frames to render:"+frames)
    f.write("\n")
    f.write("\n")
    f.write("Project Name: "+n_docname[:-4])
    f.write("\n")
    f.write("\n")
    output_data_format = str('\n'.join(output_data_format))
    f.write(output_data_format)
    f.write("\n")
    f.write("\n")
    f.write("Render Engine: "+active_render_engine_string()+" ")
    f.write("\n")
    f.write("\n")
    render_log = str('\n'.join(render_log))
    f.write(render_log)
    f.close()

def export_to_renderfarm():

    #Collect start
    save=c4d.CallCommand(12098) # Save

    #function variables
    container = renderdata.GetData()
    render_engine = active_render_engine_string()
    print render_engine+" detected"
    render_engine = rdata[c4d.RDATA_RENDERENGINE]

    #Render setting collect name
    renderdata[c4d.ID_BASELIST_NAME]= "_"+docfolder+"_To Render Farm"

    #Output Render File Formats
    #Beauty
    if render_engine == ARNOLD_RENDERER:
        BeautyFormat = ARNOLD_DUMMYFORMAT #ArnoldDummy Format
    if not render_engine == ARNOLD_RENDERER:
        BeautyFormat = c4d.FILTER_JPG #Beauty reference in JPG format
    #MultiPass
    MPFormat=c4d.FILTER_EXR
    
    container[c4d.RDATA_FORMAT] = BeautyFormat
    container[c4d.RDATA_ALPHACHANNEL]=False
    
    container[c4d.RDATA_MULTIPASS_SAVEFORMAT] = MPFormat
    saveOptions = container.GetContainerInstance(c4d.RDATA_MULTIPASS_SAVEOPTIONS)

    # OpenEXR Compression options
    bc = c4d.BaseContainer()
    bc[0] = 3 # ZIP
    bc[1] = True # clamp to half float
    
    # save OpenEXR options & continer data
    saveOptions.SetContainer(0,bc)
    renderdata.SetData(container)

    #set render paths
    renderdata[c4d.RDATA_PATH] = "./$prj/$prj_Beauty" #Beauty export is not necessary with some 3rd party renders just like C4DtoA
    renderdata[c4d.RDATA_MULTIPASS_FILENAME] = "./$prj/$prj_MP" #MP = Multipass
    
    #Safety checks settings in render engine
    if render_engine == ARNOLD_RENDERER:
        Arnold_Safety_Checks()
    elif render_engine == REDSHIFT_RENDERER:
        Redshift_Safety_Checks()
    elif render_engine == OCTANE_RENDERER:
        Octane_Safety_Checks()
    elif render_engine == PHYSICAL_RENDERER:
        Physical_Safety_Checks()
    else:
        Standard_Safety_Checks()

    #Update the scene
    c4d.EventAdd()

    #Collect New File
    c4d.CallCommand(12255, 12255) # Save Project with Assets...
    
    #Write codument with log information
    #New documents IDs
    n_docpath=doc.GetDocumentPath()
    n_docname=doc.GetDocumentName()
    n_docfolder=n_docname[:-4]

    #output data format and resolution to log
    output_data_format = get_output_data_format()

    #render log from render engine
    if render_engine == ARNOLD_RENDERER:
        render_log = Arnold_Log_Data()
    elif render_engine == REDSHIFT_RENDERER:
        render_log = Redshift_Log_Data()
    elif render_engine == OCTANE_RENDERER:
        render_log = Octane_Log_Data()
    elif render_engine == PHYSICAL_RENDERER:
        render_log = Physical_Log_Data()
    else:
        render_log = Standard_Log_Data()

    write_txt(n_docpath, n_docname, n_docfolder, render_log, output_data_format)
    print "Collected file: "+n_docname

    #Close the collected file
    c4d.CallCommand(12664, 12664) # Close collected project
    c4d.CallCommand(52000, 2) # Recent Files
    
    #Collect finish dialog
    print "Successfully Exported! Happy Rendering ;)"
    gui.MessageDialog("Successfully Exported!\nSee the console and log for more details.")


if __name__=='__main__':
    export_to_renderfarm()