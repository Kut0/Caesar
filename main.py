# Caesar - Verschlüsselung



def encrypt(clear_msg, shift,): 
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
    return(cypher_msg)

def decrypt (msg, shift):
    return encrypt(msg, -shift)

mode = input("Drücke 1 für Verschlüsseln und 2 für Entschlüsseln und 3 für brute force")
if mode == "1":
    clear_msg = input("Welche Nachricht soll verschlüsselt werden?")
    shift = int(input("Welche Scjlüssel möchtest du verwenden?"))
    cypher_msg = encrypt(clear_msg, shift)
    print(f"Die verschlüsselte Nachricht lautet: {cypher_msg}")
elif mode =="2":
    clear_msg = input("Welche Nachricht soll entschlüsselt werden?")
    shift = int(input("Welche Scjlüssel möchtest du verwenden?"))
    cypher_msg = decrypt(clear_msg, shift)
    print(f"Die verschlüsselte Nachricht lautet: {cypher_msg}")
elif mode == "3":
    clear_msg = input("Welche Nachricht soll entschlüsselt werden?")
    for shift in range(26):
        cypher_msg = decrypt(clear_msg, shift)
        print(f"Die verschlüsselte Nachricht lautet ({shift}): {cypher_msg}")






#clear_msg = "Ich bin 10 Jahre alt."
#clear_msg = input("Welchen Text möchstest du verschlüsseln")
#shift = 1
#shift = int(input("Welchen Schlüssel möchtest du verwenden?"))
#cypher_msg = encrypt(clear_msg, shift)
#print(f"Die verschlüsselte Nachricht lautet: {cypher_msg}")
