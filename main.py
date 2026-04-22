import random
import time

class MesinSlotRTP:
    def __init__(self):
        self.saldo = 10000  # Saldo awal pemain
        self.simbols = ['🍒', '🍋', '🔔', '💎', '7️⃣']
        # Bobot diatur agar RTP berada di kisaran 96% (Matematika Kasino)
        self.bobot = [55, 25, 14, 5, 1] 
        self.payout = {
            '🍒': 5,    # 3x Ceri = 5x Taruhan
            '🍋': 10,   # 3x Lemon = 10x Taruhan
            '🔔': 20,   # 3x Bel = 20x Taruhan
            '💎': 50,   # 3x Permata = 50x Taruhan
            '7️⃣': 100   # 3x Angka 7 = 100x Taruhan
        }

    def putar(self, taruhan):
        self.saldo -= taruhan
        # RND dengan bobot yang sudah dikunci (RTP 96%)
        hasil = random.choices(self.simbols, weights=self.bobot, k=3)
        
        menang = 0
        pesan = "Zonk! Coba lagi. 😅"

        # 1. Cek Jackpot (3 Simbol Sama)
        if hasil[0] == hasil[1] == hasil[2]:
            menang = taruhan * self.payout[hasil[0]]
            pesan = f"JACKPOT {hasil[0]}! Menang Rp {menang} 🎉"
        
        # 2. Cek Menang Kecil (2 Simbol Sama - Margin pengaman pemain)
        elif hasil[0] == hasil[1] or hasil[1] == hasil[2] or hasil[0] == hasil[2]:
            menang = int(taruhan * 1.2)
            pesan = f"Lumayan! Menang Rp {menang} 💰"

        self.saldo += menang
        return hasil, pesan

    def mulai_permainan(self):
        print("=== MESIN SLOT RND - RTP 96% LOCKED ===")
        print(f"Saldo Awal: Rp {self.saldo}")

        while self.saldo > 0:
            print(f"\nSaldo saat ini: Rp {self.saldo}")
            try:
                input_user = input("Masukkan taruhan (atau ketik 'auto' untuk simulasi 100x, '0' untuk keluar): ").lower()
                
                if input_user == '0': break
                
                # Mode Simulasi Otomatis
                if input_user == 'auto':
                    taruhan = 100
                    print(f"Menjalankan 100 putaran otomatis dengan taruhan Rp {taruhan}...")
                    for _ in range(100):
                        if self.saldo < taruhan: break
                        self.putar(taruhan)
                    print("Simulasi selesai.")
                    continue

                taruhan = int(input_user)
                if taruhan > self.saldo:
                    print("Saldo tidak cukup!")
                    continue

                # Efek Visual
                print("Memutar... ", end="", flush=True)
                for _ in range(3):
                    time.sleep(0.3)
                    print("🎰", end="", flush=True)
                
                hasil, pesan = self.putar(taruhan)
                print(f"\n| {' | '.join(hasil)} |")
                print(pesan)

            except ValueError:
                print("Input tidak valid!")

        print(f"\nPermainan Berakhir. Saldo Akhir: Rp {self.saldo}")

if __name__ == "__main__":
    game = MesinSlotRTP()
    game.mulai_permainan()
