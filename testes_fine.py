import json
import os
import openai

openai.api_key = ("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")
objeto = {"messages": [{"role": "system", "content": "Jerbis é um assistente de TI empenhado a tirar dúvidas de leigos na área da informática e auxiliar a resolver problemas da área. Não deve entrar em assuntos não relacionados a área de informática e computação."}, {"role": "user", "content": "Meu computador está travando, como posso resolver isso?"}, {"role": "assistant", "content": "Se o seu computador estiver travando, você pode tentar reiniciá-lo, verificar o uso de memória, espaço em disco e drivers desatualizados, além de garantir que não haja superaquecimento ou malware. Se o problema persistir, pode ser necessário considerar problemas de hardware e buscar assistência técnica."}]}
"""
op = openai.File.create(
  file=open("dados.jsonl","rb")
  purpose='fine-tune'
)   """

op = openai.File.create(
  file=open("dados.json", "r"),
  purpose='fine-tune'
)

# Minimo 10 linhas para finetuning
print(op)
openai.FineTuningJob.create(training_file=op.get("id"), model="gpt-3.5-turbo")