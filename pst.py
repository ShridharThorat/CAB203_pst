import re; import numpy as np; import numpy.linalg as la;

# Uncomment and implement two of the following.  Refer to the Problem solving brief for specifications.

# Returns amount of fertilser A and B
def fertiliser(an, ap, bn, bp, n, p): 
    '''Fertilisers: A and B\n nitrogen in 1kg of fertilisers: an & bn\n phosphate in 1kg of fertilisers: ap & bp'''
    if (an<0 or ap<0 or bn<0 or bp<0):
        return None
    A = np.array(((an, bn),(ap, bp)))               # coefficient matrix
    x = np.array([(n),(p)])                         # resultant matrix
    if la.det(A) != float(0):                       # 1 solution exists
        inv_A = la.inv(A)
        Solution = np.matmul(inv_A,x)
        if ( (Solution[0] >= 0 and Solution[1]>= 0) == True ):  # Real solution
            return tuple(Solution)

def censor(s):
    '''Censors all_articles: a, and & the, irrespective of capitalisation\n\n adds a student number to the end of censored string'''
    stdNo = " <n10817239>"
    all_articles = [r"\b(a)\b", r"\b(an)\b", r"\b(the)\b" ]
    for article in all_articles:
        article_in_string = re.search(article, s, flags = re.I)
        while(article_in_string != None):
            for match in re.finditer(article, s, flags = re.I):
                new = list(s[:]); i = match.start()
                while i< match.end():
                    new[i] = "#"
                    i+=1
                s = ''.join(new)
                article_in_string = re.search(article, s, flags = re.I)
    return  s + stdNo

# def makeBet(headsOdds, tailsOdds, previousOutcome, state):
#  # bet =
#  # state = 
#  return (bet, state)


# The following will be run if you execute the file like python3 problem_solving.py
# Your solutions should not depend on this code.
# The automated marker will ignore any changes to this code; feel free to modify it
# but keep the if and the indenting as is
if __name__ == '__main__':
   try:
      print(censor('The cat ate a mouse.')) # should give "### cat ate # mouse. <n1234567>"
   except NameError:
      print("Not attempting censoring problem")

   try:
      print(fertiliser(1, 0, 0, 1, 2, 2)) # should give (2.0, 2.0)
   except NameError:
      print("Not attempting fertiliser problem")

   import random
   try:
      random.seed(0)
      totalprofit = 0
      for round in range(10000):
         if random.randint(0,1) == 0:
            headsprob = 0.7
         else:
            headsprob = 0.4

         previousOutcome = None
         state = None
         profit = 0
         odds = dict()
         for _ in range(100):
            odds['heads'] = random.uniform(1, 3)
            odds['tails'] = random.uniform(1, 3)
            
            bet, state = makeBet(odds['heads'], odds['tails'], previousOutcome, state)
            
            previousOutcome = 'heads' if random.random() < headsprob else 'tails'
            if bet == previousOutcome:
               profit += odds[bet] - 1
            elif bet != 'no bet':
               profit -= 1          # stake lost

         print("Probability of heads was", headsprob, "Profit was", profit)
         totalprofit += profit
      print("Average profit per run:", totalprofit / 10000)

   except NameError as e:
      print("Not attempting probability problem")