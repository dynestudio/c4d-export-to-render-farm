import c4d


def main():
    
    targetPath = c4d.storage.SaveDialog()

    if not targetPath[-4:] == ".c4d":
        targetPath = targetPath+".c4d"
    else:
        None        

if __name__=='__main__':
    main()
