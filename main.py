import operator

letter_probs = {
    'e': 0.1368, 't': 0.0463, 'a': 0.1253, 'o': 0.0868,
    'i': 0.0625, 'n': 0.0671, 's': 0.0798, 'r': 0.0687,
    'h': 0.0070, 'd': 0.0586, 'l': 0.0497, 'u': 0.0393,
    'c': 0.0468, 'm': 0.0315, 'f': 0.0069, 'y': 0.0090,
    'w': 0.0001, 'g': 0.0101, 'p': 0.0251, 'b': 0.0142,
    'v': 0.0090, 'k': 0.0002, 'x': 0.0022, 'q': 0.0088,
    'j': 0.0044, 'z': 0.0052}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789"


def sum_probs(texto):
    global letter_probs
    aux = 1.0
    for c in texto:
        if c in letter_probs:
            aux = aux + letter_probs.get((c.lower()))
    return aux


def encrypt(message, key):
    global alphabet
    encrypted_message = ""
    for c in message:
        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position + key) % 63
            new_character = alphabet[new_position]
            encrypted_message += new_character
        else:
            encrypted_message += c
    return encrypted_message


def decrypt(message, key):
    global alphabet
    stringlength = len(alphabet)
    alphabet_reverse = alphabet[stringlength::-1]
    decrypted_message = ""
    for c in message:
        if c in alphabet_reverse:
            position = alphabet_reverse.find(c)
            new_position = (position + key) % 63
            new_character = alphabet_reverse[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    return decrypted_message


def decipher_force(texto):
    global alphabet
    listado = []
    for clave in range(len(alphabet)):
        translated = ''

        for symbol in texto:
            aux = []
            if symbol in alphabet:
                num = alphabet.find(symbol)
                num = num - clave
                if num < 0:
                    num = num + len(alphabet)
                translated = translated + alphabet[num]
            else:
                translated = translated + symbol
            aux.append(clave)
            aux.append(translated)
            aux.append(sum_probs(translated))
        listado.append(aux)
    sorted_list = sorted(listado, key=operator.itemgetter(2), reverse=True)
    return sorted_list


if __name__ == '__main__':
    message = input("Introduzca el mensaje: ")
    key = input("Introduzca la clave: ")
    print("Mensaje: " + message)
    print("Clave: " + str(key))
    encriptado = encrypt(message, int(key))
    print("Mensaje: " + encriptado)
    desencriptado_con = decrypt(encriptado, int(key))
    print("Mensaje con la Clave: " + desencriptado_con)
    lista = decipher_force(encriptado)
    n = len(lista)
    i = 0
    while i < n:
        print("Key por Fuerza Bruta: " + str(lista[i][0]))
        print("Mensaje por Fuerza Bruta: " + lista[i][1])
        print("Probabilidad: " + str(lista[i][2]))
        opcion = input("Te ha servido?: ")
        aux = opcion.lower()
        if aux == 's' or aux == 'y':
            break
        else:
            i = i + 1
