# ❄️ Refrigeração Inteligente com IA

Projeto de automação básica que utiliza Visão Computacional para ajustar a temperatura de um ambiente de acordo com o número de pessoas presentes.

## 📋 Como Funciona
O sistema utiliza a câmera (Webcam ou Celular via IP Webcam) para detectar rostos:

- **0 Pessoas:** 26°C (Modo Econômico)
- **1 Pessoa:** 24°C
- **2 ou mais:** A temperatura reduz 1°C para cada pessoa adicional (Limite de 18°C)

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
2. Clique em **"Start Server"** no app.
3. No código, use o endereço IP fornecido pelo app (não esqueça do `/video` no final):

```python
fonte_video = '[http://19](http://19)

## 🔧 Instalação
1. Clone o repositório.
2. Instale as dependências:

pip install -r requirements.txt

## Execute o script:
python ar.py