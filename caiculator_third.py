import sys
import os
#处理参数
class Args():
    def __init__(self,str):
        self.args = sys.argv[1:]
        self.str = str
#返回指定参数后的路径
    def deal_args(self):
        file = ''
        try:
            index_c = self.args.index(self.str)
            file = self.args[index_c+1]
        except Exception as e:
            print(e)
            exit()
        return file
#处理数据
# JiShuL = 2193.00
class Config_data():
    def __init__(self,path):
        self.path = path
#处理数据并保存成为一个字典
    def save_data(self):
        config_dict = {}
        try:
            with open(self.path,'r') as f:
                for line in f.readlines():
                    line = line.strip('\n')
                    key,value = line.split('=')
                    key = key.strip(' ')
                    value = value.strip(' ')
                    config_dict[key] = value
                return config_dict
        except Exception as e:
            print(e)
            exit()
#继承Config_data()方法
# 101,3500
class User_data(Config_data):
    def save_data(self):
        data_dict = {}
        try:
            with open(self.path,'r') as f:
                for line in f.readlines():
                    line = line.strip('\n')
                    key,value = line.split(',')
                    data_dict[key] = value
                return data_dict
        except Exception as e:
            print(e)
            exit()
#计算
class Compute():
    def __init__(self,config_dict,money):
        self.config_dict = config_dict
        self.money = money

    def _read_config(self,key):
        return self.config_dict[key]

    def compute_money(self):
        insurance_money = 0
        tax = 0

        try:
            money_l = float(self._read_config('JiShuL'))
            money_h = float(self._read_config('JiShuH'))
            YangLao = float(self._read_config('YangLao'))
            YiLiao = float(self._read_config('YiLiao'))
            ShiYe = float(self._read_config('ShiYe'))
            GongShang = float(self._read_config('GongShang'))
            ShengYu = float(self._read_config('ShengYu'))
            GongJiJin = float(self._read_config('GongJiJin'))
        except Exception as e :
            print(e)
            sys.exit()

        if self.money <= money_l :
            insurance_money = money_l*YangLao+money_l*YiLiao+money_l*ShiYe+money_l*GongShang+money_l*ShengYu+money_l*GongJiJin
        elif self.money > money_l and self.money <= money_h:
            insurance_money = self.money*YangLao+self.money*YiLiao+self.money*ShiYe+self.money*GongShang+self.money*ShengYu+self.money*GongJiJin
        elif self.money > money_h:
            insurance_money = money_h * YangLao + money_h * YiLiao + money_h * ShiYe + money_h * GongShang + money_h * ShengYu + money_h * GongJiJin

        money_before = self.money - insurance_money-3500

        if money_before <= 1500 and money_before >= 0:
            tax = money_before * 0.03
        elif money_before > 1500 and money_before <= 4500:
            tax = money_before * 0.1 - 105
        elif money_before > 4500 and money_before <= 9000:
            tax = money_before * 0.2 - 555
        elif money_before > 9000 and money_before <= 35000:
            tax = money_before * 0.25 - 1005
        elif money_before > 35000 and money_before <= 55000:
            tax = money_before * 0.3 - 2755
        elif money_before > 55000 and money_before <= 80000:
            tax = money_before * 0.35 - 5505
        elif money_before > 80000:
            tax = money_before * 0.45 - 13505
        if tax <= 0:
            tax = 0
        money = self.money - insurance_money - tax
        return format(insurance_money,'.2f'),format(tax,'.2f'),format(money,'.2f')
#main函数
def main():
    config_path = Args('-c').deal_args()
    user_path = Args('-d').deal_args()
    final_path = Args('-o').deal_args()
    config_data = Config_data(config_path).save_data()
    user_data = User_data(user_path).save_data()
    if os.path.exists(final_path):
        os.remove(final_path)

    #print(user_data)

    for key in user_data:
        insurance_money,tax,money = Compute(config_data,float(user_data[key])).compute_money()
        with open(final_path,'a') as f:
            f.write(key+','+user_data[key]+','+insurance_money+','+tax+','+money+'\n')


if __name__ == '__main__':
    main()

