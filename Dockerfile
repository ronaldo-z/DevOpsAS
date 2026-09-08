FROM python:3.14

# Definição da pasta de trabalho no container
WORKDIR /app

# Cópia e instalação das dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para io container
COPY . .

# Porta utilizada pelo Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "main.py"]