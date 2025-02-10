# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sviallon <sviallon@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/10 10:45:35 by sviallon          #+#    #+#              #
#    Updated: 2025/02/10 10:45:36 by sviallon         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys

def check_number(number):
	if number == 0:
		print("I'm Zero.")
	elif number % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		sys.exit()

	if len(sys.argv) > 2:
		print("too many args")
		sys.exit()

	try:
		num = int(sys.argv[1])
		check_number(num)
	except ValueError:
		print("wrong args")