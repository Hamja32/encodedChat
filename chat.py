def message_to_ascii(message):
    ascii_message=''
    for char in message:
        ascii_message+=str(ord(char)) + " " 
    return ascii_message
    
def ascii_to_message(ascii_message):
    message=''
    ascii_values = ascii_message.split()
    for value in ascii_values:
        message+=chr(int(value))
    return message
    
def main():
    while True:
        print("1. Message to ASCII")
        print("2. ASCII to Message")
        print("3. Quit")
        choice = input("Enter your choice : ")
        if choice=='1':
            message = input("Enter your message : ")
            ascii_message= message_to_ascii(message)
            print("ASCII Message : ",ascii_message)
        elif choice =='2':
            ascii_message = input("Enter ASCII message : ")
            message= ascii_to_message(ascii_message)
            print("Message : ",message)
        elif choice=='3':
            break
        else:
            print("Invalid choice. Please try again")
if __name__ == "__main__":
    main()
        
