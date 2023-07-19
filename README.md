<div style="display: flex; justify-content: center;">
    <h1>🔓 Xcrypt 🔐</h1>
</div>

---
<h2>
    Um CLI (Command Line Interface) em python para criptografar e descriptografar arquivos.
    <br>
    <br>
</h2>

### Criptografar:
```bash
# para um unico arquivo
$ python xcrypt.py encrypt -f /caminho/do/arquivo
# para um diretório
$ python xcrypt.py encrypt -d /caminho/do/diretório/
```

### Descriptografar:
```bash
# para um unico arquivo
$ python xcrypt.py decrypt -f /caminho/do/arquivo
# para um diretório
$ python xcrypt.py decrypt -d /caminho/do/diretório/
```

### Gerar uma key:
```bash
# a flag -v exibe a chave gerada
$ python xcrypt.py key-gen -o /aquivo/de/saida -v 
```
