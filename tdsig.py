from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import random
import requests
import threading
import time
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 466)
        Form.setFixedHeight(466)
        Form.setFixedWidth(850)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 831, 351))
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(30, 10, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 30, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 70, 81, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 10, 61, 16))
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(190, 10, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 50, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.spinBox_2 = QtWidgets.QSpinBox(Form)
        self.spinBox_2.setGeometry(QtCore.QRect(190, 50, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 50, 61, 16))
        self.label_2.setObjectName("label_2")
        self.spinBox_3 = QtWidgets.QSpinBox(Form)
        self.spinBox_3.setGeometry(QtCore.QRect(190, 70, 42, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 70, 61, 16))
        self.label_3.setObjectName("label_3")
        self.spinBox_4 = QtWidgets.QSpinBox(Form)
        self.spinBox_4.setGeometry(QtCore.QRect(190, 30, 42, 22))
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(130, 30, 61, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 10, 75, 61))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 80, 75, 21))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(370, 10, 301, 91))
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 231, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 151, 16))
        self.label_7.setObjectName("label_7")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tool TĐS IG Đa Luồng "))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "User TĐS"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "User IG"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Proxy"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Đợi Duyệt"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Tổng Xu"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Trạng Thái"))
        self.checkBox.setText(_translate("Form", "Job Folow"))
        self.checkBox_2.setText(_translate("Form", "Job Like"))
        self.checkBox_3.setText(_translate("Form", "Job like CMT"))
        self.label.setText(_translate("Form", "Time Sleep"))
        self.checkBox_4.setText(_translate("Form", "Job CMT"))
        self.label_2.setText(_translate("Form", "Time Sleep"))
        self.label_3.setText(_translate("Form", "Time Sleep"))
        self.label_4.setText(_translate("Form", "Time Sleep"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.pushButton_2.setText(_translate("Form", "Quit"))
        self.groupBox.setTitle(_translate("Form", "Info"))
        self.label_5.setText(_translate("Form", ""))
        self.label_6.setText(_translate("Form", "Zalo: "))
        self.label_7.setText(_translate("Form", "Telegram: "))
        self.pushButton.clicked.connect(self.Run_Reg)
        self.pushButton_2.clicked.connect(self.stop_thread)
    def hienthi(self, type,row, column,text):
        if type==True:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            row=self.tableWidget.rowCount()-1
        self.tableWidget.setItem(row,column, QtWidgets.QTableWidgetItem(F'{text}'))
    def Run_Reg(self):
        self.test=main(self)
        self.test.show.connect(self.hienthi)
        self.test.start()
        self.pushButton.setEnabled(False)
    def stop_thread(self):
        exit()
        #self.terminate()
        #self.test.stop()
        #self.pushButton.setEnabled(True)
        #self.pushButton_2.setEnabled(False)
class Instagram(object):
    def __init__(self,user_agent,proxies) -> None:
        self.user_agent=user_agent
        self.proxies={'http'  : F'http://{proxies}', 'https' : F'http://{proxies}'}
    def Login(self,username,password):
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'csrftoken=em88UWFiAWWyIS4pjOvwmQr8PuM6qyKk; mid=Y9PkVQALAAHMFuKTu2rbOu4dpCiD; ig_nrcb=1; ig_did=C4F3EA09-0728-4704-ABA7-22EC7798A0B3; datr=VeTTY2Acxfn7FIiV6-uHIXOy',
            'origin': 'https://www.instagram.com',
            'pragma': 'no-cache',
            'referer': 'https://www.instagram.com/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': self.user_agent,
            'viewport-width': '463',
            'x-asbd-id': '198387',
            'x-csrftoken': 'em88UWFiAWWyIS4pjOvwmQr8PuM6qyKk',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1006873778',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}',
            'username': username,
            'queryParams': '{}',
            'optIntoOneTap': 'false',
            'trustedDeviceRecords': '{}',
        }
        
        response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers=headers, data=data,proxies=self.proxies)   
        print(response.text)
        if response.json()['status'] != "ok":
            return False
        cookies = response.cookies.get_dict()
        cookie_list = []
        for items in cookies:
            cookie_list.append(F'{items}={cookies[items]}')
        self.cookies=';'.join(cookie_list)
        print(self.cookies)
        self.headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'no-cache',
            'cookie': self.cookies,
            'origin': 'https://www.instagram.com',
            'pragma': 'no-cache',
            'referer': 'https://www.instagram.com/p/CncRqzcpZRP/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': self.user_agent,
            'viewport-width': '406',
            'x-asbd-id': '198387',
            'x-csrftoken': str(self.cookies.split("csrftoken=")[1].split(";")[0]),
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR2Nc8ncW4a-SseKs1h3LLgACXFvdcRKTAAE6YA1rx97kgJK',
            'x-instagram-ajax': '1006873778',
            'x-requested-with': 'XMLHttpRequest',
        }
    
    def Folow(self,uid):
        folow = requests.post(
            f'https://www.instagram.com/api/v1/web/friendships/{uid}/follow/',
            headers=self.headers,
            proxies=self.proxies,
            timeout=10
        )
        print(folow.text)
        try:
            if folow.json()["status"] == "ok":
                return True
            return False
        except:
            return False
    def Like(self,uid):
        like = requests.post(f'https://www.instagram.com/api/v1/web/likes/{uid}/like/', 
            headers=self.headers,
            proxies=self.proxies,
            timeout=10
        ).json()
        print(like)
        try:
            if like["status"] == "ok":
                return True
            return False
        except:
            return False
    def CMT(self,content,uid):
        cmt = requests.post(f'https://www.instagram.com/api/v1/web/comments/{uid}/add/', 
            headers=self.headers, 
            data={'comment_text': content}, 
            proxies=self.proxies,
            timeout=10
        )
        print(cmt.json())
        try:
            if cmt.json()["status"] == "ok":
                return True
            return False
        except:
            return False
    def Like_CMT(self,uid):
        likecmt = requests.post(f'https://www.instagram.com/api/v1/web/comments/like/{uid}/', 
            headers=self.headers,
            proxies=self.proxies,
            timeout=10
        )
        print(likecmt.json())
        try:
            if likecmt.json()["status"] == "ok":
                return True
            return False
        except:
            return False
class TraoDoiSub(object):
    def __init__(self,usertds,passtds) -> None:
        self.usertds=usertds
        self.passtds=passtds
    def Login(self):
        headers = {
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://traodoisub.com/',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'username': self.usertds,
            'password': self.passtds,
        }
        try:
            response = requests.post('https://traodoisub.com/scr/login.php', headers=headers, data=data)
            print(response.text)
            if response.json()["success"] == True:
                return "PHPSESSID=" + response.cookies["PHPSESSID"]
        except:
            return False
    def Get_Info(self,cookies):
        self.headers = {
            'authority': 'traodoisub.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': cookies,
            'referer': 'https://traodoisub.com/view/setting/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        return requests.get('https://traodoisub.com/view/setting/load.php',headers=self.headers).json()
    def Check_Doi_Duyet_(self):
        data = {
            'page': '1',
            'query': '',
        }
        response = requests.post('https://traodoisub.com/ex/instagram_history/fetch.php',headers=self.headers, data=data)
        return response.json()["pending"]
#testig|Anh@998|luuhaiduong4351|Fivex@Software#40597|user44948:6702@in2644.huyentlc.com:44948
#testig|Anh@998|nguyenhuytuong661|$57_27h70w80|user44954:3A86@in2644.huyentlc.com:44954
#Blackspy2406|Anh@998|chuviethuong61|!95_51t84d89|user44953:9238@in2644.huyentlc.com:44953
#blackspy241226|Anh998|nguyenkhanhvy7441|a36h21j94g65|user44948:6702@in2644.huyentlc.com:44948
class main(QtCore.QThread):
    show=QtCore.pyqtSignal(bool, int,int, str)
    def __init__(self, all) -> None:
        super().__init__()
        self.all=all
    def run(self):
        list_job = []
        delay_folow_ = self.all.spinBox.text()
        delay_like_ = self.all.spinBox_4.text()
        delay_cmt_ = self.all.spinBox_2.text()
        delay_likecmt_ = self.all.spinBox_3.text()
        print(delay_folow_, delay_like_, delay_cmt_, delay_likecmt_)
        if self.all.checkBox.isChecked() == True:
            list_job.append("instagram_follow")
        if self.all.checkBox_2.isChecked() == True:
            list_job.append("instagram_like")
        if self.all.checkBox_3.isChecked() == True:
            list_job.append("instagram_comment")
        if self.all.checkBox_4.isChecked() == True:
            list_job.append("instagram_likecmt")
        if list_job == []:
            self.show.emit(True,0,5,"Chưa chọn nhiệm vụ")
            sleep(5)
            exit()
        data_file = open("C:/Users/Admin/Desktop/tdsiggui/ngu.txt").read().split("\n")


        print(data_file)
        def convert_string(input_string):
            split_string = input_string.split(":")
            new_string = f"{split_string[2]}:{split_string[3]}@{split_string[0]}:{split_string[1]}"
            return new_string
        for row in range(len(data_file)):
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
            data = data_file[row]
            usertds = data.split("|")[0]
            passtds = data.split("|")[1]
            username = data.split("|")[2]
            password = data.split("|")[3]
            proxies = convert_string(data.split("|")[4])
            print(row, usertds,passtds,username,password,proxies)
            threading.Thread(target=self.Main,args=((row, usertds,passtds,username,password,proxies,user_agent,list_job,delay_folow_,delay_like_,delay_cmt_,delay_likecmt_))).start()
    def Main(self, row,
            usertds,passtds,
            username,password,
            proxies,user_agent,
            list_job,
            delay_folow_,delay_like_,delay_cmt_,delay_likecmt_):
        def check_live_post_(uid,user_agent):
            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'cookie': 'mid=Y9X5-wALAAEjzZ3CwzvVOfVc9cX6; ig_nrcb=1; ig_did=97335641-043B-4DA0-919C-F510383687CA; datr=-_nVY2uh7_NrPQVKGtqwn68B; csrftoken=vOjbGAviEgvmK1jonVz0pm27RxPnTal9; ds_user_id=57856993827; sessionid=57856993827:q5jbXur8E2EqY7:1:AYeOf4a9jVe1FNfa4JawiC0dWDTRFyYKZlfYap9PWg; shbid="13791\05457856993827\0541706503556:01f7da845a2fcb3e1493261d5468dca930cd3f37e5df57bbacc644b76002630ae502fad2"; shbts="1674967556\05457856993827\0541706503556:01f7d5c547341a6d06f8947c2516ab851be7dc62a6342339abe6406bfc534bd722a27327"; rur="CCO\05457856993827\0541706507354:01f7a43c090cbf3921416b26d231ba7dda5256d7661ea8a395848aed31a6a7138244e32d"',
                'referer': 'https://www.instagram.com/p/Cn_I_nhPhiz/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent,
                'viewport-width': '283',
                'x-asbd-id': '198387',
                'x-csrftoken': "vOjbGAviEgvmK1jonVz0pm27RxPnTal9",
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR2Nc8ncW4a-SseKs1h3LLgACXFvdcRKTAAE6YA1rx97kj2J',
                'x-requested-with': 'XMLHttpRequest',
            }

            response = requests.get(f'https://www.instagram.com/api/v1/media/{uid}/info/', headers=headers).text
            if uid in response:
                return True
            return  False

        self.show.emit(True,row, 4,'')
        self.show.emit(False,row,5,"Đang Lấy Thông Tin")
        self.show.emit(False,row,0,usertds)
        self.show.emit(False,row,1,username)
        self.show.emit(False,row,2,proxies)
        tds = TraoDoiSub(usertds,passtds)
        cookiestds = tds.Login()
        if cookiestds == False:
            self.show.emit(False,row,5,"Sai tài khoản TĐS")
            quit()
        Infotds = tds.Get_Info(cookies=cookiestds)
        tokentds = Infotds["tokentds"]
        xu = Infotds["xu"]
        self.show.emit(False,row,4,xu)
        self.show.emit(False,row,3,tds.Check_Doi_Duyet_())
        IG = Instagram(user_agent=user_agent,proxies=proxies)
        Login = IG.Login(username=username,password=password)
        if Login == False:
            self.show.emit(False,row,5,"Sai tài khoản Instagram")
            quit()
        self.show.emit(False,row,5,f"Cấu hình user: {username}")
        if requests.get(f"https://traodoisub.com/api/?fields=instagram_run&id={username}&access_token={tokentds}").json()["success"] != 200:
            self.show.emit(False,row,5,f"Cấu hình user: {username} failed")
            quit()
        self.show.emit(False,row,5,f"Cấu hình user: {username} success")
        sleep(2)
        while True:
            type = random.choice(list_job)
            self.show.emit(False,row,5,"Đang tìm job")
            if type == "instagram_follow":
                try:
                    print(type)
                    get_job = requests.get(f"https://traodoisub.com/api/?fields={type}&access_token={tokentds}").json()["data"]
                    
                    idduyet = get_job[0]["id"]
                    id_post = get_job[0]["id"].split("_")[0]
                    print(get_job,id_post)
                    self.show.emit(False,row,5,"Đang folow id: {}".format(id_post))
                    if IG.Folow(uid = id_post) == False:
                        self.show.emit(False,row,5,"Tài khoản bị block tính năng")
                        sleep(2)
                        break
                    self.show.emit(False,row,5,"Gửi duyệt nhiệm vụ")
                    gui_duyet = requests.get(f"https://traodoisub.com/api/coin/?type=INS_FOLLOW_CACHE&id={idduyet}&access_token={tokentds}")
                    pending = gui_duyet.json()["data"]["pending"]
                    print(gui_duyet)
                    sleep(2)
                    self.show.emit(False,row,3,str(pending))
                    for i in range(int(delay_folow_),-1,-1):
                        self.show.emit(False,row,5,f'Đợi sau {i}'.format(i=i))
                        sleep(1)
                except:
                    pass
                
            if type == "instagram_like":
                try:
                    print(type)
                    get_job = requests.get(f"https://traodoisub.com/api/?fields={type}&access_token={tokentds}").json()["data"]
                    idduyet = get_job[0]["id"]
                    id_post = get_job[0]["id"].split("_")[0]
                    if check_live_post_(uid=id_post,user_agent=user_agent) == True:
                        print(id_post)
                        self.show.emit(False,row,5,"Đang like id: {}".format(id_post))

                        if IG.Like(uid = id_post) == False:
                            self.show.emit(False,row,5,"Tài khoản bị block tính năng")
                            sleep(2)
                            break
                        self.show.emit(False,row,5,"Gửi duyệt nhiệm vụ")
                        gui_duyet = requests.get(f"https://traodoisub.com/api/coin/?type=INS_LIKE_CACHE&id={idduyet}&access_token={tokentds}")
                        pending = gui_duyet.json()["data"]["pending"]
                        print(gui_duyet)
                        sleep(2)
                        self.show.emit(False,row,3,str(pending))
                        for i in range(int(delay_like_),-1,-1):
                            self.show.emit(False,row,5,f'Đợi sau {i}'.format(i=i))
                            sleep(1)
                except:
                    pass
            if type == "instagram_comment":
                try:
                    print(type)
                    get_job = requests.get(f"https://traodoisub.com/api/?fields={type}&access_token={tokentds}").json()["data"]
                    idduyet = get_job[0]["id"]
                    id_post = get_job[0]["id"].split("_")[0]
                    noidung = get_job[0]["noidung"]
                    if check_live_post_(uid=id_post,user_agent=user_agent) == True:
                        print(get_job,id_post)
                        self.show.emit(False,row,5,"Đang CMT id: {}".format(id_post))
                        if IG.CMT(uid = id_post,content = noidung) == False:
                            self.show.emit(False,row,5,"Tài khoản bị block tính năng")
                            sleep(2)
                            break
                        self.show.emit(False,row,5,"Gửi duyệt nhiệm vụ")
                        gui_duyet = requests.get(f"https://traodoisub.com/api/coin/?type=INS_COMMENT_CACHE&id={idduyet}&access_token={tokentds}")
                        pending = gui_duyet.json()["data"]["pending"]
                        print(gui_duyet)
                        sleep(2)
                        self.show.emit(False,row,3,str(pending))
                        for i in range(int(delay_cmt_),-1,-1):
                            self.show.emit(False,row,5,f'Đợi sau {i}'.format(i=i))
                            sleep(1)     
                except:
                    pass
            if type == "instagram_likecmt":
                try:
                    print(type)
                    get_job = requests.get(f"https://traodoisub.com/api/?fields={type}&access_token={tokentds}").json()["data"]
                    idduyet = get_job[0]["id"]
                    id_post = get_job[0]["id"].split("_")[0]
                    if check_live_post_(uid=id_post,user_agent=user_agent) == True:
                        print(get_job,id_post)
                        self.show.emit(False,row,5,"Đang like cmt id: {}".format(id_post))
                        if IG.Like_CMT(uid = id_post) == False:
                            self.show.emit(False,row,5,"Tài khoản bị block tính năng")
                            sleep(2)
                            break
                        self.show.emit(False,row,5,"Gửi duyệt nhiệm vụ")
                        gui_duyet = requests.get(f"https://traodoisub.com/api/coin/?type=INS_LIKECMT_CACHE&id={idduyet}&access_token={tokentds}")
                        pending = gui_duyet.json()["data"]["pending"]
                        print(gui_duyet)
                        sleep(2)
                        self.show.emit(False,row,3,str(pending))
                        for i in range(int(delay_likecmt_),-1,-1):
                            self.show.emit(False,row,5,f'Đợi sau {i}'.format(i=i))
                            sleep(1)
                except:
                    pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
