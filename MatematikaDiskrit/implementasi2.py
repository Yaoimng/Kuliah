def card_sort(cards):
    for i in range(1, len(cards)):
        current_card = cards[i]  # Simpan kartu saat ini
        j = i - 1

        # Pindahkan kartu yang lebih kecil ke posisi berikutnya
        while j >= 0 and current_card < cards[j]:
            cards[j + 1] = cards[j]
            j -= 1

        # Tempatkan kartu saat ini pada posisi yang benar
        cards[j + 1] = current_card

# Inputan kartu
deck = []
num_cards = int(input("Masukkan jumlah kartu: "))

for i in range(num_cards):
    card = input(f"Masukkan kartu ke-{i + 1}: ")
    deck.append(card)

# Tampilkan deck sebelum penyusunan
print("Deck sebelum disusun:", deck)

# Panggil fungsi penyusunan kartu
card_sort(deck)

# Tampilkan deck setelah penyusunan
print("Deck setelah disusun:")
for card in deck:
    print(card)
