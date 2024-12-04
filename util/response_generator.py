import google.generativeai as genai
import os
import random

from util import processarCsv
from frames import atividades, refrigeracao
from frames import preferencia

api = os.getenv("API_GEMINI")

genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

def resposta():
    cpus = processarCsv.gerar_lista_processadores()
    if len(cpus) > 0:
        lista_cpus = random.sample(cpus, 5)
        prompt = f"""
        Sabendo que meu usuário usa o computador de forma {atividades.get_classificacao_uso()}.
        Tem um computador bem refrigerado: {refrigeracao.eh_bem_refrigerado()}
        e tem apenas essas escolhas de cpu: {lista_cpus}. Indique apenas uma boa escolha dessa lista e me responda nesse formato: 
        Nome: nome da cpu
        Justificativa: fale como essa cpu é boa, listando possiveis atividades que o usuário poderá realizar com ela.
        responda apenas com esses 2 dados, de forma compacta, e não mencione as outras CPU's da lista de forma alguma.
        """
        response = model.generate_content(prompt)
        return response.text
    else:
        prompt = f"""
        Sabendo que meu usuário usa o computador de forma {atividades.get_classificacao_uso()}.
        Tem um computador bem refrigerado: {refrigeracao.eh_bem_refrigerado()}
        e tem preferencia por {preferencia.get_preferencia()} entre (AMD E Intel)
        Indique apenas uma boa escolha de cpu para esse usuário e me responda nesse formato: 
        Nome: nome da cpu
        Justificativa: fale como essa cpu é boa, listando possiveis atividades que o usuário poderá realizar com ela.
        responda apenas com esses 2 dados, de forma compacta, e não mencione as outras CPU's da lista de forma alguma.
        """
        response = model.generate_content(prompt)
        return response.text