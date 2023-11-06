#include <stdio.h>
#include <string.h>
#define MAKS 256



int main()
{
    int i, jumkar = 0;
    char teks[MAKS];
    puts("Masukkan suatu kalimat (maks 255 karakter).");
    //masukan dr keyboard
    gets(teks);
    for(i=0; teks[i]; i++)
    jumkar++;
    printf("\nJumlah karakter = %d\n", jumkar);
    return 0;
}