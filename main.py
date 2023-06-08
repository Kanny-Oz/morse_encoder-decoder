NUMS = {"1": ".____", "2": "..___", "3": "...__", "4": "...._", "5": ".....", "6": "_....", "7": "__...", "8": "___..",
        "9": "____.", "0": "_____"}
ALPHAS = {"A": "._", "Ã": "._._", "À": ".__._", "B": "_...", "C": "_._.", "D": "_..", "E": ".", "É": "..-..",
          "F": ".._.", "G": "__.", "H": "....", "I": "..", "J": ".___", "K": "_._", "L": "._..", "M": "__", "N": "_.",
          "O": "___", "P": ".__.", "Q": "__._", "R": "._.", "S": "...", "T": "_", "U": ".._", "V": "..._", "W": ".__",
          "X": "_.._", "Y": "_.__", "Z": "__.."}
PONCTUATIONS = {".": "._._._", ",": "__..__", ":": "___...", "?": "..__..", "¿": "..-.-", "!": "_._.__", "¡": "--...-",
                "-": "_...._", "=": "-...-", " ": " / ", "+": ".-.-.", "(": "-.--.-", ")": "-.--.-"}
SPECIALS = {"À": ALPHAS["A"], "Ä": ALPHAS["A"], "Â": ALPHAS["A"], "Ë": ALPHAS["E"], "Ê": ALPHAS["E"], "È": ALPHAS["E"],
            "Ẽ": ALPHAS["E"], "Ñ": "__.__", "Ö": "___.", "Ü": "..__"}

dico = {}
dico.update(NUMS)
dico.update(ALPHAS)
dico.update(PONCTUATIONS)
dico.update(SPECIALS)


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


def learn():
    print("Ici, apprenez les caractères morse")
    print("**********************************\n")
    print("Pour aller plus loin, vous pouvez aller à cette ressource : "
          "https://j28ro.blogspot.com/p/lecons-dapprentissage-du-morse-methode.html")


def main():
    menu_response = input("1. To encode | 2. To decode | ?. To learn | 0. Pour quitter: ")
    if menu_response == "0":
        exit()
    elif menu_response == "1":
        encode()
    elif menu_response == "2":
        decode()
    elif menu_response == "?":
        learn()
    else:
        print("Suivez les instructions svp.\n")
        main()


if __name__ == '__main__':
    main()
