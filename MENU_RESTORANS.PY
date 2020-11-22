import os
import time
from datetime import datetime
waktu = datetime.now()
daftar_menu = [  
    'mie goreng;13K',
    'nasi goreng;13K',
    'bakso;11K',
    'tekwan;11K',
    'air tawar;3K',
    'teh tawar;5K']

daftar_komentar = [
    'murah makananya enak=5 bintang',
    'murah semua makanany=5 bintang',
    'murah=5bintang']
def menu():
    os.system('cls')
    print('Menu Restoran')
    print('[1]lihat semua menu')
    print('[2].tambah menu')
    print('[3].tambahkan komentar')
    print('[4].lihat daftar komentar')
    print('[5].informasi aplikasi')
    print('[Q].keluar')

def lihat_semua_menu():
    os.system('cls')
    print('daftar menu yang tersimpan')
    for makanan in daftar_menu:
        nama, harga = makanan.split(";")
        print("%i : NAMA = %s - HARGA = %s" % (daftar_menu.index(makanan)+1, nama, harga))
    print("====================")
    input('tekan ENTER untuk kembali ke MENU')

def tambah_menu_baru():
    os.system('cls')
    print('menambahkan kontak baru')
    nama = input('nama menu baru : ')
    menu_baru = input('harga baru : ')
    data = f'{nama};{menu_baru}'
    daftar_menu.append(data)
    print('mohon tunggu data sedang disimpan...')
    print('daftar menu tersimpan')
    input('tekan ENTER untuk kembali ke MENU')

def lihat_komentar():
    os.system('cls')
    print('Daftar Komentar:')
    for komen in daftar_komentar:
        komentar,bintang = komen.split("=")
        print("%i-:%s - BINTANG : %s-"  % (daftar_komentar.index(komen)+1,komentar,bintang))
    print("====================")
    input('tekan ENTER untuk kembali ke MENU')

def tambah_komentar():
    rev = input("silahkan tinggalkan komentar anda: ")
    bintang = input("Bintang: ")
    data = f'{rev}={bintang}'
    daftar_komentar.append(data)
    print('mohon tunggu data sedang disimpan...')
    print('komentar tersimpan')
    input('tekan ENTER untuk kembali ke MENU')

def about():
    print('aplikasi ini adalah Tugas project yang diberikan oleh Sir Anas')
    print('Dibuat: 2020-11-22')
    input('tekan ENTER untuk kembali ke MENU')
while True:
    menu()
    user_input = input('pilihan : ').upper()
    if user_input =='Q':
        print('bye')
        break
    elif user_input =='1':
        lihat_semua_menu()
    elif user_input =="2":
        tambah_menu_baru()
    elif user_input == '3':
        tambah_komentar()
    elif user_input == '4':
        lihat_komentar()
    elif user_input == "5":
        about()

#SIR INI AKU UBA TEMA APLIKASI NY ASLINYA MAU BIKIN TIKET PARKIR MOBIL TAPI KARENA DIKIT FUNCTION YG TERPIKIR JADI GANTI KE MENU RESTORAN AJA
