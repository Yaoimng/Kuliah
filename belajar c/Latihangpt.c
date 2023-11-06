#include <stdio.h>

int main() {
   int bilangan;

   printf("Masukkan bilangan bulat positif: ");
   scanf("%d", &bilangan);

   printf("Bilangan ganjil dari 1 hingga %d adalah: ", bilangan);
   for(int i = 1; i <= bilangan; i++) {
       if(i % 2 == 0) {
           printf("%d ", i);
       }
   }

   return 0;
}
