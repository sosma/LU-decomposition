import numpy as np
# laskee mielivaltaiselle matriisille A LU-hajotelman matriisit L ja U
def LU(A):
    N = len(A)
    L = np.zeros([N, N])
    U = np.zeros([N, N])
    # käydään matriisin rivit ja sarakkeet läpi, siten että ratkaistaan vasemmasta yläkulmasta alaspäin arvoja
    for i in range(N):
        for k in range(i, N):
            for j in range(i, N):
                Utotal = 0;
                # aloitetaan U matriisin arvosta, koska niiden arvoja tarvitaan U matriisissa
                for j in range(i):
                    Utotal += L[i, j]*U[j, k]
                U[i,k] = A[i, k] - Utotal
                #tiedetään että L matriisissa on arvo 1 aina kun rivin ja sarakkeen arvo on sama
                if (i==k):
                    L[i, k] = 1
                #käytetään aiemmin ratkaistuja U matriisin arvoja ratkaisemaan L matriisin arvot
                else:
                    Ltotal = 0;
                    for j in range(i):
                        Ltotal += L[k, j] * U[j, i]
                    L[k,i] = (A[k, i] - Ltotal)/U[i][i]
    return L, U
A = np.array([[2, -1, -2], [-4, 6, 3], [-4, -2, 8]])
print(A)
"""
käytetty A matriisi
[[2, -1, -2]
 [-4, 6, 3]
 [-4, -2, 8]]
"""
L, U = LU(A)

print(L)
"""
saatu L matriisi
[[ 1.  0.  0.]
 [-2.  1.  0.]
 [-2. -1.  1.]]

"""
print(U)
"""
saatu U matriisi
[[ 2. -1. -2.]
 [ 0.  4. -1.]
 [ 0.  0.  3.]]
"""
