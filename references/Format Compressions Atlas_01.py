#C4D format compressions atlas.

OPENEXR - rdata[c4d.RDATA_SAVEOPTIONS][0] is a BaseContainer containing the OpenEXR options
    None
    rdata[c4d.RDATA_SAVEOPTIONS][0][0] =  0
    rdata[c4d.RDATA_SAVEOPTIONS][0][1] =  0

    Run length encoding
    rdata[c4d.RDATA_SAVEOPTIONS][0][0] =  1
    rdata[c4d.RDATA_SAVEOPTIONS][0][1] =  0

    Zip, one scan line at a time
    rdata[c4d.RDATA_SAVEOPTIONS][0][0] =  2
    rdata[c4d.RDATA_SAVEOPTIONS][0][1] =  0

    Zip, in blocks of 16 scan lines 
    rdata[c4d.RDATA_SAVEOPTIONS][0][0] =  3
    rdata[c4d.RDATA_SAVEOPTIONS][0][1] =  0
     
    Piz-based wavelet
    rdata[c4d.RDATA_SAVEOPTIONS][0][0] =  4
    rdata[c4d.RDATA_SAVEOPTIONS][0][1] =  0

    Lossy 24-bit float, Zip 
    rdata[c4d.RDATA_SAVEOPTIONS][0][0] =  5
    rdata[c4d.RDATA_SAVEOPTIONS][0][1] =  0
     
    Lossy 16-bit float, 4-by-4 pixel [B44]
    rdata[c4d.RDATA_SAVEOPTIONS][0][0] =  6
    rdata[c4d.RDATA_SAVEOPTIONS][0][1] =  1
     
    Lossy 16-bit float, 4-by-4 pixel (flat fields) [B44A]
    rdata[c4d.RDATA_SAVEOPTIONS][0][0] =  7
    rdata[c4d.RDATA_SAVEOPTIONS][0][1] =  1
     
    Lossy 16-bit float, Run length encoding
    rdata[c4d.RDATA_SAVEOPTIONS][0][0] =  1
    rdata[c4d.RDATA_SAVEOPTIONS][0][1] =  1
     
    Lossy 16-bit float, Zip, one scan line at a time
    rdata[c4d.RDATA_SAVEOPTIONS][0][0] =  2
    rdata[c4d.RDATA_SAVEOPTIONS][0][1] =  1
     
    Lossy 16-bit float, Zip, in blocks of 16 scan lines 
    rdata[c4d.RDATA_SAVEOPTIONS][0][0] =  3
    rdata[c4d.RDATA_SAVEOPTIONS][0][1] =  1
     
    Lossy 16-bit float, Piz-based wavelet
    rdata[c4d.RDATA_SAVEOPTIONS][0][0] =  4
    rdata[c4d.RDATA_SAVEOPTIONS][0][1] =  1

PNG
    Not interlaced/interlaced
    rdata[c4d.RDATA_SAVEOPTIONS][PNG_INTERLACED] = 0 (not interlaced)
    rdata[c4d.RDATA_SAVEOPTIONS][PNG_INTERLACED] = 1 (interlaced)
    
JPG
    compression percentage
    rdata[c4d.RDATA_SAVEOPTIONS][JPGSAVER_QUALITY] = percentage value

DPX
    planar
    rdata[c4d.RDATA_SAVEOPTIONS][DPX_PLANAR] = 0 (disabled)
    rdata[c4d.RDATA_SAVEOPTIONS][DPX_PLANAR] = 1 (enabled)

RLA 
    Z
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_Z) == c4d.RLAFLAGS_Z (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_Z) != c4d.RLAFLAGS_Z (disabled)

    Object
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_OBJECTBUFFER) == c4d.RLAFLAGS_OBJECTBUFFER (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_OBJECTBUFFER) != c4d.RLAFLAGS_OBJECTBUFFER (disabled)

    UV Coordinates
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_UV) == c4d.RLAFLAGS_UV (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_UV) != c4d.RLAFLAGS_UV (disabled)

    Normal
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_NORMAL) == c4d.RLAFLAGS_NORMAL (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_NORMAL) != c4d.RLAFLAGS_NORMAL (disabled)

    Non-clamped color
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_ORIGCOLOR) == c4d.RLAFLAGS_ORIGCOLOR (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_ORIGCOLOR) != c4d.RLAFLAGS_ORIGCOLOR (disabled)

    Coverage    
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_COVERAGE) == c4d.RLAFLAGS_COVERAGE (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_COVERAGE) != c4d.RLAFLAGS_COVERAGE (disabled)

RPF
    Z
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_Z) == c4d.RLAFLAGS_Z (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_Z) != c4d.RLAFLAGS_Z (disabled)

    Object
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_OBJECTBUFFER) == c4d.RLAFLAGS_OBJECTBUFFER (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_OBJECTBUFFER) != c4d.RLAFLAGS_OBJECTBUFFER (disabled)

    UV Coordinates
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_UV) == c4d.RLAFLAGS_UV (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_UV) != c4d.RLAFLAGS_UV (disabled)

    Normal
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_NORMAL) == c4d.RLAFLAGS_NORMAL (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_NORMAL) != c4d.RLAFLAGS_NORMAL (disabled)

    Non-clamped color
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_ORIGCOLOR) == c4d.RLAFLAGS_ORIGCOLOR (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_ORIGCOLOR) != c4d.RLAFLAGS_ORIGCOLOR (disabled)

    Coverage    
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_COVERAGE) == c4d.RLAFLAGS_COVERAGE (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_COVERAGE) != c4d.RLAFLAGS_COVERAGE (disabled)

    ObjectID
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_OBJECTID) == c4d.RLAFLAGS_OBJECTID (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_OBJECTID) != c4d.RLAFLAGS_OBJECTID (disabled)
    
    Color
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_COLOR) == c4d.RLAFLAGS_COLOR (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_COLOR) != c4d.RLAFLAGS_COLOR (disabled)

    Subpixel Weight
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_SUBPIXEL_WEIGHT) == c4d.RLAFLAGS_SUBPIXEL_WEIGHT (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_SUBPIXEL_WEIGHT) != c4d.RLAFLAGS_SUBPIXEL_WEIGHT (disabled)

    Subpixel Mask           
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_SUBPIXEL_MASK) == c4d.RLAFLAGS_SUBPIXEL_MASK (enabled)
    (rdata[c4d.RDATA_SAVEOPTIONS][RLA_OPTIONS] & c4d.RLAFLAGS_SUBPIXEL_MASK) != c4d.RLAFLAGS_SUBPIXEL_MASK (disabled)