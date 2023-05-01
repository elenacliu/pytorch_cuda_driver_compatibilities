import sqlite3
import pandas as pd
from tqdm import tqdm


conn = sqlite3.connect("version.db")
cur = conn.cursor()

def create_table(table_name):
    if table_name == 'pytorch':
        cur.execute(f'CREATE TABLE {table_name}(pytorch, python, cuda, cudnn, sm)')

def insert_csv_to_table(table_name, csv_name):
    df = pd.read_csv(csv_name)
    data = []

    if table_name == 'pytorch':
        for index, row in tqdm(df.iterrows()):
            seg = row[0].split('-')
            pytorch_version = seg[1]
            seg = seg[2].split('_')
            python_version = seg[0][2:]
            cuda_version = seg[1][4:]
            cudnn_version = seg[2][5:]

            for sm in row[1].split(', '):
                sm_version = sm[3:]
                data.append((pytorch_version, python_version, cuda_version, cudnn_version, sm_version))
            print(data)
            cur.executemany(f"""
                INSERT INTO {table_name} VALUES
                    (?, ?, ?, ?, ?)
            """, data)
    
    conn.commit()
    
if __name__=='__main__':
    create_table('pytorch')
    insert_csv_to_table('pytorch', 'table.csv')