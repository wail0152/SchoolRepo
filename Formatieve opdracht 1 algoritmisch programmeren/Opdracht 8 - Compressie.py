def compress(file, file_name):
    new_file = open(file_name + "_NEW.txt", "w")
    new_string = ""
    for line in file.readlines():
        line = line.strip(" ")
        if line != "\n":
            new_string += line
    new_file.write(new_string)
    new_file.close()
    return new_file


f = open("test.txt", "r")
compress(f, "test")
f.close()
