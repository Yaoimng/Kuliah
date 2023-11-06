#include <stdio.h>

int main() {
   int a, b, c, min;
   
   printf("Masukkan tiga bilangan: ");
   scanf("%d %d %d", &a, &b, &c);

   min = a;
   
   if (b < min) {
      min = b;
   }
   
   if (c < min) {
      min = c;
   }
   
   printf("Nilai terkecil adalah %d", min);
   
   return 0;
}
