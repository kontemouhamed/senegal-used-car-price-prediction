from bs4 import BeautifulSoup
import requests
import mysql.connector as connection
from mysql.connector import errorcode

# connection à la base de données

config = {
    'user' : 'root',
    'password' : '',
    'host' : '127.0.0.1',
    'database': 'webscrapping',
    'raise_on_warnings' : True
}

try:
    cnx = connection.connect(**config)
    if cnx.is_connected():
        db_Info = cnx.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = cnx.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except cnx.Error as err :
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("'L'utilisateur ou le mot de passe n'est pas correct")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de données n'existe pas!")
    else:
        print(err)
finally:
    if cnx.is_connected():
        cursor.close()
        cnx.close()
        print("MySQL connection is closed")
        
    exit()

# url = "https://www.expat-dakar.com/voitures"
# page = requests.get(url)

# soup = BeautifulSoup(page.content, 'html.parser')
# lists = soup.find_all('section', class_= "listing-search-item--list")
# print(soup.title)

# for list in lists:
#     title = list.find('a', class_ = "listing-search-item__link--title")
#     location = list.find('div', class_ = "listing-search-item__sub-title")
#     price = list.find('div', class_ = "listing-search-item__price")
#     area = list.find('li', class_ = "listing-search-item__link--title")
#     info = [title, location, price, area]
#     print(info)

