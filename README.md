# Desafio Back-End

O desafio consiste em criar uma interface web que aceite upload do arquivo CNAB, normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

## Guia da Aplicação:

#### Para Iniciar a instalação das dependências e ambientes deve-se:

rodar o seguinte comando:

```shell
        python -m venv venv
```

Para entrar no ambiente virtual basta ultilizar o seguinte comando:

```shell
        ./venv/Scripts/activate (windowns)
        ou
        source venv/bin/activate (linux)
```

instalar todas as dependências com o seguinte comando:

```shell
        pip install -r requirements.txt
```

Rodar os seguintes comandos:

```shell
        python manage.py migrate
```

Alimentar a tabela de transações:

```shell
        python manage.py loaddata files/fixture.json
```

Inicializar o servidor com o seguinte comando:

```shell
        python manage.py runserver
```

---

### Para fazer o upload do arquivo:

```shell
  localhost:8000/api/upload/
```

- O Arquivo que será feito o upload **PRECISA** estar **nomeado** como **"CNAB"** e em formato **.txt**. Caso não esteja atendendo estes requisitos será retornado um erro.

```shell
  "File name should be CNAB.txt"
```

- Deve conter apenas uma transação por linha
- O conteúdo deve possuir o formato a seguir:
  3201903010000019200845152540736777\*\*\*\*1313172712MARCOS PEREIRAMERCADO DA AVENIDA

---

### Para visualizar todos as transações:

```shell
  localhost:8000/api/interpreter/
```

### Para filtrar as transações pelo nome da empresa:

```shell
  localhost:8000/api/interpreter_filter/
```
