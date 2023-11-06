//Nama : Fadhil Zaky Budianto || NRP  : 2040221090
#include <stdio.h>

int fungsi_ganjil() {
       int bilangan;
   printf("Masukkan batas bilangan ganjil: ");
   scanf("%d", &bilangan);

   printf("Bilangan ganjil dari 1 - %d : ", bilangan);
   int j;
   for(int i = 0; i <= bilangan * 0.5; i++) {
        j = 2*i+1;
        if(i % 2 == 1) {
            j *= -1;
        }
           printf("%d ", j);
   }
}

int main() {
    fungsi_ganjil();

   return 0;
}

