# the data is false
R
RA = RB = RC = R1 = R2 = R
E

iB = i2
i1 = iB + iC
i1 = iA
i1 * R1 + iB * RB + i2 * R2 + RA * iA = E
iB * RB + i2 * R2 - iC * RC = 0

# which is

i1 * R1 + i2 * RB + i2 * R2 + RA * i1 = E
i2 * RB + i2 * R2 - (i1 - i2) * RC = 0

# which is

i1 * (R1 + RA) + i2 * (RB + R2) = E
i2 * (RB + R2 + RC) - i1 * RC = 0

i2 = i1 * RC / (RB + R2 + RC)
i1 * (R1 + RA) + i1 * RC * (RB + R2) / (RB + R2 + RC) = E
i1 * (R1 + RA + RC * (RB + R2) / (RB + R2 + RC)) = E
i1 = E/(R1 + RA + RC * (RB + R2) / (RB + R2 + RC))
