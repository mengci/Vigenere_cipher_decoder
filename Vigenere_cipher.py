import string

#mapping characters to corresponding numbers
def mapping_string_to_number():
	str1 = string.lowercase
	mapping = {}
	j = 0
	for i in str1:
		mapping[i] = j
		j += 1
	return mapping

#mapping numbers to corresponding characters
def reverse_mapping():
	str1 = string.lowercase
	mapping={}
	j = 0
	for i in str1:
		mapping[j] = i
		j += 1
	return mapping	

#modulo 26	
def mod26(K):
	if K>=0 and K<26:
		return K
	elif K<0:
		return K+26
	elif K>25:
		return K-26

#counting character frequencies in the plaintexts		
def character_frequency(str2):
	temp = 0
	key = ""
	i=0
	mapp={}
	for c in string.lowercase:
		mapp[c] = 0
	for c in str2:
		if c in mapp:
			mapp[c] += 1
		else:
			mapp[c] = 1
	print mapp
	key=sorted(mapp,key=mapp.get)
	print key
	return mapp
	
#figure out the key length
def find_the_key_length(ciphertext):
	ciphertext_displace={};
	num_of_coins = {};
	temp = 0
	for i in range(10):
		ciphertext_displace[i+1] = (i+1)*" " + ciphertext
		num_of_coins[i+1] = 0
		for j in range(len(ciphertext)):
			if ciphertext[j] == ciphertext_displace[i+1][j]:
				num_of_coins[i+1] += 1;
	for i in range(10):
		if num_of_coins[i+1]>temp:
			temp = num_of_coins[i+1]
			keyLength = i+1
	return keyLength 

#segment the ciphertext according to key length
def classify_ciphertext(index, keyLength, ciphertext):
	classified_text = ""
	i = 0
	j = 0
	while i < len(ciphertext):
		classified_text = classified_text + ciphertext[keyLength * j+index]
		j += 1
		i = keyLength * j + index
	return classified_text

#find out the key according to the character frequencies	
def find_the_key(freq, str_freq, mapping,rev_mapping):
	a = 0
	s = ""
	key = ""
	for i in str_freq:
		a = mod26(mapping[i] +19)
		s = rev_mapping[a]
		freq[s]
		print s, freq[s]
	
def find_key(char,mapping,rev_mapping):
	K = mapping[char]-mapping['e']
	if (K<-25 or K>25):
		print "Error!"
		return 1
	if K>=0 and K<26:
		K =K
	elif K<0:
		K = K+26
	print rev_mapping[K]	

#decode the ciphertext into palintext with the key
def decipher_1(key, ciphertext):
	mapping = mapping_string_to_number()
	rev_mapping = reverse_mapping()
	message = ""
	newkey = key * 300
	for i in range(0, len(ciphertext)):
		letter1 = ciphertext[i]
		if letter1==" ":
			message = message + " "
		else:
			letter2 = newkey[i]
			diff = (mapping[letter1]-mapping[letter2]) % 26
		message = message + rev_mapping[diff] 
	print message
  	
def decipher(ciphertext):
	threshold = 0.1;
	frequency={};
	mapping = mapping_string_to_number()
	rev_mapping = reverse_mapping()
	classified_text = {}
	keyLength = find_the_key_length(ciphertext)
	for i in range(keyLength):
		classified_text[i] = classify_ciphertext(i, keyLength, ciphertext)
		frequency[i]=character_frequency(classified_text[i])
#	find_the_key(frequency[5],"wu",mapping, rev_mapping)
#	find_key("w",mapping, rev_mapping)
	key = "holmes"
	decipher_1(key ,ciphertext)

#main function	
ciphertext =  "ocwyikoooniwugpmxwktzdwgtssayjzwyemdlbnqaaavsuwdvbrflauplooubfgq hgcscmgzlatoedcsdeidpbhtmuovpiekifpimfnoamvlpqfxejsmxmpgkccaykwf zpyuavtelwhrhmwkbbvgtguvtefjlodfefkvpxsgrsorvgtajbsauhzrzalkwuow hgedefnswmrciwcpaaavogpdnfpktdbalsisurlnpsjyeatcuceesohhdarkhwot ikbroqrdfmzghgucebvgwcdqxgpbgqwlpbdaylooqdmuhbdqgmyweuik"
keyLength = find_the_key_length(ciphertext)
decipher(ciphertext)




