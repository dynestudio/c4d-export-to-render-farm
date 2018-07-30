"""
Export to Render Farm - C4D script 0.9 wip 03
Thanks for download - for commercial and personal uses.
Export to Render Farm granted shall not be copied, distributed, or-sold, offered for resale, transferred in whole or in part except that you may make one copy for archive purposes only.

http://dyne.studio/
Writen by: Carlos Dordelly
Special thanks: Pancho Contreras, Terry Williams & Roberto Gonzalez.

Export to Render Farm provides a alternative way to collect a c4d file with additional features.
Date: 08/12/2017
Written and tested in Cinema 4D R18 / R17 / R16 - Not tested in older versions.

Export to Render Farm belongs to Dyne Tools (group of digital tools from dyne).

"""

import c4d
from c4d import gui

#global render engines ids
ARNOLD_RENDERER = 1029988
ARNOLD_RENDERER_COMMAND = 1039333
ARNOLD_DUMMYFORMAT = 1035823
ARNOLD_DRIVER = 1030141

REDSHIFT_RENDERER = 1036219
OCTANE_RENDERER = 1029525
PHYSICAL_RENDERER = 1023342
STANDARD_RENDERER = 0

#render data global ids
renderdata = doc.GetActiveRenderData()
rdata = renderdata.GetData()
Beauty_path = "./$prj/$prj_Beauty"
MP_path = "./$prj/$prj_MP"

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
        else:
            sampling_pattern = False
        sampling_pattern = "Sampling Pattern = " + str(sampling_pattern)

        depth_total = "Total Depth = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_TOTAL_DEPTH])
        diffuse_depth = "Diffuse Depth = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_DIFFUSE_DEPTH])
        specular_depth = "Specular Depth = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_SPECULAR_DEPTH])
        transmission_depth = "Transmission Depth = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_TRANSMISSION_DEPTH])
        volume_depth = "Volume Depth = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_GI_VOLUME_DEPTH])
        transparency_depth = "Transparency Depth = " + str(arnoldRenderSettings[c4d.C4DAIP_OPTIONS_AUTO_TRANSPARENCY_DEPTH])

        #drivers to log
        #scene objects list
        objectsList = doc.GetObjects()

        driver_list = []

        for obj in objectsList:
            obj_type = obj.GetType()
            if obj_type == ARNOLD_DRIVER:
                  driver_name = obj[c4d.ID_BASELIST_NAME]
                  driver_name = "Driver: " + driver_name
                  driver_list.append("\n")
                  driver_list.append(driver_name)
                  driver_AOVs = obj.GetChildren()

                  for aov in driver_AOVs:
                    AOV_name = aov[c4d.ID_BASELIST_NAME]
                    AOV_name = "AOV: " + AOV_name
                    driver_list.append(AOV_name)
            else:
                  None
        if len(driver_list) == 0:
            driver_list.append("\n")
            driver_empty = "There aren't any driver in this project."
            driver_list.append(driver_empty)

        #lists to log
        arnold_samples_list = ["C4DtoA Samplings:", "", AA_samples, diffuse_samples, specular_samples, transmission_samples, sss_samples, volume_indirect_samples, sampling_pattern, ""]
        arnold_depth_list = ["C4DtoA Ray Depth:", "", depth_total, diffuse_depth, specular_depth, transmission_depth, volume_depth, transparency_depth, ""]
        arnold_driver_list = ["Arnold Drivers:"]
        arnold_log_list = []

        for i in arnold_samples_list:
            arnold_log_list.append(i)

        for i in arnold_depth_list:
            arnold_log_list.append(i)

        for i in driver_list:
            arnold_driver_list.append(i)

        for i in arnold_driver_list:
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
        redshiftRenderSettings[c4d.REDSHIFT_RENDERER_UNIFIED_DEBUG_DRAW_SAMPLES] = False
        redshiftRenderSettings[c4d.REDSHIFT_RENDERER_UNIFIED_RANDOMIZE_PATTERN] = False
        redshiftRenderSettings[c4d.REDSHIFT_RENDERER_AOV_FIX_RAW_HALO_ARTIFACTS] = True
        redshiftRenderSettings[c4d.REDSHIFT_RENDERER_CONSERVE_GI_REFLECTION_ENERGY] = True
        redshiftRenderSettings[c4d.REDSHIFT_RENDERER_AUTOMATIC_MEMORY_MANAGEMENT] = True
        redshiftRenderSettings[c4d.REDSHIFT_RENDERER_INTEGRATION_OPTIONS_DEFAULT_LIGHT] = False

def Redshift_Log_Data():
        # find the Redshift video post data   
        redshiftRenderSettings = GetRedshiftRenderSettings()
        if redshiftRenderSettings is None:
            raise BaseException("Failed to find Redshift render settings")
        
        # settings to log
        #unifed sampling
        samples_min = "Samples Min = " + str(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_UNIFIED_MIN_SAMPLES])
        samples_max = "Samples Max = " + str(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_UNIFIED_MAX_SAMPLES])
        adaptive_error_threshold = "Adaptive Error Threshold = " + str(round(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_UNIFIED_ADAPTIVE_ERROR_THRESHOLD],4))
        
        randomize_pattern = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_UNIFIED_RANDOMIZE_PATTERN]
        if randomize_pattern == 1:
            randomize_pattern = True
        else:
            randomize_pattern == False
        randomize_pattern = "Randomize Pattern Every Frame = " + str(randomize_pattern)

        #sampling overrides
        #override reflection
        override_samples_reflection = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_REFLECT_SAMPLES_ENABLED]
        if override_samples_reflection == False:
            override_samples_reflection = "Override Reflection: Disabled"
        else:
            override_samples_reflection = "Override Reflection: Enabled"

            override_samples_reflection_mode = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_REFLECT_SAMPLES_MODE]
            if override_samples_reflection_mode == 0:
                override_samples_reflection_mode = "Mode: Replace"
                override_samples_reflection_samples = "Override Samples = " + str(int(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_REFLECT_SAMPLES_COUNT]))
                override_samples_reflection_list = [override_samples_reflection_mode, override_samples_reflection_samples, ""]
            else:
                override_samples_reflection_mode = "Mode: Scale"
                override_samples_reflection_samples = "Override Scale = " + str(int(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_REFLECT_SAMPLES_SCALE]))
                override_samples_reflection_list = [override_samples_reflection_mode, override_samples_reflection_samples, ""]

            override_samples_reflection_mode = "Override Samples Reflection Mode: " + override_samples_reflection_mode

        override_samples_reflection_mode_list = [override_samples_reflection]
        override_samples_reflection_mode_list_space = [""]

        if override_samples_reflection == "Override Reflection: Enabled":
            for i in override_samples_reflection_list:
                override_samples_reflection_mode_list.append(i)
        else:
            for i in override_samples_reflection_mode_list_space:
                override_samples_reflection_mode_list.append(i)

        #override refraction
        override_samples_refraction = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_REFRACT_SAMPLES_ENABLED]
        if override_samples_refraction == False:
            override_samples_refraction = "Override Refraction: Disabled"
        else:
            override_samples_refraction = "Override Refraction: Enabled"

            override_samples_refraction_mode = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_REFRACT_SAMPLES_MODE]
            if override_samples_refraction_mode == 0:
                override_samples_refraction_mode = "Mode: Replace"
                override_samples_refraction_samples = "Override Samples = " + str(int(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_REFRACT_SAMPLES_COUNT]))
                override_samples_refraction_list = [override_samples_refraction_mode, override_samples_refraction_samples, ""]
            else:
                override_samples_refraction_mode = "Mode: Scale"
                override_samples_refraction_samples = "Override Scale = " + str(int(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_REFRACT_SAMPLES_SCALE]))
                override_samples_refraction_list = [override_samples_refraction_mode, override_samples_refraction_samples, ""]

            override_samples_refraction_mode = "Override Samples Refraction Mode: " + override_samples_refraction_mode

        override_samples_refraction_mode_list = [override_samples_refraction]
        override_samples_refraction_mode_list_space = [""]

        if override_samples_refraction == "Override Refraction: Enabled":
            for i in override_samples_refraction_list:
                override_samples_refraction_mode_list.append(i)
        else:
            for i in override_samples_refraction_mode_list_space:
                override_samples_refraction_mode_list.append(i)

        #override AO
        override_samples_AO = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_AO_SAMPLES_ENABLED]
        if override_samples_AO == False:
            override_samples_AO = "Override AO: Disabled"
        else:
            override_samples_AO = "Override AO: Enabled"

            override_samples_AO_mode = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_AO_SAMPLES_MODE]
            if override_samples_AO_mode == 0:
                override_samples_AO_mode = "Mode: Replace"
                override_samples_AO_samples = "Override Samples = " + str(int(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_AO_SAMPLES_COUNT]))
                override_samples_AO_list = [override_samples_AO_mode, override_samples_AO_samples, ""]
            else:
                override_samples_AO_mode = "Mode: Scale"
                override_samples_AO_samples = "Override Scale = " + str(int(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_AO_SAMPLES_SCALE]))
                override_samples_AO_list = [override_samples_AO_mode, override_samples_AO_samples, ""]

            override_samples_AO_mode = "Override Samples AO Mode: " + override_samples_AO_mode

        override_samples_AO_mode_list = [override_samples_AO]
        override_samples_AO_mode_list_space = [""]

        if override_samples_AO == "Override AO: Enabled":
            for i in override_samples_AO_list:
                override_samples_AO_mode_list.append(i)
        else:
            for i in override_samples_AO_mode_list_space:
                override_samples_AO_mode_list.append(i)

        #override light
        override_samples_light = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_LIGHT_SAMPLES_ENABLED]
        if override_samples_light == False:
            override_samples_light = "Override Light: Disabled"
        else:
            override_samples_light = "Override Light: Enabled"

            override_samples_light_mode = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_LIGHT_SAMPLES_MODE]
            if override_samples_light_mode == 0:
                override_samples_light_mode = "Mode: Replace"
                override_samples_light_samples = "Override Samples = " + str(int(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_LIGHT_SAMPLES_COUNT]))
                override_samples_light_list = [override_samples_light_mode, override_samples_light_samples, ""]
            else:
                override_samples_light_mode = "Mode: Scale"
                override_samples_light_samples = "Override Scale = " + str(int(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_LIGHT_SAMPLES_SCALE]))
                override_samples_light_list = [override_samples_light_mode, override_samples_light_samples, ""]

            override_samples_light_mode = "Override Samples Light Mode: " + override_samples_light_mode

        override_samples_light_mode_list = [override_samples_light]
        override_samples_light_mode_list_space = [""]

        if override_samples_light == "Override Light: Enabled":
            for i in override_samples_light_list:
                override_samples_light_mode_list.append(i)
        else:
            for i in override_samples_light_mode_list_space:
                override_samples_light_mode_list.append(i)

        #override volume
        override_samples_volume = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_VOLUME_SAMPLES_ENABLED]
        if override_samples_volume == False:
            override_samples_volume = "Override Volume: Disabled"
        else:
            override_samples_volume = "Override Volume: Enabled"

            override_samples_volume_mode = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_VOLUME_SAMPLES_MODE]
            if override_samples_volume_mode == 0:
                override_samples_volume_mode = "Mode: Replace"
                override_samples_volume_samples = "Override Samples = " + str(int(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_VOLUME_SAMPLES_COUNT]))
                override_samples_volume_list = [override_samples_volume_mode, override_samples_volume_samples, ""]
            else:
                override_samples_volume_mode = "Mode: Scale"
                override_samples_volume_samples = "Override Scale = " + str(int(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_VOLUME_SAMPLES_SCALE]))
                override_samples_volume_list = [override_samples_volume_mode, override_samples_volume_samples, ""]

            override_samples_volume_mode = "Override Samples Volume Mode: " + override_samples_volume_mode

        override_samples_volume_mode_list = [override_samples_volume]
        override_samples_volume_mode_list_space = [""]

        if override_samples_volume == "Override Volume: Enabled":
            for i in override_samples_volume_list:
                override_samples_volume_mode_list.append(i)
        else:
            for i in override_samples_volume_mode_list_space:
                override_samples_volume_mode_list.append(i)

        #override single scattering
        override_samples_single_scatter = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_SINGLE_SCATTERING_SAMPLES_ENABLED]
        if override_samples_single_scatter == False:
            override_samples_single_scatter = "Override Single Scattering: Disabled"
        else:
            override_samples_single_scatter = "Override Single Scattering: Enabled"

            override_samples_single_scatter_mode = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_SINGLE_SCATTERING_SAMPLES_MODE]
            if override_samples_single_scatter_mode == 0:
                override_samples_single_scatter_mode = "Mode: Replace"
                override_samples_single_scatter_samples = "Override Samples = " + str(int(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_SINGLE_SCATTERING_SAMPLES_COUNT]))
                override_samples_single_scatter_list = [override_samples_single_scatter_mode, override_samples_single_scatter_samples, ""]
            else:
                override_samples_single_scatter_mode = "Mode: Scale"
                override_samples_single_scatter_samples = "Override Scale = " + str(int(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_SINGLE_SCATTERING_SAMPLES_SCALE]))
                override_samples_single_scatter_list = [override_samples_single_scatter_mode, override_samples_single_scatter_samples, ""]

            override_samples_single_scatter_mode = "Override Samples Single Scattering Mode: " + override_samples_single_scatter_mode

        override_samples_single_scatter_mode_list = [override_samples_single_scatter]
        override_samples_single_scatter_mode_list_space = [""]

        if override_samples_single_scatter == "Override Single Scattering: Enabled":
            for i in override_samples_single_scatter_list:
                override_samples_single_scatter_mode_list.append(i)
        else:
            for i in override_samples_single_scatter_mode_list_space:
                override_samples_single_scatter_mode_list.append(i)

        #GI
        primary_engine = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_PRIMARY_GI_ENGINE]
        if primary_engine == 0:
            primary_engine = "None"
        elif primary_engine == 1:
            primary_engine = "Photon Map"
        elif primary_engine == 2:
            primary_engine = "None"
        elif primary_engine == 3:
            primary_engine = "Irradiance Cache"
        elif primary_engine == 4:
            primary_engine = "Brute Force"
        primary_engine = "Primary GI Engine: " + primary_engine

        secondary_engine = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_SECONDARY_GI_ENGINE]
        if secondary_engine == 0:
            secondary_engine = "None"
        elif secondary_engine == 1:
            secondary_engine = "Photon Map"
        elif secondary_engine == 2:
            secondary_engine = "Irradiance Point Cloud"
        elif secondary_engine == 3:
            secondary_engine = "None"
        elif secondary_engine == 4:
            secondary_engine = "Brute Force"
        secondary_engine = "Secondary GI Engine: " + secondary_engine

        GI_bounces = "Number of GI Bounces = " + str(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_NUM_GI_BOUNCES])

        GI_reflect_energy = redshiftRenderSettings[c4d.REDSHIFT_RENDERER_CONSERVE_GI_REFLECTION_ENERGY]
        if GI_reflect_energy == False:
            GI_reflect_energy = "Disabled"
        else:
            GI_reflect_energy = "Enabled"
        GI_reflect_energy = "Converse Reflections Energy: " + GI_reflect_energy

        GI_rays = "Brute Force GI - Number of Rays = " + str(redshiftRenderSettings[c4d.REDSHIFT_RENDERER_BRUTE_FORCE_GI_NUM_RAYS])

        #lists to log
        redshift_samples_list = ["Unifed Samplings:", "", samples_min, samples_max, adaptive_error_threshold, randomize_pattern, ""]
        redshift_override_list = ["Samplings Overrides:", ""]
        redshift_engine_list = ["GI Engines:", "", primary_engine, secondary_engine, GI_bounces, GI_reflect_energy, GI_rays, ""]
        redshift_log_list = []

        for i in redshift_samples_list:
            redshift_log_list.append(i)

        #overrides start
        for i in override_samples_reflection_mode_list:
            redshift_override_list.append(i)

        for i in override_samples_refraction_mode_list:
            redshift_override_list.append(i)

        for i in override_samples_AO_mode_list:
            redshift_override_list.append(i)

        for i in override_samples_light_mode_list:
            redshift_override_list.append(i)

        for i in override_samples_volume_mode_list:
            redshift_override_list.append(i)

        for i in override_samples_single_scatter_mode_list:
            redshift_override_list.append(i)
        #override ends

        for i in redshift_override_list:
            redshift_log_list.append(i)

        for i in redshift_engine_list:
            redshift_log_list.append(i)

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
        octaneRenderSettings[c4d.SET_PASSES_ENABLED] = True
        octaneRenderSettings[c4d.SET_PASSES_SAVEPATH] = MP_path
        Pxr24 = 5 #pixar EXR compression
        octaneRenderSettings[c4d.SET_PASSES_EXR_COMPR] = Pxr24
        octaneRenderSettings[c4d.SET_PASSES_SHOWPASSES] = True
        octaneRenderSettings[c4d.SET_PASSES_SAVE_MAINPASS] = True
        octaneRenderSettings[c4d.SET_PASSES_MULTILAYER] = True
        octaneRenderSettings[c4d.SET_PASSES_IMAGECOLORPROFILE] = 1
        octaneRenderSettings[c4d.SET_PASSES_TONEMAPTYPE] = 1

def Octane_Log_Data():
        # find the Octane video post data   
        octaneRenderSettings = GetOctaneRenderSettings()
        if octaneRenderSettings is None:
            raise BaseException("Failed to find Octane render settings")
        
        # settings to log
        temp_log = "Octane does not support log yet."
        None

        #lists to log
        octane_samples_list = []
        octane_depth_list = []
        octane_log_list = [temp_log]

        return octane_log_list

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
        else:
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

def Standard_Log_Data():
        # options to log
        transparency = renderdata[c4d.RDATA_OPTION_TRANSPARENCY]
        if transparency  == 1:
            transparency  = True
        else:
            transparency  = False
        transparency  = "Transparency = "+str(transparency)

        refraction = renderdata[c4d.RDATA_OPTION_REFRACTION]
        if refraction  == 1:
            refraction  = True
        else:
            refraction  = False
        refraction  = "Refraction = "+str(refraction)

        reflection = renderdata[c4d.RDATA_OPTION_REFLECTION]
        if reflection  == 1:
            reflection  = True
        else:
            reflection  = False
        reflection  = "Reflection = "+str(reflection)

        shadow = renderdata[c4d.RDATA_OPTION_SHADOW]
        if shadow  == 1:
            shadow  = True
        else:
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
        else:
            None

        for i in standard_options_list:
            standard_log_list.append(i)

        if anti_aliasing == "Best":
            for i in AA_best_list:
                standard_AA_list.append(i)        
        else:
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
    else:
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
    else:
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

    txtfilename=n_docpath+"/"+n_docfolder+"_Frames to Render "+frames+"_(Log file)"+fileformat
    print "Collected log saved in " + txtfilename

    f=open(txtfilename,"w")
    f.write(n_docname+" "+"- Frames to render: "+frames+"\n\n")
    f.write("Project Name: "+n_docname[:-4]+"\n\n")
    output_data_format = str('\n'.join(output_data_format))
    f.write(output_data_format+"\n\n")
    f.write("Render Engine: "+active_render_engine_string()+"\n\n")
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
    elif render_engine == REDSHIFT_RENDERER:
        BeautyFormat = ARNOLD_DUMMYFORMAT #ArnoldDummy Format
    else:
        BeautyFormat = c4d.FILTER_JPG #Beauty reference in JPG format
    #MultiPass
    MPFormat=c4d.FILTER_EXR
    
    container[c4d.RDATA_FORMAT] = BeautyFormat

    if render_engine == ARNOLD_RENDERER:
        container[c4d.RDATA_ALPHACHANNEL]=False
    else:
        container[c4d.RDATA_ALPHACHANNEL] = True
    
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
    renderdata[c4d.RDATA_PATH] = Beauty_path #beauty export is not necessary with some 3rd party renders just like C4DtoA

    if render_engine == OCTANE_RENDERER:
        renderdata[c4d.RDATA_MULTIPASS_FILENAME] = ""
        renderdata[c4d.RDATA_MULTIPASS_SAVEIMAGE] = False
    else:
        renderdata[c4d.RDATA_MULTIPASS_SAVEIMAGE] = True
        renderdata[c4d.RDATA_MULTIPASS_FILENAME] = MP_path #MP = Multipass
    
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

    #open question dialog
    string_open_collect = "Do you want to open the collected file?"
    open_collect_question = c4d.gui.QuestionDialog(string_open_collect)

    if open_collect_question == True:
        None
    else:
        #Close the collected file
        c4d.CallCommand(12664, 12664) # Close collected project
        c4d.CallCommand(52000, 2) # Recent Files
    
    #Collect finish dialog
    print "Successfully Exported! Happy Rendering ;)"
    gui.MessageDialog("Successfully Exported!\nSee the console and log for more details.")


if __name__=='__main__':
    export_to_renderfarm()