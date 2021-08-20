def Thunder():
    filename=input("enter file name:")
    numberofwords=0
    file=open(filename,'r')
    for line in file:
        words=line.split()
        numberofwords=numberofwords+len(words)
    print("number of words:"+numberofwords)
    print(numberofwords)
Thunder()