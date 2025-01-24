from gsdc import Box, Mol, Pot
import time

if __name__ == "__main__":
    m1 = m2 = 5
    n1 = 3
    n2 = 5
    p1 = p2 = 6
    p = p1//2
    script = f"(X)1(A){m1//2}[(S){n1}](A){m1//2}((B){m2//2+1}[(C){n2}](B){m2//2}(A){m1//2+1}[(S){n1}](A){m1//2}){p-1}(B){m2//2+1}[(C){n2}](B){m2//2}(L)1(A){m2//2}[(S){n1}](A){m2//2}((B){m2//2+1}[(C){n2}](B){m2//2}(A){m1//2+1}[(S){n1}](A){m1//2}){p-1}(B){m1//2+1}[(C){n2}](B){m1//2-1}(E)1"
    mol = Mol(script)
    box = Box(2000.0, 2000.0, 2000.0)
    pot = Pot(box)
    # pot.add(mol)
    # pot.add_bead("B")
    t1 = time.time()
    for _ in range(24000):
        pot.add_bead('B')
    pot.brew()
    t2 = time.time()
    # print(pot.types)
    # print(pot.coords)
    # print(len(pot.coords))
    print(t2-t1)