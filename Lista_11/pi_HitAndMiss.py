#%%
import random
random.seed(55)
N :int = 20000000000
def pit(N):
    nHits=0
    for i in range(N):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if x**2+y**2 < 1:
            nHits+=1
    return nHits
pi = 4*pit(N)/N
print(f"{pi}")

# %%
