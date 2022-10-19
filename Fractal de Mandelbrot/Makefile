compileFractal: mandelbrot.c
	gcc -o mandelbrot mandelbrot.c -lm

generateFractal:
	gcc -shared -o libMandelbrot.so -fPIC mandelbrot.c

generateExecutableLinux:
	gcc -o mandelbrot mandelbrot.c -lm
	gcc -shared -o libMandelbrot.so -fPIC mandelbrot.c
	pyinstaller --onefile --add-data 'libMandelbrot.so:.' fractalMandelbrot.py
	mv ./dist/fractalMandelbrot ./

generateExecutableWindows:
	gcc -o mandelbrot mandelbrot.c -lm
	gcc -shared -o libMandelbrot.so -fPIC mandelbrot.c
	pyinstaller --onefile --add-data 'libMandelbrot.so;.' fractalMandelbrot.py
	move \dist\fractalMandelbrot .\