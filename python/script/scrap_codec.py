#!/bin/python3.4
# -*- coding: utf-8 -*-
#__ scrap_codec.py _______________________________________
# Author: Frederic MAURY
# Date  : 2018/09/01
# Goal  : Scrapper : upload wallpaper cisco codec sx20
# j'importe les librairie nécessaire pour mon script
#yum install python
#yum install python-pip (au pire tu fais yum search)
# on les installe avec pip install <nom de librairie>
'''
Comme tu peux le voir en haut, il est utilisé avec python3.4, et il s'éxécute avec
chmod o+x comme un script
Normalement il devrait être compatible toute les versions mais non testé
bref à partir de la trois sur, il suffit donc de changer le !/bin/python2.7 par ex.
prérequis : yum -y install gtk3-devel gtk3-devel-docs
wget https://chromedriver.storage.googleapis.com/2.42/chromedriver_linux64.zip
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
un peu de doc : http://chromedriver.chromium.org/getting-started
encore un peu de doc : https://selenium-python.readthedocs.io/installation.html
au pire tu connais un bon site de dev
SINON :
quand tu ouvre un page internet avec un brownser (chrome ou firefox, le reste c'est de la merde mais c'est mieux chrome
 vu que j'utilise son moteur pour le bot)tu peux appuyer sur f12
tu arrive sur l'inspecteur, a gauche de l'inspecteur tu a une icone sélectionner un élément sur la page
tu séléctionne l'élément que tu veux boutton cliquable (voir plus bas .click()), ou champ de texte(send_keys)
clic droit sur la console de ton navigateur sur l'élément qui devrait être surligner en bleu et copier en tant que xpath.
Comme tu peux le voir plus bas je sélectionne aussi byname, il donc d'autre moyen de sélectionner mais
ca nécessite de connaître un peu le html, c'est pas compliqué juste un peu de boulot.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

#brownser option
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


#variables
user = "user"
passwd = "password"
url = ""
#je spécifie le webbrownser, j'ai mis le chromedriver dans /root/scrapper
driver = webdriver.Chrome(executable_path="/root/scrapper/chromedriver", chrome_options=chrome_options)
#je spécifie l'url
driver.get(url);


#j'attend que la page se charge (ou pas a voir)
time.sleep(1)
driver.get_screenshot_as_file('/root/scrapper/google.png')





# authentification, je rempli les champs
driver.find_element_by_name("username").send_keys(user)
driver.find_element_by_name("password").send_keys(passwd)
# je prend un screenshot pour voir si ca marche
driver.get_screenshot_as_file('/root/scrapper/authent.png')
# je click sur le bouton pour me logger
driver.find_element_by_xpath("/html/body/div/form/div/div[2]/button").click()
# je fais une pause de 5s (pour atttendre que la page se charge, c'est un peu trop j'ajusterais)
time.sleep(5)
#screen
driver.get_screenshot_as_file('/root/scrapper/afterauthent.png')
#je rempli le champ pour upload le fichier, il était caché dans le code xD les petits malin
#normalement c'est input quelquechose
driver.find_element_by_xpath("/html/body/div/div/form/div/input").send_keys("/root/scrapper/google.png")
# et je click sur upload et la suis un peu con car je peux pas supprimer le fond d'écran que j'ai mis en corée.
driver.find_element_by_xpath("/html/body/div/div/form/button").click()
#je prend un screen de vérif
driver.get_screenshot_as_file('/root/scrapper/file.png')
# je quitte le programme
driver.quit()
