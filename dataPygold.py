class Data():
    def __init__(self, values):
        self.namesmetall = values[0:4]
        self.pricemetall = values[4:8]
        self.usd = values[0:20]                #
        self.eur = values[20:40]
        

    def get_all_list(self):
        message = ""
        i = 0
        while i < len(self.namesmetall): 
            message += f'{self.namesmetall[i]}:\n {self.pricemetall[i]} \n\n '
            i += 1

        message = message.rstrip()
        return message 

    def get_gold_value(self):
        message = ""
        i = 0
        message += f'{self.namesmetall[i]}:\n {self.pricemetall[i]} \n\n '  
        message = message.rstrip()
        return message

    def get_ser_value(self):
        message = ""
        i = 1
        message += f'{self.namesmetall[i]}:\n {self.pricemetall[i]} \n\n '  
        message = message.rstrip()
        return message

    def get_plat_value(self):
        message = ""
        i = 2
        message += f'{self.namesmetall[i]}:\n {self.pricemetall[i]} \n\n '  
        message = message.rstrip()
        return message

    def get_pallad_value(self):
        message = ""
        i = 3
        message += f'{self.namesmetall[i]}:\n {self.pricemetall[i]} \n\n '  
        message = message.rstrip()
        return message

    def get_usd_value(self):  #
        message = ""
        message += self.usd
        return message

    def get_eur_value(self):  #
        message = ""
        message += self.eur
        return message



class DataCrip():
    def __init__(self, values):
        self.namecrip = values[0:8:2]
        self.pricecrip = values[1:8:2]
        #self.namecrip = values[0:100:2]             # Для вывода всех криптовалют (100 штук)
        #self.pricecrip = values[1:100:2]
        

    def get_all_list_crip(self):
        message = ""
        i = 0
        while i < len(self.namecrip):
            message += f'{self.namecrip[i]}: \n {self.pricecrip[i]} \n\n'
            i += 1

        message = message.rstrip()
        return message

    def get_bit_value(self):    
        message = ""
        i = 0
        message += f'{self.namecrip[i]}:\n {self.pricecrip[i]} \n\n '  
        message = message.rstrip()
        return message

    def get_eth_value(self):    
        message = ""
        i = 1
        message += f'{self.namecrip[i]}:\n {self.pricecrip[i]} \n\n '  
        message = message.rstrip()
        return message

    def get_dog_value(self):    
        message = ""
        i = 2
        message += f'{self.namecrip[i]}:\n {self.pricecrip[i]} \n\n '  
        message = message.rstrip()
        return message

    def get_monero_value(self):    
        message = ""
        i = 3
        message += f'{self.namecrip[i]}:\n {self.pricecrip[i]} \n\n '  
        message = message.rstrip()
        return message



class DataSP():
    def __init__(self, values):
        self.sp500 = values[0:1]
        

    def get_all_list_sp(self):
        message = ""
        i = 0
        while i < len(self.sp500):
            message += f'S&P 500 (SPX):  {self.sp500[i]}'
            i += 1

        message = message.rstrip()
        return message