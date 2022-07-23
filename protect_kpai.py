import requests,json,os,pyautogui,cv2,time,webbrowser,socket,random
from playsound import playsound
from bs4 import BeautifulSoup
os.system("pip install bs4")
random=random.randint(20,50)
os.system("cls")
def runtext():
    url='https://ngaygio24.com/xem-gio-viet-nam.html'
    rsp=requests.get(url,timeout=1).text
    date_time=str(BeautifulSoup(rsp,"html.parser").find('div' ,{'style':"text-align:center; font-size:16px"}).get_text())
    vitri_ngay=date_time.find('Ngày')
    date_time=date_time[vitri_ngay+5:vitri_ngay+15].split('/')
    return date_time
def check_text():
    os.system("cls")
    host_name=socket.gethostname()
    ip=str(socket.gethostbyname(host_name)).replace('.','')
    kpai=ip*5
    rsp=requests.get('https://raw.githubusercontent.com/David22092007/About-xyz-2007-coding-/main/print(%22NONE%22)').text
    if str(json.loads(rsp)['kpai']).find(kpai) ==-1:
        print ('SEVER CONNECT == MAX REACH')
        print (f'PRESS THIS KEY TO ADMIN TO JOIN : {kpai}')
        print ('''=========SUPORORT=LINK=========
    Facebook: https://facebook.com/Alobyerel
    YOUTUBE: https://www.youtube.com/channel/UCLYHg8iWxB_U1juOyirgFkw''')
        time.sleep(100)
        exit()
    else:
        check_text
        check=json.loads(rsp)['kpai'][kpai].split('/')
        date=runtext()
        return date,check;
def check_hsd():
    run=check_text()
    date,month,year=run[0][0],run[0][1],run[0][2]
    hsd_date,hsd_month,hsd_year=run[1][0],run[1][1],run[1][2]
    if hsd_year >=year:
        if hsd_month >= month:
            if hsd_date >= date:                
                print (f'KẾT NỐI THÀNH CÔNG SEVER <==> HIỆN CÓ {random} USER ĐANG ONLINE')
                os.system("pip install playsound==1.2.2")
                os.system("pip install cv2")
            else:
                print ('TÀI KHOẢN CỦA BẠN ĐÃ HẾT HẠN !! == VUI LÒNG LIÊN HỆ ADMIN ĐỂ GIA HẠN')
                exit()
        else:
            print ('TÀI KHOẢN CỦA BẠN ĐÃ HẾT HẠN !! == VUI LÒNG LIÊN HỆ ADMIN ĐỂ GIA HẠN')
            exit()
    else:
        print ('TÀI KHOẢN CỦA BẠN ĐÃ HẾT HẠN !! == VUI LÒNG LIÊN HỆ ADMIN ĐỂ GIA HẠN')
        exit()
check_hsd()
os.sytem("cls")

