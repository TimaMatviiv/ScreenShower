# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ss.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(650, 520)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 650, 520))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabs.setFont(font)
        self.tabs.setStyleSheet("")
        self.tabs.setObjectName("tabs")
        self.songs = QtWidgets.QWidget()
        self.songs.setObjectName("songs")
        self.list_songs = QtWidgets.QListWidget(self.songs)
        self.list_songs.setGeometry(QtCore.QRect(10, 30, 221, 411))
        self.list_songs.setObjectName("list_songs")
        self.song_search = QtWidgets.QLineEdit(self.songs)
        self.song_search.setGeometry(QtCore.QRect(10, 10, 221, 20))
        self.song_search.setObjectName("song_search")
        self.list_words = QtWidgets.QListWidget(self.songs)
        self.list_words.setGeometry(QtCore.QRect(240, 10, 401, 431))
        self.list_words.setUniformItemSizes(False)
        self.list_words.setObjectName("list_words")
        self.av_songbooks = QtWidgets.QComboBox(self.songs)
        self.av_songbooks.setGeometry(QtCore.QRect(160, 450, 221, 22))
        self.av_songbooks.setObjectName("av_songbooks")
        self.label_6 = QtWidgets.QLabel(self.songs)
        self.label_6.setGeometry(QtCore.QRect(20, 450, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.new_song_btn = QtWidgets.QPushButton(self.songs)
        self.new_song_btn.setGeometry(QtCore.QRect(390, 450, 75, 21))
        self.new_song_btn.setObjectName("new_song_btn")
        self.edit_song_btn = QtWidgets.QPushButton(self.songs)
        self.edit_song_btn.setGeometry(QtCore.QRect(470, 450, 75, 21))
        self.edit_song_btn.setObjectName("edit_song_btn")
        self.tabs.addTab(self.songs, "")
        self.bible = QtWidgets.QWidget()
        self.bible.setObjectName("bible")
        self.av_translations = QtWidgets.QComboBox(self.bible)
        self.av_translations.setGeometry(QtCore.QRect(10, 445, 161, 22))
        self.av_translations.setObjectName("av_translations")
        self.label_3 = QtWidgets.QLabel(self.bible)
        self.label_3.setGeometry(QtCore.QRect(10, 420, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.bible_chapters_list = QtWidgets.QListWidget(self.bible)
        self.bible_chapters_list.setGeometry(QtCore.QRect(160, 30, 51, 381))
        self.bible_chapters_list.setObjectName("bible_chapters_list")
        self.bible_verses_list = QtWidgets.QListWidget(self.bible)
        self.bible_verses_list.setGeometry(QtCore.QRect(220, 30, 411, 381))
        self.bible_verses_list.setObjectName("bible_verses_list")
        self.chapter_input = QtWidgets.QLineEdit(self.bible)
        self.chapter_input.setGeometry(QtCore.QRect(160, 10, 51, 20))
        self.chapter_input.setObjectName("chapter_input")
        self.bible_books_list = QtWidgets.QListWidget(self.bible)
        self.bible_books_list.setGeometry(QtCore.QRect(10, 30, 141, 381))
        self.bible_books_list.setObjectName("bible_books_list")
        self.verse_input = QtWidgets.QLineEdit(self.bible)
        self.verse_input.setGeometry(QtCore.QRect(220, 10, 411, 20))
        self.verse_input.setObjectName("verse_input")
        self.book_input = QtWidgets.QLineEdit(self.bible)
        self.book_input.setGeometry(QtCore.QRect(10, 10, 141, 20))
        self.book_input.setObjectName("book_input")
        self.quick_bible_search = QtWidgets.QLineEdit(self.bible)
        self.quick_bible_search.setGeometry(QtCore.QRect(510, 450, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quick_bible_search.setFont(font)
        self.quick_bible_search.setText("")
        self.quick_bible_search.setObjectName("quick_bible_search")
        self.label_4 = QtWidgets.QLabel(self.bible)
        self.label_4.setGeometry(QtCore.QRect(510, 420, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.bible)
        self.label_5.setGeometry(QtCore.QRect(200, 420, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.bible_search = QtWidgets.QLineEdit(self.bible)
        self.bible_search.setGeometry(QtCore.QRect(200, 450, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bible_search.setFont(font)
        self.bible_search.setObjectName("bible_search")
        self.av_translations.raise_()
        self.label_3.raise_()
        self.bible_chapters_list.raise_()
        self.bible_verses_list.raise_()
        self.chapter_input.raise_()
        self.bible_books_list.raise_()
        self.book_input.raise_()
        self.quick_bible_search.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.bible_search.raise_()
        self.verse_input.raise_()
        self.tabs.addTab(self.bible, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.btn_save = QtWidgets.QPushButton(self.settings)
        self.btn_save.setGeometry(QtCore.QRect(430, 50, 101, 23))
        self.btn_save.setObjectName("btn_save")
        self.screensCB = QtWidgets.QComboBox(self.settings)
        self.screensCB.setGeometry(QtCore.QRect(20, 50, 181, 22))
        self.screensCB.setObjectName("screensCB")
        self.checkbox_stream_mode = QtWidgets.QCheckBox(self.settings)
        self.checkbox_stream_mode.setGeometry(QtCore.QRect(320, 50, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkbox_stream_mode.setFont(font)
        self.checkbox_stream_mode.setObjectName("checkbox_stream_mode")
        self.label = QtWidgets.QLabel(self.settings)
        self.label.setGeometry(QtCore.QRect(20, 30, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.checkbox_show_words = QtWidgets.QCheckBox(self.settings)
        self.checkbox_show_words.setGeometry(QtCore.QRect(220, 50, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkbox_show_words.setFont(font)
        self.checkbox_show_words.setObjectName("checkbox_show_words")
        self.tabWidget = QtWidgets.QTabWidget(self.settings)
        self.tabWidget.setGeometry(QtCore.QRect(20, 90, 601, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.simple_mode_settings_tab = QtWidgets.QWidget()
        self.simple_mode_settings_tab.setObjectName("simple_mode_settings_tab")
        self.label_2 = QtWidgets.QLabel(self.simple_mode_settings_tab)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_2.setObjectName("label_2")
        self.font_size_input = QtWidgets.QSpinBox(self.simple_mode_settings_tab)
        self.font_size_input.setGeometry(QtCore.QRect(70, 20, 42, 22))
        self.font_size_input.setObjectName("font_size_input")
        self.label_7 = QtWidgets.QLabel(self.simple_mode_settings_tab)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_7.setObjectName("label_7")
        self.text_color_input = QtWidgets.QLineEdit(self.simple_mode_settings_tab)
        self.text_color_input.setGeometry(QtCore.QRect(80, 50, 71, 20))
        self.text_color_input.setObjectName("text_color_input")
        self.tabWidget.addTab(self.simple_mode_settings_tab, "")
        self.stream_mode_settings_tab = QtWidgets.QWidget()
        self.stream_mode_settings_tab.setObjectName("stream_mode_settings_tab")
        self.tabWidget.addTab(self.stream_mode_settings_tab, "")
        self.tabs.addTab(self.settings, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScreenShower"))
        self.song_search.setPlaceholderText(_translate("MainWindow", "Пошук..."))
        self.label_6.setText(_translate("MainWindow", "Avaliable songbooks:"))
        self.new_song_btn.setText(_translate("MainWindow", "new song"))
        self.edit_song_btn.setText(_translate("MainWindow", "edit song"))
        self.tabs.setTabText(self.tabs.indexOf(self.songs), _translate("MainWindow", "Songs"))
        self.label_3.setText(_translate("MainWindow", "Translations"))
        self.chapter_input.setPlaceholderText(_translate("MainWindow", "chapter"))
        self.verse_input.setPlaceholderText(_translate("MainWindow", "verse"))
        self.book_input.setPlaceholderText(_translate("MainWindow", "book"))
        self.quick_bible_search.setPlaceholderText(_translate("MainWindow", "мт 10 10"))
        self.label_4.setText(_translate("MainWindow", "Quick search"))
        self.label_5.setText(_translate("MainWindow", "Search in bible"))
        self.tabs.setTabText(self.tabs.indexOf(self.bible), _translate("MainWindow", "Bible"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.checkbox_stream_mode.setText(_translate("MainWindow", "Stream mode"))
        self.label.setText(_translate("MainWindow", "Availabel screens:"))
        self.checkbox_show_words.setText(_translate("MainWindow", "Show words"))
        self.label_2.setText(_translate("MainWindow", "Font size"))
        self.label_7.setText(_translate("MainWindow", "Text color"))
        self.text_color_input.setPlaceholderText(_translate("MainWindow", "black"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.simple_mode_settings_tab), _translate("MainWindow", "Simple Mode Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stream_mode_settings_tab), _translate("MainWindow", "Stream Mode Settings"))
        self.tabs.setTabText(self.tabs.indexOf(self.settings), _translate("MainWindow", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
