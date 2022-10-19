# Fractal de Mandelbrot

## **📂 Organização dos Diretórios**:

```
├── Fractal de Mandelbrot
│   ├── avatares
│   ├── interface
│   └── testes
│       ├── arithmatic
│       ├── imagens
│       ├── mandelbrot
│       ├── mandelbrotIterative
│       └── mandelbrotWithGraphics
└────── .gitignore
    ├── fractalMandelbrot.py
    ├── loadingPage.py
    ├── Makefile
    ├── mandelbrot
    ├── mandelbrot.c
    ├── mandelbrot.h
    ├── showFractal.py
    └── README.md
```

## **🤔 Explicação dos diretórios**:

- _avatares_: Contém as fotos .png dos avatares dos integrantes do grupo utilizadas na interface;
- _interface_: Contém os arquivos .ui (XML) na qual consiste na interface da aplicação geradas no QtDesigner com a biblioteca PyQt5;
- _testes_: Neste diretório contém todos os testes feitos para chegar no resultado final da nossa aplicação; - _arithmatic_: Aqui geramos a primeira biblioteca compartilhada, assim aprendendo a consumir a mesma no Python; - _imagens_: Resultados de alguns fractais durante o período de teste; - _mandelbrot e mandelbrotWithGraphics_: Modelos geradores de Fractais de Mandelbrot testados e descartados, pois não favoreciam a integração com o Python.
- _.gitignore_: Ignoramos arquivos não necessários para o funcionamento da aplicação
- _fractalMandelbrot .py, loadingPage .py e showFractal .py_: São os arquivos em Python da interface gráfica da aplicação, sendo o menu principal, a tela de carregamento e a tela em que é mostrado o fractal gerado, nessa respectiva ordem;
- _mandelbrot .c e mandelbrot .h_: São os arquivos em C utilizados para gerar o fractal, sendo o .c o código em si e o .h a biblioteca do mesmo;
- _Makefile_: Arquivo para facilitar a compilação e execução do código, sendo possível fazer isso com uma quantidade reduzida de comandos;

## **💻 Como Executar?**

- Bibliotecas Python necessárias: - pyqt5 -> `pip install pyqt5` - pyinstaller -> `pip install pyinstaller`
- **Windows** - Instalar Make -> `winget install GnuWin32.Make`
