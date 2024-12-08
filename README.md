# cpu-recommender
Recomendador de CPU para usuários leigos, desenvolvido para a disciplina de Arquitetura de Computadores.

## Passo a passo para rodar o projeto
1. Faça o download ou um clone desse repositório.
2. Crie um ambiente virtual:  `python3 -m venv ambiente`
3. Ative o ambiente virtual: `source ambiente/bin/activate`
4. Instale a dependência do projeto: `pip install -U google-generativeai`
5. Crie uma chave de api no [google-gemini](https://ai.google.dev/).
6. Exporte uma variável de ambiente com sua chave do gemini: `export API_GEMINI="sua chave aqui"`
7. Rode o projeto: `python3 cpu_recommender.py`
