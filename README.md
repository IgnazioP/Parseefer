# Parseefer
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
