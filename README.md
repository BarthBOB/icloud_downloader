# 📥 iCloud Downloader (via Python)

Script em Python para baixar pastas e arquivos diretamente do **iCloud Drive**, com autenticação e suporte a 2FA. Ideal para fazer backup local de grandes quantidades de arquivos organizados em pastas.

---

## 🚀 Funcionalidades

- Autenticação segura com Apple ID
- Suporte completo a autenticação em duas etapas (2FA)
- Navegação interativa pelas pastas do iCloud Drive
- Download completo de qualquer pasta com subpastas
- Preservação da estrutura original e timestamps
- Interface via terminal simples e amigável
- Totalmente offline após autenticação

---

## 📦 Requisitos

- Python 3.7 ou superior
- Conta Apple com iCloud Drive ativado

---

## 🔧 Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/icloud_downloader/icloud-downloader.git
cd icloud-downloader
```

2. **Instale as dependências:**

```bash
pip install pyicloud
```

---

## ▶️ Como usar

1. **Execute o script:**

```bash
python icloud_downloader.py
```

2. **Digite seu Apple ID e senha.**
   - Caso tenha 2FA ativado, você receberá um código no seu dispositivo confiável.

3. **Escolha a pasta do iCloud Drive que deseja baixar.**
   - O script listará todas as pastas da raiz do seu iCloud Drive.
   - Digite o número correspondente à pasta desejada.

4. **Aguarde o download.**
   - Todos os arquivos serão baixados para: `G:\ICLOUD BAIXAR` (pode alterar no código).
   - A estrutura original de pastas será preservada.

---

## 💡 Exemplo de uso

```bash
Digite seu Apple ID: meunome@icloud.com
Digite sua senha: **********
🔐 Autenticação de dois fatores requerida.
Digite o código de 2FA: 123456
📂 Conteúdo do iCloud Drive:
[0] Documentos
[1] Fotos
[2] Passeio
Digite o número do item que deseja baixar: 2
🚀 Iniciando download de 'Passeio'...
...
✅ C0425.MP4
✅ C0426.MP4
✨ Concluído: 2079 arquivos baixados.
```

---

## ✏️ Personalização

Para alterar a pasta de destino dos arquivos, modifique a linha:

```python
DIR_DOWNLOAD = r"G:\ICLOUD BAIXAR"
```

Para, por exemplo:

```python
DIR_DOWNLOAD = r"D:\Backup\iCloud"
```

---

## ❗ Avisos

- Este projeto **não acessa fotos do iCloud** (use a biblioteca `pyicloud-ipd` para isso).
- A Apple pode ocasionalmente alterar APIs internas — em caso de erro, verifique se há forks atualizados da lib.

---

## 🙌 Contribuições

Sinta-se livre para abrir *issues* ou *pull requests* se quiser ajudar a melhorar!

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
