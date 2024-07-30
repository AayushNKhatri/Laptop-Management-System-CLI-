def file_read():
    file = open("laptop.txt", "r")
    my_dictionary = {}
    laptop_id = 1
    for i in file:
        i = i.replace("\n", "")
        my_dictionary.update({laptop_id: i.split(",")})
        laptop_id += 1
    file.close()
    return my_dictionary