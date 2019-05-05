# Molecular Dynamics (分子动力学）

概览：利用分子的温度压强的参数，用牛顿第二定律的原理进行计算。
网站：
lammps.sandia.gov

units metal
boundary p p p # f f f

variable name stykle args

read_data "modal.data"

pair_style rebo #势能 每两个原子之间的相互作用
pair_coeff * * CH.airbo C C C C C C    #原子类一号，二号... 势能，把每一个值调出来   # 意味着所有原子 # C, H的意思是碳和氢

timestep ${dt}
 "# thermo

group myFix id 1:40 3241:3280 #不动的两头

compute
compute
...
variale
velocity   all create ${T_run} 11009988 mom yes rot yes

dump
fix

reset_timestep
dump
fix
minimize #把原子之间最开始的相互作用消除掉。
undump
unfix

NPT (？？？？)
nve: number, volumn, energy (nvt,nve,net都可以, 放的是不想变得值)