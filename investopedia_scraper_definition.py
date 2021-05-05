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

fails = []

# Print words to file
f = open("financial_words_defs.txt", "w")

# Find the distict <h2> tags, as these are the numeral, a-z headings I'm after
letters = soup.find_all("h2")
for letter in letters:
    rsp = f.write(f"{letter.span.text}\n")
    # Get words for current letter
    words = letter.find_next_siblings("div")[0].find_all("a")
    # print(f" '\u2610'  '\u2610'  {letter.span.text}  ::  {words[0].span.text}")
    print(f"{letter.span.text}")
    for word in words:
        # Write word to file
        rsp = f.write(f"{word.span.text}")
        # Get definition, write to file as well
        def_url = word['href']; def_page = urlopen(def_url)
        def_html = def_page.read().decode("utf-8")
        def_soup = BeautifulSoup(def_html, "html.parser")
        heading = def_soup.find_all("h2")[0]
        try:
            definition = heading.find_next_siblings("p")[0]
        except: 
            heading = def_soup.find_all("h2")[1]
            definition = heading.find_next_siblings("p")[0]
        try:
            rsp = f.write(definition.text + "\n")
        except Exception as e:
            rsp = f.write( str(e) + "\n")
            fails.append(word.span.text)
    rsp = f.write("\f")

f.close()


# # Get the link for the definition:
# def_url = word['href']
# def_page = urlopen(def_url)
# def_html = def_page.read().decode("utf-8")
# def_soup = BeautifulSoup(def_html, "html.parser")
# definition = def_soup.find_all("h2")[0]


