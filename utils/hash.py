import hashlib

def metodoHash(texto):
    texto_bytes = texto.encode('utf-8')
    
    hash_obj = hashlib.sha256(texto_bytes)

    hash_hex = hash_obj.hexdigest()

    #return print(f"el hash SHA-256 de {texto} es: '{hash_hex}")
    return hash_hex