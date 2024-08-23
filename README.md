# Simple Discovering Device Files Script
Simples projeto de um script para varrer arquivos em mídias removíveis utilizando a linguagem Python

O projeto surgiu da ideia de estudar como pendrives com código malicioso funcionam e com isso aproveitei para fazer um script para checar todos os arquivos do pendrive e gerar
um arquivo de texto com o codigo de um .cmd(windows) caso encontrado

O pendrive "malicioso" utilizado foi feito a partir dessa fonte: [How to Make a Malicious USB Device and Have Some Harmless Fun](https://hackernoon.com/how-to-make-a-malicious-usb-device-and-have-some-harmless-fun) - (foi feito exatamente da forma ensinada aqui)

**obs**: o pendrive em si nao tem um codigo malicioso que o Windows Defender detecta(no meu caso, utilizei minha maquina pessoal com Windows 11), pois é um netcat para conexão remota.

**obs2**: provavelmente com o tempo eu vou mudar a forma como o programa funciona, pois é um caso bastante especifico por buscar um .cmd e com certeza existem formas mais reais e inteligentes de fazer um pendrive malicioso. Então sinta-se livre para mandar uma mensagem no meu discord(está na minha página do github) caso tenha algo que possa contribuir ainda mais com o meu aprendizado em infosec.


# Utilização
Os modulos são da biblioteca padrão do python, então caso você ja tenha instalado a linguagem [Python](https://www.python.org/downloads/), provavelmente vai funcionar

a forma de utilização é bem simples, basta conectar a midia removivel e rodar o script

```powershell
python .\SDDFS.py
```

Caso tenha um .cmd vai gerar um arquivo de texto chamado "log_do_cmd.txt" no diretorio onde voce rodou o programa

# Imagens

o pendrive:

![pendrive01](/images/pendrive01.png)

#

pasta do payload:

![pendrive02](/images/pendrive02.png)

#

rodando o script:

![script_rodando](/images/script_rodando.png)

#

caso encontre uma extensão .cmd:

![log_do_cmd](/images/log_do_cmd.png)


# Referências

https://abdus.dev/posts/python-monitor-usb/

https://docs.python.org/3/library/subprocess.html

https://hackernoon.com/how-to-make-a-malicious-usb-device-and-have-some-harmless-fun

https://www.tutorialspoint.com/python/os_walk.htm

https://stackoverflow.com/questions/63153352/how-to-pass-output-of-a-command-in-cmd-to-a-txt-file-using-python 

https://www.w3schools.com/python/ref_file_read.asp

https://www.geeksforgeeks.org/writing-to-file-in-python/








