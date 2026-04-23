# ❄️ Refrigeração Inteligente com IA

Projeto de automação básica que utiliza Visão Computacional para ajustar a temperatura de um ambiente de acordo com o número de pessoas presentes.

## 📋 Como Funciona
O sistema utiliza a câmera (Webcam ou Celular via IP Webcam) para detectar rostos:

- **0 Pessoas:** 26°C (Modo Econômico)
- **1 Pessoa:** 24°C
- **2 ou mais:** A temperatura reduz 1°C para cada 2 pessoa adicional (Limite de 18°C)

## 🛠️ Tecnologias
- **Python 3.12**
- **OpenCV** (Haar Cascades)

## ⚙️ Configuração da Câmera
Antes de executar, escolha qual fonte de vídeo você vai utilizar no arquivo `ar.py`:

### Opção A: Usando Webcam Integrada ou USB
No código, configure a variável da seguinte forma:
```python
fonte_video = 0

### Opção B: Usando Telefone (IP Webcam)
1. Instale o app **IP Webcam** no seu Android.
2. Clique em **"Start Server"**(tres ponto acima canto superior direito)no app.
3. No código, use o endereço IP fornecido pelo app 1 aparece(não esqueça do `/video` no final):
4. linha 7 do codigo tem as instrucoes 

```python
fonte_video = '[http://192.168.](http://192.168.)x.x:8080/video'
## 🔧 Instalação
1. Clone o repositório.
2. Instale as dependências:
```bash
pip install -r requirements.txt

Execute o script:

Bash
python ar.py
