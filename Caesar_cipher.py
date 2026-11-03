alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction=input("Type 'encode' to encrypt and 'decode'to decrypt:\n").lower()

text=input("Enter your message:\n").lower()

shift=int(input("Enter how much you want to shift the alphabet:\n"))

def caeser(original_text,shift_amount,encode_or_decode):
    
    output_text=""
    
    if encode_or_decode=="decode":
        shift_amount*=-1
    
    for letter in original_text:
            
        shifted_amount=alphabet.index(letter)+shift_amount
        
        shifted_amount%=len(alphabet)
        
        output_text+=alphabet[shifted_amount]
        
    print(f"Here is the {encode_or_decode}d result: {output_text}")
    
caeser(original_text=text,shift_amount=shift,encode_or_decode=direction)

Again=input("Do you want to go agaain?").lower()

if Again=="yes":
    
    direction=input("Type 'encode' to encrypt and 'decode'to decrypt:\n").lower()
    
    text=input("Enter your message:\n").lower()
    
    shift=int(input("Enter how much you want to shift the alphabet:\n"))
    
    def caeser(original_text,shift_amount,encode_or_decode):
        
        output_text=""
        
        for letter in original_text:
        
            if encode_or_decode=="decode":
                shift_amount*=-1
            
            shifted_amount=alphabet.index(letter)+shift_amount
            
            shifted_amount%=len(alphabet)
        
            output_text+=alphabet[shifted_amount]
        
        print(f"Here is the {encode_or_decode}d result: {output_text}") 
    
    caeser(original_text=text,shift_amount=shift,encode_or_decode=direction)    

if Again=="no":
    print("Thank You ")