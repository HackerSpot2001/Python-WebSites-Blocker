#!/usr/bin/python3
import sqlite3

get_Table = "select name from sqlite_master where type='table';"
create_table = "CREATE TABLE websites (id INT PRIMARY KEY AUTOINCREMENT,website CHAR(200) NOT NULL);"
insert_data = "INSERT INTO websites (id,website) VALUES (2,'http://www.youtube.com');"
getData = "SELECT id,website from websites;"
removeData = "DELETE FROM websites WHERE id=2"
updateData = "UPDATE websites SET website = 'www.google.com' WHERE id=1"
