# Diamond Problem

## MRO(Method Resolution Order)


### C3 linearization
* a consistent extended precedence graph
* preservation of local precedence order, and fitting the monotonicity criterion.
```
class B(A)

mro(B) = [B, A]
```

```
class B(A1,A2,A3 ...)
mro(B) = [B] + merge(mro(A1), mro(A2), mro(A3) ..., [A1,A2,A3])
```

```
class A(O):pass
class B(O):pass
class C(O):pass
class E(A,B):pass
class F(B,C):pass
class G(E,F):pass

mro(E) = [E] + merge(mro(A), mro(B), [A,B])
       = [E] + merge([A,O], [B,O], [A,B])
       = [E,A] + merge([O], [B,O], [B])
       = [E,A,B] + merge([O], [O])
       = [E,A,B,O]

mro(F) = [F] + merge(mro(B), mro(C), [B,C])
       = [F] + merge([B,O], [C,O], [B,C])
       = [F,B] + merge([O], [C,O], [C])
       = [F,B,C] + merge([O], [O])
       = [F,B,C,O]

mro(G) = [G] + merge(mro[E], mro[F], [E,F])
       = [G] + merge([E,A,B,O], [F,B,C,O], [E,F])
       = [G,E] + merge([A,B,O], [F,B,C,O], [F])
       = [G,E,A] + merge([B,O], [F,B,C,O], [F])
       = [G,E,A,F] + merge([B,O], [B,C,O])
       = [G,E,A,F,B] + merge([O], [C,O])
       = [G,E,A,F,B,C] + merge([O], [O])
       = [G,E,A,F,B,C,O]
```