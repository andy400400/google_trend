# -*- coding: utf-8 -*-

import google_trend as gt
import datetime

def main():
    #股票清單
    search_list = ['2330','2886','0050','0056','0056','006208','00850']
	#類別
    search_type = 7
	#幾天前資料
    day = datetime.date.today() + datetime.timedelta(-1)
    google_trend = gt.google_trend(search_type, day)
    trend_data = google_trend.start(search_list)
    return trend_data
    
if __name__ == "__main__":
    trend_data = main() 


