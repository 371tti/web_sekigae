import random , time, re
from datetime import timedelta 
from datetime import datetime
import asyncio
import threading
import logging
#ページキー毎時確認やめる、
class Osession():

        


        #self.now_time = 0　#同期させるなら。


    def async_task(self):
        # 何か非同期で行いたい処理
        logging.info(f"session_tick...")
        logging.info(self.session_list)




    def now_time(self):
        return int(time.time())
    

    def create_session_key(self ,old_key = ''):#pageKEYの生成
        key = hex(random.randint(0, 16**self.key_len - 1))#16桁のhexを生成
        if key == old_key:
            return self.create_session_key(old_key)
        else:
            return key

    def create_session_id(self):#IDの生成
        id = hex(random.randint(0, 16**self.id_len - 1))#16桁のhexを生成
        if id in self.session_list.keys():
            return self.create_session_id()
        else:
            return id
        
    def create_session(self):
        id = self.create_session_id()
        key = self.create_session_key()
        self.session_list[id] = {'page-key':key,'lst-access-t':self.now_time}
        return id , key
    


    def ref_session(self ,id , key):


        if id == None:
            return self.create_session()
        else :
            if id in self.session_list.keys():
                if not self.enable_page_key:
                    self.session_list[id]['page-key'] = 0
                    return id , 0
                if key == self.session_list[id]['page-key']:
                    new_key = self.create_session_key(key)
                    self.session_list[id]['page-key'] = new_key
                    return id , new_key
                return self.create_session()
            else :
                return self.create_session()






    

        




