# Exercice 1

###############################################################################
# Question 1
###############################################################################

def le_mot_est_ici(texte, mot, i):
    """ Précondition : i <= len(t) - len(m)
        Retourne Vrai si m[0] == t[i] et m[1] == t[i + 1] et ... et m[len(m) - 1] == t[i + len(m) - 1]
        Retourne Faux sinon
    """
    j = 0
    while j < len(mot) and mot[j] == texte[i + j]:
        j = j + 1
    if j == len(mot):
        return True
    else:
        return False

def recherche_mot(texte, mot):
    """ Retourne le plus petit indice i tel que :
                     t[i] == m[0] et t[i + 1] == m[1] et ... et t[i + len(m) - 1] == m[len(m) - 1]
        Retourne -1 si cet indice n'existe pas
    """
    i = 0
    while i <= len(texte) - len(mot) and not le_mot_est_ici(texte, mot, i):
        i += 1
    if i > len(texte) - len(mot):
        return -1
    else:
        return i

# Jeu de tests

text = list('Je suis en BCPST en 1ère année')
mot = list('en')
mot2 = list('easdf')

assert recherche_mot(text, mot) == 8
assert recherche_mot(text, mot2) == -1


###############################################################################
# Question 2
###############################################################################

def modifier_mot(texte, mot, i):
    """ Précondition : indice <= len(texte) - len(mot)
        Retourne texte2, une copie de texte, sauf pour
        texte2[indice] == mot[0], texte2[indice+1] == mot[1], etc
    """

    a=0
    b=0
    while a <= len(texte)-len(mot):
        a+=1 #needed sinon boucle infinie car sinon il augmente pas quand a > len mot
        #donc sort jamais boucle car a tjrs le meme
        while b < len(mot):
            texte[i]=mot[b]
            b+=1
            i+=1
    return texte

#besoin b en plus de a

# Jeu de tests
text = list('Je suis en BCPST en 1ère année')
mot = list('ne')
text2 = list('Je suis ne BCPST en 1ère année')

assert modifier_mot(text, mot, 8) == text2



###############################################################################
# Question 3
###############################################################################


def chercher_et_remplacer(texte, mot1, mot2):
    """ Précondition : len(mot1) == len(mot2)
        Retourne la liste de chaînes texte où mot1 est remplacé par mot2
        Retourne texte si mot1 n'est pas présent"""
#tout d abord, cherchons mot1 dans texte:
    i=0
    j=0
    n=0 #n: nombre de fois qu'il a fait else
    is_broken=False
    while i<len(texte)and j<len(mot1): #pas <= sinon  index out of range
        if texte[i]==mot1[j]:
            i+=1
            j+=1
        else:
            j=0
            i+=1#pas oublier
            n+=1
            if n>=len(texte):
                is_broken=True
                print("ca a marché.le mot n'est pas trouvé")
                break#sort de la boucle
    if not is_broken:
        i-=len(mot1)
        modifier_mot(texte, mot2, i)#return i #retourne la position de l'indice
        f=0
        while f<len(mot2):
            texte[i] = mot2[f]
            i+=1
            f+=1
            texte2=texte

    #if mot1 in texte:

    else:
        return -1
        texte2=texte

    return texte2


#Jeu de tests
texte = list('Je suis en BCPST en 1ère année')
mot2 = list('ne')
mot1 = list('en')
texte2 = list('Je suis ne BCPST en 1ère année')



assert chercher_et_remplacer(texte, mot2, mot2) == texte
#assert chercher_et_remplacer(texte, mot1, mot2) == texte2


###############################################################################
# Question 4
###############################################################################


def chercher_et_remplacer_tout(texte, mot1, mot2):
    """ Retourne une liste de chaîne de caractères où les occurrences de mot1
        ont été remplacées par les occurrences de mot2
    """



# Jeu de tests

text = list('Je suis en BCPST en 1ère année')
mot2 = list('ne')
mot1 = list('en')
text2 = list('Je suis ne BCPST ne 1ère année')

#assert chercher_et_remplacer_tout(text, mot1, mot2) == text2

###############################################################################
# Question 5
###############################################################################


def modifier_mot2(texte, mot, indice1, taille):
    """ Précondition : indice <= len(texte) - taille
        Retourne texte2, une copie de texte,
        où on a remplacé la liste de chaînes de caractères de taille taille par
        la liste de chaînes de caractère mot.
    """



# Jeu de tests

text = list('Je suis en BCPST en 1ère année')
mot = list('encore en')
text2 = list('Je suis encore en BCPST en 1ère année')

#assert modifier_mot2(text, mot, 8, 2) == text2


###############################################################################
# Question 6
###############################################################################

def chercher_et_remplacer_tout2(texte, mot1, mot2):
    """ Retourne une liste de chaîne de caractères où les occurrences de mot1
        ont été remplacées par les occurrences de mot2
    """

# Jeu de tests
text = list('Je suis en BCPST en 1ère année')
mot2 = list('none')
mot1 = list('en')
text1 = list('Je suis en BCPST en 1ère année')
text2 = list('Je suis none BCPST none 1ère année')

#assert chercher_et_remplacer_tout2(text1, mot1, mot2) == text2

mot3 = list('encore en')
text3 = list('Je suis encore en BCPST encore en 1ère année')

#assert chercher_et_remplacer_tout2(text1, mot1, mot3) == text3




