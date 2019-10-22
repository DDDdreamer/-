import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PyQt5 import QtCore, QtGui, QtWidgets
import one
import two
import three
import four
import five
import six
import seven
import eight
import httpfunctions
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication,QMainWindow

class one1(QtWidgets.QMainWindow, one.Ui_MainWindow):#开始页面
    # 建立的是Main Window项目，故此处导入的是QMainWindow
    # 参考博客中建立的是Widget项目，因此哪里导入的是QWidget
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
    def slot1(self):
        self.close()
        w = two2(window)
        w.resize(775,549)
        w.show()

class two2(QtWidgets.QMainWindow, two.Ui_MainWindow):#登录

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
    def slot2(self):#登录按钮事件
        global token
        login_name = self.lineEdit_3.text()
        login_password = self.lineEdit_4.text()
        # self.close()
        # w = four4(window)
        # w.resize(775, 549)
        # w.show()
        if login_name == "" or login_password == "":
            if login_name == "":
                print('请输入用户名!')
            elif login_password == "":
                print('请输入密码!')

        else:
            status1 = httpfunctions.login(login_name,login_password)
            if status1 == 0:
                self.close()
                w = four4(window)
                w.resize(775, 549)
                w.show()
            elif status1 == 1004:
                print("Token过期!")
            elif status1 == 3002:
                print('用户名不存在!')
            else:
                print('密码错误!')

    def slot3(self):#注册按钮事件
        self.close()
        w = three3(window)
        w.resize(775, 549)
        w.show()

class three3(QtWidgets.QMainWindow, three.Ui_MainWindow):#注册界面

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
    def slot4(self):
        login_name = self.User_name.text()
        login_password = self.user_password.text()
        login_student_name = self.Student_name.text()
        login_student_password = self.Student_password.text()
        if login_name == "" or login_password == "" or login_student_name == "" or login_student_password == "":
            if login_name == "":
                print('请输入用户名!')
            elif login_password == "":
                print('请输入密码!')
            elif login_student_name == "":
                print('请输入学号!')
            else:
                print('请输入教务处密码!')

        else:
            status2 = httpfunctions.register_with_bind(login_name,login_password,login_student_name,login_student_password)
            if status2 == 0:
                print('注册成功!')
                self.close()
                w = four4(window)
                w.resize(775, 549)
                w.show()
            elif status2 == 1001:
                print('用户名已被使用!')
            else:
                print('注册失败!')

    def slot5(self):
        self.close()
        w = two2(window)
        w.resize(775, 549)
        w.show()

class four4(QtWidgets.QMainWindow, four.Ui_MainWindow):#游戏界面
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
    def slot6(self):#排行榜
        # self.close()
        w = five5(window)
        w.resize(775, 549)
        w.show()
    def slot8(self):#查询战绩
        # self.close()
        w = six6(window)
        w.resize(775, 549)
        w.show()
    def slot10(self):#开启游戏
        w = seven7(window)
        # self.close()
        w.show()
    def slot12(self):#注销

        reply = QMessageBox.warning(self,
                                    "警告",
                                    "确认注销？",
                                    QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.hide()
            httpfunctions.logout()
            print('注销成功！')
            w = two2(window)
            w.resize(775, 549)
            w.show()

    def slot14(self):#往期对战
        # self.close()
        w = eight8(window)
        w.show()

class five5(QtWidgets.QMainWindow, five.Ui_MainWindow):#排行榜
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.page = 1
        self.setupUi(self)
        res = httpfunctions.get_rank()
        quece = (self.page - 1) * 4 + 1

        self.rank1.setText('No.{}'.format(quece))
        self.rank2.setText('No.{}'.format(quece + 1))
        self.rank3.setText('No.{}'.format(quece + 2))
        self.rank4.setText('No.{}'.format(quece + 3))
        self.id1.setText(str(res[(self.page - 1) * 4]['player_id']))
        self.id2.setText(str(res[(self.page - 1) * 4 + 1]['player_id']))
        self.id3.setText(str(res[(self.page - 1) * 4 + 2]['player_id']))
        self.id4.setText(str(res[(self.page - 1) * 4 + 3]['player_id']))
        self.name1.setText(str(res[(self.page - 1) * 4]['name']))
        self.name2.setText(str(res[(self.page - 1) * 4 + 1]['name']))
        self.name3.setText(str(res[(self.page - 1) * 4 + 2]['name']))
        self.name4.setText(str(res[(self.page - 1) * 4 + 3]['name']))
        self.point1.setText(str(res[(self.page - 1) * 4]['score']))
        self.point2.setText(str(res[(self.page - 1) * 4 + 1]['score']))
        self.point3.setText(str(res[(self.page - 1) * 4 + 2]['score']))
        self.point4.setText(str(res[(self.page - 1) * 4 + 3]['score']))

    def slot7(self):
        self.hide()

class six6(QtWidgets.QMainWindow, six.Ui_MainWindow):#战局详情

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
    def slot9(self):
        self.hide()
    def search_game(self):
        game_id = self.game_id.text()
        game_info = httpfunctions.get_history_detail(game_id)
        if game_info['status'] == 0:
            game_data = game_info['data']['detail']
            self.user_id1.setText(str(game_data[0]['player_id']))
            self.user_id2.setText(str(game_data[1]['player_id']))
            self.user_id3.setText(str(game_data[2]['player_id']))
            self.user_id4.setText(str(game_data[3]['player_id']))

            self.username1.setText(str(game_data[0]['name']))
            self.username2.setText(str(game_data[1]['name']))
            self.username3.setText(str(game_data[2]['name']))
            self.username4.setText(str(game_data[3]['name']))

            self.score1.setText(str(game_data[0]['score']))
            self.score2.setText(str(game_data[1]['score']))
            self.score3.setText(str(game_data[2]['score']))
            self.score4.setText(str(game_data[3]['score']))

            if len(game_data[0]['card'] )== 3:
                self.cards_type1.setText(str(game_data[0]['card'][0]) + '\n' +  str(game_data[0]['card'][1]) + '\n' + str(game_data[0]['card'][2]))
            else :
                self.cards_type1.setText(str(game_data[0]['card']))

            if len(game_data[1]['card']) == 3:
                self.cards_type2.setText(str(game_data[1]['card'][0]) + '\n' +  str(game_data[1]['card'][1]) + '\n' + str(game_data[1]['card'][2]))
            else:
                self.cards_type2.setText(str(game_data[1]['card']))

            if len(game_data[2]['card'] )== 3:
                self.cards_type3.setText(str(game_data[2]['card'][0]) + '\n' +  str(game_data[2]['card'][1]) + '\n' + str(game_data[2]['card'][2]))
            else:
                self.cards_type3.setText(str(game_data[2]['card']))
            if len(game_data[3]['card'] )== 3:
                self.cards_type4.setText(str(game_data[3]['card'][0]) + '\n' +  str(game_data[3]['card'][1]) + '\n' + str(game_data[3]['card'][2]))
            else:
                self.cards_type4.setText(str(game_data[3]['card']))
        elif game_info['status'] == 2003:
            print('战局id不合法!')
        elif game_info['status'] == 3001:
            print('战局未结束或战剧不存在!')

class seven7(QtWidgets.QMainWindow, seven.Ui_MainWindow):    #开启游戏界面
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def find_game(self):
        self.pushButton_2.setText('Finding...')
        self.pushButton_2.setEnabled(False)
        game_info = httpfunctions.startgame()
        game_id = ""
        cards = ""
        if game_info['status'] == 0:
            color = {'*': 'meihua', '#': '#', '&': 'hongtao', '$': 'heitao'}
            Cards = game_info['data']['card']
            cards = Cards.split(" ")
            game_id = game_info['data']['id']
            # 显示手牌
            img1 = color[cards[0][:1]] + cards[0][1:] + '.jpg);'
            self.s1.setStyleSheet('border-image: url(:/beijing1/icons/' + img1)
            img2 = color[cards[1][:1]] + cards[1][1:] + '.jpg);'
            self.s2.setStyleSheet('border-image: url(:/beijing1/icons/' + img2)
            img3 = color[cards[2][:1]] + cards[2][1:] + '.jpg);'
            self.s3.setStyleSheet('border-image: url(:/beijing1/icons/' + img3)
            img4 = color[cards[3][:1]] + cards[3][1:] + '.jpg);'
            self.s4.setStyleSheet('border-image: url(:/beijing1/icons/' + img4)
            img5 = color[cards[4][:1]] + cards[4][1:] + '.jpg);'
            self.s5.setStyleSheet('border-image: url(:/beijing1/icons/' + img5)
            img6 = color[cards[5][:1]] + cards[5][1:] + '.jpg);'
            self.s6.setStyleSheet('border-image: url(:/beijing1/icons/' + img6)
            img7 = color[cards[6][:1]] + cards[6][1:] + '.jpg);'
            self.s7.setStyleSheet('border-image: url(:/beijing1/icons/' + img7)
            img8 = color[cards[7][:1]] + cards[7][1:] + '.jpg);'
            self.s8.setStyleSheet('border-image: url(:/beijing1/icons/' + img8)
            img9 = color[cards[8][:1]] + cards[8][1:] + '.jpg);'
            self.s9.setStyleSheet('border-image: url(:/beijing1/icons/' + img9)
            img10 = color[cards[9][:1]] + cards[9][1:] + '.jpg);'
            self.s10.setStyleSheet('border-image: url(:/beijing1/icons/' + img10)
            img11 = color[cards[10][:1]] + cards[10][1:] + '.jpg);'
            self.s11.setStyleSheet('border-image: url(:/beijing1/icons/' + img11)
            img12 = color[cards[11][:1]] + cards[11][1:] + '.jpg);'
            self.s12.setStyleSheet('border-image: url(:/beijing1/icons/' + img12)
            img13 = color[cards[12][:1]] + cards[12][1:] + '.jpg);'
            self.s13.setStyleSheet('border-image: url(:/beijing1/icons/' + img13)
            QtWidgets.QApplication.processEvents()

            res = httpfunctions.postcards(Cards)
            final_cards = res[0]
            shangdun = final_cards[0].split(' ')
            zhongdun = final_cards[1].split(' ')
            xiadun = final_cards[2].split(' ')
            # 前墩
            img_f1 = color[shangdun[0][:1]] + shangdun[0][1:] + '.jpg);'
            self.f1.setStyleSheet('border-image: url(:/beijing1/icons/' + img_f1)
            img_f2 = color[shangdun[1][:1]] + shangdun[1][1:] + '.jpg);'
            self.f2.setStyleSheet('border-image: url(:/beijing1/icons/' + img_f2)
            img_f3 = color[shangdun[2][:1]] + shangdun[2][1:] + '.jpg);'
            self.f3.setStyleSheet('border-image: url(:/beijing1/icons/' + img_f3)
            # 中墩
            img_m1 = color[zhongdun[0][:1]] + zhongdun[0][1:] + '.jpg);'
            self.m1.setStyleSheet('border-image: url(:/beijing1/icons/' + img_m1)
            img_m2 = color[zhongdun[1][:1]] + zhongdun[1][1:] + '.jpg);'
            self.m2.setStyleSheet('border-image: url(:/beijing1/icons/' + img_m2)
            img_m3 = color[zhongdun[2][:1]] + zhongdun[2][1:] + '.jpg);'
            self.m3.setStyleSheet('border-image: url(:/beijing1/icons/' + img_m3)
            img_m4 = color[zhongdun[3][:1]] + zhongdun[3][1:] + '.jpg);'
            self.m4.setStyleSheet('border-image: url(:/beijing1/icons/' + img_m4)
            img_m5 = color[zhongdun[4][:1]] + zhongdun[4][1:] + '.jpg);'
            self.m5.setStyleSheet('border-image: url(:/beijing1/icons/' + img_m5)
            # 后墩
            img_b1 = color[xiadun[0][:1]] + xiadun[0][1:] + '.jpg);'
            self.b1.setStyleSheet('border-image: url(:/beijing1/icons/' + img_b1)
            img_b2 = color[xiadun[1][:1]] + xiadun[1][1:] + '.jpg);'
            self.b2.setStyleSheet('border-image: url(:/beijing1/icons/' + img_b2)
            img_b3 = color[xiadun[2][:1]] + xiadun[2][1:] + '.jpg);'
            self.b3.setStyleSheet('border-image: url(:/beijing1/icons/' + img_b3)
            img_b4 = color[xiadun[3][:1]] + xiadun[3][1:] + '.jpg);'
            self.b4.setStyleSheet('border-image: url(:/beijing1/icons/' + img_b4)
            img_b5 = color[xiadun[4][:1]] + xiadun[4][1:] + '.jpg);'
            self.b5.setStyleSheet('border-image: url(:/beijing1/icons/' + img_b5)
            QtWidgets.QApplication.processEvents()
            QMessageBox.information(self,
                                    "提示",
                                    "找到对局，成功出牌！",
                                    QMessageBox.Yes)
        else:
            QMessageBox.warning(self,
                                        "错误",
                                        "寻找对局失败，请检查你的账号是否已绑定！",
                                        QMessageBox.Yes)
        self.pushButton_2.setText('寻找对局')
        self.pushButton_2.setEnabled(True)

    def slot11(self):#退出
        self.hide()

class eight8(QtWidgets.QMainWindow, eight.Ui_MainWindow):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def back(self):
        self.hide()

    def list_search(self):
        page = self.page.text()
        user_id =self.userid.text()
        info = httpfunctions.get_history_list(user_id,page)

        msg = ""
        if info['status'] == 0:
            for i in info['data']:
                # print(i)
                # print(msg,i['id'],i['card'],i['score'],type(msg),type(i['card']),type(i['score']))
                msg += '战局id:' + str(i['id']) +'            ' +  '牌型:' + str(i['card'])+'           得分:' + str(i['score']) +'\n\n'
            self.textEdit.setText(msg)
            if info['data'] == []:
                QMessageBox.information(self,'提示','该页面不存在',QMessageBox.Yes)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    window = one1()

    window.show()

    sys.exit(app.exec_())