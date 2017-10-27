def encode_caesar(message, n):
	from string import ascii_uppercase as alphabet
	x = alphabet
	e = {}
	for i in range(len(x)):
		e[x[i]] = x[(i+n)%26]
	message = message.upper()
	encoded = ''
	for c in message:
		if c in x:
			encoded += e[c]
		else:
			encoded += c

	return encoded

