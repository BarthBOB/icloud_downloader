from pyicloud import PyiCloudService
import os
import time
import shutil

def criar_estrutura_local(caminho):
    try:
        os.makedirs(caminho, exist_ok=True)
        return True
    except Exception as e:
        print(f"Erro ao criar pasta {caminho}: {str(e)}")
        return False
def obter_drive_node_por_caminho(ponto_inicial, caminho):
    node = ponto_inicial
    partes = caminho.strip("/").split("/")
    for parte in partes:
        node = node[parte]
    return node


def baixar_arquivo_icloud(file_node, caminho_local):
    try:
        os.makedirs(os.path.dirname(caminho_local), exist_ok=True)
        with file_node.open(stream=True) as resposta:
            with open(caminho_local, 'wb') as f:
                shutil.copyfileobj(resposta.raw, f)

        # Tentar preservar o timestamp (não é garantido)
        try:
            mod_time = time.mktime(file_node.date_modified.timetuple())
            os.utime(caminho_local, (mod_time, mod_time))
        except Exception as e:
            print(f"Aviso: não foi possível ajustar o timestamp de {caminho_local}: {e}")
        return True
    except Exception as e:
        print(f"Erro ao baixar '{caminho_local}': {e}")
        return False

def listar_conteudo_recursivo(item, caminho_atual=''):
    conteudo = []
    try:
        if item.type == 'folder':
            for nome in item.dir():
                filho = item[nome]
                novo_caminho = os.path.join(caminho_atual, nome).replace("\\", "/")
                if filho.type == 'folder':
                    conteudo.extend(listar_conteudo_recursivo(filho, novo_caminho))
                else:
                    conteudo.append(novo_caminho)
        else:
            conteudo.append(caminho_atual)
    except Exception as e:
        print(f"Erro ao listar {caminho_atual}: {e}")
    return conteudo

def baixar_conteudo_icloud(api, item, dir_download):
    criar_estrutura_local(dir_download)
    print("🔍 Escaneando conteúdo do iCloud...")
    arquivos = listar_conteudo_recursivo(item)
    print(f"📦 Total de arquivos encontrados: {len(arquivos)}")
    
    baixados = 0
    for caminho_arquivo in arquivos:
        try:
            file_node = obter_drive_node_por_caminho(item_selecionado, caminho_arquivo)

            caminho_local = os.path.join(dir_download, caminho_arquivo)
            print(f"⬇️ Baixando: {caminho_arquivo}")
            if baixar_arquivo_icloud(file_node, caminho_local):
                print(f"✅ {caminho_arquivo}")
                baixados += 1
            else:
                print(f"❌ Falhou: {caminho_arquivo}")
        except Exception as e:
            print(f"Erro ao acessar {caminho_arquivo}: {e}")
    print(f"\n✨ Concluído: {baixados}/{len(arquivos)} arquivos baixados.")

# --- Execução Principal ---

DIR_DOWNLOAD = r"G:\ICLOUD BAIXAR"


# Login
api = PyiCloudService(
    input("Digite seu Apple ID: "),
    input("Digite sua senha: ")
)

# 2FA
if api.requires_2fa:
    print("🔐 Autenticação de dois fatores requerida.")
    code = input("Digite o código de 2FA: ")
    if not api.validate_2fa_code(code):
        print("❌ Código inválido.")
        exit()
    print("🔓 Autenticado com sucesso.")

# Listar itens do Drive
print("\n📂 Conteúdo do iCloud Drive:")
try:
    itens = api.drive.dir()
    for i, nome in enumerate(itens):
        print(f"[{i}] {nome}")
except Exception as e:
    print(f"Erro ao acessar iCloud Drive: {e}")
    exit()

# Selecionar item
try:
    indice = int(input("\nDigite o número do item que deseja baixar: "))
    nome_item = list(itens)[indice]
    item_selecionado = api.drive[nome_item]
except Exception as e:
    print(f"❌ Seleção inválida: {e}")
    exit()

# Iniciar download
destino = os.path.join(DIR_DOWNLOAD, nome_item)
print(f"\n🚀 Iniciando download de '{nome_item}'...")
baixar_conteudo_icloud(api, item_selecionado, destino)
print(f"\n📁 Verifique os arquivos em: {os.path.abspath(DIR_DOWNLOAD)}")
