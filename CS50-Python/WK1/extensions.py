file = input("file name?:")
def extension(file):
    filetype = file.split('.')[-1].lower().strip()
    if filetype == "gif":
        print("image/gif")
    elif filetype == "jpg":
        print("image/jpeg")
    elif filetype == "jpeg":
        print("image/jpeg")
    elif filetype == "png":
        print("image/png")
    elif filetype == "pdf":
        print("application/pdf")
    elif filetype == "txt":
        print("text/plain")
    elif filetype == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")
extension(file)
