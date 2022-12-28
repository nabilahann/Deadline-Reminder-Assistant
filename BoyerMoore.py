def buildLast(pattern):
    last = [-1]*128
    
    for i in range (0,len(pattern)):
        last[ord(pattern[i])] = i

    return last

def bmMatch(text, pattern):
    patt = pattern.lower()
    text2 = text.lower()
    last = buildLast(patt)
    # for i in range (len(last)):
    #     print(last[i])
    n = len(text2)
    m = len(patt)
    i = m-1
    if (i > n-1) :
        return -1   # no match if pattern is 
                    # longer than text
    j = m-1
    found = -1
    while True:
        if (patt[j] == text2[i]):
            if (j == 0) :
                found = i # match
                break
            else : # looking-glass technique
                i = i - 1
                j = j - 1
        else : # character jump technique
            lo = last[ord(text2[i])] #last occ 
            i = i + m - min(j, 1+lo)
            j = m - 1
        if (i > n-1):
            break

    return found # no match

# Driver program to test above function
def main():
    txt = "saya adalah Seorang pelaut"
    pat = "seorang"
    posn = bmMatch(txt, pat)
    if (posn == -1):
        print("Pattern not found")
    else :
        print("Pattern starts at posn " + str(posn))

if __name__ == '__main__':
    main()