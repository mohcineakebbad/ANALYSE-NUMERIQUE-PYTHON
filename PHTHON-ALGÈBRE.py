import numpy as np
#A- Prise en main des matrices
A=np.array([[2,1,1],[1,3,2],[3,2,4]])
b=np.array([[110],[160],[240]])
print("Dimension=",np.shape(A))
print("Dimension=",np.shape(b))
print("La transposé de la matrice A est:",A.T)
print("la deuxieme ligne de A ",A[1])
print("la troisième colonne de A",A[:,2])
print("le coficient a23",A[1][2])
print("A+tr(A)",A+A.T)
print("2*A=",2*A)
print("A*tr(A)",A@A.T)
#B-Déterminant et inversibilité
det=np.linalg.det(A)
print("le determinant de A:",det)
if det==0:
    print("A est non invessible")
else:
    print("A est inverssible")
    Inv=np.linalg.inv(A)
    print("l'inverse de A est :",Inv)
    print("A*inv(A)",A@Inv)
# C-la résolution du système linéaire
X=Inv@b
print("la solution du système linéaire A*X=b est X=",X)
Y=np.linalg.solve(A,b)
print("la solutin par numpy est X=",Y)
print(np.allclose(X,Y))
AX=A@X
print("AX=",AX)
r=AX-b
print("le résidu",r)
print("la norme de r",np.linalg.norm(r))
# D- Que se passe-t-il si la matrice est singulière ?
C=np.array([[1,2,3],[2,4,6],[1,1,2]])
d=np.array([[1],[2],[3]])
detC=np.linalg.det(C)
print("det(C)=",detC)
print("Alors la matrice est non inversible")
try:
    print("l'invese de C est:",np.linalg.inv(C))
except np.linalg.LinAlgError:
    print("il n'y pas d'invese pur ce matrice ")
try:
    print("la solution deCX=d est:",np.linalg.solve(C,d))
except:
    print("il est impossible de résoudre ce système")

print("on observe que la deuxième ligne est deux fois de la première L2=2L1 alors C est singulière ce qui expique le résulatat")
#E-Petit programme réutilisable
def analyser_systeme(A, b):
    detA=np.linalg.det(A)
    if detA!=0:
        print("la matrice est inversible")
        print("l'inverse de la matrice est:",np.linalg.inv(A))
        X=np.linalg.solve(A, b)
        print("la solution du système",X)
        r=A@X-b
        print("le résidu")
        print(r)
        print("la norme de r",np.linalg.norm(r))

    else:
        print("la matrice est non inversible")
analyser_systeme(A, b)




