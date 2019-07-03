#Sk adib Asker
#CS 100, 2017F SEC 103
#HW-8

#Problem 1
def file_copy(in_file,out_file):
    inputFile=open(in_file,'r')
    outputFile=open(out_file,'w')
    #content=inputFile.read()
    #outputFile=write.(contecnt)
    #close both file
    for line in inputFile:
        outputFile.write(line)
         
file_copy('created_equal.txt','copy.txt')
print(open('copy.txt').read())


# Problem 2

 
def file_stats(in_file):
    lineCount=0
    wordCount=0
    charCount=0
    inputFile=open(in_file,'r')
    for line in inputFile:
        if line is not ' ':
            lineCount +=1
    for char in line:
        if char is not ' ':
               charCount +=1
    for word in line:
            if word is not ' ':
               wordCount +=1
    print('Line ',lineCount)
    print('Words ',wordCount)
    print('Characters ',charCount)  
 
file_stats('created_equal.txt')

# Problem 3


def repeat_words(inputfile, outputfile):
    import string
    
    infile = open(inputfile, 'r')
    outfile = open(outputfile, 'w')
    
    for line in infile:
        repeat = []
        newText = ''
        text = line
        text = text.lower()
        
        for i in text:
            newText += i.strip(string.punctuation)
            
        for j in newText.split():
            if (newText.count(j)) >= 2:
                repeat.append(j)
                
            if (repeat.count(j) > 1):
                repeat.remove(j)
                
        outfile.write(' '.join(repeat))
        outfile.write('\n')
        text = ''
        
inF = 'catInTheHat.txt'
outF = 'catRepWords.txt'
repeat_words(inF, outF)        
