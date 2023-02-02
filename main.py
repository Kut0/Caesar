# Caesar - Verschlüsselung

clear_msg = input("Welchen Text möchstest du verschlüsseln")
shift = int(input("Welchen Schlüssel möchtest du verwenden?"))

shift = shift % 26
# beschränke die Verschiebung auf max 26


cypher_msg = ""
clear_msg = clear_msg.upper()
for char in clear_msg:
    nb = ord(char)
    new_nb = nb + shift
    if char.isalpha():
        new_nb = nb + shift
        if new_nb > 90:
            new_nb -= 26
    else:
        new_nb = nb
    new_char = chr(new_nb)
    #print(char, nb, new_nb, new_char)
    cypher_msg += new_char

print(f"Die verschlüsselte Nachricht lautet: {cypher_msg}")
