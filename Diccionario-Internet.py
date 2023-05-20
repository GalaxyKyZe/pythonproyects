meme_dict = {
            "ROFL": "Es una expresion usada para referirte a una broma",
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Es un simbolo que representa una risa",
            "SHEESH": "es una ligera desaprobación",
            "CREEPY": "Es cuando algo te da miedo",
            "AGGRO": "Es cuando te ofendes o te pones agresivo"
            }
while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    word.upper()

    if word in meme_dict.keys():
        print(word, ":", meme_dict[word])
    else:
        print("Lo sentimos, no existe la palabra o el sistema no es capaz de reconocerlo")