#!/bin/python
# -*- coding: utf-8 -*-
#__ survey_credential.py _______________________________________
# Author: Frederic MAURY
# Date  : 2018/09/01
# Goal  : Survey CMS user credential
# WARNING : non compatible python3 use urllib
#________________________________________________________
import xmltodict
Output = "monfichier.csv"
heading = [
     'IP',
     'Hardware',
     'Hardware1',
     'Colonne4',
     'Colonne5'
]

values = []
## _______________________VARIABLE___________________________
filePath = "listIp.txt" # chemin du fichier contenant les ip
url = "http://121.52.155.234/status.xml"
user = "admin"
passwd = "1234"
##___________________________FUNCTIONS_________________________________

## __________________________VALIDER ET TESTER________________________
def connectUrl(url,user,passwd):
    '''
    Je me connecte en basic authent, et place le contenu de la page dans une variable
    prend trois parametre url, user,passwd
    return le contenu ou l'erreur
    '''
    import urllib2
    # create a password manager
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # Add the username and password.
    # If we knew the realm, we could use it instead of None.
    password_mgr.add_password(None, url, user, passwd)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)
    # use the opener to fetch a URL
    try:
        content = opener.open(url)
    except urllib2.HTTPError, e:
        content = e.code
    except urllib2.URLError, e:
        content = "URLError"

    return content


def fileInAList(filePath):
    '''
    j'ouvre un fichier, et je passe chaque ligne dans une liste, je retourne la liste
    un parametre "listPath" qui correspond au chemin du fichier
    '''
    with open(filePath, 'r') as tempoIp:
        tempoIp = tempoIp.readlines()
        listIp= []
        for line in tempoIp:
            listIp.append(line.rstrip())
    return listIp

def writeCsv(path,heading,values):
    '''
    headings = [
         u'HardSerial',
         u'Colonne2',
         u'Colonne3',
         u'Colonne4',
         u'Colonne5'
    ]

    values = [
         [u'Valeur1', u'Valeur2', u'Valeur3', u'Valeur4', u'Valeur5'],
         [u'Valeur6', u'Valeur7', u'Valeur8', u'Valeur9', u'Valeur10'],
         [u'Valeur11', u'Valeur12', u'Valeur13', u'Valeur14', u'Valeur15']
    ]
    this function take 3 args (path,heading,values)
    path = path of file
    values = list of value[class list]
    heading = heading of board
    '''
    f = open(path, 'w')
    ligneHeading = ";".join(heading) + "\n"
    f.write(ligneHeading)
    for value in values:
        line = ";".join(value) + "\n"
        f.write(line)

    f.close()

class AllMyFields:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

def main(user,passwd,filePath,Output,heading,values):

    listIp = fileInAList(filePath)

    for ip in listIp:
        url ='http://'+ip+'/status.xml'
        #j'essaye d'ouvrir la page pour récuperer le contenu
        try:
            file = connectUrl(url,user,passwd)
            print(ip)
            doc = xmltodict.parse(file.read())
            try:
                # je récupère les champs du XML qui m'interesse
                HardSerial = doc['Status']['SystemUnit']['Hardware']['Module']['SerialNumber']['#text']
            except:
                # si le champ n'est pas présent je marque "NA"
                HardSerial = "NA"
            try:
                # je récupère les champs du XML qui m'interesse
                HardSerial1 = doc['Status']['SystemUnit']['Hardware']['Module']['SerialNumber']['#text']
            except:
                # si le champ n'est pas présent je marque "NA"
                HardSerial1 = "NA"
            #je rentre la liste obtenue dans une variable
            value = [ip,HardSerial, HardSerial]
        #si la page ne s'ouvre pas
        except:
            errorCode = connectUrl(url,user,passwd)
            value = [ip,errorCode]
        #je rentre les variables dans la liste values
        values.append(value)
        writeCsv(Output,heading,values)
    #j'écris les
main(user,passwd,filePath,Output,heading,values)
#doc['mydocument']['@has'] # == u'an attribute'
#doc['mydocument']['and']['many'] # == [u'elements', u'more elements']
#doc['mydocument']['plus']['@a'] # == u'complex'
#doc['mydocument']['plus']['#text'] # == u'element as well'
