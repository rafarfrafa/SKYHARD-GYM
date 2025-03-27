import os
import autopep8

# Diretório raiz do projeto
diretorio_raiz = '.'

# Percorre todos os arquivos .py no diretório e subdiretórios
for raiz, diretorios, arquivos in os.walk(diretorio_raiz):
    for arquivo in arquivos:
        if arquivo.endswith('.py'):
            caminho_arquivo = os.path.join(raiz, arquivo)
            print(f'Processando: {caminho_arquivo}')

            # Lê o conteúdo do arquivo
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                conteudo = f.read()

            # Aplica o autopep8
            conteudo_formatado = autopep8.fix_code(
                conteudo, options={'aggressive': 2})

            # Salva o conteúdo formatado de volta no arquivo
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo_formatado)
