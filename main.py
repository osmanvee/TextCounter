
##Read a file from input
# @param fileName: Name of file to check
# @return none
def ReadFile(fileName):
    #Slicing the name to remove the ".in"
    newName = fileName[0:fileName.find(".in")]

    #Checking is the string contains an ".in"
    testSee = fileName.find(".in")
    if testSee == -1:
        #Reading the file and adding "in"
        inf = open(fileName+".in", "r")
        #Opening the file to output 
        outf = open(fileName+".out", "w")
    else:
        #Reading the file with an "in"
        inf = open(fileName, "r")
        outf = open(newName+".out", "w")

    #Checking paragraph (Empty line)
    linecount = 0 #Counting the number of lines
    para=0 #Paragragh counter
    outf.write("         ") 
    #Read every line of inf
    for line in inf.readlines():
        #If line is an empty line it means a paragraph ended
        if line in ('\n', '\r\n'):
            #incrementing para if there was a line before
            if linecount ==0:
                para = para + 1
                #para stays same
            linecount = linecount + 1
        else:
            linecount = 0
            #split the line into array
            x = line.split()
            #Number of words = length of the array
            words = len(x)
            outf.write("         ")
            outf.write("\nParagraph ")
            #Writing the paragraph number
            outf.write(str(para+1))
            outf.write(":")
        
            sentence = 0
            #For every word
            for j in x:
                #For every letter check if it is . , ! , ?
                for i in j:
                    if i == '.':
                        sentence = sentence + 1
                    elif i == '!':
                        sentence = sentence + 1
                    elif i == '?':
                        sentence = sentence + 1
                        #incrementing sentence if there is !, . , ?
            #Writing number of sentences
            outf.write("\n# of sentences: " )
            outf.write(str(sentence))
            outf.write("\n# of words: ")
            #Writing number of words 
            outf.write(str(words))
            outf.write("\n")
    
    #Going to the beginning of the file 
    outf.seek(0)
    #Writing number of paragraph
    outf.write("# of paragraphs: ")
    outf.write(str(para+1))
    outf.write("\n")

    #Closing the files
    inf.close()
    outf.close()

#main 
def main():
    file = input("Enter the name of file : ")
    ReadFile(file)

main()