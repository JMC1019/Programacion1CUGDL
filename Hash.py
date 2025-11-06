import hashlib

texto = "Feliz cumlpleaños Oswaldo!"
hash_hex = hashlib.sha512(texto.encode()).hexdigest()
print("SHA-512:", hash_hex)