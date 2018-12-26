import numpy as np
import pandas as pd
# from pathlib import Path

# script_location = Path(__file__).absolute().parent
# file_location = script_location / 'input.csv'
# input_file = file_location.open()

file_location = 'input.csv'

df = pd.read_csv(file_location, sep = ',', header = None)
print('\n'.join([df.values[i][0] for i in (np.where(df == np.amax(df.values[:,1:]))[0])]))