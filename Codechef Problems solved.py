from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import sys

links = {}

def display_all_problems(user):
    try:
        try:
            response = requests.get('https://www.codechef.com/users/'+user)
        except:
            input('response could not be created')
            return False
        
        try:
            soup = BeautifulSoup(response.text,'lxml')
        except:
            input('Could not make soup')
            return False

        content = soup.find('section',{'class':'rating-data-section problems-solved'})
        Solved = content.find_all(['h5'])
        sets = content.find_all(['article'])
	
        print('\n')
        for i in range(0,2):
            print(Solved[i].text)
            types = sets[i].find_all(['p'])
	        
            for typ in types:
                competition = typ.find(['strong']).text
                print(competition,end = ' ')
                problems = typ.find_all(['a'])
                for prob in problems:
                    links[prob.text]=prob['href']
                    print(prob.text,end = ' ')
                print()
	            
            print('\n')
	
        input('content found')
        return True
    except:
        input('content not found')
        return False


usr = input('Enter userhandle: ')
if not display_all_problems(usr):
    sys.exit()
problem = input('Enter problem code: ')
if problem in links.keys():
    driver = webdriver.Chrome()
    driver.get('https://www.codechef.com'+links[problem])
else:
    input('Problem not done by user')
