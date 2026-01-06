# write a program to fill in a letter template given below with name and date


letter= """
           dear <|name|>,
           you are selected!
           <|date|>"""
 

print(letter.replace("<|name|>" ,"Ayush").replace("<|date|>","5th sep 2024"))
# chaining of .replace 