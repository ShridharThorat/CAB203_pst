import re; import numpy as np; import numpy.linalg as la;

# Returns amount of fertilser A and B
def fertiliser(an, ap, bn, bp, n, p): 
    '''Fertilisers: A and B\n nitrogen in 1kg of fertilisers: an & bn\n phosphate in 1kg of fertilisers: ap & bp'''
    if (an<0 or ap<0 or bn<0 or bp<0):
        return None
    A = np.array(((an, bn),(ap, bp)))               # coefficient matrix
    x = np.array([(n),(p)])                         # resultant matrix
    if la.det(A) != float(0):                       # 1 solution exists
        inv_A = la.inv(A)
        Solution = np.matmul(inv_A,x)               # A*S = x, S = inv_A * x
        if ( (Solution[0] >= 0 and Solution[1]>= 0) == True ):  # Real solution
            return tuple(Solution)

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

censortests = [
   ('The cat ate a mouse.', '### cat ate # mouse.'),
   ('I went to the store.', 'I went to ### store.'),
   ('A cookie is a very nice thing', '# cookie is # very nice thing'),
   ('THe thing over there.is.tHe.best!', '### thing over there.is.###.best!'),
   ('aN-otter-ate-An-apple.', '##-otter-ate-##-apple.'),
   ('aN_otter_ate_An_apple.', 'aN_otter_ate_An_apple.'),
   ("Don't change anything!", "Don't change anything!")
]

fertilisertests = [
   ((1.0, 0.0, 0.0, 1.0, 2.0, 2.0), (2.0,  2.0)),
   ((0.3, 0.2, 0.1, 0.4, 10,  20 ), (20.0, 40.0)),
   ((0.1, 0.4, 0.3, 0.2, 10,  20 ), (40.0, 20.0)),
   ((0.5, 0.5, 0.5, 0.3, 10,  2  ), None),
   ((0.3, 0.3, 0.3, 0.3, 10,  20 ), None)
]

if __name__ == '__main__':

    studentid = "n10817239"
    print('==================================================================================')
    print('Attempting censor topic')
    for text, result in censortests:
        print('----------------------------------------------------------------------------------')
        sol = censor(text)
        if text != result: result = f'{result} <{studentid}>'
        feedback = 'Correct!' if sol == result else 'Incorrect.'
        print(f'Text:           {text}')
        print(f'Result:         {sol}')
        print(f'Desired result: {result}')
        print(feedback)

    # Fertiliser
    print('==================================================================================')
    print('Attempting fertiliser topic')
    for args, result in fertilisertests:
        print('----------------------------------------------------------------------------------')
        an, ap, bn, bp, n, p = args
        print(f'Function arguments: an = {an} ap = {ap} bn = {bn} bp = {bp} n = {n} p = {p} ')
        sol = fertiliser(*args)
         
        if sol is None:
            print(f'Result:         None')
            print(f'Desired result: {str(result)}')
            if sol == result:
                print('Correct!')
            else:
                print('Incorrect.')
        elif type(sol) is tuple:
            if result is None:
                print(f'Result:         {sol}')
                print(f'Desired result: {str(result)}')
                print('Incorrect.')
                continue
            if len(sol) != 2:
                print(f'Expected a tuple of length two, got {sol}')
            else:
                a, b = sol
                aresult, bresult = result
                print(f'Result:         a = {a} b = {b}')
                print(f'Desired result: a = {aresult} b = {bresult}')
                if abs(a - aresult) > 0.001 or abs(b - bresult) > 0.001:
                    print('Incorrect.')
                else:
                    print('Correct!')
        else:
            print(f'Expected None or a tuple of length 2.  Got {str(sol)}')
