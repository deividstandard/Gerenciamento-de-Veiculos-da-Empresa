FROM python:3.6.7-alpine3.7

# Diretório de trabalho
RUN mkdir -p /code
WORKDIR /code

EXPOSE 8000

# Instalação das dependências do OS
RUN apk update && \
    apk add --no-cache \
        gcc \
        musl-dev \
        libc-dev \
        linux-headers

# Instalação das dependências da aplicação
COPY requirements.txt .
RUN pip install -r requirements.txt && pip install gunicorn

# Copia do código da aplicação
COPY gve/ ./gve/
COPY api/ ./api/

WORKDIR /code/

# Inicialização da aplicação
ENTRYPOINT ["gunicorn"]
CMD ["gve.wsgi"]