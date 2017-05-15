jsonString = "["

with open('wordlist.txt') as f:
    word = f.readline().rstrip()
    while(word):
        definition = f.readline().rstrip()
        example = f.readline().rstrip().replace('"', '')

        #format json file
        jsonString += '{\nword: "' + word + '",\ndefinition: "' + definition + '",\nexample: "' + example + '",\n},\n'
        word = f.readline().rstrip()

jsonString += "]"

jsonFile = open('wordlist.json', 'w')
jsonFile.write(jsonString)
jsonFile.close()

print(jsonString)



