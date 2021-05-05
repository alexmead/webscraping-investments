"""
Author: Alex R. Mead
Company: BC Sys
Date: May 3, 2021

Description:
This script parses the Investopedia Dictionary (abridged terms) for the links
which I will go over as a learning tool for the Financial Services Industry.

"""
from bs4 import BeautifulSoup
from urllib.request import urlopen

#####
# String parsing of the raw HTML
url = "https://www.investopedia.com/financial-term-dictionary-4769738"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# Print words to file
f = open("financial_words.txt", "w")

# Find the distict <h2> tags, as these are the numeral, a-z headings I'm after
letters = soup.find_all("h2")
for letter in letters:
    rsp = f.write(f"{letter.span.text}\n")
    # Get words for current letter
    words = letter.find_next_siblings("div")[0].find_all("a")
    # print(f" '\u2610'  '\u2610'  {letter.span.text}  ::  {words[0].span.text}")
    print(f"{letter.span.text}")
    for word in words:
        rsp = f.write(f"   {word.span.text} \n")
        # rsp = f.write(f"      {word['href']} \n")
    rsp = f.write("\f")

f.close()



# # Get the link for the definition:
# def_url = word['href']
# def_page = urlopen(def_url)
# def_html = def_page.read().decode("utf-8")
# def_soup = BeautifulSoup(def_html, "html.parser")
# definition = def_soup.find_all("h2")[0]


