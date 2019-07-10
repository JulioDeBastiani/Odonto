class RepoIndicacoes:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="3Ewu85B8bB",
            database="Odonto"
        )

    def insert(self, values):
        cursor = self.mydb.cursor()
        uid = str(uuid.uuid4())
        sql = 'INSERT INTO Indicacoes (Id, Descricao) VALUES (%s, %s)'
        val = (uid, *values)

        cursor.execute(sql, val)
        self.mydb.commit()

    def update(self, id, values):
        cursor = self.mydb.cursor()
        sql = 'UPDATE Indicacoes SET Descricao = %s WHERE Id = %s'
        val = (*values, str(id))

        cursor.execute(sql, val)
        self.mydb.commit()

    def delete(self, id):
        cursor = self.mydb.cursor()
        uid = str(uuid.uuid4())
        sql = f'DELETE FROM Indicacoes WHERE Id = {str(id)}'

        cursor.execute(sql)
        self.mydb.commit()