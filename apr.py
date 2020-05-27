'''
Name: Bot Facebook
Aurhor: Pandas ID
Date: 19-05-2020
Note: Sengaja saya tidak Compile karna saya yakin di luar sana
masih ada orang yang mau belajar.Ingat!!!recode tidak akan membuat mu menjadi hebat
'''


#Import modul
from bs4 import BeautifulSoup as bs
from requests import Session
from headerz import headerz
import html
import time
import re
import os

class Main:
    
    banner = '''
    
        ----------------------------
            [•] Bot Facebook [•]
            
            [•] Versi : 1.0  [•]
        ----------------------------
    '''
    
    def __init__(self):
        self.banner = Main.banner
        self.head = 'https://mbasic.facebook.com'
        self.req = Session()
        
        self.login()
    
    def login(self):
        os.system('clear')
        print(self.banner)
        list_dir = []
        for i in os.listdir("."):
            if '.log' in i:
                list_dir.append(i)
        if len(list_dir) != 0:
            for l in list_dir:
                print('        ['+str(list_dir.index(l)+1)+']', l)
        else:
            print('        > Buat file cookies dulu')
            exit()
        print('')
        pilihan = int(input('        >>> '))
        file_cookies = open(list_dir[pilihan-1], 'r').read()
        header = headerz().parser(file_cookies)
        cookie = headerz().cookie_builder(header["cookie"])
        self.kuki = {'Cookie':cookie}
        get_me = self.req.get(self.head+'/me', cookies=self.kuki)
        soup_me = bs(get_me.text, 'html.parser')
        self.username = soup_me.find('title').text
        if self.username == 'Masuk ke Facebook':
            print('        > Invalid Cookies')
            os.system('rm -rf '+list_dir[pilihan-1])
            exit()
        self.menu()
        
    def menu(self):
        os.system('clear')
        print(self.banner)
        print('        User: '+self.username)
        print('        ----------------------------')
        print('        [01] Buat postingan')
        print('        [02] Bot spam chat')
        print('        [03] Info')
        print('        [00] Keluar')
        self.pilihMenu()
        
    def pilihMenu(self):
        print('')
        pilihan = input('        >>> ')
        if pilihan == '1':
            self.spamPost()
        elif pilihan == '2':
            self.spamChat()
        elif pilihan == '3':
            self.info()
        elif pilihan == '0' or pilihan == '00':
            print('        [!] exit')
            exit()
        else:
            print('        > Pilihan lu gak tersedia bro')
            time.sleep(1)
            self.menu()
    
    def info(self):
        print('                  [ Info ]')
        print('        ----------------------------')
        print('          > Author : -Pandas ID')
        print('          > Thaks to : -Allah Swt')
        print('                       -Karjok Pangesty')
        print('                       -Internet(Beserta antek" nya:v)')
        print('          > Blog : -https://pandasid.blogspot.com')
        print('          > Sosial : -Wa --> 082250223147')
        print('                     -FB --> Pandas ID')
        print('                     -Telegram --> https://t.me/PandasID')
        print('')
        input('        [ Kembali ]')
        self.menu()
        
    def spamPost(self):
        get_url = self.req.get(self.head, cookies=self.kuki)
    
        url_post = re.search(r'\<form\ method\=\"post\"\ action\=\"(.*?)\"\ class\=\"(.*?)\"\ id\=\"mbasic-composer-form\"\>', get_url.text).group(1)
        unescape_url = html.unescape(url_post)
        fb_dtsg = re.search(r'\<input\ type\=\"hidden\"\ name\=\"fb_dtsg\"\ value\=\"(.*?)\"\ autocomplete\=\"off\"\ \/\>', get_url.text).group(1)
        jazoest = re.search(r'\<input\ type\=\"hidden\"\ name\=\"jazoest\"\ value\=\"(.*?)\"\ autocomplete\=\"off\"\ \/\>', get_url.text).group(1)
        privacyx = re.search(r'\<input\ type\=\"hidden\"\ name\=\"privacyx\" value\=\"(.*?)\"\ \/\>', get_url.text).group(1)
        target = re.search(r'\<input\ type\=\"hidden\"\ name\=\"target\"\ value\=\"(.*?)\"\ \/\>', get_url.text).group(1)
        c_src = re.search(r'\<input\ type\=\"hidden\"\ name\=\"c_src\"\ value\=\"(.*?)\"\ \/\>', get_url.text).group(1)
        cwevent = re.search(r'\<input\ type\=\"hidden\"\ name\=\"cwevent\"\ value\=\"(.*?)\"\ \/\>', get_url.text).group(1)
        referrer = re.search(r'\<input\ type\=\"hidden\"\ name\=\"referrer\"\ value\=\"(.*?)\"\ \/\>', get_url.text).group(1)
        ctype = re.search(r'\<input\ type\=\"hidden\"\ name\=\"ctype\"\ value\=\"(.*?)\"\ \/\>', get_url.text).group(1)
        cver = re.search(r'\<input\ type\=\"hidden\"\ name\=\"cver\"\ value\=\"(.*?)\"\ \/\>', get_url.text).group(1)
    
        input_text = input('          >>> Masukan text: ')
        data = {
            'fb_dtsg':fb_dtsg,
            'jazoest':jazoest,
            'privacyx':privacyx,
            'target':target,
            'c_src':c_src,
            'cwevent':cwevent,
            'referrer':referrer,
            'ctype':ctype,
            'cver':cver,
            'rst_icv':'',
            'xc_message':input_text,
            'view_post':'Posting'
        }
        send = self.req.post(self.head+unescape_url, data=data, cookies=self.kuki)
        print('          >>> Sukses terkirim')
            
    def spamChat(self):
        input_id = input('          >>> Masukan ID Teman: ')
        input_text = input('          >>> Pesan: ')
        jml_spam = int(input('          >>> Jumlah: '))
        print('')
        get_url = self.req.get(self.head+'/messages/compose/?ids='+input_id, cookies=self.kuki)
        url_post = re.search(r'\<form\ method\=\"post\"\ action\=\"(.*?)\"\ class\=\"(.*?)\"\ id\=\"composer_form\"\>', get_url.text).group(1)
        unescape_url = html.unescape(url_post)
        fb_dtsg = re.search(r'\<input\ type\=\"hidden\"\ name\=\"fb_dtsg\"\ value\=\"(.*?)\"\ autocomplete\=\"off\"\ \/\>', get_url.text).group(1)
        jazoest = re.search(r'\<input\ type\=\"hidden\"\ name\=\"jazoest\"\ value\=\"(.*?)\"\ autocomplete\=\"off\"\ \/\>', get_url.text).group(1)
        ids = re.search(r'\<input\ type\=\"hidden\"\ name\=\"ids\[(.*?)\]\"\ value\=\"(.*?)\"\ \/\>', get_url.text)
        text_ids = re.search(r'\<input\ type\=\"hidden\"\ name\=\"text_ids\[(.*?)\]\"\ value\=\"(.*?)\"\ \/\>', get_url.text)
        data = {
            'fb_dtsg':fb_dtsg,
            'jazoest':jazoest,
            'ids['+ids.group(1)+']':ids.group(2),
            'text_ids['+text_ids.group(1)+']':text_ids.group(2),
            'body':input_text,
            'Send':'Kirim'
            }
        for x in range(jml_spam):
            send = self.req.post(self.head+unescape_url, data=data, cookies=self.kuki)
            print(f'\r          >>> Terkirim: {str(x+1)}',end="",flush=True)

try:
    Main()
except KeyboardInterrupt:
    print('        [!] Exit')
    exit()
