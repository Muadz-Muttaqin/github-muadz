import random
welcome_message='HAI PERKENALKAN SAYA MUADZ'
muadz_position= random.randint(1,4)


Nama = 'Muadz Muttaqin'
Usia = 19
print ('*************************')
print (f'**{welcome_message}**')# Output Welcome
print ('*************************')

print(f'''
nama saya adalah {Nama}
usia saya adalah {Usia}
      ''')

nomor_saya = 5
if nomor_saya == 4:
      
      print('benar nomor saya 4')
      

else:
      print('ah bukan 4 teryata...')
      
      
nama_user = input('masukan nama anda:')
print(f'''hallo bang {nama_user} coba isi jawaban ini
|_| |_| |_| |_|
''')

pilihan_user = int(input('dimana goa menurut kamu muadz berada? [1/2/3/4] '))

def pilihan_ya_tidak():
      while True:
            pilihan = input('apakah melanjutkana? (ya/tidak):').lower()
            


print(f'pilihan kamu adalah {pilihan_user}')

if pilihan_user == muadz_position:
      print(f'selamat {nama_user} kamu menang! muadz berada di {muadz_position} dan pilihanmu adalah {pilihan_user}')
      
else: 
      print(f'kamu kalah muadz bukan berada di situ, tapi muada berada di goa nomor {muadz_position} sedangkan kamu memilih goa {pilihan_user}')
