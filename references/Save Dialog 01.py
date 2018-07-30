import c4d


def main():
    
    #fn = c4d.storage.SaveDialog()

    test = "desktop/path.c4d"

    if not test[-4:] == ".c4d":
        test = test+".c4d"
    else:
        None


if __name__=='__main__':
    main()
