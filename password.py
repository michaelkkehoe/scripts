import hashlib
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. MD5 Password (non-hashed)")
print ("2. MD5 Password (hashed)")
print ("3. SHA Password")
print (30 * '-')

## Wait for valid input in while...not ###
is_valid=0
 
while not is_valid :
        try :
                choice = int ( raw_input('Enter your choice [1-3] : ') )
                is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
if choice == 1:
        #test = raw_input("Do you want to auto-generate a password? Y/N")
	key_string = raw_input( "Key to turn into an MD5 password? " )
	print hashlib.md5( key_string ).hexdigest()
elif choice == 2:
        print ("Starting user management...")
elif choice == 3:
        print ("Rebooting the server...")
else:
        print ("Invalid number. Try again...")


