def compress(file, fileName):
    newFile = open(fileName + "_NEW.txt", "w")
    newString = ""
    for line in file.readlines():
        line = line.strip(" ")
        if line != "\n":
            newString += line
    newFile.write(newString)
    newFile.close()
    return newFile


f = open("test.txt", "r")
compress(f, "test")
f.close()
