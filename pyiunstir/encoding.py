import xml.etree.ElementTree as ET


def decode_iberian(line, encoding, fmt="simplified"):
    """ Use an iberian JSON encoding to decode a text into one of the supported
        output formats (dual, simplified or SVG):

        line:list: list of symbols
        encoding:json: encoding infomation
        fmt:str: output format (simplified, dual or iberian)

        Returns a string (dual or simplied) or a list of strings (iberan)"""

    output = []
    for current_chr in line:
        if current_chr < 0:
           current_chr = 0

        for dict_chr in encoding:
            if dict_chr["id"] == current_chr:
                output.append(dict_chr[fmt])
    if fmt != "iberian":
        output = "".join(output)
    return output


def break_syl(word):
    """ Splits a word in elements taking into account the semisyllabic
        nature of most of the iberian scripts (all letters but ka, ta, ba, etc.).

        E.g. biderogan --> ['bi', 'de', 'r', 'o', 'ga', 'n']
    """

    output = []
    word = word.strip().replace(" ", "")
    for i, str_chr in enumerate(word):
        if str_chr in ("k", "g", "d", "t", "b"):
            output.append(str_chr)
            if i < len(word) - 1 and (word[i + 1] not in ("a", "e", "i", "o", "u")):
                output.append("e ")
            elif i == len(word) - 1:
                output.append("e ")
        else:
            output.append(str_chr)
            output.append(" ")
    output = "".join(output).strip()
    return output.split(" ")


def standarize_word(word):
    """ Standarize some particularities of the iberian scripts """

    changes = [
        ["binḿr", "binar"],
        ["ś", "s"],
        ["ŕ", "r"],
        ["nḿl", "nal"],
        ["nḿb", "num"],
        ["uḿb", "um"],
        ["ḿb", "um"],
        ["ḿlbe", "nalbe"],
        ["nḿ", "na"],
        ["ḿ", "na"],
        ["baborotenbo", "protemo"],
    ]

    change_ends = [
        ["um", "un"],
        ["kem", "ken"],
        ["bim", "bin"],
        ["bam", "ban"],
        ["bami", "bani"],
    ]

    change_starts = [["nbat", "mat"], ["bare", "mare"]]

    for change in change_ends:
        if word.endswith(change[0]):
            word = word.replace(change[0], change[1])

    for change in changes:
        word = word.replace(change[0], change[1])

    for change in change_starts:
        if word.startswith(change[0]):
            word = word.replace(change[0], change[1])

    return word

def standarize_input(word):
    ''' Replace several letter combinations with iberian equivalents '''

    changes = [
        ["j", "i"],
        ["p", "b"],
        ["v", "b"],
        ["tra", "tar"],
        ["tre", "ter"],
        ["tri", "tir"],
        ["tro", "tor"],
        ["tru", "tur"],
        ["bra", "bar"],
        ["bre", "ber"],
        ["bri", "bir"],
        ["bro", "bor"],
        ["bru", "bur"],
        ["dra", "dar"],
        ["dre", "der"],
        ["dri", "dir"],
        ["dro", "dor"],
        ["dru", "dur"],
        ["kra", "kar"],
        ["kre", "ker"],
        ["kri", "kir"],
        ["kro", "kor"],
        ["kru", "kur"],
        ["gra", "gar"],
        ["gre", "ger"],
        ["gri", "gir"],
        ["gro", "gor"],
        ["gru", "gur"],
    ]

    for change in changes:
        word = word.replace(change[0], change[1])

    return word

def encode_iberian(line, encoding, signary="northeastern", dual=True):
    """ Encode a human-readable text using one of the available
        encodings (northeastern, southeastern, greekiberian):

        line:str: text to encode allowed characters (a,e,i,o,u,r,ŕ,s,ś,k,g,t,d,b,l,n,_,- and :)
                  and m,ḿ,ñ only for northeastern
        encoding:json: information about symbols
        signary:str: output format (northeastern, southeastern, greekiberian)

        Retunrs a list of integers
    """

    output = []
    common_chars = ["_", ":", "-"]

    source = 'dual'

    if signary == 'southeastern':
        dual = False

    if not dual:
        line = line.replace("g", "k").replace("d", "t")
        source = 'simplified'

    if signary != 'northeastern':
        line = line.replace('m', 'nb')

    if signary != 'greekiberian':
        line = standarize_input(line)
        line = break_syl(line)
    else:
        line = line.replace('j','i').replace('p','b').replace('v','b')

    for str_chr in line:
        for dict_chr in encoding:
            if dict_chr["signary"].lower() != signary.lower() and not str_chr in common_chars:
                continue
            if dict_chr[source] == str_chr:
                output.append(dict_chr["id"])
                break

    return output

def render_letter(list_of_letters):
    """ Generates a text that can be used with SVG() to produce a
        image for notebooks (iberian encoding)
    """

    nletters = len(list_of_letters)

    svg = ET.Element(
        "svg",
        xmlns="http://www.w3.org/2000/svg",
        version="1.1",
        height="4em",
        width=f"{2.15*nletters}em",
    )

    mat = ET.SubElement(svg, "g", transform="matrix(0.03,0,0,-0.03,0,0)")
    i = 0
    for symbol in list_of_letters:
        c = ET.SubElement(mat, "g", transform=f"translate({i},-750)")
        d = ET.SubElement(c, "path", fill="darkred", d=symbol)
        i += 1000
    return ET.tostring(svg)
