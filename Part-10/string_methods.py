text = "      i WILL print        "

upper_text = text.upper()
lower_text = text.lower()
title_text = text.title()

#strip remove space from both side
strip_text = text.strip()
lstrip_text = text.lstrip()
lstrip_text = text.rstrip()

#find method
find_text = text.find('pri')

#replace method
rep_text = text.replace('WILL', 'have')

###################


print(upper_text)
print(lower_text)
print(title_text)
print(strip_text)
print(lstrip_text)
print(find_text)
print(rep_text)





#########################

in_text = "print" in text
not_in_text = "name" not in text

print(in_text)
print(not_in_text)