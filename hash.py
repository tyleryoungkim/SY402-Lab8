import os
import hashlib
from datetime import datetime #https://www.programiz.com/python-programming/datetime/current-time

def main():
    skip = ["/DONTHASH","/dev","/proc","/run","/sys","/tmp","/var/lib","/var/run"]
    home = os.path.expanduser("./")
    #storedFiles = {}
    path = home
    for root, d_names, f_names in os.walk(path):
        #print(root, d_names, f_names)
        for item in skip:
            if item in root:
               # print("hello")
                continue
            else:
                #print(root, d_names, f_names)
                for f in f_names:
                    filePath = root + "/" + f
                    h = hashlib.sha256() #hash object
                    print(filePath)
                    file_contents = open(filePath,"rb")
                    contents = file_contents.read()
                    h.update(contents)
                    hashed = h.hexdigest
                    currentTime = datetime.now()
                   # storedFiles.add(filePath)
                   # data = (filePath, (hashed, currentTime))
                    print(h.hexdigest)
                    file_contents.close()


main()
