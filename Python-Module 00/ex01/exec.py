# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sviallon <sviallon@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/10 10:45:46 by sviallon          #+#    #+#              #
#    Updated: 2025/02/10 10:45:48 by sviallon         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
	if len(sys.argv) > 1:
		text = " ".join(sys.argv[1:])
		result = text[::-1].swapcase()
		print(result)

if __name__ == "__main__":
	main()