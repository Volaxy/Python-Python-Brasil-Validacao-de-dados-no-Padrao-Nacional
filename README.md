# Python Brasil - Validação de Dados no Padrão Nacional

Curso da Alura sobre Validação de Dados, expressões regulares e formatação de informações como CPF e CEP.

## Objetivo Final &#x1F3AF;

Criar bibliotecas capazes de validar CPF, buscar endereço pelo CEP e formatar informações como meses e datas.

URL do curso -> [Python 3: Trabalhando com I/O](https://cursos.alura.com.br/course/python-validacao-dados)

![Python 3: Trabalhando com I/O](https://www.alura.com.br/assets/api/share/curso-python-validacao-dados.png)

## Links Úteis &#x1F517;
* [PyPI](https://pypi.org/) - Site para procura de pacotes e bibliotecas **Pyhton**.
* [ViaCEP](https://viacep.com.br/) - API para requisições de Endereços através do **CEP**.
* [HTTP for Humans](https://docs.python-requests.org/en/master/) - Biblioteca para uma **API** que já vem junto com o **Python**.

## 01 - Validando CPF e Acessando o PYPI &#x1F516;
* Validar um documento pela quantidade de caracteres.
* Encontrar, instalar e importar bibliotecas no PyPI.
* Ler documentações de bibliotecas e utilizá-las em seus códigos.

### 01 - Validando um CPF
* O `raise` lança um erro no **Python**.
* Separar uma string usando `[n:n]` ou `[:n]`.

### 02 - Pacotes Python
* Instalar novos pacotes com o terminal do **Python**.

### 03 - Utilizando um Pacote
* Importar o pacote do `validate-docbr` dentro da classe `Cpf`.

## 02 - Validando CNPJ e Construindo uma Factory &#x1F516;
* Como utilizar mais uma classe da `validate_docbr`.
* O que é o padrão de projeto `Factory`.
* Como e quando implementar uma `Factory` em nosso código.

### 01 - Validando CNPJ
* Criando a classe `CNPJ`.

### 02 - Máscara para CNPJ
* Retornar uma máscara formatada de `CNPJ`.

### 03 - Refatorando o Código
* Criar uma **Factory**.

## 03 - Validando Telefones com Expressões Regulares &#x1F516;
* O que são expressões regulares.
* Como construir padrões e encontra-los dentro de textos.
* Como validar com expressões regulares.
* Como criar máscaras com expressões regulares.

### 01 - Resumo Regex
* Usar `import re` para importar a biblioteca de expressões regulares.
    * Os colchetes `[]` são caracteres especiais que definem um *range* ou um grupo de caracteres, como `[0-9]`, `[a-z]` ou `[abc]` por exemplo.
    * Já o `*` pega uma ou mais ocorrências do padrão definido anteriormente.
    * As chaves `{}` nos permitem definir uma quantidade específica de vezes que queremos que o padrão se repita ou um intervalo de possibilidades, como `[abc]{5}` por exemplo.
    * O `\w` pode ser qualquer número de zero a nove ou letra de "A" a "Z".
    * A barra `|` representa uma coisa ou outra como em `@|$` por exemplo.
    * Os parênteses `()` capturam um grupo.
* A função `re.search(EXPRESSION, STRING)` procura uma expressão regular dentro de uma *string*.

### 02 - Definindo Padrão para Telefones
* A função `re.findall(PATTERN, TEXT)` encontra todas as correspondências em um texto.

### 03 - Criando Máscara para o Número de Telefone
* Criar máscara para os números de telefone.

## 04 - Manipulando e Formatando Datas &#x1F516;
* Como trabalhar com datas e horas no Python.
* Métodos da classe `datetime`.
* Para que serve o `timedelta()` e como utilizá-lo.

### 01 - Datas no Python
* Usar a biblioteca built-in **datetime**.
* A função `datetime.today()` retorna a data e horário atual no momento que a função é executada.
* A função `.month` retorna o inteiro do mês.
* A função `.weekday` retorna o inteiro do dia da semana.

### 02 - Formatando Datas
* A função `.strftime()` formata uma data de acordo com os caracteres passados para a função.

### 03 - Diferença entre Datas e Timedelta
* Somar ou substrair datas e horas.

## 05 - Trabalhando com CEP e Acessando uma API &#x1F516;
* O que são requisições HTTP.
* Para que serve e como acessar uma API.
* Como utilizar a biblioteca `requests` do Python.
* Acessar a API do [ViaCEP](https://viacep.com.br/) e retornar informações do endereço a partir do CEP.

### 01 - Introdução APIs e Validação de CEP
* Para acessar uma **API**, é nescessário enviar uma requisição *http*.
* O retorno de uma **API** é uma resposta *serializada*, no qual é um ***json*** ou ***xml*** e realiza a integração entre sistemas.

### 02 - Acessando APIs com Python
* Como usar uma **API** para requisições no **Python**.
* Usar `dir()` para mostrar todos os atributos de um *objeto*.

### 03 - Respostas API via CEP
* Utilizando o método `.json` para retornar um dicionário do conteúdo da requisição.