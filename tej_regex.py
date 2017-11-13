import re

p = re.compile('(ab)*')

m = p.match('ababababab'))

m.group(0)

gender = '(\b[Mm]ale)|(\b[Ff]emale)'

Date = '(([A-Z0-9][A-Z0-9]?[/])?[A-Z0-9][A-Z0-9]?[/][A-Z0-9][A-Z0-9][A-Z0-9]?[A-Z0-9]?)|([A-Za-z][A-Za-z][A-Za-z]\s..?[,]\s....)'

product_type = '(\b[Pp]roduct\s[Tt]ype):\s?.*'

faceamount = '(\b[Ff]ace\s?[Aa]mount:?\s?.*)'

genderfollowedbyage = '((\b[Mm]ale)|(\b[Ff]emale))\s\d{2}'
