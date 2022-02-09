Durante a aula, vimos alguns dos caracteres importantes para podermos trabalhar com as regex. A lista utilizada está aqui também:

| Caracteres | Descrição | Exemplos |
| ---------- | --------- | -------- |
| [] |	Define um range ou um grupo de caracteres	| [0-9]; [a-z]; [abc]
| *	 |Marca nenhuma, uma ou mais ocorrências	| sol*
| {} |	Quantidade de repetições de uma ocorrência definida	| [abc]{5}
| \d |	Qualquer número de 0 até 9	| \d{3,4}
| \w |	Qualquer número de a té 9 letra de a até z ou _	| \w{10}
|  PIPE  | Um ou outro	| @$
| () |	Captura e agrupa	| (\w{4})

Lembre que capturar em grupo utilizando os parênteses `()` é importante, pois deixa o padrão melhor explicado e mais fácil de ser controlado, além de os grupos poderem ser separados utilizando o método `.group(index)`. Para se aprofundar nos caracteres da lista acima e, ainda, conhecer todos os outros que são utilizados pela biblioteca `re`, leia [este texto da W3Scools](https://www.w3schools.com/python/python_regex.asp), uma ótima fonte para vocês buscarem mais informações.