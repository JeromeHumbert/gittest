txt = "Jérôme Humbert"
ind = txt.find(" ")
txt = txt[0:ind]+" 'L'Assistant' "+txt[ind+1:]
print(txt)

