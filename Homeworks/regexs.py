import re

nospace = re.compile("[^ \n]+")
#print(nospace.findall(text))

quotation = re.compile('\"[^ ][^"]+[^ ]\"')
#print(quotation.findall(text))

twonum = re.compile('(\-?[0-9][.]?([0-9]+)?)[, ][ ]?(\-?[0-9][.]?([0-9]+)?)')
#print(twonum.findall(text))

likely_name = re.compile('([A-Z][.][ ])[A-Z][a-z]+([ ][A-Z][a-z]+)?|[A-Z][a-z]+[ ][A-Z][a-z]+([ ][A-Z][a-z]+)?')
#likely name
