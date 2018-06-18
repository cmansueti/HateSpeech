import string
import nltk
import requests
from bs4 import BeautifulSoup

#loop through all pages under DS Jewish tab (25 total)
urlBase = "https://dailystormer.name/section/jewish-problem/"

for i in range(1, 26):
    urlBasePageNumber = "https://dailystormer.name/section/jewish-problem/page/"
    numStr = str(i)
    urlBasePageNumber += numStr
    urlBasePageNumber += "/"

    #download page using requests.get method
    page = requests.get(urlBasePageNumber)

    if page.status_code >= 200 and page.status_code < 400:
        print("page download successful")
        print(page.status_code)
    else:
        print("page download not successful")
        print(page.status_code)


    #parse html document
    soup = BeautifulSoup(page.content, 'html.parser')

    #find all links that redirect to articles
    links = soup.findAll("a", {"class": "more-link"})
    num_of_links = len(links)

    #for each article redirect in links, go to that page and extract paragraphs
    #and write to a text file with the name of the article/page
    for i in range(0, num_of_links):
        pageX = requests.get(links[i].get('href'))
        if pageX.status_code >= 200 and page.status_code < 400:
            #parse html document
            soupX = BeautifulSoup(pageX.content, 'html.parser')
            #find all paragraphs
            paragraphs = soupX.find_all('p')
            #count number of paragraph tags in document
            num_of_parag = len(paragraphs)
            #put all paragraphs into one string
            str1=''
            for i in range(0, num_of_parag):
                str1+= ' ' + paragraphs[i].get_text()
        
            #get title of web page and store in a string
            title = soupX.title.string
            #remove whitespaces from title
            title = title.replace(" ", "")
            title = title.replace("/", "")
            title = title.replace("-", "")
            #make title the name of a text file
            title += '.txt'
        
            #write paragraphs as one long string to text file
            str1 = str1.encode('ascii', 'ignore').decode('ascii')
            outfile = open(title, "w+")
            outfile.write(str1)
            outfile.close()
        
            pageX.close()
        else:
            print("page download not successful")
            print(page.status_code)
    
    page.close()
        
    






