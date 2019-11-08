# -*- coding: utf-8 -*-

import time
import pandas as pd
from pytrends.request import TrendReq
import random

class google_trend():

    global day
    global search_type

    def __init__(self, search_type, day):  
        self.search_type = search_type
        self.day = day
        
    def start(self, search_list):
        try:    
            #1. 資料準備
            word_list = []
            search_list = list(set(search_list))
            trend_data = pd.DataFrame(columns = ['word','count','day'])
            
            #2. 取得google_trend資料  
            for index in range(len(search_list)):
                word_list.append(search_list[index])
    
                #五筆發一次
                if(len(word_list) >= 5):
                    #發request
                    request_data = self.trend_request(word_list)
                    trend_data_1 = self.data_sammary(request_data)
                    
                    #清除list
                    word_list = []
                    self.random_sleep();
                    #break
        
            #最後不足5筆資料
            request_data = self.trend_request(word_list)
            trend_data_2 = self.data_sammary(request_data)
            
            trend_data = trend_data.append(trend_data_1)
            trend_data = trend_data.append(trend_data_2)
            
            return trend_data
        except Exception as e:
            print(e)
        
    #發送request
    def trend_request(self, word_list):    
        try :
            pytrend = TrendReq(hl='en-CN', tz=360)
            pytrend.build_payload(kw_list = word_list, cat = self.search_type, timeframe='now 7-d', geo='TW', gprop='')
            trend_data = pytrend.interest_over_time()
            #若無資料回傳空list
            if(len(trend_data) == 0):
                return trend_data
            else:
                return trend_data.loc[trend_data.index.date == self.day]
        except Exception as e:
            print(e)
    
    #更新data中的count欄位
    def data_sammary(self, trend_data):
        data_df = pd.DataFrame(columns = ['word','count','day'])
        for col_name in trend_data.columns:
            if(col_name == 'isPartial'):
                continue
            try :
                count = trend_data[col_name].sum()
                cores = pd.Series({'word':col_name, 'count':count, 'day':self.day})
                data_df = data_df.append(cores, ignore_index=True)
            except Exception as e:
                 print(e)
                 
        return data_df
                 
    def random_sleep(self):
        r_number = random.uniform(0,0.8)
        time.sleep(r_number)

