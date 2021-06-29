#!/usr/bin/python3
from sqlite3.dbapi2 import connect
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QWidget
import sys
import os
import sqlite3
from datetime import datetime as dt
import time

class websiteBlocker(QWidget):
    def __init__(self):
        super().__init__()
        top = 200
        left = 400
        width = 700
        height = 250
        db_name = "websites.db" 
        if os.path.exists(os.path.join(os.getcwd(),db_name)):
            self.conn = sqlite3.connect(db_name)
            self.conn_cursor = self.conn.cursor()
        
        else:
            with open(db_name,"w") as f:
                pass
            self.conn = sqlite3.connect(db_name)
            self.conn_cursor = self.conn.cursor()
            create_table = "CREATE TABLE blocked_websites (web_id INTEGER PRIMARY KEY AUTOINCREMENT,web_name CHAR(200) NOT NULL);"
            self.conn_cursor.execute(create_table)
            self.conn.commit()
        
        self.setWindowIcon(QIcon("block.png"))
        self.setWindowTitle("Python Websites Blocker")
        self.setGeometry(left,top,width,height)
        self.setStyleSheet("background-color:rgb(150,150,150)")
        self.vbox = QVBoxLayout()

        self.block_inp = QLineEdit()
        self.block_inp.setPlaceholderText("Enter URL Here :)")
        self.block_inp.setText('')
        self.block_inp.setStyleSheet("background-color:white;color:black;height:40px;padding:0px 10px;font-size:18px;border-radius:10px;")

        self.block_btn = QPushButton("Block URL")
        self.block_btn.setStyleSheet("height:25px;font-size:20px;color:rgb(50,50,05);")
        self.block_btn.clicked.connect(self.block_url)
        
        self.vbox.addWidget(self.block_inp)
        self.vbox.addWidget(self.block_btn)
        self.setLayout(self.vbox)
        self.show()
    # self.conn.close()

    def getWebsites(self):
        global websites
        getdata = "select web_name from blocked_websites;"
        self.conn_cursor.execute(getdata)
        for i in self.conn_cursor.fetchall():
            websites.add(i[0])

        try:
            with open(hosts_path,"r+") as f:
                content = f.read()
                for website in websites:
                    if website in content:
                        pass
                    
                    else:
                        f.write(f"{redirect}  {website}\n")


        except Exception as e:
            print("Error: ",e)



    def block_url(self):
        URL = self.block_inp.text()
        if URL == '':
            QMessageBox.question(self,"Data Error....","Please fill URL field",QMessageBox.Ok)

        else:
            try:
                insertData = f"INSERT INTO blocked_websites (web_name) VALUES ('{URL}');"
                self.conn_cursor.execute(insertData)
                self.conn.commit()

            except Exception as e:
                print("Error ",e)

        self.block_inp.setText('')
        self.getWebsites()


if __name__ == '__main__':
    websites = set()
    hosts_path = "/etc/hosts"
    redirect = "127.0.0.1"
    app = QApplication(sys.argv)
    win = websiteBlocker()
    sys.exit(app.exec())