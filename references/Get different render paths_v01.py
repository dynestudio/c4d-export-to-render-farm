import c4d

# document global ids
doc     = c4d.documents.GetActiveDocument()
docname = doc.GetDocumentName()
docpath = doc.GetDocumentPath()

# render global ids
beauty_path  = ".\\$prj\\$prj_proxy"
mp_path      = ".\\$prj\\$prj_mp"

# docpath = "Y:\\My Drive\\Dyne - Works\\Canda Dry - FAXXI '19\\04_3D\\01_C4D\\04_Anim"

# set still of animation folder path
def path_type(folder_render_type, file_type):
    # define render folder type
    if folder_render_type:
        folder_render_type = "\\01_Styleframes"
    else:
        folder_render_type = "\\02_Animation"

    # clear c4d folder path
    docpath_list = docpath.split("\\")
    docpath_main = docpath_list[:-3]

    # set new path
    path = ""
    path_drive_render = "07_Render\\01_Render_3D"

    for i in docpath_main:
        path = path + i + "\\"

    path = path + path_drive_render + folder_render_type + file_type[1:]
    return path


if __name__=='__main__':
    path_type(1,beauty_path)