#include <stdio.h>


int main()
    {   
        int Alas,Tinggi,Luas;
        printf("Masukkan Alas: \n");
        scanf("%d", &Alas);
        printf("Masukkan Tinggi: \n");
        scanf("%d", &Tinggi);
        
        Luas = 0.5 * Alas * Tinggi;

        printf("Luas Segitiga Adalah %2d \n", Luas);
        
        return 0;
    } 
