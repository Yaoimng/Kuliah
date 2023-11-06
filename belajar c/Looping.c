#include <stdio.h>

main() 
{
  char kar;
  int jumkar = 0, jumspasi = 0;
  printf("Masukkan Kalimat!\n\n");
  while ((kar = getchar() != '\n') 
  {
    jumkar = jumkar + 1;
    if (kar == ' ')
    	jumspasi = jumspasi + 1;
  }
  printf("\nJumlah karakter = %d", jumkar);
  printf("\nJumlah SPASI - %d\n\n", jumspasi);
}