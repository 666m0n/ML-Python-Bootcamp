# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sviallon <sviallon@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/10 10:54:29 by sviallon          #+#    #+#              #
#    Updated: 2025/02/10 10:54:31 by sviallon         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def text_analyzer(text=None):
	"""Analyse un texte et compte ses caractères.
	Cette fonction prend une chaîne de caractères et affiche :
	- Le nombre total de caractères imprimables
	- Le nombre de lettres majuscules
	- Le nombre de lettres minuscules
	- Le nombre de signes de ponctuation
	- Le nombre d'espaces
	Si aucun texte n'est fourni, demande à l'utilisateur d'en saisir un."""
	if text is None:
		text = input("What is the text to analyze?\n>> ")
	if not isinstance(text, str):
		print("AssertionError: argument is not a string")
		return

	upper_count = sum(1 for c in text if c.isupper())
	lower_count = sum(1 for c in text if c.islower())
	punct_count = sum(1 for c in text if c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
	space_count = sum(1 for c in text if c.isspace())

	total_chars = upper_count + lower_count + punct_count + space_count

	print(f"The text contains {total_chars} printable character(s):")
	print(f"- {upper_count} upper letter(s)")
	print(f"- {lower_count} lower letter(s)")
	print(f"- {punct_count} punctuation mark(s)")
	print(f"- {space_count} space(s)")

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 2:
		print("AssertionError: more than one argument provided")
	elif len(sys.argv) == 2:
		text_analyzer(sys.argv[1])
	else:
		text_analyzer()