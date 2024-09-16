# List data user
login_data = [
    {'Role': 'Admin', 'UserID': 'AD01', 'Username': 'Admin', 'Pass': 'Admin'},
    {'Role': 'Anggota', 'UserID': 'AP01', 'Username': 'Amin', 'Pass': 'Gacor'},
    {'Role': 'Anggota', 'UserID': 'AP02', 'Username': 'Zakaria', 'Pass': 'Ngecor'}
]

# List alat
barang_dict = [
    {'No': 1, 'Nama Alat': 'Gelas beaker', 'Qty': 10, 'Status': 'Tersedia'},
    {'No': 2, 'Nama Alat': 'Gelas ukur', 'Qty': 3, 'Status': 'Tersedia'},
    {'No': 3, 'Nama Alat': 'Erlenmeyer', 'Qty': 4, 'Status': 'Tersedia'},
    {'No': 4, 'Nama Alat': 'Corong kaca', 'Qty': 0, 'Status': 'Habis'}
]

def login():
    print('Selamat datang di Laboratorium Aplus Corp.!\nSilakan Login terlebih dahulu')
    while True:
        username = input('Username/User ID: ')
        password = input('Pass: ')
        for user in login_data:
            if username == user['Username'] and password == user['Pass']:
                return user['Role']
        print('Username atau Password salah.')

def menu_admin():
    global barang_dict
    while True:
        print('Selamat datang di Panel Admin!\n1. List Alat\n2. Edit Alat\n3. List Anggota\n4. Edit Anggota\n5. Keluar')
        pilihan = input('Silakan pilih menu yang tersedia: ')
        if pilihan == '1':
            tampilkan_alat()
        elif pilihan == '2':
            edit_alat()
        elif pilihan == '3':
            tampilkan_anggota()
        elif pilihan == '4':
            edit_anggota()
        elif pilihan == '5':
            print('Silakan pilih menu keluar.\n1. Akhiri Program\n2. Ganti akun.')
            keluar = int(input('[1/2] ? :'))
            if keluar == 1 :
                print('Terima kasih sudah mampir\n-\n-\n-\n-.')
                exit()
            elif keluar == 2 :
                main()
            else: 
                print('Pilih menu yang sesuai.')
        else:
            print('Pilih menu yang sesuai.')

def tampilkan_anggota():
    print('-'*30)
    print('Role\t\tUsername')
    print('-'*30)
    for user in login_data:
        print(f"{user['Role']}\t\t{user['Username']}")
    print('-'*30)

def tampilkan_alat():
    global barang_dict
    print('-'*41)
    print('No.\tNama Alat\tQty\tStatus')
    print('-'*41)
    for alat in barang_dict:
        print(f"{alat['No']}\t{alat['Nama Alat']}\t{alat['Qty']}\t{alat['Status']}")
    print('-'*41)

def edit_alat():
    global barang_dict
    while True:
        print('1. Update Alat\n2. Tambah Alat\n3. Hapus Alat\n4. Kembali ke Menu Utama')
        menu_edit_alat = input('Pilih Menu [1-4]: ')
        tampilkan_alat()
        if menu_edit_alat == '1':
            try:
                no_alat = int(input('Nomor Alat: '))
                perubahan_qty = int(input('Perubahan Qty (bila berkurang input dengan [-]: '))
                update_alat(no_alat,perubahan_qty)
            except ValueError:
                print('Input tidak valid. Masukkan angka yang benar.')
        elif menu_edit_alat == '2':
            nama_alat = input('Masukkan Nama alat baru: ')
            try:
                qty = int(input('Masukkan Jumlah Qty: '))
                tambah_alat(nama_alat, qty)
            except ValueError:
                print('Input tidak valid. Masukkan angka yang benar.')
        elif menu_edit_alat == '3':
            try:
                no_alat = int(input('Nomor Alat yang ingin dihapus: '))
                hapus_alat(no_alat)
            except ValueError:
                print('Input tidak valid. Masukkan angka yang benar.')
        elif menu_edit_alat == '4':
            break
        else:
            print('Masukkan menu yang tersedia.')

def update_alat(no_alat,perubahan_qty):
    global barang_dict
    for alat in barang_dict:
        if alat['No'] == no_alat :
            alat['Qty'] += perubahan_qty
            alat['Status'] = 'Tersedia' if alat['Qty'] > 0 else 'Habis'
            tampilkan_alat()
            print(f"Jumlah alat pada Alat No. {no_alat} berhasil diperbarui.")
            return
    print("No Alat tidak ditemukan.")

def tambah_alat(nama_alat, qty):
    tampilkan_alat()
    if any(alat['Nama Alat'].lower() == nama_alat.lower() for alat in barang_dict):
        print("Alat dengan nama ini sudah ada dalam list.")
        return
    no_baru = max(alat['No'] for alat in barang_dict) + 1 if barang_dict else 1
    status = 'Tersedia' if qty > 0 else 'Habis'
    barang_dict.append({'No': no_baru, 'Nama Alat': nama_alat, 'Qty': qty, 'Status': status})
    tampilkan_alat()
    print(f"Alat berhasil ditambahkan dengan No {no_baru}.")

def hapus_alat(no_alat):
    global barang_dict
    barang_dict = [alat for alat in barang_dict if alat['No'] != no_alat]
    tampilkan_alat()
    print('Alat telah dihapus.')

def edit_anggota():
    while True:
        global login_data
        print('1. Tambah Anggota\n2. Hapus Anggota\n3. Kembali ke Menu Utama')
        menu_edit_anggota = input('Masukkan Menu yang tersedia [1-3]: ')
        if menu_edit_anggota == '1':
            username = input('Masukkan username: ').capitalize()
            tambah_anggota(username)
            tampilkan_anggota()
        elif menu_edit_anggota == '2':
            username = input('Masukkan username yang ingin dihapus: ').capitalize
            hapus_anggota(username)
            tampilkan_anggota()
        elif menu_edit_anggota == '3':
            menu_admin()
        else:
            print('Masukkan menu yang tersedia.')

def tambah_anggota(username):
    if any(user['Username'] == username for user in login_data):
        print('Username sudah terdaftar.')
        return
    role = input('Masukkan role user: ').capitalize()
    userid = input('Masukkan UserID (AD-- untuk Admin // AP-- untuk Anggota): ').upper()
    login_data.append({'Role': role, 'UserID': userid, 'Username': username, 'Pass': '12345'}) # Tambahkan password default
    print('Data telah didaftarkan.')

def hapus_anggota(username):
    global login_data
    login_data = [user for user in login_data if user['Username'] != username]
    print('Anggota telah dihapus.')

def menu_anggota():
    while True:
        print('Selamat datang di Panel Anggota!\n1. List Alat\n2. Pinjam Alat\n3. Keluar')
        pilihan = input('Silakan pilih menu yang tersedia: ')
        if pilihan == '1':
            tampilkan_alat()
        elif pilihan == '2':
            pinjam_alat()
        elif pilihan == '3':
            print('Silakan pilih menu keluar.\n1. Akhiri Program\n2. Ganti akun.')
            keluar = int(input('[1/2] ? :'))
            if keluar == 1 :
                print('Terima kasih sudah mampir\n-\n-\n-\n-.')
                exit()
            elif keluar == 2 :
                main()
            else: 
                print('Pilih menu yang sesuai.')
        else:
            print('Pilih menu yang sesuai.')

def pinjam_alat():
    tampilkan_alat()
    try:
        no_alat = int(input('Nomor Alat: '))
        sewa_qty = int(input('Jumlah Qty: '))
        sewa_alat(no_alat, sewa_qty)
    except ValueError:
        print('Input tidak valid. Masukkan angka yang benar.')

def sewa_alat(no_alat, sewa_qty):
    for alat in barang_dict:
        if alat['No'] == no_alat:
            if alat['Status'] == 'Habis':
                print('Alat sedang habis.')
            elif alat['Qty'] >= sewa_qty:
                alat['Qty'] -= sewa_qty
                alat['Status'] = 'Tersedia' if alat['Qty'] > 0 else 'Habis'
                print(f"Alat No. {no_alat} berhasil dipinjam.")
            else:
                print(f"Jumlah alat yang tersedia tidak cukup. Sisa: {alat['Qty']}.")
            return
    print("No Alat tidak ditemukan.")

def main():
    user_role = login()
    if user_role == 'Admin':
        print(f'Login berhasil! Role Anda adalah: {user_role}')
        menu_admin()
    elif user_role == 'Anggota':
        menu_anggota()

main()