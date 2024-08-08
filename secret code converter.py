value = input("enter any value: ")
words = value.split(" ")
coding = input("1 for coding and 0 for decoding: ")
coding = True if (coding == '1') else False
print(coding)
if (coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = 'fhg'
            r2 = 'vcx'
            stnew = r1+ word[1:]+ word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    