

from Levenshtein import ratio


class POS_tagger:
    def __init__(self):
        self.verbs = self.generate_verbs()
        self.personal_name = self.generate_personal_names()
        self.numbers = self.generate_numbers()
        self.common_words = self.generate_common_words()
        self.places_people = self.generate_places_and_peoples()
        return

    def tag_word(self, word):
        ''' Tag word based on internal dictionaries '''
        w = word.replace('ś','s').replace('ŕ','r').replace('ḿ','n')
        # Try to find a exact match first
        match = []
        for v in self.verbs:
            if v[0] == w:
                match.append(['Verb', v])
        for pn in self.personal_name:
            if pn[0] == w:
                match.append(['Personal Name', pn])
        for nn in self.numbers:
            if nn[0] == w:
                match.append(['Quantity', nn])
        for cw in self.common_words:
            if cw[0] == w:
                match.append(['Name', cw])
        for p in self.places_people:
            if p[0] == w:
                match.append(['PlacesPeople', p])

        if len(match) == 0:
            for v in self.verbs:
                if ratio(v[0],w) >= 0.9:
                    match.append(['Sim Verb', v])
            for pn in self.personal_name:
                if ratio(pn[0],w) >= 0.9:
                    match.append(['Sim Personal Name', pn])
            for nn in self.numbers:
                if ratio(nn[0],w) >= 0.9:
                    match.append(['Sim Quantity', nn])
            for cw in self.common_words:
                if ratio(cw[0],w) >= 0.9:
                    match.append(['Sim Name', cw])
            for p in self.places_people:
                if ratio(p[0],w) >= 0.9:
                    match.append(['Sim PlacesPeople', p])




        return match


    def generate_places_and_peoples(self):
        ''' Generate places and peoples, mostly for coins '''
        pp = []
        people = [['oskun','iberian'],
                  ['arses', 'iberian'],
                  ['laies', 'iberian'],
                  ['otobe', 'iberian'],
                  ['oskum', 'iberian'],
                  ['neron', 'iberian'],
                  ['untikes','iberian'],
                  ['seteis','iberian'],
                  ['iltirkes','iberian'],
                  ['auses','iberian'],
                  ['untikir','iberian']]
        suffix_people = [['ken', 'From the people of'],
                         ['','']]

        for p in people:
            name = p[0]
            desc_p = p[1]
            for row in suffix_people:
                suffix = row[0]
                desc = row[1]
                pp.append([f'{name}{suffix}', name, suffix, f'{desc} {name} {desc_p}'])

        return pp


    def generate_common_words(self):
        ''' Generate a dictionary of common names '''
        common_names_dict = []
        terms = [['kutur', 'letter/document'], 
                  ['kastaun', 'spindle whorl'], 
                  ['baikar', 'cup/glass/plate'], 
                  ['eriar', 'pottery'], 
                  ['seltar', 'grave'], 
                  ['siltar', 'grave'],
                  ['salir', 'money'],
                  ['otar', 'bronze'],
                  ['etar', 'bronze'],
                  ['kite', 'silver'],
                  ['kitar', 'silver'],
                  ['kurs', 'unknown']]

        suffix_name = [['ban', 'the'], ['', '']]
        prefix_name = [['ban', 'the'],
                       ['is', 'this']]

        for term_row in terms:
            term = term_row[0]
            term_desc = term_row[1]
            for row in suffix_name:
                suffix = row[0]
                desc = row[1]
                common_names_dict.append([f'{term}{suffix}', term, suffix, f'{desc} {term_desc}'])
            for row in prefix_name:
                prefix = row[0]
                desc = row[1]
                common_names_dict.append([f'{prefix}{term}', term, prefix, f'{desc} {term_desc}'])

        return common_names_dict

        

    def produce_verb_dict(self, root):
        verbs_dict = []
        suffix_verb = ['', 'n', 'r', 'a', 'o', 'e', 'tan', 'tetine', 'tine', 'tetan',  'an', 'in', 'en', 'ar', 'ir', 'er', 'ur' , 'etan', 'itan', 'otan', 'atan', 'utan', 'atetan', 'etetan', 'itetan', 'otetan', 'utetan', 'atine', 'etine', 'itine', 'otine', 'utine', 'atetine', 'etetine','itetine','otetine','utetine', 'iar', 'ear', 'sar', 'sir', 'ser', 'saran', 'siran', 'seran', 'la', 'le', 'li', 'lo', 'lu', 'ain', 'ila', 'ile', 'ili', 'ilo', 'ilu', 'ana', 'ina', 'ena', 'ato', 'eto', 'ito', 'uto', 'irte', 'erte', 'arte', 'orte', 'urte' ]
        prefix_verb = ['', 't', 'it', 'bit', 'bi', 'e', 'i', 'bite', 'biti', 'ite', 'iti', 'ti', 'te', 's']

        for i in range(len(suffix_verb)):
            s = suffix_verb[i]
            for j in range(len(prefix_verb)):
                p = prefix_verb[j]
                cverb = f'{p}{root}{s}'
                verbs_dict.append([cverb, p, root, s])

        return verbs_dict


    def generate_verbs(self):
        ''' Apply some suffixes/prefixes to some roots '''
        verb_roots = ['euk', 'eki', 'ban', 'bas', 'tar', 'tak', 'rok', 'ust', 'unst', 'oka']
        all_verbs = []
        for r in verb_roots:
            v = self.produce_verb_dict(r)
            all_verbs.extend(v)

        all_verbs.append(['nai', 'n', 'ai', ''])


        return all_verbs



    def generate_numbers(self):
        ''' Generate numbers '''
        bases = ['', 'abar', 'abarke', 'bar', 'barke', 'orkei', 'orkeike', 'orkeiabar', 'lakei', 'erdi']
        units = ['', 'ban', 'ba', 'bin', 'bi', 'irur', 'laur', 'bors', 'sei', 'sisbi', 'sorse']
        nums_dict = []
        for i in range(len(bases)):
            s = bases[i]
            for j in range(len(units)):
                p = units[j]
                if len(s) == 0 and len(p) == 0:
                    continue
                if len(s) > 0 and len(p) > 0:
                    cnum = f'{s}{p}'
        
                elif len(s) > 0:
                    cnum = f'{s}'
                elif len(p) > 0:
                    cnum = f'{p}'

                nums_dict.append([cnum, s, p])
        # Add some suffixes - metals, uunits, etc.
        suffix = ['', 'tor', 'ei', 'te', 'otar', 'etar', 'kitar', 'kite']
        suffix_description = ['', 'Thing', 'fraction', 'ergative', 'bronze', 'of bronze', 'of silver', 'silver']
        numbers_dict_full = []
        for cname in nums_dict:
            for i in range(len(suffix)):
                s = suffix[i]
                name = cname[0]
                o = f'{name}{s}'
                o = o.replace('ee','e').replace('rr','r').replace('ss','s').replace('ii','i').replace('oo','o')
                o = [o]
                o.extend(cname)
                o.append(suffix_description[i])
                numbers_dict_full.append(o)
        clean_nums = []
        for cname in numbers_dict_full:
            name = cname[0]
            cname[0] = cname[0].replace('ee','e').replace('rr','r').replace('ss','s').replace('ii','i').replace('oo','o')
            clean_nums.append(cname)

        return clean_nums


    def generate_personal_names(self):
        ''' Generate a useful dictionary of personal names for the POS tagger '''
        # A somewhat safe and non-controversial list of prefixes/suffixes
        names = [['baise', 'baiser', None, None],
                  ['bilos', 'bilos', None, None],
                  [None, 'tibas', None, None],
                  ['esker', 'esker', None, None],
                  ['isker', 'isker', None, None],
                  ['ulti', None, None, None],
                  ['talsko', None, None, None],
                  ['iske', None, None, None],
                  ['kisker', None, None, None],
                  ['isbetar', None, None, None],
                  [None, 'ker', None, None],
                  [None, 'sker', None, None],
                  ['tartin', 'tartin', None, None],
                  ['tarti', 'tar', None, None],
                  [None, 'tanes', None, None],
                  ['turs', None, None, None],
                  ['biur', 'biur', None, None],
                  ['biurti', None, None, None],
                  ['tikan', 'tikan', None, None],
                  ['tikirs', 'tikirs', None, None],
                  ['tikis', 'tikis', None, None],
                  [None, 'tiker', None, None],
                  [None, 'tikar', None, None],
                  [None, 'tiki', None, None],
                  ['ortin', 'ortin', None, None],
                  ['tortin', 'ortin', None, None],
                  ['tarban', 'tarban', None, None],
                  [None, 'kine', None, None],
                  ['likine', None, None, None],
                  ['kelto', None, None, None],
                  [None, 'arker', None, None],
                  [None, 'teker', None, None],
                  [None, 'nius', None, None],
                  ['betu', None, None, None],
                  ['kule', None, None, None],
                  ['kules', None, None, None],
                  ['laur', 'belaur', None, None],
                  [None, 'balaur', None, None],
                  ['leis', 'tileis', None, None],
                  ['iltir', 'iltir', None, None],
                  ['sosin', 'sosin', None, None],
                  ['nalbe', None, None, None],
                  ['iltun', 'iltun', None, None],
                  ['alor', None, None, None],
                  ['alos', None, None, None],
                  ['alo', None, None, None],
                  ['aiun', None, None, None],
                  ['balke', None, None, None],
                  ['balkes', None, None, None],
                  ['laku', 'laku', None, None],
                  ['lako', 'lako', None, None],
                  ['lakon', 'lakon', None, None],
                  ['laker', 'laker', None, None],
                  ['salai', None, None, None],
                  ['arki', 'arkis', None, None],
                  [None, 'arkir', None, None],
                  [None, 'berton', None, None],
                  ['atin', 'atin', None, None],
                  ['beles', 'beles', None, None],
                  ['bels', 'bels', None, None],
                  ['bel', 'bel', None, None],
                  ['ikor', 'ikor', None, None],
                  ['tasku', None, None, None],
                  ['tas', 'tas', None, None],
                  ['sike', None, None, None],
                  ['sakar', None, None, None],
                  ['saka', None, None, None],
                  [None, 'unin', None, None],
                  [None, 'aunin', None, None],
                  [None, 'bas', None, None],
                  ['bin', 'bin', None, None],
                  ['akin', 'akin', None, None],
                  ['akir', None, None, None],
                  ['akiru', None, None, None],
                  ['abar', None, None, None],
                  ['ars', None, None, None],
                  [None, 'ir', None, None],
                  ['nerse', None, None, None],
                  ['selke', None, None, None],
                  ['selki', None, None, None],
                  ['kares', None, None, None],
                  ['bekon', 'bekon', None, None],
                  ['labeis', None, None, None],
                  ['betiki', 'beti', None, None],
                  ['iltur', 'iltur', None, None],
                  ['bikir', 'bikir', None, None],
                  ['biki', 'bikis', None, None],
                  ['aitu', None, None, None],
                  [None, 'betin', None, None],
                  [None,'', None, None],
                 ]
        # Generate names
        full_names = []
        for i in range(len(names)):
            prefix = names[i][0]
            if prefix is not None:
                for j in range(i+1, len(names)):
                    suffix = names[j][1]
                    if suffix is not None:
                        cn = [f"{prefix}{suffix}", prefix, suffix]
                        full_names.append(cn)
            suffix = names[i][1]
            if suffix is not None:
                for j in range(i+1, len(names)):
                    prefix = names[j][0]
                    if prefix is not None:
                        cn = [f"{prefix}{suffix}", prefix, suffix]
                        full_names.append(cn)

        # Remove unusual sequences 
        clean_full_names = []
        for cname in full_names:
            name = cname[0]
            cname[0] = cname[0].replace('ee','e').replace('rr','r').replace('ss','s').replace('ii','i').replace('oo','o')
            clean_full_names.append(cname)

        # Combine these names with common suffixes

        names_dict = []
        # -ar (for/from) -en (of, genitive) -te (ergative), -e (dative) -ka (recieve/give something)
        suffix_nominal = ['', 'te', 'ike', 'ite', 'ka', 'ika', 'ar', 'en', 'e', 'kate']
        suffix_description = ['', 'ergative', '?', '?', 'to recieve/give', 'to recieve/give', 'for/from', 'of', 'for', '?']
        for cname in clean_full_names:
            for i in range(len(suffix_nominal)):
                s = suffix_nominal[i]
                name = cname[0]
                o = [f'{name}{s}']
                o.extend(cname)
                o.append(f'{suffix_description[i]}')
                names_dict.append(o)
        # Add some verbs?

        # -nai (I am), -ai (you are), -tai (he/she/it/they is/are) -keai(we are)
        # Except -nai, the rest are completely made up
        suffix_izan = ['','nai','tai','ai','keai']
        suffix_description = ['', 'I am', 'is/are', 'are', 'are']
        names_dict_full = []
        for cname in names_dict:
            for i in range(len(suffix_izan)):
                s = suffix_izan[i]
                name = cname[0]
                o = f'{name}{s}'
                o = o.replace('ee','e').replace('rr','r').replace('ss','s').replace('ii','i').replace('oo','o')
                o = [o]
                o.extend(cname)
                o.append(suffix_description[i])
                names_dict_full.append(o)

        return names_dict_full



         



