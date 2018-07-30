import c4d


def main():
    
    collect_path = c4d.storage.SaveDialog()

    if not collect_path[-4:] == ".c4d":
        collect_path = collect_path+".c4d"
    else:
        None        

if __name__=='__main__':
    main()
