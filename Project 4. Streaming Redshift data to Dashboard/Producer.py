import pandas as pd
from sqlalchemy import create_engine
import time
import json

connstr = 'redshift+psycopg2://user_name:password@redshift-cluster-1.cccg7kqejxio.us-east-1.redshift.amazonaws.com:5439/dev'

engine = create_engine(connstr) 
with engine.connect() as conn, conn.begin():
   df = pd.read_sql("select * from <your_table_name>", conn)

file_dict = df.to_dict('index')

n = 0
b = 10
for i in file_dict.values():
    with open(r"your_path\json_file.txt", "a") as f:
        f.write(json.dumps(i)+"\n")
    n+=1
    if n == b:
        b+=10
        time.sleep(1)
    else:
        continue