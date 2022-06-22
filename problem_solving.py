import re; import numpy as np;
studentid = 'n10817239'
# Returns amount of fertilser A and B
def fertiliser(an, ap, bn, bp, n, p): 
    '''Fertilisers: A and B\n nitrogen in 1kg of fertilisers: an & bn\n phosphate in 1kg of fertilisers: ap & bp'''
    if (an<0 or ap<0 or bn<0 or bp<0):
        return None
    A = np.array(((an, bn),(ap, bp)))              # coefficient matrix
    x = np.array([(n),(p)])                        # resultant matrix
    if np.linalg.det(A) != float(0):               # 1 solution exists
        inv_A = np.linalg.inv(A)
        Solution = np.matmul(inv_A,x)              # A*S = x, S = inv_A * x
        if ( (Solution[0] >= 0 and Solution[1]>= 0) == True ):  # Real solution
            a = Solution[0];  b = Solution[1];
            return a, b 

def censor(s):
    '''Censors all_articles: a, and & the, irrespective of capitalisation\n\n adds a student number to the end of censored string'''
    stdNo = " <n10817239>"
    # array of regex expressions for each article
    all_articles = [r"\b(a)\b", r"\b(an)\b", r"\b(the)\b" ] 
    censored_s = s
    for article in all_articles:
        article_in_string = re.search(article, censored_s, flags = re.I)
        # while the article exists in the string
        while(article_in_string != None):
            # For each article matched
            for match in re.finditer(article, censored_s, flags = re.I): 
                new = list(censored_s[:]); i = match.start()
                while i< match.end():
                    new[i] = "#"
                    i+=1
                censored_s = ''.join(new)
                article_in_string = re.search(article, censored_s, flags = re.I)
    # If anything has been censored
    if censored_s != s:
        return  censored_s + stdNo
    # Otherwise
    else:
        return s