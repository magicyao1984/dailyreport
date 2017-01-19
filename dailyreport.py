# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daily_report.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import MySQLdb, csv, sys, os, codecs
from PyQt4 import QtCore, QtGui
from datetime import date, datetime
import webbrowser

reload(sys)
sys.path.append("libs")
sys.setdefaultencoding("utf-8")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(829, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(640, 60, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel |
                                          QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 20, 371, 71))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.comboBox = QtGui.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(150, 30, 74, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.dateEdit = QtGui.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(20, 30, 110, 22))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit.setDate(datetime.today())
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_24 = QtGui.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(250, 0, 78, 20))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.textEdit_2 = QtGui.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 20, 111, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(20, 100, 791, 191))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.textEdit = QtGui.QTextEdit(self.frame_2)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(670, 140, 104, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.layoutWidget = QtGui.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 12, 182, 92))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout.addWidget(self.doubleSpinBox, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.gridLayout.addWidget(self.doubleSpinBox_2, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.gridLayout.addWidget(self.doubleSpinBox_3, 3, 1, 1, 1)
        self.layoutWidget_4 = QtGui.QWidget(self.frame_2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(20, 112, 182, 61))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.layoutWidget_4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_19 = QtGui.QLabel(self.layoutWidget_4)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_5.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.layoutWidget_4)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_5.addWidget(self.label_18, 0, 0, 1, 2)
        self.doubleSpinBox_13 = QtGui.QDoubleSpinBox(self.layoutWidget_4)
        self.doubleSpinBox_13.setObjectName(_fromUtf8("doubleSpinBox_13"))
        self.gridLayout_5.addWidget(self.doubleSpinBox_13, 1, 1, 1, 1)
        self.layoutWidget_2 = QtGui.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(400, 12, 182, 92))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_10 = QtGui.QLabel(self.layoutWidget_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 2)
        self.label_11 = QtGui.QLabel(self.layoutWidget_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.doubleSpinBox_7 = QtGui.QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox_7.setObjectName(_fromUtf8("doubleSpinBox_7"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_7, 1, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.layoutWidget_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox_8.setObjectName(_fromUtf8("doubleSpinBox_8"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_8, 2, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.layoutWidget_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)
        self.doubleSpinBox_9 = QtGui.QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox_9.setObjectName(_fromUtf8("doubleSpinBox_9"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_9, 3, 1, 1, 1)
        self.layoutWidget_3 = QtGui.QWidget(self.frame_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(590, 12, 182, 92))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.layoutWidget_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_14 = QtGui.QLabel(self.layoutWidget_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 2)
        self.label_15 = QtGui.QLabel(self.layoutWidget_3)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_4.addWidget(self.label_15, 1, 0, 1, 1)
        self.doubleSpinBox_10 = QtGui.QDoubleSpinBox(self.layoutWidget_3)
        self.doubleSpinBox_10.setObjectName(_fromUtf8("doubleSpinBox_10"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_10, 1, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.layoutWidget_3)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_4.addWidget(self.label_16, 2, 0, 1, 1)
        self.doubleSpinBox_11 = QtGui.QDoubleSpinBox(self.layoutWidget_3)
        self.doubleSpinBox_11.setObjectName(_fromUtf8("doubleSpinBox_11"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_11, 2, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.layoutWidget_3)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_4.addWidget(self.label_17, 3, 0, 1, 1)
        self.doubleSpinBox_12 = QtGui.QDoubleSpinBox(self.layoutWidget_3)
        self.doubleSpinBox_12.setObjectName(_fromUtf8("doubleSpinBox_12"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_12, 3, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.frame_2)
        self.label_20.setGeometry(QtCore.QRect(600, 150, 61, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.layoutWidget1 = QtGui.QWidget(self.frame_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(210, 12, 182, 92))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 2)
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.gridLayout_2.addWidget(self.doubleSpinBox_4, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.doubleSpinBox_5 = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_5.setObjectName(_fromUtf8("doubleSpinBox_5"))
        self.gridLayout_2.addWidget(self.doubleSpinBox_5, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget1)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.doubleSpinBox_6 = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_6.setObjectName(_fromUtf8("doubleSpinBox_6"))
        self.gridLayout_2.addWidget(self.doubleSpinBox_6, 3, 1, 1, 1)
        self.layoutWidget2 = QtGui.QWidget(self.frame_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(250, 110, 138, 71))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.layoutWidget2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_22 = QtGui.QLabel(self.layoutWidget2)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_6.addWidget(self.label_22, 0, 0, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.layoutWidget2)
        self.spinBox.setMaximum(1000)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout_6.addWidget(self.spinBox, 0, 1, 1, 1)
        self.label_23 = QtGui.QLabel(self.layoutWidget2)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_6.addWidget(self.label_23, 1, 0, 1, 1)
        self.spinBox_2 = QtGui.QSpinBox(self.layoutWidget2)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.gridLayout_6.addWidget(self.spinBox_2, 1, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(600, 20, 91, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 20, 91, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 20, 91, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox,
                               QtCore.SIGNAL(_fromUtf8("accepted()")),
                               self.onBtnClicked)
        #Dialog.accept)
        QtCore.QObject.connect(self.buttonBox,
                               QtCore.SIGNAL(_fromUtf8("rejected()")),
                               Dialog.reject)
        #add by new button
        QtCore.QObject.connect(self.pushButton,
                               QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.onGetFile)

        QtCore.QObject.connect(self.pushButton_2,
                               QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.showGraph)

        QtCore.QObject.connect(self.pushButton_3,
                               QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.updateInfo)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "DailyReport", None))
        self.comboBox.setItemText(0, _translate("Dialog", "==NAME==", None))

        #这里可以从数据库中读出来加载上
        self.comboBox.setItemText(1, _translate("Dialog", "staffA", None))
        self.comboBox.setItemText(2, _translate("Dialog", "staffB", None))
        self.comboBox.setItemText(3, _translate("Dialog", "staffC", None))
        self.comboBox.setItemText(4, _translate("Dialog", "staffD", None))
        self.comboBox.setItemText(5, _translate("Dialog", "staffD", None))
        self.label.setText(
            _translate("Dialog", "-------User Info Area-----", None))
        self.label_24.setText(_translate("Dialog", "项目名称：", None))
        self.label_2.setText(
            _translate("Dialog", "|----------- 设计 -----------|", None))
        self.label_3.setText(_translate("Dialog", "用例设计：", None))
        self.label_4.setText(_translate("Dialog", "需求理解：", None))
        self.label_5.setText(_translate("Dialog", "交流沟通：", None))
        self.label_19.setText(_translate("Dialog", "其    他：", None))
        self.label_18.setText(
            _translate("Dialog", "|----------- 其他 -----------|", None))
        self.label_10.setText(
            _translate("Dialog", "|----------- BUG -----------|", None))
        self.label_11.setText(_translate("Dialog", "BUG提出：", None))
        self.label_12.setText(_translate("Dialog", "Bug Fix：", None))
        self.label_13.setText(_translate("Dialog", "调查/交流：", None))
        self.label_14.setText(
            _translate("Dialog", "|----------- 管理 -----------|", None))
        self.label_15.setText(_translate("Dialog", "会    议：", None))
        self.label_16.setText(_translate("Dialog", "文档作成：", None))
        self.label_17.setText(_translate("Dialog", "技术提升：", None))
        self.label_20.setText(_translate("Dialog", "合计工时：", None))
        self.label_6.setText(
            _translate("Dialog", "|----------- 测试 -----------|", None))
        self.label_7.setText(_translate("Dialog", "用例执行：", None))
        self.label_8.setText(_translate("Dialog", "探索测试：", None))
        self.label_9.setText(_translate("Dialog", "开发交流：", None))
        self.label_22.setText(_translate("Dialog", "用例条数：", None))
        self.label_23.setText(_translate("Dialog", "BUG数(当日)：", None))
        self.pushButton.setText(_translate("Dialog", "GetReportList", None))
        self.pushButton_2.setText(_translate("Dialog", "showGraph", None))
        self.pushButton_3.setText(_translate("Dialog", "Update", None))

        #获取脚本文件的当前路径
    def cur_file_dir(self):
        #获取脚本路径
        path = sys.path[0]
        #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)
            #打印结果

    def onGetFile(self):
        result = []
        temp = []
        temp2 = []
        try:
            (conn, cur) = self.getConnAndCursor()
            cur.execute('select * from daily_data order by day(date) asc')
            conn.commit()
            count = len(cur.description)

            for re in cur.description:
                temp.append(re)

            for i in xrange(0, count):
                temp2.append(temp[i][0])

            for res in cur:
                result.append(res)

        except mysql.connector.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

        finally:
            self.closeConnAndCursor(cur, conn)

        #下载文件
        todayDate = datetime.now().strftime("%Y%m%d_%H%M%S")
        savepath = self.cur_file_dir() + '\\'
        #print savepath
        savename = todayDate + '.csv'
        if (len(result) >= 0):
            with open(savepath + savename, 'wb') as csvfile:
                # CSV文件UTF8乱码解决方案，win下追加bom
                csvfile.write(codecs.BOM_UTF8)
                spamwriter = csv.writer(csvfile, dialect='excel')
                #, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(temp2)
                for res in result:
                    spamwriter.writerow(res)

        msgBox = QtGui.QMessageBox()
        msgBox.setText(u"<a href=" + savepath + savename +
                       ">-------下载成功,点我查看！------</a>" + "<br><br><a href=" +
                       savepath + ">--------点我查看文件夹！-------</a>")
        msgBox.exec_()

    #2017/1/17追加修改功能
    def updateInfo(self):
        #Update数据库
        date = self.dateEdit.text()
        name = self.comboBox.currentText()
        pjname = self.textEdit_2.toPlainText()

        cl_design = self.doubleSpinBox.text()
        cl_rikayi = self.doubleSpinBox_2.text()
        cl_comm = self.doubleSpinBox_3.text()

        exc_cl = self.doubleSpinBox_4.text()
        exc_exp = self.doubleSpinBox_5.text()
        exc_comm = self.doubleSpinBox_6.text()

        bug_comt = self.doubleSpinBox_7.text()
        bug_fix = self.doubleSpinBox_8.text()
        bug_comm = self.doubleSpinBox_9.text()

        mgt_mting = self.doubleSpinBox_10.text()
        mgt_doc = self.doubleSpinBox_11.text()
        mgt_olddoc = self.doubleSpinBox_12.text()

        bug_num = self.spinBox_2.text()
        cl_num = self.spinBox.text()

        other_other = self.doubleSpinBox_13.text()

        total = float(cl_design) + float(cl_rikayi) + float(cl_comm) + float(
            exc_cl) + float(exc_exp) + float(exc_comm) + float(
                bug_comt) + float(bug_fix) + float(bug_comm) + float(
                    mgt_mting) + float(mgt_doc) + float(mgt_olddoc) + float(
                        other_other)

        self.textEdit.setText(str(total))

        if name == "==NAME==":
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"请正确选择更新者的姓名！")
            msgBox.exec_()

        else:
            sql = "UPDATE daily_data SET cl_design ='"\
                                            + cl_design +"', cl_rikayi ='"\
                                            + cl_rikayi +"', cl_comm ='"\
                                            + cl_comm +"', exc_cl ='"\
                                            + exc_cl +"', exc_exp ='"\
                                            + exc_exp +"', exc_comm ='"\
                                            + exc_comm +"', bug_comt ='"\
                                            + bug_comt +"', bug_fix ='"\
                                            + bug_fix +"', bug_comm ='"\
                                            + bug_comm +"', mgt_mting ='"\
                                            + mgt_mting +"', mgt_doc ='"\
                                            + mgt_doc +"', mgt_olddoc ='"\
                                            + mgt_olddoc +"', other_other ='"\
                                            + other_other +"', bug_num ='"\
                                            + bug_num +"', cl_num ='"\
                                            + cl_num +"', total ='"\
                                            + str(total) + "'" + " where date ='"+ date + "'and name ='"\
                                                                            + name +"'and pjname ='"\
                                                                            + pjname +"'"

            print sql
            try:
                (conn, cur) = self.getConnAndCursor()
                cur.execute(str(sql).strip())
                conn.commit()

            except Exception as e:

                msgBox = QtGui.QMessageBox()
                msgBox.setText(str(e))
                msgBox.exec_()
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setText(u"日报修改成功：\n" + sql)
                msgBox.exec_()

            finally:
                self.closeConnAndCursor(cur, conn)

    def onBtnClicked(self):
        #插入数据库
        date = self.dateEdit.text()
        name = self.comboBox.currentText()
        pjname = self.textEdit_2.toPlainText()

        cl_design = self.doubleSpinBox.text()
        cl_rikayi = self.doubleSpinBox_2.text()
        cl_comm = self.doubleSpinBox_3.text()

        exc_cl = self.doubleSpinBox_4.text()
        exc_exp = self.doubleSpinBox_5.text()
        exc_comm = self.doubleSpinBox_6.text()

        bug_comt = self.doubleSpinBox_7.text()
        bug_fix = self.doubleSpinBox_8.text()
        bug_comm = self.doubleSpinBox_9.text()

        mgt_mting = self.doubleSpinBox_10.text()
        mgt_doc = self.doubleSpinBox_11.text()
        mgt_olddoc = self.doubleSpinBox_12.text()

        bug_num = self.spinBox_2.text()
        cl_num = self.spinBox.text()

        other_other = self.doubleSpinBox_13.text()

        total = float(cl_design) + float(cl_rikayi) + float(cl_comm) + float(
            exc_cl) + float(exc_exp) + float(exc_comm) + float(
                bug_comt) + float(bug_fix) + float(bug_comm) + float(
                    mgt_mting) + float(mgt_doc) + float(mgt_olddoc) + float(
                        other_other)

        self.textEdit.setText(str(total))

        if name == "==NAME==":
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"请正确选择提交者的姓名！")
            msgBox.exec_()

        else:
            # + bug_comm +"', '"\
            sql = "INSERT into daily_data VALUES ('"\
                                            + date + "', '"\
                                            + name +"', '"\
                                            + pjname +"', '"\
                                            + cl_design +"', '"\
                                            + cl_rikayi +"', '"\
                                            + cl_comm +"', '"\
                                            + exc_cl +"', '"\
                                            + exc_exp +"', '"\
                                            + exc_comm +"', '"\
                                            + bug_comt +"', '"\
                                            + bug_fix +"', '"\
                                            + bug_comm +"', '"\
                                            + mgt_mting +"', '"\
                                            + mgt_doc +"', '"\
                                            + mgt_olddoc +"', '"\
                                            + other_other +"', '"\
                                            + bug_num +"', '"\
                                            + cl_num +"', '"\
                                            + str(total) + "'" +")"
            #print sql
            #sql = "select * from daily_data"
            print sql
            try:
                (conn, cur) = self.getConnAndCursor()
                cur.execute(str(sql).strip())
                conn.commit()

            except Exception as e:

                msgBox = QtGui.QMessageBox()
                msgBox.setText(str(e))
                msgBox.exec_()
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setText(u"日报提交成功：\n" + sql)
                msgBox.exec_()

            finally:
                self.closeConnAndCursor(cur, conn)

    #数据库连接信息
    def getConnAndCursor(self):
        conn = MySQLdb.connect(
            host='x.x.x.x',
            port=3306,
            user='xxxxxx',
            passwd='xxxxxx',
            db='xxxxxxxx',
            charset='utf8')
        cur = conn.cursor()
        return (conn, cur)

    # 追加打开图表页面 数据可视化端
    def showGraph(self):
        #这里配置自己的IP
        url = 'http://ip:9080/showgraph.html'
        webbrowser.open(url)

    def closeConnAndCursor(self, cur, conn):
        cur.close()
        conn.close()

    # QtGui.QMessageBox()
    # def isokcheck(self):
    #     result = QtGui.QMessageBox.question(
    #         self, 'message', 'who are you?', QtGui.QMessageBox.Yes |
    #         QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    #     if result == QtGui.QMessageBox.Yes:
    #         print 'you select yes'
    #     elif result == QtGui.QMessageBox.No:
    #         print 'you select no'

    # if name == "==NAME==":
    #     QtGui.QMessageBox()

    #
    # self.buttonBox.Ok.setText('aaa')
    # self.buttonBox.Ok.open()
    # self.buttonBox.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())