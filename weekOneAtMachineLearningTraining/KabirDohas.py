startIndex, endIndex = 0, 0

book = []

with open("pg6519.txt", "r") as file:
    #print file.read()
    for line in file:
        book.append(line)

#print book

for index, line in enumerate(book):
    if "KABIR'S POEMS" in line:
        print "starts at ", index, line
        startIndex = index
    elif "End of the Project Gutenberg EBook of Songs of Kabir, by Kabir" in line:
        print "ends at ", index, line
        endIndex = index


allKabirDohas = book[startIndex + 1 : endIndex]

print allKabirDohas


