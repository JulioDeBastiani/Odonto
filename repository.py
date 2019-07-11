import mysql.connector

class Repository:
    def __init__(self, table_name):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="3Ewu85B8bB",
            database="Odonto"
        )
        self.table_name = table_name

    def get_next_id(self):
        cursor = self.mydb.cursor()
        sql = f'SELECT MAX(Id) FROM {self.table_name}'
        cursor.execute(sql)
        res = cursor.fetchone()[0]
        return int(res) + 1 if res != None else 1

    def get_by_id(self, id):
        cursor = self.mydb.cursor()
        sql = f'SELECT * FROM {self.table_name} WHERE Id = {id}'
        cursor.execute(sql)
        return cursor.fetchone()

    def get_all(self, columns):
        cursor = self.mydb.cursor()
        conjunction = ''
        scolumns = ''

        for column in columns:
            scolumns = scolumns + conjunction + column
            conjunction = ', '

        sql = f'SELECT {scolumns} FROM {self.table_name}'
        cursor.execute(sql)
        return cursor.fetchall()

    def get_where(self, columns, values_dict):
        cursor = self.mydb.cursor()
        conjunction = ''
        scolumns = ''

        for column in columns:
            scolumns = scolumns + conjunction + column
            conjunction = ', '

        conjunction = ''
        where = ''

        for key, value in values_dict.items():
            where = where + conjunction + f'{key} LIKE \'%{value}%\''
            conjunction = ' AND '

        sql = f'SELECT {scolumns} FROM {self.table_name} WHERE {where}'
        cursor.execute(sql)
        return cursor.fetchall()

    def insert(self, values_dict):
        cursor = self.mydb.cursor()
        id = self.get_next_id()
        fields = 'Id'
        values_str = '%s'

        for field in values_dict.keys():
            fields = fields + ', ' + field
            values_str = values_str + ', %s'

        values = list(values_dict.values())
        values.insert(0, id)

        sql = f'INSERT INTO {self.table_name} ({fields}) VALUES ({values_str})'
        cursor.execute(sql, values)
        self.mydb.commit()

    def update(self, id, values_dict):
        cursor = self.mydb.cursor()
        clauses = ''
        conjunction = ''

        for field in values_dict.keys():
            clauses = clauses + conjunction + field + ' = %s'
            conjunction = ', '

        sql = f'UPDATE {self.table_name} SET {clauses} WHERE Id = {id}'
        print(sql)
        print(list(values_dict.values()))
        cursor.execute(sql, list(values_dict.values()))
        self.mydb.commit()

    def delete(self, id):
        cursor = self.mydb.cursor()
        sql = f'DELETE FROM {self.table_name} WHERE Id = {str(id)}'

        cursor.execute(sql)
        self.mydb.commit()
