import socket

from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6 import QtWidgets
import threading

from PyQt6 import QtCore

import first_player
import second_player_field
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from classes import Player1, Player2


def receive():
    while True:
        window.messages.append(sock.recv(1024).decode('utf-8'))
        if window.number == 2:
            if len(window.messages[0]) == 1:
                checking = window.messages[0]
                if checking == '1':
                    window.mistake.setText('')
                    for j in range(len(window.word)):
                        if window.word[j] == window.input[j].lower():
                            window.massive[window.i - 5 + j].setStyleSheet("background-color:#fff000")
                            window.flag += 1
                        elif window.input[j].lower() not in window.word:
                            window.massive[window.i - 5 + j].setStyleSheet("background-color:#606160; color:white")
                    if window.flag == 5:
                        window.mistake.setText('Поздравляем, вы выиграли!')
                        window.Play.setEnabled(False)
                    else:
                        window.input = ''
                        window.flag = 0
                        window.words += 1
                        if window.words == 6:
                            window.mistake.setText(
                                f'К сожалению,вы проиграли,\nтак как у вас закончились слова\nПравильное слово - {window.word}')
                            window.input = 'aaaaa'
                            window.Play.setEnabled(False)
                else:
                    window.mistake.setText('Данного слова не существет,\nпожалуйста, измените его')
            else:
                window.word = window.messages[0]
                window.label.setText('Второй игрок загадал слово.\n Попробуйте разгадать его!')
                window.Play.clicked.connect(window.check)
                window.Play.setEnabled(True)
            window.messages.pop()


if __name__ == '__main__':
    app = QApplication([])
    sock = socket.socket()
    sock.connect(('localhost', 50000))
    number = sock.recv(1024).decode('utf-8')
    if number == '1':
        window = Player1(sock)
        window.Play.setEnabled(True)
    else:
        window = Player2(sock)
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    window.show()
    app.exec()
