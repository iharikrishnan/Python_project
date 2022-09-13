
"""This is a simple tool to find subdomains of a website. This tool will take input from the user
and give live subdomains as output . colorama and requests are the packages used in this tool.
colorama is used to give color to the text
requests is used to give requests to the website
"""

import colorama  # for giving color to text
from colorama import Fore, Back, Style  # for giving color
colorama.init()

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}
#You can add more colors and backgrounds to the dictionary if you like.


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

#Example printing out an ASCII file
f  = open("banner.txt","r")
ascii = "".join(f.readlines())
print(colorText(ascii))


#main program

import requests #import requests it allows you to send HTTP requests easily

url =  input("Enter the domain:") #input the domain from user
wordlist = open("wordlist.txt","r") #open the wordlist and give read permissions

domain = wordlist.read() #read the content from wordlist
subdomains = domain.splitlines() #split the lines  into a list

for subdomain in subdomains:
    url1 = f"https://{subdomain}.{url}" #for https

    try:  #using try except block
        requests.get(url1) #request subdomain
        print(Fore.LIGHTGREEN_EX+ f"SUBDOMAIN:{url1}") #print subdomain available
    except requests.ConnectionError: #if their is any connection error return nothing
        """print(Fore.RED + f"NOT-FOUND:{subdomain}.{url}")"""

