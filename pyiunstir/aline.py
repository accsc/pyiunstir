#feature values

import numpy as np


class aline_base:
    ''' Base class with all default values '''
    def __init__(self):

        self.gvec =  [5, 40, 50, 10, 10, 10, 10, 5, 1, 5, 5, 5, 10]
        self.FT_LEN = 13
        self.TAB = 4
        self.NSEG = 26
        self.FSyl = 0
        self.syl = 100
        self.nsl = 0
        self.FPlace = 1
        self.glo = 10
        self.vel = 60
        self.pal = 70
        self.pav = 75
        self.rfl = 80
        self.alv = 85
        self.dnt = 90
        self.lbd = 95
        self.blb = 100
        self.FStop  = 2
        self.lvl = 0
        self.mvl = 20
        self.hvl = 40
        self.vwl = self.hvl
        self.apr = 60
        self.frc = 80
        self.afr = 90
        self.stp = 100
        self.FVoice = 3
        self.vce = 100
        self.vls = 0
        self.FNasal = 4
        self.nas = 100
        self.FRetro = 5
        self.ret = 100
        self.FLat  = 6
        self.lat = 100
        self.FAsp  = 7
        self.asp = 100
        self.FLong = 8
        self.lng = 100
        self.FHigh = 9
        self.hgh = 100
        self.mid = 50
        self.low = 0
        self.FBack = 10
        self.frt = 100
        self.cnt = 50
        self.bak = 0
        self.FRound = 11
        self.rnd = 100
        self.FDouble = 12

        self.FVW = [self.syl, self.pal, self.vwl, self.vce, 0, 0, 0, 0, 0]
        self.BVW = [self.syl, self.vel, self.vwl, self.vce, 0, 0, 0, 0, 0]
        self.FGL = [self.nsl, self.pal, self.vwl, self.vce, 0, 0, 0, 0, 0]
        self.BGL = [self.nsl, self.vel, self.vwl, self.vce, 0, 0, 0, 0, 0]
        self.CNS = [self.nsl]

        self.features = {}

        self.features['a'] = self.BVW.copy()
        self.features['a'].extend([self.low, self.cnt, 0, 0])

        self.features['b'] = self.CNS.copy()
        self.features['b'].extend([self.blb, self.stp, self.vce, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['c'] = self.CNS.copy()
        self.features['c'].extend([self.alv, self.afr, self.vls, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['d'] = self.CNS.copy()
        self.features['d'].extend([self.alv, self.stp, self.vce, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['e'] = self.FVW.copy()
        self.features['e'].extend([self.mid, self.frt, 0, 0])

        self.features['f'] = self.CNS.copy()
        self.features['f'].extend([self.lbd, self.frc, self.vls, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['g'] = self.CNS.copy()
        self.features['g'].extend([self.vel, self.stp, self.vce, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['h'] = self.CNS.copy()
        self.features['h'].extend([self.glo, self.frc, self.vls, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['i'] = self.FVW.copy()
        self.features['i'].extend([self.hgh, self.frt, 0, 0])

        self.features['j'] = self.CNS.copy()
        self.features['j'].extend([self.alv, self.afr, self.vce, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['k'] = self.CNS.copy()
        self.features['k'].extend([self.vel, self.stp, self.vls, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['l'] = self.CNS.copy()
        self.features['l'].extend([self.alv, self.apr, self.vce, 0, 0, self.lat, 0, 0, 0, 0, 0, 0])

        self.features['m'] = self.CNS.copy()
        self.features['m'].extend([self.blb, self.stp, self.vce, self.nas, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['n'] = self.CNS.copy()
        self.features['n'].extend([self.alv, self.stp, self.vce, self.nas, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['ñ'] = self.CNS.copy()
        self.features['ñ'].extend([self.blb, self.stp, self.vce, self.nas, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['o'] = self.BVW.copy()
        self.features['o'].extend([self.mid, self.bak, self.rnd, 0])

        self.features['p'] = self.CNS.copy()
        self.features['p'].extend([self.blb, self.stp, self.vls, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['q'] = self.CNS.copy()
        self.features['q'].extend([self.glo, self.stp, self.vls, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['r'] = self.CNS.copy()
        self.features['r'].extend([self.rfl, self.apr, self.vce, 0, self.ret, 0, 0, 0, 0, 0, 0, 0])

        self.features['ŕ'] = self.CNS.copy()
        self.features['ŕ'].extend([self.rfl, self.apr, self.vce, 0, self.ret, 0, 0, 0, 0, 0, 0, 0])

        self.features['s'] = self.CNS.copy()
        self.features['s'].extend([self.alv, self.frc, self.vls, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['ś'] = self.CNS.copy()
        self.features['ś'].extend([self.alv, self.frc, self.vls, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['t'] = self.CNS.copy()
        self.features['t'].extend([self.alv, self.stp, self.vls, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['u'] = self.BVW.copy()
        self.features['u'].extend([self.hgh, self.bak, self.rnd, 0])

        self.features['v'] = self.CNS.copy()
        self.features['v'].extend([self.lbd, self.frc, self.vce, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['w'] = self.BGL.copy()
        self.features['w'].extend([self.hgh, self.bak, self.rnd, self.blb])

        self.features['x'] = self.CNS.copy()
        self.features['x'].extend([self.vel, self.frc, self.vls, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features['y'] = self.FGL.copy()
        self.features['y'].extend([self.hgh, self.frt, 0, 0])

        self.features['z'] = self.CNS.copy()
        self.features['z'].extend([self.alv, self.frc, self.vce, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.features = self.applyRedundancyRules(self.features)

    def applyRedundancyRules(self, FCon):
        for i in FCon.keys():
            if self.vowel(FCon[i]):
                if FCon[i][self.FHigh] == self.hgh:
                    FCon[i][self.FStop] = self.hvl
                elif FCon[i][self.FHigh] == self.mid:
                    FCon[i][self.FStop] = self.mvl
                elif FCon[i][self.FHigh] == self.low:
                    FCon[i][self.FStop] = self.lvl
                else:
                    return False

            if not self.vowel(FCon[i]):
                FCon[i][self.FHigh] = self.hgh

        return FCon

    def vowel(self, p):
        return p[self.FStop] <= self.vwl


class aline_word(aline_base):
    ''' Class for wrapping up aline word methods and data '''
    def __init__(self, word):
        ''' Init all default values and scores '''
        super().__init__()

        self.ind = []
        self.phon = []
        self.n  = 0
        #self.FCon = []

        self.outn = len(word);
        assert self.outn > 0, 'Error with word'
        #assert ord(word[0]) >= ord('a'), f'Error with characters {word[0]}'
        self.out = word
        self.fconvert()

    def fconvert(self):
        j = -1
        self.ind = []
        for k in range(self.outn+1):
            self.ind.append(0)

        for seg in range(self.outn):
            c = self.out[seg]
            if ord(c) >= ord('a'):
                j += 1
                self.ind[j] = seg
                self.phon.append(self.features[c])
            else:
                print("TODO. implement modifiers", c)
        self.ind[j+1] = self.outn
        self.n=j+1

    def phlen(self):
        return self.n

    def flush(self, wi, aback, abackcount):
        assert wi >= 0 and wi < self.n, 'Error on flush'
        o1 = self.ind[wi]
        o2 = self.ind[wi+1]
        for t in range(self.TAB):
            if o1 != o2:
                o1 += 1
                aback[abackcount] = self.out[o1-1]
                abackcount += 1
            else:
                aback[abackcount] = ' '
                abackcount += 1

        return [abackcount, aback]


class aline_word_utils(aline_base):

    def __init__(self):
        super().__init__()

    def diff(self, p1, p2, f):
        d = p1[f] - p2[f]
        if d < 0:
            d = -d
        return d

    def places(self, p1, p2):
        pd = abs( p1[self.FPlace] - p2[self.FPlace])
        if p1[self.FDouble] > 0:
            if pd > abs( p1[self.FDouble] - p2[self.FPlace]):
                pd = abs( p1[self.FDouble] - p2[self.FPlace])

        if p2[self.FDouble] > 0:
            if pd > abs( p1[self.FPlace] - p2[self.FDouble] ):
                pd = abs( p1[self.FPlace] - p2[self.FDouble] )

        if p1[self.FDouble] > 0 and p2[self.FDouble] > 0:
            if pd > abs( p1[self.FDouble] - p2[self.FDouble] ):
                 pd = abs( p1[self.FDouble] - p2[self.FDouble] )

        return pd * self.gvec[self.FPlace]


    def ladDist(self, p1, p2):
        dist = 0
        d = 0
        if self.vowel(p1) and self.vowel(p2):
            dist += self.diff(p1, p2, self.FSyl) * self.gvec[self.FSyl]
            dist += self.diff(p1, p2, self.FNasal) * self.gvec[self.FNasal]
            dist += self.diff(p1, p2, self.FRetro) * self.gvec[self.FRetro]
            dist += self.diff(p1, p2, self.FHigh) * self.gvec[self.FHigh]
            dist += self.diff(p1, p2, self.FBack) * self.gvec[self.FBack]
            dist += self.diff(p1, p2, self.FRound) * self.gvec[self.FRound]
            dist += self.diff(p1, p2, self.FLong) * self.gvec[self.FLong]
        else:
            dist += self.diff(p1, p2, self.FSyl) * self.gvec[self.FSyl]
            dist += self.diff(p1, p2, self.FStop) * self.gvec[self.FStop]
            dist += self.diff(p1, p2, self.FVoice) * self.gvec[self.FVoice]
            dist += self.diff(p1, p2, self.FNasal) * self.gvec[self.FNasal]
            dist += self.diff(p1, p2, self.FRetro) * self.gvec[self.FRetro]
            dist += self.diff(p1, p2, self.FLat) * self.gvec[self.FLat]
            dist += self.diff(p1, p2, self.FAsp) * self.gvec[self.FAsp]
            dist += self.places(p1, p2)

        return dist

# 3500

# compute score for substitution
    def sigmaSub(self, wA, iA, wB, iB):
        if iA == 0 or iB == 0:
            return -99999

        pA = wA.phon[wA.n-iA]
        pB = wB.phon[wB.n-iB]

        score = 3500 - self.ladDist(pA, pB)
    
        if self.vowel(pA):
            score -= 1000
        if self.vowel(pB):
            score -= 1000

        return score


    def sigmaExp(self, wA, iA, wB, i1B, i2B):
        if iA == 0 or i2B == 0:
            return -99999
    
        if i1B == 0:
            return -99999
    
        pA = wA.phon[wA.n-iA]
        p1B = wB.phon[wB.n-i1B]
        p2B = wB.phon[wB.n-i2B]
    
        d1 = self.ladDist( p1B, pA)
        d2 = self.ladDist( p2B, pA)

        if d1 == 0 and d2 == 0:
            return -99999

        score = 4500 - (d1 + d2)
    
        if self.vowel(p1B) or self.vowel(p2B):
            score -= 1000
        if self.vowel(pA):
            score -= 1000

        return score;

    def sigmaIdent(self, wA, iA, wB, iB):
    
        pA = wA.phon[wA.n-iA]
        pB = wB.phon[wB.n-iB]

        for f in range(self.FT_LEN):
            if pA[f] != pB[f]:
                return 0

        return 1

    def sigmaSkip(self, w, i, skippen):
        return 0


class aline_stack:
    ''' A class to provide stacks for ALINE '''

    def __init__(self):
        self.stack = []
        self.top = 0
        self.MAXL = 80
        for i in range(2):
            current_list = []
            for j in range(self.MAXL):
                current_list.append(0)
            self.stack.append(current_list)

    def clear(self):
        self.top = 0

    def push(self, i1, i2=-1):
        if self.top >= 0 and self.top < self.MAXL:
            self.stack[0][self.top] = i1
            self.stack[1][self.top] = i2
            self.top += 1

    def pop(self, k = 1):
        self.top -= k

    def showAlign(self, w, row, aback):
        n = w.phlen()
        abackcount = 0
        for ind in range(self.top):
            i = self.stack[row][ind]
            if i == -1:
                aback[abackcount] = '-'
                abackcount += 1
                aback[abackcount] = ' '
                abackcount += 1
                aback[abackcount] = ' '
                abackcount += 1
                aback[abackcount] = ' '
                abackcount += 1
            elif i == -2:
                aback[abackcount] = '|'
                abackcount += 1
                aback[abackcount] = ' '
                abackcount += 1
                aback[abackcount] = ' '
                abackcount += 1

            elif i == -3:
                aback[abackcount] = '<'
                abackcount += 1
                aback[abackcount] = ' '
                abackcount += 1
                aback[abackcount] = ' '
                abackcount += 1
                aback[abackcount] = ' '
                abackcount += 1

            else:
                abackcount, aback = w.flush(n-i, aback, abackcount)
            aback[abackcount] = "#" 

        return aback


class aline_wagner(aline_word_utils):
    ''' Wagner class '''
    def __init__(self):
        super().__init__()
        self.SQUASH = True
        self.ONE_ONLY = False
        self.MAXL = 80
        self.S = np.zeros((self.MAXL, self.MAXL))
        self.DpScore = 0
        self.AcptScore = 0
        self.FallThru = False
        self.Trace = aline_stack()
        self.Out = aline_stack()
        self.Cost = aline_stack()
        self.S = np.zeros((self.MAXL, self.MAXL))
        self.GLOBAL = False
        self.SEMI_GLOBAL = False
        self.LOCAL = True

    def Score(self, i,j):
        if i >= 0 and j >= 0:
            return self.S[i,j]
        else:
            return -99999

    def maxim_5(self, m1, m2, m3, m4, m5):
        return max( max( max( m1, m2 ), m3 ), max( m4, m5 ) )

    def maxim_6(self, m1, m2, m3, m4, m5, m6):
        return max( max( max( m1, m2 ), m3 ), max( max( m4, m5 ), m6 ) )


    def allowed(self, w):
        for i in range(w.top):
            if w.stack[0][i] == -1 and w.stack[1][i-1] == -1:
                return False
        return True

    def similarity(self, wA, wB):
        lenA = wA.phlen()
        lenB = wB.phlen()
        sgmax = 0
        m1 = -99999
        m2 = -99999
        m3 = -99999
        m4 = -99999
        m5 = -99999
        lmax = 0

        self.S[0,0] = 0
        for i in range(1, lenA+1):
            if self.GLOBAL:
                self.S[i,0] = self.S[i-1,0] + self.sigmaSkip(wA, i, 0)
            else:
                self.S[i,0] = 0

        for j in range(1, lenB+1):
            if self.GLOBAL:
                self.S[0,j] = self.S[0,j-1] + self.sigmaSkip(wB, i, 0)
            else:
                self.S[0,j] = 0

        for i in range(1, lenA+1):
            for j in range(1, lenB+1):
                m1 = self.Score(i-1, j) + self.sigmaSkip(wA, i, 0)
                m2 = self.Score(i, j-1) + self.sigmaSkip(wB, j, 0)
                m3 = self.Score(i-1,j-1) + self.sigmaSub(wA, i, wB, j)
                if self.SQUASH:
                    m4 = self.Score(i-1,j-2) + self.sigmaExp( wA, i, wB, j-1, j)
                    m5 = self.Score(i-2,j-1) + self.sigmaExp( wB, j, wA, i-1, i)
                if self.LOCAL:
                    lmax = self.maxim_6( m1, m2, m3, m4, m5, 0)
                else:
                    lmax = self.maxim_5( m1, m2, m3, m4, m5 )

                self.S[i,j] = lmax
                if lmax > sgmax:
                    if self.SEMI_GLOBAL:
                        if i == lenA or j == lenB:
                            sgmax = lmax
                    else:
                        sgmax = lmax
        return sgmax


    def alignment(self, wA, wB, i, j, T, getScore, aback1, aback2):

        if self.FallThru and self.ONE_ONLY:
            return getScore, aback1, aback2

        if i == 0 and j == 0:
            assert self.Score(i,j) == 0, 'Error with Scores'
            if self.allowed(self.Out) and not self.FallThru:
                self.Out.push(-2,-2)
                for i1 in range(i,0,-1):
                    self.Out.push(i1, -1)
                for j1 in range(j,0,-1):
                    self.Out.push(-1, j1)


                aback1 = self.Out.showAlign( wA, 0, aback1)
                aback2 = self.Out.showAlign( wB, 1, aback2)
                self.Out.pop(i+j+1)

                if self.GLOBAL:
                    score = T + (i+j)*self.sigmaSkip(wA,0,0)
                else:
                    score = T

                #getScore = self.show(score)
                getScore = score / 100
                FailThru = True
        else:
            subSc = self.sigmaSub( wA, i, wB, j)
            if self.Score(i-1, j-1) + subSc + T >= self.AcptScore:    
                self.Cost.push(subSc)
                self.Out.push(i, j)
                self.Trace.push(i, j)
                getScore, aback1, aback2 = self.alignment(wA, wB, i-1, j-1, T+subSc, getScore, aback1, aback2)
                self.Trace.pop()
                self.Out.pop()
                self.Cost.pop()


            insSc = self.sigmaSkip( wB, j, 0)
            if (i == 0 ) or (self.Score(i,j-1) + insSc + T >= self.AcptScore ):
                self.Cost.push(insSc)
                self.Out.push(-1, j)
                getScore, aback1, aback2 = self.alignment(wA, wB, i, j-1, T + insSc, getScore, aback1, aback2)
                self.Out.pop()
                self.Cost.pop()

            if self.SQUASH:
                expSc = self.sigmaExp( wA, i, wB, j-1, j)
                if self.Score(i-1,j-2) + expSc + T >= self.AcptScore:
                    self.Cost.push(expSc)
                    self.Cost.push(-1)
                    self.Out.push(i,j)
                    self.Out.push(-3, j-1)
                    self.Trace.push(i,j)
                    self.Trace.push(i, j-1)
                    getScore, aback1, aback2 = self.alignment(wA, wB, i-1, j-2, T + expSc, getScore, aback1, aback2)
                    self.Trace.pop(2)
                    self.Out.pop(2)
                    self.Cost.pop(2)

            delSc = self.sigmaSkip( wA, j, 0)
            if (j == 0) or ( self.Score(i-1,j) + delSc + T >= self.AcptScore ):
                self.Cost.push( delSc )
                self.Out.push( i, -1)
                getScore, aback1, aback2 = self.alignment( wA, wB, i-1, j, T + delSc, getScore, aback1, aback2)
                self.Out.pop()
                self.Cost.pop()

            if self.SQUASH:
                 cmpSc = self.sigmaExp( wB, j, wA, i-1, i)
                 if self.Score(i-2,j-1) + cmpSc + T >= self.AcptScore:
                     self.Cost.push(cmpSc)
                     self.Cost.push(-1)
                     self.Out.push(i,j)
                     self.Out.push(i-1, -3)
                     self.Trace.push(i,j)
                     self.Trace.push(i-1, j)
                     getScore, aback1, aback2 = self.alignment( wA, wB, i-2, j-1, T + cmpSc, getScore, aback1, aback2)
                     self.Trace.pop(2)
                     self.Out.pop(2)
                     self.Cost.pop(2)
        return getScore, aback1, aback2


    def align(self, wA, wB):
        getScore = 0
        aback1 = []
        aback2 = []
        for i in range(200):
            aback1.append('#')
            aback2.append('#')
        lenA = wA.phlen()
        lenB = wB.phlen()
        self.Cost.clear()
        self.Trace.clear()
        self.Out.clear()
        self.FallThru = False
        sgmax = self.similarity(wA, wB)
        if self.GLOBAL:
            self.DpScore = self.Score(lenA, lenB)
        else:
            self.DpScore = sgmax

        self.AcptScore = self.DpScore * 1.0

        for i in range(lenA+1):
            for j in range(lenB+1):
                if self.GLOBAL:
                    if i < lenA or j < lenB:
                        continue
                if self.SEMI_GLOBAL:
                    if i < lenA and j < lenB:
                        continue
                if self.S[i,j] >= self.AcptScore:
                    for j1 in range(lenB,j,-1):
                        self.Out.push(-1, j1)
                    for i1 in range(lenA,i,-1):
                        self.Out.push(i1, -1)

                    self.Out.push(-2, -2)
                    getScore, aback1, aback2 = self.alignment(wA, wB, i, j, 0, getScore, aback1, aback2)
                    self.Out.pop(lenA-i+lenB-j+1)
                    if self.FallThru:
                        return getScore, aback1, aback2
        return getScore, aback1, aback2




