print ("WELCOME TO MY ENCODER")
print('')
loop = 1
no = 0
while loop == 1:
	no = input('Press'+'\n'+
'1 For Encoders'+'\n'+
'2 For Decoders'+'\n'+
'0 To Quit'+'\n'+
':::::=====----->>>>>')
	print ('')
	if no == ('1') or no == ('01'):
		opperand = input('Press 1 For Base16'+'\n'+
	'Press 2 For Base32'+'\n'+
	'Press 3 For Base64'+'\n'+
	'Press 4 For Binary'+'\n'+
	'Press 5 For Caesar.Cipher'+'\n'+
	':::::-----/////\\\\=====>>>>>')
		if opperand == ('1') or opperand == ('01'):
			import base64
			message = input("Message to be Encoded--->>>")
			message_bytes = message.encode('ascii')
			base64_bytes = base64.b16encode(message_bytes)
			base16_message = base64_bytes.decode('ascii')
			print ("")
			print ("Encoded Message--->>", base16_message)
		elif opperand == ('2') or opperand == ('02'):
			import base64
			message = input("Message to be Encoded--->>>")
			message_bytes = message.encode('ascii')
			base64_bytes = base64.b32encode(message_bytes)
			base32_message = base64_bytes.decode('ascii')
			print ("")
			print ("Encoded Message--->>", base32_message)
		elif opperand == ('3') or opperand == ('03'):
			import base64
			message = input("Message to be Encoded--->>>")
			message_bytes = message.encode('ascii')
			base64_bytes = base64.b64encode(message_bytes)
			base64_message = base64_bytes.decode('ascii')
			print ("")
			print ("Encoded Message--->>", base64_message)
		elif opperand == ('4') or opperand == ('04'):
			test = input("Message to be Encoded--->>>")
			res = ' '.join(format(ord(x), 'b') for x in test)
			print (" ")
			print("Encoded Message--->>" + " " + str(res))
		elif opperand == ('5') or opperand == ('05'):
			def encrypt(string, shift):
				cipher = ''
				for char in string:
					if char == ' ':
						cipher = cipher + char
					elif  char.isupper():
						cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
					else:
						cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
				return cipher
			text = str(input("Enter Text:::--->>> "))
			s = int(input("Enter Encoding Key:::--->>> "))
			print (" ")
			print("After Encryption:::--->>", encrypt(text, s))
		else:
			print ('Wrong Input')
			print ('')
			print ('Please Try Again')
	elif no == ('2') or no == ('02'):
		opperand2 = input('Press 1 For Base16'+'\n'+
	'Press 2 For Base32'+'\n'+
	'Press 3 For Base64'+'\n'+
	'Press 4 For Binary'+'\n'+
	'Press 5 For Caesar.Cipher'+'\n'+
	':::::-----/////\\\\=====>>>>>')
		if opperand2 == ('1') or opperand2 == ('01'):
			import base64
			base64_message = input("Message to be Decoded--->>>")
			base64_bytes = base64_message.encode('ascii')
			message_bytes = base64.b16decode(base64_bytes)
			message = message_bytes.decode('ascii')
			print ("")
			print ("Decoded Message--->>", message)
		elif opperand2 == ('2') or opperand2 == ('02'):
			import base64
			base64_message = input("Message to be Decoded--->>>")
			base64_bytes = base64_message.encode('ascii')
			message_bytes = base64.b32decode(base64_bytes)
			message = message_bytes.decode('ascii')
			print ("")
			print ("Decoded Message--->>", message)
		elif opperand2 == ('3') or opperand2 == ('03'):
			import base64
			base64_message = input("Message to be Decoded--->>>")
			base64_bytes = base64_message.encode('ascii')
			message_bytes = base64.b64decode(base64_bytes)
			message = message_bytes.decode('ascii')
			print ("")
			print ("Decoded Message--->>", message)
		elif opperand2 == ('4') or opperand2 == ('04'):
			a_binary_string = input("Message to be Decoded--->>>")
			binary_values = a_binary_string.split()
			ascii_string = ""
			for binary_value in binary_values:
				an_integer = int(binary_value, 2)
				ascii_character = chr(an_integer)
				ascii_string += ascii_character
			print ("")
			print ("Decoded Message----->>>>>"+" "+ascii_string)
		elif opperand2 == ('5') or opperand2 == ('05'):
			def encrypt(string, shift):
				cipher = ''
				for char in string:
					if char == ' ':
						cipher = cipher + char
					elif  char.isupper():
						cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
					else:
						cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
				return cipher
			text = str(input("Enter Encrypted Text:::--->>> "))
			s = int(input("Enter Decoding Key:::--->>> "))
			print (" ")
			print("After Decryption:::--->>", encrypt(text, -s))
		else:
			print ('Wrong Input')
			print ('')
			print ('Please Try Again')
	elif no == ('0') or no == ('00'):
		loop = 0
print ('')
print ('THANK YOU, VISIT AGAIN')
print ('')
print ('                      --DEBAYANGSHU SEN')
