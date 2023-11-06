#include <stdio.h>

// Tipe_data Nama_variabel = Nilai_variabel

// Soal Latihan 1 dan 2

void main(){
    int i;
    char letters[20] = {'a', 'b', 'c', 'z', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'};
    char cari;
    printf("Masukkan karakter yang dicari: \n");
    scanf("%c", &cari);
    for (i = 0; i < 20; i++)
    {
        if (letters[i] == cari)
        {
            printf("Karakter %c ada di dalam letters. \n", cari);
        } else
        {
            printf("Karakter %c Tidak ada dalam letters. \n", cari);
        }
        
        
    } 

}