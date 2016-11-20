import re

def parsetype1(ref):
 # first type of reference, with name of journal and volume separated by comma & space ", "
    pattern = re.compile("\d\d\d\d,")
    m = pattern.search(ref)
    i1 = m.start() 
    i2 = m.end()
    string = m.string  # initial reference
    string2 = string[i2:]  #  all the rest but year and authors
    authors = string[0:(i1-1)]  # everything before the year is the list of authors
    j2 = [m2.start() for m2 in re.finditer(', ', authors)] # find the separator in authors' string
    nauthors = len(j2)+1
    if nauthors is 1: 
        firstauth = authors
    else: 
        firstauth = authors[0:(j2[0])]
    year = string[i1:(i2-1)] # this is the year of the publication
    j1 = [m1.start() for m1 in re.finditer(', ', string2)] # find the separator of year, volume and page, j1 is a list
    journal = string2[1:j1[0]]                           # the journal (as a string)
    volume  = string2[(j1[0]+2):j1[1]]                   # the volume (as a string)
    page    = string2[(j1[1]+2):]                        # the page   (as a string)
    parsedlist = {'firstauth':firstauth, 'authors':authors, 'year':year, 
                  'journal':journal, 'volume':volume, 'page':page}
    return parsedlist


def parsetype1a(ref):
 # first type of reference with name of journal and volume separated by a space
    pattern = re.compile("\d\d\d\d,")
    m = pattern.search(ref)
    i1 = m.start() 
    i2 = m.end()
    string = m.string  # initial reference
    string2 = string[i2:]  #  all the rest but year and authors
    authors = string[0:(i1-1)]  # everything before the year is the list of authors
    j2 = [m2.start() for m2 in re.finditer(', ', authors)] # find the separator in authors' string
    nauthors = len(j2)+1
    if nauthors is 1: 
        firstauth = authors
    else: 
        firstauth = authors[0:(j2[0])]
    year = string[i1:(i2-1)] # this is the year of the publication
    j1 = [m1.start() for m1 in re.finditer(', ', string2)]   # find the separator of year, volume and page, j1 is a list
    tmpjournal = string2[1:j1[0]]                            # the journal+volume (as a string) es.: APJ 500
    j3 = [m3.start() for m3 in re.finditer(' ', tmpjournal)] # separate journal name from volume
    journal = tmpjournal[:j3[0]]                             # journal name
    volume  = tmpjournal[(j3[0]+1):]                         # the volume (as a string)
    page    = string2[(j1[0]+2):]                            # the page   (as a string)
    parsedlist = {'firstauth':firstauth, 'authors':authors, 'year':year, 
                  'journal':journal, 'volume':volume, 'page':page}
    return parsedlist

def parsetype2(ref):
    pattern=re.compile("(\d\d\d\d)") # match year second type
    m=pattern.search(ref)
    i1 = m.start() 
    i2 = m.end()
    string = m.string  # initial reference
    year = string[(i1):(i2)] # this is the year of the publication
    string2 = string[:(i1-2)]  #  everything but the year 
    j1 = [m1.start() for m1 in re.finditer(', ', string2)] # find the separator in string2
    authors = string2[0:(j1[-2])]                    # everything before the year and the journal name is the list of authors
    journal = string2[(j1[-2]+2):(j1[-1])]               # the journal+volune (as a string)
    j2 = [m2.start() for m2 in re.finditer(' ', journal)] 
    volume  = journal[(j2[-1]+1):]                   # the volume (as a string)
    journal = journal[:(j2[-1])]                     # only the journal
    page    = string2[(j1[-1]+2):]                   # the page   (as a string)
    firstauth = authors[0:(j1[0])]
    nauthors = len(j1)-1
    parsedlist = {'firstauth':firstauth, 'authors':authors, 'year':year, 
                  'journal':journal, 'volume':volume, 'page':page}
    return parsedlist
    
def parsetype3(ref):
    pattern=re.compile("\d{1,}.")   # match Year and DOT: YYYY.
    m=pattern.search(ref)
    i1 = m.start() 
    i2 = m.end()
    string = m.string  # initial reference
    year = string[(i1):(i2-1)] # this is the year of the publication
    authors = string[:(i1-1)]  #  everything before the year is the authors list
    j1 = [m1.start() for m1 in re.finditer(', ', authors)] # find the separator in authors' string
    nauthors = len(j1)+1
    if nauthors is 1: 
        firstauth = authors
    else: 
        firstauth = authors[0:(j1[0])]
    string2 = string[(i2+1):]
    j2 = [m2.start() for m2 in re.finditer(' ', string2)] 
    j3 = [m3.start() for m3 in re.finditer(':', string2)] 
    journal = string2[:j2[0]]                           # the journal (as a string)
    volume  = string2[(j2[0]+1):j3[0]]                   # the volume (as a string)
    j4 = [m4.start() for m4 in re.finditer('-', string2)] 
    page    = string2[(j3[0]+1):j4[0]]                        # the page   (as a string)
    parsedlist = {'firstauth':firstauth, 'authors':authors, 'year':year, 
                  'journal':journal, 'volume':volume, 'page':page}
    return parsedlist
    

def parsetype4(ref):
    pattern = re.compile("\D{1,}\d{1,}")
    m = pattern.search(testref4)
    string = m.string
    string1= string[m.start():m.end()]
    string2= string[(m.end()+2):]
    j1 = [m1.start() for m1 in re.finditer(' \d{1,}', string1)]
    authors=string1[0:j1[0]]
    j1a = [m1a.start() for m1a in re.finditer(',', string1)]
    if j1a is 1:
        firstauth=authors
    else:
        firstauth=string1[0:j1a[0]]
    year   =string1[(j1[0]+1):]
    j2 = [m2.start() for m2 in re.finditer(' \(\D{1,}', string2)]
    title  = string2[0:j2[0]]
    j3 = [[m3.start(),m3.end()] for m3 in re.finditer('\(\D{1,}: ', string2)]
    editor =string2[j3[0][1]:(-1)]
    town   =string2[(j3[0][0]+1):(j3[0][1]-2)]
    parsedlist = {'firstauth':firstauth, 'authors':authors, 'year':year, 
                 'editor':editor, 'town':town}
    return parsedlist


def parsetype5(ref): 
    # type 5 is similar to type 4, only Title is preceded by " in"
    pattern = re.compile("\D{1,}\d{1,}")
    m = pattern.search(testref5)
    string = m.string
    string1= string[m.start():m.end()]
    string2= string[(m.end()+2):]
    j1 = [m1.start() for m1 in re.finditer(' \d{1,}', string1)]
    authors=string1[0:j1[0]]
    j1a = [m1a.start() for m1a in re.finditer(',', string1)]
    if j1a is 1:
        firstauth=authors
    else:
        firstauth=string1[0:(j1a[0]+4)]
    year   =string1[(j1[0]+1):]
    j2 = [m2.start() for m2 in re.finditer(' \(\D{1,}', string2)]
    title  = string2[3:j2[0]]
    j3 = [[m3.start(),m3.end()] for m3 in re.finditer('\(\D{1,}:\D{1,}\)', string2)]
    string3 = string2[j3[0][0]:j3[0][1]]
    j4 = [m4.start() for m4 in re.finditer(': ', string3)]
    town  =string3[1:j4[0]]
    editor=string3[(j4[0]+2):-1]
    volume=string2[(j3[0][1]+2):]
    parsedlist = {'firstauth':firstauth, 'authors':authors, 'year':year, 
                  'editor':editor, 'volume':volume, 'town':town}
    return parsedlist


def parsetype6(ref): 
    pattern = re.compile("\d{1,},")
    m = pattern.search(testref6)
    string = m.string
    string1= string[0:m.start()]
    string2= string[(m.end()+1):]
    j1 = [m1.start() for m1 in re.finditer(', et. al\.', string1)]
    firstauth=string1[0:j1[0]]
    authors=string1
    year   =string[m.start():(m.end()-1)]
    j2 = [m2.start() for m2 in re.finditer(' \d{1,}', string2)]
    journal = string2[:(j2[0])]
    if journal[-3:] == 'No.': journal= journal[:-4]
    volume  = string2[(j2[0]+1):]
    parsedlist = {'firstauth':firstauth, 'authors':authors, 'year':year, 
                  'journal':journal, 'volume':volume}
    return parsedlist


def parsetype7(ref):
    pattern = re.compile("Ph. D. Thesis")
    m = pattern.search(testref7)
    string = m.string
    string1= string[0:m.start()]
    string2= string[(m.end()+1):]
    j1 = [[m1.start(),m1.end()] for m1 in re.finditer('\d{1,4}',string1)]
    year = string1[j1[0][0]:j1[0][1]]
    authors=string1[:(j1[0][0]-1)]
    firstauth= authors
    editor= string2[1:-1]
    parsedlist = {'firstauth':firstauth, 'authors':authors, 'year':year, 
                  'editor':editor}
    return parsedlist


# ------------------------------------------------------------------------------------------
def parseefer(ref):

    """ 'Parseefer' is a set of python functions to parse a reference string and return a dictionary with:
    - authors, 
    - first author, 
    - journal, 
    - volume, 
    - page and 
    - year of the publication.
    In case of book or proceedings it returns town and editor instead of journal and volume. 
    Various formats of references are considered and can be parsed, 
    however the lack of a standard for reference format complicates things.
    New formats can be easily added with a proper REGEX pattern search and a related formatting 
    function.
    Currently these formats are recognized and parsed: 
    - 1. Journals in "modern" Astronomical style:
      "Accomazzi, A., Eichhorn, G., Kurtz, M. J., Grant, C. S., & Murray, S. S. 2000, A&AS, 143, 85"
    - 1a. Journals in modern astro style missing a comma between Journal and Volume: 
      "Bar-Kana R. 1997, ApJ 489, 21"
    - 2. Journals in "modern" Physics style:
      "J. B. Gupta, K. Kumar, and J. H. Hamilton, Phys. Rev. C 16, 427 (1977)."
    - 3. Journals in "Annual Reviews" style:
      "Adainson M, Kerr Th, Whittet DCB, Duley WW. 1994. MNRAS 268:705-8"
    - 4. Books:
      "Wali, K. 1991, Chandra: A Biography of S. Chandrasekhar (Chicago: Univ. Chicago Press)"
    - 5. Conferences and conference series:
      "Rees, M. J. 1984, in Formation and Evolution of Galaxies and Large Scale Structure in the Universe, ed. J.
      Audouze and T. T. Van (Dordrecht: Reidel), 271"
    - 6. Various small publications:
      "Hermsen, W., et. al. 1992, IAU Circ. No. 5541"
    - 7. Ph. D. theses:
      "Pollock, J. T. 1982, Ph. D. Thesis, University of Florida."
    Author: Ignazio Pillitteri. 11/20/2016
    """
    p1 =  re.compile("\d{1,},\s{1,1}\D{1,},{1,1}\s{1,1}\d{1,},\s{1,1}") #  modern astro - type 1
    p1a = re.compile("\d{1,},\s{1,1}[\w&]{1,}\s{1,1}\d{1,},\s{1,1}")    #  modern astro - type 1a 
    p2 = re.compile("\d{1,},\s\d{1,}\s\(\d{1,}\).")                     #  modern phys. - type 2
    p3 = re.compile("\d{1,}.\s\D{1,}\s\d{1,}:\d{1,}-\d{1,}")            #  ann. review - type 3
    p4 = re.compile("\D{1,}\d{1,}\D{1,}\(\D{1,}:\D{1,}\)")              #  book  - type 4
    p5 = re.compile("\D{1,}\d{1,}\D{1,}\(\D{1,}:\D{1,}\),\s\d{1,}")     #  book - type 5
    p6 = re.compile("et. al.")                                          #  Misc. - type 6 
    p7 = re.compile("Ph. D. Thesis")                                    #  Ph. D. Thesis - type 7

    m1 = p1.search(ref)
    m1a = p1a.search(ref)
    m2 = p2.search(ref)
    m3 = p3.search(ref)
    m4 = p4.search(ref)
    m5 = p5.search(ref)
    m6 = p6.search(ref)
    m7 = p7.search(ref)

    parsedlist= None
    print m1, m1a, m2, m3, m4, m5, m6, m7               # TMP
    if (m1 is not None): parsedlist= parsetype1(ref)
    if (m1a is not None): parsedlist= parsetype1a(ref)
    if (m2 is not None): parsedlist= parsetype2(ref)
    if (m3 is not None): parsedlist= parsetype3(ref)
    if (m4 is not None): parsedlist= parsetype4(ref)
    if (m5 is not None): parsedlist= parsetype5(ref)
    if (m6 is not None): parsedlist= parsetype6(ref)
    if (m7 is not None): parsedlist= parsetype7(ref)
    return parsedlist


