"""
Author: Alex R. Mead
Company: BC Sys
Date: May 2021

"""
from urllib.request import urlopen 


#####
# String parsing of the raw HTML
url = "http://olympus.realpython.org/profiles/aphrodite"
# Get raw HTML
page = urlopen(url)
# Extract HTML, convert to string
html_bytes = page.read()
html = html_bytes.decode('UTF-8')

# Find the <title> tag
start_index = html.find('<title>') + len('<title>')
end_index = html.find('</title>')

title = html[start_index:end_index]
title

# Problems with string search for parsing HTML
url = "http://olympus.realpython.org/profiles/poseidon
url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
title
#####

#####
# Regular Expressions ("regexes")
# Regular expressions are a concept beyond Python and can be used to process
# text in several languages
import re

# *   = "zero or more"
# .   = "wildcard character"
# .*  = "zero or more wildcard characters"
# .*? = "non-greedy patthern maching for shortest possible match"

re.findall("ab*c", "ac")
re.findall("ab*c", "acc")
re.findall("ab*c", "abcac")
re.findall("ab*c", "abdc")

# re.search() is a more complicated search result than re.findall(), use 
#   re.group() with the result of the re.search() call, which is a MatchObject

# re.sub(), "substitute" which allows replacing text in string that matches 
#   a given regex.

# "greedy" an adjective to describe the fact that Python's re.sub() method will
#    attempt to find the longest possible substitution in the string.

# Example:
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)








