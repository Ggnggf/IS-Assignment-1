def caeser_encrypt(text,shift):
    result=""
    for char in text:
        if char.isalpha(): #only shift letters
            if char.isupper():
                start=ord('A')
            else:
                start=ord('a')
                new_char=chr((ord(char)-start+shift)%26+start)
                result+=new_char
        else:
            result+=char #kep spaces and symbols same
    return result
def caeser_decrypt(ciphertext,shift):
    return caeser_encrypt(ciphertext,-shift) #just reverse the shift

message=input('Enter message: ')
shift=int(input('Enter shift: '))
encrypted_message=caeser_encrypt(message,shift)
print("encrypted:",encrypted_message)
decrypted_message=caeser_decrypt(encrypted_message,shift)
print("decrypted:",decrypted_message)