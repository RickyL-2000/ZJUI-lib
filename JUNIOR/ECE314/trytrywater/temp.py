mu_air = {}
besp = viscosity_data.split(',')
besp1 = []
besp1 = besp[1:]
mu_air['C'] = besp1[0]
mu_air['T_0'] = besp1[1]
mu_air['mu_0'] = besp1[2]

# %%
s = "12345"
translator = str.maketrans()

# %%
in_table = 'ab'
out_table = '12'
other_table = 'yz'  # ord('y')=121, ord('z')=122
trans_table = str.maketrans(in_table, out_table, other_table)
trans_table

# %%
a = {}
set.union()