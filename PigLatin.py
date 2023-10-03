'''
Name: Grace Nguyen
U-Number: U86550360
Description: This program accepts an input file and reads the input file, converting it to string
by placing it in a list, to translate the text to pig latin. The pig latin translation is then put into
a new file that the user is allowed to name. 
'''
def main():
    #naming files
    fileName= input('Please enter the file name (as a text file with ".txt" at the end): ')
    newfileName = input('''Please input the new file's name (as a text file with ".txt" at the end): ''')
    
    #create a new text file
    with open(newfileName, 'w') as outputFile:
        new_lines = convert_file(fileName)
        for line in new_lines:
            newline = '\n'.join(new_lines)
        outputFile.write(newline)


        
def convert_file(fileName):
    #opening the file
    with open(fileName, 'r') as inputFile:
    
        #creating a list for the output
        converted_lines = []
    
        #seperating each word, as designated by a space, in each line into a new list
        for line in inputFile:
            line = line.split()
            new_words = []

            #reforming each word to pig latin
            for word in line:
                word = word.lower()
                endString= str(word[1:])
                them=endString, str(word[0:1]), 'ay'
                new_word="".join(them)
                new_words.append(new_word)

            #putting the words back together in each sentence
            new_sentence = ' '.join(new_words)
            if len(new_sentence):
                new_sentence = new_sentence[0] + new_sentence[1:]

            #adding each new sentence to the output list
            converted_lines.append(new_sentence)
            
    return converted_lines

main()

#finish
print('Translation Complete!')
print('Check your files for your new file with your translated text!')


    

