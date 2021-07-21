import pandas as pd
from flask import jsonify
import sqlite3
class DB:
    def __init__(self):
        self.con = sqlite3.connect('Database.db')
        self.cursor = self.con.cursor()

    def add_csv_vacinas(self,data):
        df = pd.read_csv(data)
        df.to_sql('dados', self.con,index_label='id',if_exists='replace')
        self.con.commit()
    
    def add_csv_type_vaccine(self,data):
        df = pd.read_csv(data)
        df.to_sql('tipes',self.con,index_label='id',if_exists='replace')
        self.con.commit()
    
    def add_csv_cases_covid(self,data):
        df = pd.read_csv(data)
        df.to_sql('cases',self.con,index_label='id',if_exists='replace')
        self.con.commit()

    def all_data(self,table):
        headers = self.get_headers(table)
        data = self.cursor.execute(f'Select * from {table}')
        result = [dict(zip(headers,row)) for row in data.fetchall()]
        return jsonify(result)                

    def get_country(self,country_ISO,table):
        headers = self.get_headers(table)
        data = self.cursor.execute(f'SELECT * FROM {table} WHERE iso_code = ?',(country_ISO,))
        result = [dict(zip(headers,row)) for row in data.fetchall()]
        return jsonify(result)
        
    def get_by_country_name(self,country_name,table):
        headers = self.get_headers(table)
        if table == 'dados' or table=='cases':
            data = self.cursor.execute(f'SELECT * FROM {table} WHERE country = ?',(country_name,))
        else:
            data = self.cursor.execute(f'SELECT * FROM {table} WHERE location = ?',(country_name,))
        result = [dict(zip(headers,row)) for row in data.fetchall()]
        return jsonify(result)
    
    def get_headers(self,table):
        columns = self.cursor.execute(f'PRAGMA table_info({table})')
        col = columns.fetchall()
        valores = []
        for i in col:
            valores.append(i[1])
        return valores
    def get_by_attribute(self,attribute,result):
        vaccine_daily = [x[attribute] for x in result]
        index_of_vaccine = vaccine_daily.index(max(vaccine_daily))
    def get_by_date(self,table,date):
        headers = self.get_headers(table)
        att = ['people_vaccinated','people_fully_vaccinated','daily_vaccinations','total_vaccinations_per_hundred','people_vaccinated_per_hundred','people_fully_vaccinated_per_hundred']
        retorno = []
        data = self.cursor.execute(f'select * from {table} where date = ? ',(date,))
        result = [dict(zip(headers,row)) for row in data.fetchall()]
        for at in att:
            retorno.append({at:self.get_by_attribute(at,result)})
        return jsonify(retorno)        
