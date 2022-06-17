import re; import numpy as np;

# Returns amount of fertilser A and B
def fertiliser(an, ap, bn, bp, n, p): 
    '''Fertilisers: A and B\n nitrogen in 1kg of fertilisers: an & bn\n phosphate in 1kg of fertilisers: ap & bp'''
    if (an<0 or ap<0 or bn<0 or bp<0):
        return None
    A = np.array(((an, bn),(ap, bp)))       # coefficient matrix
    x = np.array([(n),(p)])                 # resultant matrix
    if np.linalg.det(A) != float(0):               # 1 solution exists
        inv_A = np.linalg.inv(A)
        Solution = np.matmul(inv_A,x)               # A*S = x, S = inv_A * x
        if ( (Solution[0] >= 0 and Solution[1]>= 0) == True ):  # Real solution
            a = Solution[0];  b = Solution[1];
            return a,b

def censor(s):
    '''Censors all_articles: a, and & the, irrespective of capitalisation\n\n adds a student number to the end of censored string'''
    stdNo = " <n10817239>"
    all_articles = [r"\b(a)\b", r"\b(an)\b", r"\b(the)\b" ]
    sNew = s
    for article in all_articles:
        article_in_string = re.search(article, sNew, flags = re.I)
        while(article_in_string != None):
            for match in re.finditer(article, sNew, flags = re.I):
                new = list(sNew[:]); i = match.start()
                while i< match.end():
                    new[i] = "#"
                    i+=1
                sNew = ''.join(new)
                article_in_string = re.search(article, sNew, flags = re.I)
    if sNew != s:
        return  sNew + stdNo
    else:
        return s