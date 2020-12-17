from pyiunstir.aline import *
import collections
import numpy as np

from scipy.cluster.hierarchy import linkage, dendrogram


def aline_compare(word1, word2):
    ''' Uses the ALINE Wagner method to align two words and computes thes 
        distance based on the eq. 1 - [ (2*ScoreAB) / (ScoreAA+ScoreBB)] '''

    # Word1 vs Word2
    u = aline_wagner()
    w1 = aline_word(word1)
    w2 = aline_word(word2)
    ab,a1,a2 = u.align(w1,w2)
    ali1 = ''.join(a1)
    ali2 = ''.join(a2)

    # Word1 vs Word1
    w1 = aline_word(word1)
    w2 = aline_word(word1)
    aa ,a1,a2 = u.align(w1,w2)

    # Word2 vs Word2
    w1 = aline_word(word2)
    w2 = aline_word(word2)
    bb ,a1,a2 = u.align(w1,w2)

    # Calculate score
    score = 1.0- (2.0*ab/(aa+bb))

    # Tidy up alignment
    ali1 = ali1.replace(' ','').split('|')[1]
    ali2 = ali2.replace(' ','').split('|')[1]
    return score, ali1, ali2


def aline_align_profiles(profile1, profile2, gap=1):
    """
        Use the Needleman–Wunsch algorithm to align two alignments or a word and an alignment
        using the ALINE scores

        Params:
        profile1: nested list
        profile2: nested list
        gap:float: Gap penalty value (distance)


        Returns aligment1, aligment2, distance

    """

    gap_profile = 0.5
    gap_codes = ('<', '-')

    # Pre-calculate scores
    len1 = len(profile1)
    len2 = len(profile2)
    precalc_scores = np.zeros((len1,len2))
    for i in range(len1): # Lenght of the profile1
        for j in range(len2): # Lenght of the profile2
            current_dist = 0.0
            c = 0
            for k in range(len(profile1[i])): # For each aligned word inside profile1
                for l in range(len(profile2[j])): # For each aligned word inside profile2
                    m1 = profile1[i][k]
                    m2 = profile2[j][l]
                    if m1 in gap_codes or m2 in gap_codes:
                        current_dist += gap_profile # Aligned with gap
                    else:
                        d, _, _ = aline_compare(m1,m2)
                        current_dist += d
                    c += 1
                # Normalize by number of comparisons
                precalc_scores[i, j] = current_dist / float(c)

    pointer = np.zeros((len1 + 1, len2 + 1), dtype='i')
    matrix = np.zeros((len1 + 1, len2 + 1), dtype='f')
    length = np.zeros((len1 + 1, len2 + 1), dtype='f')
    pointer[0, 0] = 0
    pointer[0, 1:] = 1
    pointer[1:, 0] = 2
    for i in range(1, len1 + 1):
        matrix[i,0] = matrix[i-1,0] + gap
        length[i,0] = length[i-1,0] + gap
    for j in range(1, len2 + 1):
        matrix[0,j] = matrix[0,j-1] + gap
        length[0,j] = length[0,j-1] + gap
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            gap_a = matrix[i-1,j] + gap 
            gap_b = matrix[i,j-1] + gap 
            match = matrix[i-1,j-1] + precalc_scores[i-1,j-1]
            if gap_a < match and gap_a <= gap_b:
                matrix[i,j] = gap_a
                pointer[i,j] = 2
            elif match <= gap_b:
                matrix[i,j] = match
                pointer[i,j] = 3
            else:
                matrix[i,j] = gap_b
                pointer[i,j] = 1
            p = pointer[i,j]
            l_gap_a = length[i-1,j]
            if p == 2:
                l_gap_a += length[i-1,j] + gap 
            l_gap_b = length[i,j-1]
            if p == 1:
                l_gap_b = length[i,j-1] + gap 
            l_match = length[i-1,j-1]
            if p == 3:
                l_match = length[i-1,j-1] + precalc_scores[i-1,j-1]

            length[i,j] = max(l_gap_a,l_gap_b,l_match)

    distance = matrix[len1,len2] / length[len1,len2]

    i, j = len1, len2
    align1, align2 = [], []
    fill_a, fill_b = '-', '-'
    if any(isinstance(e, (tuple, list)) for e in profile1):
        fill_a = ('-',) * len(profile1[0])
    if any(isinstance(e, (tuple, list)) for e in profile2):
        fill_b = ('-',) * len(profile2[0])
    while True:
        p = pointer[i, j]
        if p == 0: 
            break
        if p == 3:
            align1.append(profile1[i-1])
            align2.append(profile2[j-1])
            i, j = i - 1, j - 1
        elif p == 1:
            align1.append(fill_a)
            align2.append(profile2[j-1])
            j -= 1
        elif p == 2:
            align1.append(profile1[i-1])
            align2.append(fill_b)
            i -= 1

    return align1[::-1], align2[::-1], distance

def aline_mwa(words):
    """
        Perform a progressive multiple word alignment.

        Params:
        words:list:List of words

        Returns:

        List of aligned words (not preverving the order)
    """

    gap = 1.0 # Distance value for a gap
    # Compute a tree for the multiple alignment
    nw = len(words)
    mat = np.ones((nw,nw))
    for i, w1 in enumerate(words):
        for j in range(i+1, len(words)):
            w2 = words[j]
            s, w1_a, w2_a = aline_compare(w1,w2)
            mat[i, j] = 1.0-s
            mat[j, i] = 1.0-s

    Z = linkage(mat, method='single')

    # Use the tree for progressive alignment
    calc_alignments = {}
    for node_id, (node1, node2, _, _) in enumerate(Z, nw):
        node1 = int(node1)
        node2 = int(node2)
        if node1 < nw and node2 < nw:  # Word vs Word. Use ALINE
            d, align1, align2 = aline_compare(words[node1], words[node2])
        else: # A "profile" is involved in the alignment. Use NW
            if node1 < nw:   # Node1 is a word, while node2 is a previous alignment
                word_a, word_b = [[itm] for itm in words[node1]], calc_alignments[node2]
            elif node2 < nw: # Node2 is a word, while node2 is a previous alignment
                word_a, word_b = calc_alignments[node1], [[itm] for itm in words[node2]]
            else: # Both nodes are previous alignments
                word_a, word_b = calc_alignments[node1], calc_alignments[node2]

            align1, align2, _ = aline_align_profiles(word_a, word_b, gap)

        calc_alignments[node_id] = merge_alignments(align1, align2)

    # Collect all the words in the alignment
    res = list(zip(*map(just_flatten, calc_alignments[max(calc_alignments)])))
    # Join all the chars
    clean_res = []
    for word in res:
        clean_res.append(''.join(word))
    return clean_res


def isString(obj):
    ''' Checks for string type '''
    return isinstance(obj, str)

def isIterable(obj):
    ''' Checks for iterable type '''
    return isinstance(obj, collections.Iterable)

def iterable_flatten(obj_item):
    ''' Recursive method together with just_flatten to flatten iterables with depth '''
    for itm in obj_item:
        if isIterable(itm) and not isString(itm):
            for sub in just_flatten(itm):
                yield sub
        else:
            yield itm

def just_flatten(obj_item):
    ''' Recursive method together with iterable_flatten to flatten iterable with depth '''
    return list(iterable_flatten(obj_item))

def merge_alignments(*alignments):
    ''' Merge aligned words'''
    return list(map(just_flatten, zip(*alignments)))
