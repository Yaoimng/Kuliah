#include <stdio.h>
#include <time.h>

struct ParkingTicket {
    char plate_number[10];
    time_t time_in;
};

int main() {
    struct ParkingTicket ticket;
    time_t current_time;

    printf("Enter plate number: ");
    scanf("%s", ticket.plate_number);

    int pilihan;
    printf("Pilih Kendaraan: \n ");
    printf("1.Mobil \t Rp.5000 \n");
    printf("2.Motor \t RP.3000 \n");
    printf("Pilih kendaraan (1-2): ");
    scanf("%d", &pilihan);


    time(&current_time);
    ticket.time_in = current_time;

    printf("=====PT. Pagi Siang Sore=====\n");
    printf("---Tiket Parkir---\n");
    printf("Ticket created\n");
    printf("Plate number: %s\n", ticket.plate_number);
    printf("Time in: %s", ctime(&ticket.time_in));

    return 0;
}
