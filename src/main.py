import sys
from myutils import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from typing import List
import random

class GUI:
  def __init__(self, app:QApplication, words_list: List[str]):
    self.app = QApplication(sys.argv) # 创建QApplication类的实例
    self.words_list = words_list
    self.current_word_idx = 0
    # 设置窗口
    self.main_win = QWidget() # 创建一个窗口
    self.main_win.resize(1000,600) # 设置窗口尺寸
    self.main_win.setWindowTitle("Vocabulary-Helper") # 设置窗口的标题
    # 单词显示文本框
    self.words_displayer = QLineEdit(self.main_win)
    self.words_displayer.setText(words_list[self.current_word_idx])
    self.words_displayer.setReadOnly(True)
    self.words_displayer.setAlignment(Qt.AlignCenter)
    self.words_displayer.setGeometry(350, 100, 300, 100)
    self.words_displayer.setFont(QFont("微软雅黑", 16))
    # 显示上一个单词
    self.prev_button = QPushButton(self.main_win)
    self.prev_button.setText("Previous")
    self.prev_button.setGeometry(150, 350, 150, 100)
    self.prev_button.setFont(QFont("微软雅黑", 10))
    self.prev_button.clicked.connect(self.prev_button_click)
    # 显示下一个单词
    self.next_button = QPushButton(self.main_win)
    self.next_button.setText("Next")
    self.next_button.setGeometry(700, 350, 150, 100)
    self.next_button.setFont(QFont("微软雅黑", 10))
    self.next_button.clicked.connect(self.next_button_click)
    self.main_win.show() # 显示窗口
    # 当前单词下标


  # def __del__(self):


  def prev_button_click(self):
    self.current_word_idx -= 1
    if (self.current_word_idx < 0):
      self.current_word_idx = 0
    self.words_displayer.setText(self.words_list[self.current_word_idx])
    print("prev button clicked")


  def next_button_click(self):
    self.current_word_idx += 1
    if (self.current_word_idx >= len(self.words_list)):
      self.current_word_idx = 0
    self.words_displayer.setText(self.words_list[self.current_word_idx])
    print("next button clicked")


if __name__ == '__main__':
  xls_path = "resources/vocabulary.xls"
  txt_path = "resources/words.txt"
  excel2txt(xls_path, txt_path)
  words_list = []
  with open(txt_path, "r") as file:
    words = file.readlines()
    for word in words:
      words_list.append(word)

  random.shuffle(words_list)

  app = QApplication(sys.argv) # 创建QApplication类的实例
  gui = GUI(app, words_list)
  sys.exit(app.exec_()) # 等待用户关闭窗口
