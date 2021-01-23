from time import sleep

import requests
from threading import Thread
import random,string,hashlib,json

class Miner(Thread):


    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.stop_threads = False
        self.url = "http://localhost:8000/mining/"
        self.value = 0
        self.start()


    def run(self):
        while True:
            resp = requests.get("{}?status=False".format(self.url))
            if self.stop_threads:
                break
            if resp.json()['id'] != None:
                self.mining(resp.json()['id'],resp.json()['p_hash'],resp.json()['hash'])
            else:
                print("Yeni Düğüm yok")
                print("Miner Durduruluyor")
                self.stop_threads = True
                if resp.status_code != 200:
                    print("error")

    def register(self,id):
        task = { 'id': id}
        update_resp = requests.put(self.url, data=json.dumps(task))
        if  update_resp.status_code != 200:
            print("error")
            return True

    def mining(self,id,p_hash,hash_value):
        try:
            self.value += 1
            data_x = ''.join(random.choices(string.ascii_letters + string.digits, k=1))
            if p_hash == "0":
                hash_calc = hashlib.md5(data_x.encode())
                print("ilk düğüm  : {}----->{}".format(hash_calc.hexdigest(), hash_value))
            else:
                total_value = str(p_hash + data_x)
                hash_calc = hashlib.md5(total_value.encode())
                print("yeni düğüm ekleniyor : {}----->{}".format(hash_calc.hexdigest(),hash_value))
            if hash_calc.hexdigest() == hash_value:
                print("Bulunan hash: {}".format(hash_calc.hexdigest()))
                print("Buldun Tebrikler")
                print(" {} kez hash denendi".format(self.value))
                print("Düğüm onaylanıyor........")
                sleep(3)
                register = self.register(id)
                if register:
                    print("Yeni Düğüm Aranıyor")
                    Miner()


        except Exception as err:
            print(err)

Miner()
while True:
    pass
