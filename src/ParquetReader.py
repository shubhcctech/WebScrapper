import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import numpy as np


# Create a simple DataFrame
value = pd.DataFrame({'one':[-1,np.nan,2.5],
                      'two':['foo','bar','baz'],
                      'three':[True,False,True]},
                      index=list('123'))

# Write the DataFrame to a parquet file
table = pa.Table.from_pandas(value)
pq.write_table(table,'example.parquet')

# Read the parquet file
table2 = pq.read_table('files/mobiles.parquet')
df = table2.to_pandas()
print(df)
