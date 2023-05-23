# Importaçoes
from zipfile import ZipFile, ZIP_DEFLATED
import pathlib
import os
import requests

# Pasta que vai os arquivos
SAIDA_DIR = "output"

# Links para donwload
urls = [
    "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546_571_577.pdf",
    "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546_571_577.xlsx",
    "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN540_RN541_RN542_RN544_546_550_553_571v2_575_576_577.pdf",
    "https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_III_DC_2021_RN_465.2021.v2.pdf",
    "https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf"
]

# Baixando os arquivos e colocando na pasta do Output
for url in urls:
    response = requests.get(url, timeout=20)

    if response.status_code == 200:
        arquivo_path = os.path.join(SAIDA_DIR, os.path.basename(url))
        with open(arquivo_path, 'wb') as f:
            f.write(response.content)

# Zipando e compactando os arquivos da pasta Output
ZIP_PATH = './output.zip'
DIRECTORY_TO_ZIP = './output'

folder = pathlib.Path(DIRECTORY_TO_ZIP)

with ZipFile(ZIP_PATH, 'w', ZIP_DEFLATED) as zip:
    for file in folder.iterdir():
        zip.write(file, arcname=file.name)
