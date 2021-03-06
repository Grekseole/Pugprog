# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExhibitionForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExhibitionForm(object):
    def setupUi(self, ExhibitionForm):
        ExhibitionForm.setObjectName("ExhibitionForm")
        ExhibitionForm.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ExhibitionForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(ExhibitionForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.ExhibitionNameLabel = QtWidgets.QLabel(ExhibitionForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ExhibitionNameLabel.setFont(font)
        self.ExhibitionNameLabel.setText("")
        self.ExhibitionNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ExhibitionNameLabel.setObjectName("ExhibitionNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ExhibitionNameLabel)
        self.label_4 = QtWidgets.QLabel(ExhibitionForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.ExhibitionDateLabel = QtWidgets.QLabel(ExhibitionForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ExhibitionDateLabel.setFont(font)
        self.ExhibitionDateLabel.setText("")
        self.ExhibitionDateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ExhibitionDateLabel.setObjectName("ExhibitionDateLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ExhibitionDateLabel)
        self.label_5 = QtWidgets.QLabel(ExhibitionForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.ExperOrParticipateComboBox = QtWidgets.QComboBox(ExhibitionForm)
        self.ExperOrParticipateComboBox.setObjectName("ExperOrParticipateComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ExperOrParticipateComboBox)
        self.WhatDogComboBox = QtWidgets.QComboBox(ExhibitionForm)
        self.WhatDogComboBox.setObjectName("WhatDogComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.WhatDogComboBox)
        self.label_2 = QtWidgets.QLabel(ExhibitionForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_6 = QtWidgets.QLabel(ExhibitionForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.RinParticipateLabel = QtWidgets.QLabel(ExhibitionForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RinParticipateLabel.setFont(font)
        self.RinParticipateLabel.setText("")
        self.RinParticipateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RinParticipateLabel.setObjectName("RinParticipateLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.RinParticipateLabel)
        self.RingExpertLabel = QtWidgets.QLabel(ExhibitionForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RingExpertLabel.setFont(font)
        self.RingExpertLabel.setText("")
        self.RingExpertLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RingExpertLabel.setObjectName("RingExpertLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.RingExpertLabel)
        self.label_7 = QtWidgets.QLabel(ExhibitionForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_3 = QtWidgets.QLabel(ExhibitionForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_8 = QtWidgets.QLabel(ExhibitionForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.ClubParticipateNumberLabel = QtWidgets.QLabel(ExhibitionForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ClubParticipateNumberLabel.setFont(font)
        self.ClubParticipateNumberLabel.setText("")
        self.ClubParticipateNumberLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ClubParticipateNumberLabel.setObjectName("ClubParticipateNumberLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.ClubParticipateNumberLabel)
        self.verticalLayout.addLayout(self.formLayout)
        self.OkButton = QtWidgets.QPushButton(ExhibitionForm)
        self.OkButton.setObjectName("OkButton")
        self.verticalLayout.addWidget(self.OkButton)

        self.retranslateUi(ExhibitionForm)
        QtCore.QMetaObject.connectSlotsByName(ExhibitionForm)

    def retranslateUi(self, ExhibitionForm):
        _translate = QtCore.QCoreApplication.translate
        ExhibitionForm.setWindowTitle(_translate("ExhibitionForm", "Выставка"))
        self.label.setText(_translate("ExhibitionForm", "Название выставки"))
        self.label_4.setText(_translate("ExhibitionForm", "Дата выставки"))
        self.label_5.setText(_translate("ExhibitionForm", "Тип привлечения к выставке"))
        self.label_2.setText(_translate("ExhibitionForm", "Используемая собака"))
        self.label_6.setText(_translate("ExhibitionForm", "Собака учавствует на ринге"))
        self.label_7.setText(_translate("ExhibitionForm", "Вы судите ринг"))
        self.label_8.setText(_translate("ExhibitionForm", "Клубный номер участника"))
        self.OkButton.setText(_translate("ExhibitionForm", "Ок"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExhibitionForm = QtWidgets.QWidget()
    ui = Ui_ExhibitionForm()
    ui.setupUi(ExhibitionForm)
    ExhibitionForm.show()
    sys.exit(app.exec_())
