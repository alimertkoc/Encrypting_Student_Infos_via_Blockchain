from block import Block
import datetime
import sqlite3

block_chain = [Block.create_genesis_block()]

print("İlk blok oluşturuldu!")

print("Öğrenci verileri eklemek için 1'e basınız:")
secim = int(input())

con = sqlite3.connect("veritabani.db")
cursor = con.cursor()

def tabloolustur():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS tablo1 (ad TEXT, soyad TEXT, fakulte TEXT, bolum TEXT, no TEXT, hash1 TEXT, hash2 TEXT bno INT)")
tabloolustur()

def son_al():
    cursor.execute("SELECT bno from tablo1")
    data = cursor.fetchall()
    for i in data:
        son = i[-1]
    return son

def son_hash1_al():
    cursor.execute("SELECT hash1 from tablo1")
    data = cursor.fetchall()
    for i in data:
        son_hash11_al = i[-1]
    return son_hash11_al

hash2 = son_hash1_al()
bno3 = son_al()
bno3 = bno3-1

block_chain[bno3-1].hash = son_hash1_al()

ad1 = input("Ad giriniz:")
soyad1 = input("Soyad giriniz:")
fakulte1 = input("Fakülte giriniz:")
bolum1 = input("Bölüm giriniz:")
no1 = (input("Öğrenci numarası giriniz:"))

if secim == 1:
    try:
        block_chain.append(Block(block_chain[bno3].hash,
                             ad1+soyad1+fakulte1+bolum1+no1,
                             datetime.datetime.now()))
        print("Blok oluşturuldu.")
        print("Blok Hash Değeri: %s" % block_chain[-1].hash)
    except IndexError:
        block_chain.append(Block(block_chain[bno3-1].hash,
                                 "DATA!",
                                 datetime.datetime.now()))
        print("Blok oluşturuldu." % bno3)
        print("Blok Hash Değeri: %s" % block_chain[-1].hash)

hash1 = block_chain[-1].hash
bno3 = bno3 + 1

cursor.execute("INSERT INTO tablo1 (ad, soyad, fakulte, bolum, no, hash1, hash2, bno) VALUES (?,?,?,?,?,?,?,?)",
                   (ad1, soyad1, fakulte1, bolum1, no1, hash1, hash2, bno3))

con.commit()

tabloolustur()

con.close()
