from random import *

seed(8)

st_metov_na_polje5 = 0 # 0 1 ...100
sestevek_polj = 0 # 0 6 10 12
st_metov = 0 # 0 1  2 3

while st_metov_na_polje5 < 100:
    pain = randint(1, 6)
    sestevek_polj += pain
    if sestevek_polj % 6 == 5:
        st_metov_na_polje5 += 1
    st_metov += 1

print(st_metov)


# 10 % 5 = 0

# 0+2 = 2
# 2+3 = 5
# 4+ 4 = 8  ---- 3
# 5+6 =11 ---- 0
