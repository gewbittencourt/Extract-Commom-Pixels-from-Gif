# Extrator de pixels em comum entre frames de um GIF

Este código foi desenvolvido para facilitar a detecção de imagens animadas de GIFs para um bot antigamente desenvolvido por mim. O objetivo é identificar e extrair os pixels comuns em todas as frames de um GIF, permitindo uma análise mais precisa das animações garantindo maior eficácia na detecção de padrões visuais utilizados pelo bot. Isso possibilitou que um threshold maior fosse aplicado no processo, diminuindo o número de falso positivo.


## Tecnologias Utilizadas

Python: Linguagem principal para desenvolvimento do script.

PIL (Pillow): Biblioteca usada para manipulação de imagens, permitindo abrir, processar e salvar as imagens.

ImageChops: Módulo do Pillow utilizado para operações de comparação entre imagens.


## Como Funciona
O script carrega todas as frames de um GIF.
Compara os pixels de cada frame, identificando aqueles que permanecem constantes ao longo de todas as frames.
Cria uma nova imagem contendo apenas os pixels comuns entre todas as frames.
Salva a imagem resultante em formato PNG.


## Resultados
### Entrada
![](https://www.tibiawiki.com.br/images/2/2d/Alicorn_Ring.gif)

### Resultado
![](https://i.ibb.co/wC0Xdbj/output.png)
