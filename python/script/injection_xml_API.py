#need to install with pip requests and beautifulsoup4
# import module
import lxml
import requests
import json
import time
import os
import re
import sys
from bs4 import BeautifulSoup


############## need to install a parser
 ###https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser

## Main function for each url feed by "url.txt", i do something
def main():

    for ip in url_list :

        try:
            my_file = open('output.txt', "a") #I open the output file
            url ='http://'+ip+'/getxml?location=/Status/HttpFeedback'
            print(url) #control string url
            my_file.write(str(url))
            # connect and define time in second.
            response = requests.get(url, auth=('censuré', 'censuré'), timeout=4)

            print(response.text)


            with open('tempo.xml', 'w') as my_tempo:
                my_tempo.write(str(response.text))
            parseLog('tempo.xml')
            #soup = BeautifulSoup('tempo.xml', 'html.parser')
            #for p in soup.find_all('HttpFeedback'):
            #        print(p)

            print(response.status_code)
            my_file.write(str(response.status_code))

            #print(response.content)
        except requests.exceptions.Timeout: #catch timeout error
            error_time = print("Timeout occured")
            my_file.write(str("Timeout occured"))
        finally:
            my_file.write('\n')
            my_file.close # i close the file.

def parseLog(file):
    handler = open(file).read()
    soup = BeautifulSoup(handler, "xml")
    for p in soup.find_all('HttpFeedback'):
        print(p)




#I open url file and strip the newline character, the loop for have issue here.
url_list = [line.rstrip('\n') for line in open('url.txt')]
main()
