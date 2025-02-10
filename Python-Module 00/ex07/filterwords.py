import sys
import string

def filter_words(string_s, number_n):
	"""
	Filtre les mots d'une chaine qui ont plus de N caracteres (hors ponctuation)
	"""
	try:
		if not isinstance(number_n, int):
			number_n = int(number_n)
		translator = str.maketrans('', '', string.punctuation)
		words = string_s.translate(translator).split()
		filtered_words = [word for word in words if len(word) > number_n]
		return filter_words
	except ValueError:
		return "ERROR"

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("ERROR")
	else:
		result = filter_words(sys.argv[1], sys.argv[2])
		print(result if result != "ERROR" else "ERROR")