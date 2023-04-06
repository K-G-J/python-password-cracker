import hashlib

# python3 dictionary.py

pass_found = False

i_hash = input("Enter the hashed password: ")
p_doc = input("\nEnter password filename including path: ")  # passwords.txt

p_file = open(p_doc, 'r')

for word in p_file:
    enc_word = word.encode('utf-8')
    hash_word = hashlib.sha256(enc_word.strip())
    digest = hash_word.hexdigest()

    if digest == i_hash:
        print(f"\nPassword found : {word}")
        pass_found = True
        break

if not pass_found:
    print("\nPassword not found")
