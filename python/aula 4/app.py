minha_string = "  Qualquer Texto "

print(minha_string.upper())
print(minha_string.lower())
print(minha_string.capitalize())
print(minha_string.isupper())
print(minha_string.islower())
print(minha_string.strip())
print(minha_string.replace("u", "U",1))
print(len(minha_string))
print(minha_string[5:10])
print(minha_string[-10:-5])
print(minha_string.index("que"))

x = "u" in minha_string

print(x)

minha_string= """linha1, 
linha2,
linha3
"""
print(minha_string)

minha_string =""" linha 1,\nlinha2,\nlinha3."""
print(minha_string)

minha_string="adiciona entre \"aspas\" no texto"
print(minha_string)