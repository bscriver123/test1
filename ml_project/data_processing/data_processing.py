# Dummy data processing script
import pandas as pd
import pyarrow.parquet as pq

def read_data(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.parquet'):
        return pq.read_table(file_path).to_pandas()
    else:
        raise ValueError('Unsupported file format')
