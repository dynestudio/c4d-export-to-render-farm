''' import c4d

#document global ids
doc     = c4d.documents.GetActiveDocument()
docname = doc.GetDocumentName()
docpath = doc.GetDocumentPath()

'''

docpath = "Y:\\My Drive\\Dyne - Works\\Canda Dry - FAXXI '19\\04_3D\\01_C4D\\04_Anim"
drive_path = "07_Render\\01_Render_3D"

folder_render_type = 0
if folder_render_type:
    folder_render_type = "\\01_Styleframes"
else:
    folder_render_type = "\\02_Animation"

file_name = "\\$prj\\$prj_MP"

def main():
    docpath_list = docpath.split("\\")
    docpath_newroot = docpath_list[:-3]

    path = ""

    for i in docpath_newroot:
        path = path + i + "\\"

    print path + drive_path + folder_render_type + file_name


if __name__=='__main__':
    main()