"""
Aplikasi deteksi gempa terkini


tanggal : 23 Juni 2023
waktu : 23:03:09 WIB
Magnitudo: 2.6
Kedalaman : 9 km
Lokasi : 3.51 LS - 135.43 BT
Pusat : Pusat gempa berada di darat 18 km BaratDaya Nabire
Dirasakan : Dirasakan (Skala MMI): II Nabire

"""
def ekstrasi_data():
    pass

    hasil = dict()
    hasil['tanggal'] = '23 Juni 2023'
    hasil['waktu'] = '23:03:09 WIB'
    hasil['magnitudo'] = 2.6
    hasil['lokasi'] = {'ls': 3.51, 'bt': 135.43}
    hasil['pusat'] = 'Pusat gempa berada di darat 18 km BaratDaya Nabire'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI) : II Nabire'



    return hasil

def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")



if __name__=='__main__':
    print('Aplikasi Utama')
    result = ekstrasi_data()
    tampilkan_data(result)

