all: compileFractal generateFractal generateExecutable

compileFractal: mandelbrot.c
	gcc -o mandelbrot mandelbrot.c -lm

generateFractal:
	gcc -shared -o libMandelbrot.so -fPIC mandelbrot.c

generateExecutable:
	gcc -o mandelbrot mandelbrot.c -lm
	gcc -shared -o libMandelbrot.so -fPIC mandelbrot.c
	pyinstaller --onefile --add-data 'libMandelbrot.so:.' fractalMandelbrot.py
	mv ./dist/fractalMandelbrot ./