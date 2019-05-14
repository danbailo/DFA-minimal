## Minimizar Automatos Finítos Determinísticos Reduzidos

### Pré-requisitos
* python3
### Observações
* Considerar os colchetes '[ ]' como sendo o símbolo para representar um conjunto, visto que este é representado com chaves '{ }'.
* Por exemplo: Seguindo a observação acima, o conjunto vazio será representado por [ ] .
### Executar
Basta executar <code>$ python3 main.py nome_do_arquivo.txt</code><br>
Onde o arquivo "nome_do_arquivo.txt" deve seguir o seguinte formato para o autômato representado
pelo diagrama de transições a seguir:

<image src="automato1.png"></image>

o nome_do_arquivo.txt terá de seguir o seguinte formato:

	'a','b','c','d','e','f'
	01
	'b','c'
	'a','d'
	'e','f'
	'e','f'
	'e','f'
	'f','f'
	'a'
	'c','d','e'

Onde a<br>
<b>Primeira linha: </b>Indica o nome dos estados<br>
<b>Segunda linha: </b>Indica o alfabeto<br>
<b>Terceira, quarta e quinta linha... referente a quantidade de estados: </b>Indicando a matriz delta considerando a primeira coluna como a transição após a leitura do primeiro símbolo em diante<br>
<b>Obs:</b> Considerando que este autômato possui seis estados, a matriz terá seis linhas, logo, as duas últimas linhas sempre serão estado inicial e estado final, respectivamente.<br>
<b>Nona linha: </b> Indica o estado inicial<br>
<b>Décima linha: </b> Indica os estados finais<br>

Nesta pasta contém três automatos([Automato 1](automato1.txt), [Automato 2](automato2.txt) e [Automato 3](automato3.txt)) no formato apresentado acima.
O [Automato 1](automato1.txt) é o exemplo do diagrama mostrado acima.<br>
Ao executar <code>$ python3 main.py automato1.txt</code><br>
A saída do programa será: 


	Estados:
	["['c', 'd', 'e']", "['a', 'b']", "['f']"]

	Sigma:
	['0', '1']

	Delta:
	["['c', 'd', 'e']", "['f']"]
	["['a', 'b']", "['c', 'd', 'e']"]
	["['f']", "['f']"]

	Estado inicial:
	['a', 'b']

	Estados finais:
	["['c', 'd', 'e']"]

Este ainda perguntará se você desejas sair do programa ou testar alguma palavra que o autômato reconheça ou não.