import random, time, sys


def desenhos(erros):
	if erros == 0:
		print(
			"""
			______
			|    
			|
			|
			|
			|
			|
			"""
		)
	if erros == 1:
		print(
			"""
			______
			|    o
			|
			|
			|
			|
			|
			"""
		)
	if erros == 2:
		print(
			"""
			______
			|    o
			|    |
			|
			|
			|
			|
			"""
		)
	if erros == 3:
		print(
			"""
			______
			|    o
			|   /|
			|
			|
			|
			|
			"""
		)
	if erros == 4:
		print(
			"""
			______
			|    o
			|   /|\\
			|   
			|
			|
			|
			"""
		)
	if erros == 5:
		print(
			"""
			______
			|    o
			|   /|\\
			|   / 
			|
			|
			|
			"""
		)
	if erros == 6:
		print(
			"""
			______
			|    o
			|   /|\\
			|   / \\
			|
			|
			|
			"""
		)

class forca:
	def __init__():
		pass
	def jogo():
		palavras = ["queijo", "beterraba", "triângulo", "basquete", "cidade", "zona rural", "urbanização", "escola", "animes", "jogos", "esportes"]
		palavra = random.choice(palavras)
		acertos = []
		erros = 0
		tentativas = []
		p = ""
		while True:
			if erros >= 6:
				print(f"\033[1;92mA palavra era: {palavra}\033[0;0m")
				break
			p = ""
			for l in palavra:
				if l in acertos or l == " ": p += l
				else: p += "_ "
			if p == palavra: #palavras com duas letras iguais seram reconhecidas xd
				print("\033[1;92mParabéns, você ganhou! :D") 
				print(f"A palavra era: {palavra}\033[0;0m")
				time.sleep(3)
				sys.exit()
			desenhos(erros)
			print(f"\n			{p}\n")
			tentativa = input("Digite uma letra ou a palavra: ").lower().strip()
			print("\n"*10)
			if len(tentativa) > 1:
				if tentativa == palavra:
					print("\033[1;92mParabéns, você ganhou! :O\033[0;0m")
					time.sleep(3)
					sys.exit()
				else: break
			else:
				if tentativa in tentativas:
					print("\033[1;94mVocê já usou essa letra.\033[0;0m")
				else:
					if tentativa in palavra:
						acertos.append(tentativa)
						print("\033[1;92mParabéns, você acertou!\033[0;0m")
					else:
						print("\033[1;91mVocê errou :(\033[0;0m")
						erros += 1
						print(f"\033[1;92mChances restantes: {6-erros}\033[0;0m")
					tentativas.append(tentativa)



forca.jogo()
print("\033[1;91mVocê perdeu.\033[0;0m")
time.sleep(3)