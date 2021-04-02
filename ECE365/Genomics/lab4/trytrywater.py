# %%
import numpy as np
import pandas as pd

# %%
df = pd.DataFrame({'a':[1,0,0,1,3],'b':[0,0,1,0,1],'c':[0,0,0,0,0]})

# %%
print(np.sum(df['b'] > 0))
# %%
