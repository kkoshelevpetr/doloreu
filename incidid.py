import numpy as np

# Create new column based on color condition using np.where
df['ModifiedColor'] = np.where(df['Color'] == 'Red', '#' + df['Color'], df['Color'])

print(df)
