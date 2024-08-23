#(S)imple (D)iscovering (D)evice (F)iles (S)cript

'''
TIPO DE DISPOSITIVO(NUMERO) | DESCRIÇÃO
0 | Unknown
1 | No Root Directory
2 | Removable Disk (o que queremos)
3 | Local Disk
4 | Network Drive
5 | Compact Disc
6 | RAM Disk
'''

#iremos usar um comando do powershell para pegar todas essas informações, colocar em um json
# e fazer o python mostrar isso como saida utilizando o modulo 'subprocess'

import subprocess
import json
import os


def list_pendrives():
    # o comando que voce pode utilizar no porwershell é ese para listar todos os drives:
    '''PS> Get-WmiObject -Class Win32_LogicalDisk'''
    #para filtrar as informações desejadas e converter na sintaxe do json
    '''PS> Get-WmiObject -Class Win32_LogicalDisk | Select-Object deviceid,volumename,drivetype | ConvertTo-Json'''

    proc = subprocess.run(
        args=[
        'powershell',
        '-noprofile',
        '-command',
        'Get-WmiObject -Class Win32_LogicalDisk | Select-Object deviceid,volumename,drivetype | ConvertTo-Json'
        ],text=True,stdout=subprocess.PIPE
    )
    # o subprocess.PIPE de forma geral é um argumento para o Popen que indica o fluxo que os comandos vão seguir
    
    if proc.returncode != 0 or not proc.stdout.strip():
        print("Enumeração de drivers falhou")
        return []

    devices = json.loads(proc.stdout)

    #como o drive de interesse será apenas pendrives(Removable Disk), irei retornar apenas ele do json
    for device in devices:
        if (device['drivetype'] == 2):
            return device
        
def find_files(list):
    if list==None:
        #caso nao tenha um disco removivel conectado
        print("Nao foi encontrado um disco removivel")
    else:#usando o os.walk "varrer" o disco removivel
        pendrive_path = list['deviceid']+"\\"
        for root,dirs,files in os.walk(pendrive_path,topdown=True):
            for filename in files:
                file_path = os.path.join(root,filename)
                print(file_path)
                #pensando em um pendrive com um codigo malicioso, irei buscar por arquivos com a extensao '.cmd' e retornar um txt para o meu diretorio atual antes de abrir o arquivo
                if file_path.endswith(".cmd"): 
                    output = subprocess.getoutput(file_path)
                    output_txt = open("log_do_cmd.txt","a+")
                    output_txt.write(output)
                    output_txt.close()             
            for dirname in dirs:
                print(os.path.join(root,dirname))


list = list_pendrives()

if __name__=='__main__':
    find_files(list)
