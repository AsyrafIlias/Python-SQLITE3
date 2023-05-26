import sqlite3

database =  input("Enter database: ")
db = sqlite3.connect(database)

cur = db.cursor()

cur.execute ('''CREATE TABLE IF NOT EXISTS LIST 
                (
                ID INTEGER PRIMARY KEY,
                ITEM TEXT,
                BOUGHT INTEGER,
                SOLD INTEGER,
                STOCK INTEGER 
                );
            ''')

choice = int(input("1 - Enter record\n2 - View record \n3 - Delete record\n4 - Update record\n"))

match choice: 
    case 1:
        num = int(input("Enter number of items: "))

        for x in range (num):
            item = input("Enter item's name: ")
            bought = int(input("Bought: "))
            sold = int(input("Sold: "))
            stock = bought - sold

            cur.execute("INSERT INTO LIST (ITEM, BOUGHT, SOLD, STOCK) VALUES (?, ?, ?, ?)", (item, bought, sold, stock))
            
        db.commit()

    case 2:
        cursor = cur.execute ("SELECT * FROM LIST")

        for row in cursor:
            print ("---------------")
            print("ID: ", row[0])
            print("ITEMS: ", row[1])
            print("BOUGHT: ", row[2])
            print("SOLD: ", row[3])
            print("STOCK: ", row[2]-row[3])

        cur.close()

    case 3:
        x= input("Enter which want to delete (id/item)?: ")
        y= input("Enter id/item: ")
        query = f"DELETE from LIST where {x} = '{y}'"
        cur.execute(query)
        db.commit()

    case 4:
        a= input("Want to update bought or sold?: ")
        b= int(input("Enter new value: "))
        c= input("Which item you want to update?: ")
        query = f"UPDATE LIST set {a} = ? where ITEM = ?"
        cur.execute(query, (b, c))
        db.commit()

db.close()