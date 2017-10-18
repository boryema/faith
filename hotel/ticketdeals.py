import sys
sys.path.append("/home/woo/git_repos/expediascraperoneway")
import requests
from lxml import html
from collections import OrderedDict

def checkingForNonEmptyList(url):
    testingValue = 1
    json_data_xpath =[]
    
    while(testingValue==1):
        print(url)

        response = requests.get(url)

        parser = html.fromstring(response.text)
        print parser
        exit()

        json_data_xpath = parser.xpath("//script[@id='cachedResultsJson']//text()")
        
        lenghtOfjson_data_xpath = len(json_data_xpath)
        
        if not lenghtOfjson_data_xpath:
            testingValue = 1 
            print ("List is Empty")
        else:
            testingValue = 0
            print ("List is Not Empty")
    
    return json_data_xpath 
            
        
        
    

            
            
    

            
            
    
        

#def openBrowserToPurchaseTicket(url):
    #response=raw_input("Do you want to purchase the tickets? (Y/N): ")
    #response = response.capitalize().strip()

    #if(response=="Y"):
        #new = 2
        #webbrowser.open(url, new)
    #else:
        #print ("Proceed with the program")

