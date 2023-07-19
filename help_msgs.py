PROGRAM_USAGE = """
commands
    key-gen
        Gera uma chave de encripitação.
        -v : Exibe a chave gerada.
        -o : Caminho de arquivo para armazenar a chave.
    
    encrypt/decrypt
        -f : Expecifica que um arquivo sera criptografado/descriptografado.
        -d : Expecifica que um diretório sera criptografado/descriptografado.
        
        --ignore-suffix : Ignora arquivos que terminam com o valor passado. (apenas para encrypt)
"""

OUTPUT_KEYFILE_MSG = 'Caminho de arquivo para armazenar a chave.'
VIEWKEY_MSG = 'Exibe a chave gerada.'
FILE_MSG = 'Expecifica que um arquivo sera criptografado/descriptografado.'
DIRECTORY_MSG = 'Expecifica que um diretório sera criptografado/descriptografado.'
IGNORE_SUFFIX_MSG = 'Ignora arquivos que terminam com o valor passado. (apenas para encrypt)'
