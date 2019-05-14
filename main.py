from afd import *
from afdmin import *

while True:
	try:
		u=input("\nDigite 's' para sair ou pressione Ctrl+C/Ctrl+D ou\nDigite palavra para testar: ")
		if u[0].lower() == 's': break
		if afd.feed(u): print('-'*50+"\nAFD Original: O autômato RECONHECE a palavra!")
		else: print('-'*50+"\nAFD Original: O autômato NÃO reconhece a palavra!")
	except RuntimeError as err:
		if str(err)=="word not in sigma":
			print("Palavra inválida! Por favor, entre somente com símbolos do alfabeto!")
			afd.reset()
			continue
		raise err
	except IndexError as err:
		continue
	except EOFError as err:
		print('\n\nSaindo...')
		break
	except KeyboardInterrupt as err:
		print('\n\nSaindo...')
		break	
	if afdmin.feed(u): print("AFD Mínimo: O autômato RECONHECE a palavra!"+'\n'+'-'*50)
	else: print("AFD Mínimo: O autômato NÃO reconhece a palavra!"+'\n'+'-'*50)
	afd.reset()
	afdmin.reset()