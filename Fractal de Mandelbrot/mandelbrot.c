#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
    srand(time(NULL));

    /* screen ( integer) coordinate */
    int iX,iY;
    const int iXmax = 1280; 
    const int iYmax = 720;

    /* world ( double) coordinate = parameter plane*/
    double Cx,Cy;
    const double CxMin = rand() % (int)(0 + 1 - (-2)) + (-2); 
    const double CyMin = rand() % (int)(0 + 1 - (-2)) + (-2);
    const double CxMax = rand() % (int)(2 + 1 - (0)) + (0);
    const double CyMax = rand() % (int)(2 + 1 - (0)) + (0);
    // const double CxMin = -1;
    // const double CxMax = 0;
    // const double CyMin = -1;
    // const double CyMax = 1;

    printf("CxMin = %f, CxMax = %f, CyMin = %f, CyMax = %f", CxMin, CxMax, CyMin, CyMax);

    double PixelWidth=(CxMax-CxMin)/iXmax;
    double PixelHeight=(CyMax-CyMin)/iYmax;

    /* color component ( R or G or B) is coded from 0 to 255 */
    /* it is 24 bit color RGB file */
    const int MaxColorComponentValue=255; 
    
    FILE * fp;
    char *filename="new4.png";

    char *comment="# ";/* comment should start with # */

    static unsigned char color[3];

    /* Z=Zx+Zy*i  ;   Z0 = 0 */
    double Zx, Zy;
    double Zx2, Zy2; /* Zx2=Zx*Zx;  Zy2=Zy*Zy  */

    /*  */
    int Iteration;
    const int IterationMax=3000;

    /* bail-out value , radius of circle ;  */
    const double EscapeRadius= 2;
    double ER2=EscapeRadius*EscapeRadius;

    /*create new file,give it a name and open it in binary mode  */
    fp= fopen(filename,"wb"); /* b -  binary mode */
    /*write ASCII header to the file*/

    fprintf(fp,"P6\n %s\n %d\n %d\n %d\n",comment,iXmax,iYmax,MaxColorComponentValue);

    int rInteriorMandelbrot = rand() % MaxColorComponentValue;
    int gInteriorMandelbrot = rand() % MaxColorComponentValue;
    int bInteriorMandelbrot = rand() % MaxColorComponentValue;

    printf("\n\nRGB INTERIOR= %d, %d, %d\n\n", rInteriorMandelbrot, gInteriorMandelbrot, bInteriorMandelbrot);

    int rExteriorMandelbrot = rand() % MaxColorComponentValue;
    int gExteriorMandelbrot = rand() % MaxColorComponentValue;
    int bExteriorMandelbrot = rand() % MaxColorComponentValue;

    printf("RGB EXTERIOR= %d, %d, %d\n\n", rExteriorMandelbrot, gExteriorMandelbrot, bExteriorMandelbrot);

    do{
        rInteriorMandelbrot = rand() % MaxColorComponentValue;
        gInteriorMandelbrot = rand() % MaxColorComponentValue;
        bInteriorMandelbrot = rand() % MaxColorComponentValue;
    } while (rInteriorMandelbrot - rExteriorMandelbrot < 100 && gInteriorMandelbrot - gExteriorMandelbrot < 100 && bInteriorMandelbrot - bExteriorMandelbrot < 100);

   printf("\n\nRGB INTERIOR DEPOIS DO WHILE= %d, %d, %d\n\n", rInteriorMandelbrot, gInteriorMandelbrot, bInteriorMandelbrot);

    /* compute and write image data bytes to the file*/
    for(iY = 0; iY < iYmax; iY++){
        Cy = CyMin + iY * PixelHeight;

        if (fabs(Cy) < PixelHeight/2) Cy = 0.0; /* Main antenna */

        for(iX = 0; iX < iXmax; iX++){         
            Cx = CxMin + iX * PixelWidth;
            /* initial value of orbit = critical point Z= 0 */
            Zx=0.0;
            Zy=0.0;
            Zx2=Zx*Zx;
            Zy2=Zy*Zy;
            /* */
            for (Iteration = 500; Iteration < IterationMax && ((Zx2+Zy2)<ER2);Iteration++){
                Zy = 2*Zx*Zy + Cy;
                // Zy = 2*Zx*Zy + Cy;
                Zx = Zx2-Zy2 +Cx;
                Zx2 = Zx*Zx;
                Zy2 = Zy*Zy;
            };
            /* compute  pixel color (24 bit = 3 bytes) */
            if (Iteration == IterationMax){ /*  EXTERIOR of Mandelbrot set = black */
                color[0] = rExteriorMandelbrot;
                color[1] = gExteriorMandelbrot;  
                color[2] = bExteriorMandelbrot;                        
            } else { /* INTERIOR of Mandelbrot set = white */
                color[0] = rInteriorMandelbrot;
                color[1] = gInteriorMandelbrot;
                color[2] = bInteriorMandelbrot;   
                
            };
            /*write color to the file*/
            fwrite(color,1,3,fp);
        }
    }
    fclose(fp);
    return 0;
 }