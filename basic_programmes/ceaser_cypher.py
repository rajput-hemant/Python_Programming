def ceaser_cypher(text: str, key: int, en_dec: str):
    if en_dec == "en":
        new_text = "".join(chr(ord(i) + key) for i in text)
    elif en_dec == "de":
        new_text = "".join(chr(ord(i) - key) for i in text)
    return new_text


text = input("Enter the text for encoding/decoding -> ")
key = int(input("Enter the Key for encoding/decoding -> "))
en_de = input("Enter 'en' for encoding & 'de' for decoding -> ")
if en_de == ("en" or "de"):
    print(f"{en_de.capitalize()}coded cypher text -> {ceaser_cypher(text, key, en_de)}")
else:
    print("Wrong Input!")
