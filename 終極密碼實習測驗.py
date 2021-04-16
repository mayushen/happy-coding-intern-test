#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 22:06:12 2021

@author: motishittt
"""
#讓使用者規定範圍並產生密碼
from random import randint
print('歡迎來到終極密碼的最終試煉，你準備好回答密碼了嗎？\n請自訂密碼的範圍，須為整數數字')
lowest=int(input('輸入密碼的最小值:'))
highest=int(input('輸入密碼的最大值:'))
ans= randint(lowest, highest)
guess=0
times=1#紀錄使用者回答的次數

#讓使用者重複猜數字，直到正確為止
while True:
    guess = input('密碼介於 ' + str(lowest) + '～' + str(highest) + ':\n請回答>>')
    
    #檢查使用者輸入的是否為數字
    try:
        guess=int(guess)#將使用者所填內容轉換成整數
    except ValueError:
        times+=1
        print('輸入格式錯誤！答案請輸入數字\n>>')#若內容不是數字，便要求重新輸入
        continue
       
    #檢查輸入的數字是否在範圍內
    if guess<lowest or guess>highest:
        times+=1
        print('錯誤！請輸入'+str(lowest)+'~'+str(highest)+'之間的整數\n' )
        continue
        
    #一：判斷有沒有猜中答案
    #二：答錯的話，給予限定範圍的提示，並記錄回答次數
    if guess != ans:
        times+=1
        if guess < ans:
         print('答錯了！再大一點！')
         lowest=guess
        else:
         print('答錯了！再小一點！')
         highest=guess
     
        #判斷回答正確時，停止迴圈運行，並顯示回答次數
    else:
         print('答對了！！算你厲害！\n'+'密碼就是',(ans),'，你一共猜了',times,'次')
         break
                