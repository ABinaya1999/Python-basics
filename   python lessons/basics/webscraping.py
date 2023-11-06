# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://news.ycombinator.com/')
# # # f.writet(response.status_code)
# # # f.writet(response.content)
# soup = BeautifulSoup(response.content,'html.parser')
# # f.writet(soup.prettify())

# # f.writet(soup.find('center'))
# # f.writet(soup.find('a'))
# # f.writet(len(soup.find_all('a')))

# news = soup.find_all('span', class_="titleline")
# f.write(news)
# with open('news.txt', 'w') as f:
#     for item in news:
#         f.write(item.text)
#         f.write("    ")
#         f.write(item.find('a').get('href'))
#         f.write('\n')


# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://www.goodreads.com/quotes/tag/motivational')
# soup = BeautifulSoup(response.content, 'html.parser')

# quotes = soup.find_all('div', class_="quoteDetails")

# with open('quotes.txt', 'w') as f:
#     for i in quotes:
#         quote = i.find('div',class_= "quoteText").text.strip().replace('\n',"").split("      ―      ")
#         # quote = quote.split("      ―      ")
#         a = quote[0]
#         a = a.replace('“',"")
#         a = a.replace('”',"")
#         f.write(a)
#         f.write("\n")
#         # author = quote[1]
#         author = quote[1].split(",")[0]
#         f.write(author)
#         f.write("\n") 
#         like = i.find("a",class_="smallText").text.split(" ")
#         f.write(like[0])
#         f.write("\n")
        
#         f.write("******************\n")
        
        
# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://www.scrapethissite.com/pages/simple/')
# soup = BeautifulSoup(response.content, 'html.parser')
# countries = soup.find_all('div', class_="col-md-4 country")
# with open('country.txt', 'w') as f:
#     for i in countries:
#         f.write(i.find('h3', class_= "country-name").text.strip())
#         # f.write("\n")
#         # info = i.find('div', class_="country-info").text.split()
#         # capital = info[1]
#         # pop = info[3]
#         # area = info[5]
#         # f.write(f"{capital} { pop} {area}")
#         f.write("\n")
        
# capital = soup.find_all('')


# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://www.goodreads.com/quotes/tag/motivational')
# soup = BeautifulSoup(response.content,'html.parser')
# # f.write(soup.prettify())
# quotes = soup.find_all('div',class_='quoteDetails')


# with open('quotes.txt', 'w',) as f:
#     for i in quotes:
#         splited = i.find('div', class_="quoteText").text.split('―')
#         f.write(splited[0].strip().replace("“","").replace("”",""))
#         f.write(splited[1].split(',')[0].strip())
#         f.write(i.find('a', class_="smallText").text.split(" ")[0])
#         f.write('\n')
        
        


# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://www.scrapethissite.com/pages/simple/')
# soup = BeautifulSoup(response.content,'html.parser')
# print(soup.prettify())
# countries = soup.find_all('div',class_='col-md-4 country')

# with open('country.txt', 'w') as f:
#     for i in countries:
#         f.write(i.find('h3',class_="country-name").text.strip())
#         f.write("\n")
#         splitted_info = i.find('div', class_="country-info").text.split("\n")
#         f.write(splitted_info[1].split(':')[1].strip())
#         f.write("\n")
#         f.write(splitted_info[2].split(':')[1].strip())
#         f.write("\n")
#         f.write(splitted_info[3].split(':')[1].strip())
#         f.write("\n")
#         f.write("##########\n")


    
            
