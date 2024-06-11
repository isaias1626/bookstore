#!/bin/bash

# Exibir mensagem de início
echo "Iniciando o processo de build..."

# Remover qualquer diretório existente antes de clonar
if [ -d "src/bookstore" ]; then
    echo "Removendo diretório existente src/bookstore..."
    rm -rf src/bookstore
fi

# Clonar o repositório usando HTTPS
echo "Clonando o repositório..."
git clone --filter=blob:none --quiet 'https://github.com/isaias1626/bookstore.git' src/bookstore
if [ $? -ne 0 ]; then
    echo "Erro ao clonar o repositório."
    exit 1
fi

# Instalar dependências
echo "Instalando dependências..."
python3.12 -m pip install -r src/bookstore/requirements.txt

# Verificar se Django foi instalado corretamente
if ! python3.12 -c "import django" &> /dev/null; then
    echo "Django não está instalado. Verifique o arquivo requirements.txt."
    exit 1
fi

# Coletar arquivos estáticos
echo "Coletando arquivos estáticos..."
python3.12 src/bookstore/manage.py collectstatic --noinput

# Criar o diretório de build para arquivos estáticos
echo "Criando diretório de build para arquivos estáticos..."
mkdir -p staticfiles
mv src/bookstore/static staticfiles/

echo "Build completo com sucesso!"
