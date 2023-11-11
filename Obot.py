import requests
from bs4 import BeautifulSoup
import sys

def search_google(query, num_results=5):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all('div', class_='tF2Cxc')

    print("\nObot Results:")
    for i in range(min(num_results, len(results))):
        result = results[i]
        link_container = result.find('a')
        if link_container and 'href' in link_container.attrs:
            link = link_container['href']
            print(link)

print("#WELCOME TO AI SEARCH by Ryotec#")
name = str(input("Enter your name to continue: "))

while True:
    ques = input("Proceed to Search-Bot(y/n)? ")
    check = ques.lower()

    if check != "y":
        sys.exit()

    if name == "":
        sys.exit()

    print(" ┈┏━╮╭━┓┈╭━━━━╮")
    print(' ┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃')
    print("┈╰┓▋▋┏╯╯╰━━━━╯")

    print(' ╭━┻╮╲┗━━━━╮╭╮┈ Hi there '+name+' i @m ÔBoT')
    print(' ┃▎▎┃╲╲╲╲╲╲┣━╯┈  ----------------------------')
    print('╰━┳┻▅╯╲╲╲╲┃┈┈┈')
    print('┈┈╰━┳┓┏┳┓┏╯┈┈┈')
    print('┈┈┈┈┗┻┛┗┻┛┈┈┈┈')

    query = input("ÔBoT>>> WHAT CAN I HELP YOU SEARCH UP " + name + "? ")

    # Web scraping using BeautifulSoup and requests
    h = input("ÔBoT>>> How many search results do you want? : ")
    try:
        h = int(h)
    except ValueError:
        print("Please enter a valid integer.")
        sys.exit()

    print("ÔBoT>>> Be patient while results are loading")

    search_google(query, num_results=h)

    print("""
    .                                                      .
            .n                   .                 .                  n.
      .   .dP                  dP                   9b                 9b.    .
     4    qXb         .       dX                     Xb       .        dXp     t
    dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
    9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
     9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
      `9XXXXITSJAXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
        `9XXXXXXXXXXXP' `9XX'   XXX    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
            ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                            )b.  .dbo.dP'`v'`9b.odb.  .dX(
                          ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                         dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                        dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                        9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                         `'      9XXXXXX(   )XXXXXXP      `'
                                  XXXX X.`v'.X XXXX
                                  XP^X'`b   d'`X^XX
                                  X. 9  `   '  P )X
                                  `b  `       '  d'
                                   `             '
    """)

    print("Look up ^")

    AnoT = input("Would you like to make another search? (y/n): ")
    low = AnoT.lower()

    if (low == "n" or low != "y"):
        print('Credits: Ade Josh, David Nwachukwu, OpenAI')
        print("2023 © Ryotec")
        sys.exit()
  
