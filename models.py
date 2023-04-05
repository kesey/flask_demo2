import sqlite3

class Destination:
    def __init__(self, title: str="", price: float=0.0, duration: str="5 Jours", resume: str="", include: tuple=(0, ), program: dict={"jour 1": 0}): # , include: str="", program: str=""):
        self.title = title
        self.price = price
        self.duration = duration
        self.resume = resume
        self.include = include
        self.program = program

class Bdd_interact:
    def __init__(self, bdd_name: str= "bdd"):
        self.bdd_name = bdd_name
        self.connect = sqlite3.connect(self.bdd_name)
        self.cursor = self.connect.cursor()

    def create_table(self, table_name: str= "default", fields:dict = {}):
        self.table_name = table_name
        self.fields = fields
        fields_str = ""
        i = 0
        for key, value in fields.items():
            fields_str += key + " " + value
            if not i == len(fields) - 1:
                fields_str += ", "
            i += 1
        sql_request = "CREATE TABLE IF NOT EXISTS " + table_name + "(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, " + fields_str + ")"
        try:
            self.cursor.execute(sql_request)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            raise e
    
    def get_item(self, table_name, item_id):
        self.cursor.execute("SELECT * FROM " + table_name + " WHERE id = ?", str(item_id))
        find_item = self.cursor.fetchone()
        return find_item

    def get_all_items(self, table_name):
        self.cursor.execute("SELECT * FROM " + table_name)
        item_list = self.cursor.fetchall()
        return item_list

    def add_item(self, table_name, item):
        fields_str = ""
        values_str = ""
        i = 0
        for field in self.fields.keys():
            fields_str += field
            values_str += "?"
            if not i == len(self.fields) - 1:
                fields_str += ","
                values_str += ","
            i += 1
        sql_request = "INSERT INTO " + table_name + " (" + fields_str + ") VALUES(" + values_str + ")"
        self.cursor.execute(sql_request, (item.title, item.price, item.duration, item.resume, item.include, item.program))
        self.connect.commit()
        return item
    
    def update_item(self, table_name, item):
        fields_str = ""
        i = 0
        for field in self.fields.keys():
            fields_str += field + " = ?"
            if not i == len(self.fields) - 1:
                fields_str += ", "
            i += 1
        sql_request = "UPDATE " + table_name + " SET" + fields_str + "WHERE id = ?"
        self.cursor.execute(sql_request, (item[1], item[2], item[3], item[4], item[5], item[0]))
        self.connect.commit()
        return item
        
    def delete_item(self, table_name, item_id):
        self.cursor.execute("DELETE FROM " + table_name + " WHERE id = ?", str(item_id))
        self.connect.commit()
    
    def delete_table(self, table_name):
        self.cursor.execute("DROP TABLE " + table_name)
        self.connect.commit()