# Acervo Cobalto

## Sobre o projeto:

O Acervo Cobalto é um site interativo que permite aos usuários salvar seus personagens favoritos da série Rick and Morty em seus perfis pessoais. Através da integração com a API oficial da série, o site exibe informações detalhadas sobre cada personagem, como sua espécie, status de vida e sua origem. O objetivo é oferecer uma plataforma onde os fãs da série podem acompanhar seus personagens favoritos e ter fácil acesso às informações mais recentes.

## Instalação do Projeto:

Para rodar este projeto localmente, siga os passos abaixo:

### 1. Clonar o repositório

Primeiro, clone o repositório para o seu ambiente local. No terminal, use o comando:

```bash
git clone https://github.com/Matheus-Farias86/wsBackend-Fabrica25.1.git
```

### 2. Criar o ambiente virtual

Crie um ambiente virtual para isolar as dependências do projeto. Execute o seguinte comando:

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

- **No Windows**, ative o ambiente virtual com o seguinte comando:

  ```bash
  .\venv\Scripts\activate
  ```

- **No macOS/Linux**, use o comando:

  ```bash
  source venv/bin/activate
  ```

### 4. Instalar as dependências

Com o ambiente virtual ativado, instale as dependências necessárias para o projeto utilizando o `pip`:

```bash
pip install -r requirements.txt
```

Isso vai instalar todas as bibliotecas listadas no arquivo `requirements.txt`.

## Como Iniciar o Docker Compose:

Para rodar o projeto com o Docker Compose, siga os seguintes passos:

### 1. Pré-requisitos

- Certifique-se de que o [Docker](https://www.docker.com/get-started) e o [Docker Compose](https://docs.docker.com/compose/install/) estão instalados na sua máquina.

### 2. Iniciar o Docker Compose

- No diretório onde o docker-compose.yml está localizado, execute o seguinte comando:

```bash
docker-compose up
```

Esse comando vai:

- Baixar as imagens necessárias.
- Criar os containers.
- Iniciar os serviços definidos no arquivo docker-compose.yml.

### 3. Acessar o site

No seu navegador acesse o site pelo http://localhost:8000/

## API utilizada:

RickandMorty API: https://rickandmortyapi.com/
