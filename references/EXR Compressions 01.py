rd = doc.GetActiveRenderData()
container = rd.GetData()

# OpenEXR
container[c4d.RDATA_FORMAT] = c4d.FILTER_EXR

saveOptions = container.GetContainerInstance(c4d.RDATA_SAVEOPTIONS)

# OpenEXR options
bc = c4d.BaseContainer()
bc[0] = 3 # ZIP
bc[1] = True # clamp to half float

# save OpenEXR options
saveOptions.SetContainer(0,bc)

# save render data
rd.SetData(container)

c4d.EventAdd()