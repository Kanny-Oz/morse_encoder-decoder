dico = {"1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
        "9": "----.", "0": "-----", "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
        "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..", "À": ".--.-", "Â": ".--.-", "Æ": ".-.-", "Ç": "-.-..", "È": ".-..-", "Ë": "..-..", "É": "..-..",
        "Ê": "-..-.", "Î": "..", "Ï": "-..--", "Ô": "---.", "Ü": "..--", "Û": "..--", ",": "--..--", " ": "  "}


def encode():
    string = input("Entrez votre texte à encoder : ")
    morse = []
    for letter in string:
        if letter.upper() in dico:
            letter = dico[letter.upper()]
        morse.append(letter)
    morse = " ".join(morse)
    print(morse)


def decode():
    morse = input("Entrez le morse : ")
    words = morse.split("  ")
    for word in words:
        letters = word.split(" ")
        for letter in letters:
            for key in dico.keys():
                if letter == dico[key]:


encode_or_decode = input("1. To encode | 2. To decode : ")


if encode_or_decode == "1":
    encode()
elif encode_or_decode == "2":
    decode()
else:
    print("Veuillez taper 1 pour encoder ou 2 pour décoder")

