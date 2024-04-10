import logging ,time ,random 
from datetime import timedelta 

class SESSION():
    
    def __init__(self):
        self.session_list = {}
        self.enable_page_key = False #セッションkeyを有効にする
        self.id_len = 128 #セッションIDの長さHEX
        self.key_len = 32 #セッションkeyの長さHEX
        self.server_session_lifetime = timedelta(days=1).total_seconds() #サーバー側セッションのライフタイム
        self.server_session_expirytime = timedelta(days=30).total_seconds() #サーバー側セッションの失効時間
        logging.basicConfig(
            level=logging.DEBUG,  # 最低レベルをDEBUGに設定
            format='[%(asctime)s] %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
            )
        
    def now_time(self):
        return int(time.time())
    
    def tick_task(self):
        logging.info(f"session_tick...")
        logging.debug(self.session_list)


    def create_session_id(self):#IDの生成
        id = hex(random.randint(0, 16**self.id_len - 1))
        if id in self.session_list.keys():
            return self.create_session_id()
        else:
            return id
        
    def create_session_key(self ,old_key = ''):#pageKEYの生成
        key = hex(random.randint(0, 16**self.key_len - 1))#16桁のhexを生成
        if key == old_key:
            return self.create_session_key(old_key)
        else:
            return key    

    def create_session(self):
        id = self.create_session_id()
        if self.enable_page_key:
            key = self.create_session_key()
        else:
            key = 0
        self.session_list[id] = {'page-key':key,'last-accessed-time':self.now_time()}
        return id , key ,True
    
    def update_session(self ,id ,key):
        new_id = self.create_session_id()
        if self.enable_page_key:
            new_key = self.create_session_key(key)
            self.session_list[id]['page-key'] = new_key
        else:
            None 
        self.session_list[new_id] = self.session_list[id]

        return new_id ,new_key ,False

    def ref_session(self ,id , key):


        if id == None:
            return self.create_session()
        else :
            if id in self.session_list.keys():
                if not self.enable_page_key:
                    self.session_list[id]['page-key'] = 0
                    self.session_list[id]['last-accessed-time'] = self.now_time()
                    return id , 0 ,False
                elif key == self.session_list[id]['page-key']:
                    new_key = self.create_session_key(key)
                    self.session_list[id]['page-key'] = new_key
                    self.session_list[id]['last-accessed-time'] = self.now_time()
                    return id , new_key ,False
                else:
                    return self.create_session()
            else :
                return self.create_session()
