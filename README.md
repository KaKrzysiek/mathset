# mathset Python module

## TABLE OF CONTENTS

1) GENERAL INFO
2) REQUIREMENTS
3) USAGE
4) METHODS
5) EXAMPLES
6) ACKNOWLEDGEMENTS
7) ABOUT AUTHOR

## GENERAL INFO

mathset is an [open source](https://opensource.org/osd) Python module with MathSet class that inherits methods and properties from built-in class Set. The code is made available on terms of [*The Mozilla Public License Version 2.0*](https://www.mozilla.org/en-US/MPL/2.0/) described precisely in the LICENSE file. Due to limitations of modern computers, so far the module can handle only finite sets.

## REQUIREMENTS

I guarantee it works with Python 3.10.12 and later versions. However, fell free to test it with earlier versions. If you have any problems with the module on your computer, please contact me so I can fix the bug.

## USAGE

Call class constructor to create new object. It should be passed one iterable parameter, preferably a set or a list. If no parameter is passed, the empty set is created. Since sets are unhashable in Python, if you want to create family of sets, make sure you pass list of sets to the constructor.

#### **`main.py`**
```python
from mathset import MathSet
A = MathSet({1, 2, 3})
print(A)
B = MathSet()
print(B)
C = MathSet([A, B])
print(C)
```

```console
krzysiek@krzysiek:~/Documents$ ls
MathSet.py main.py
krzysiek@krzysiek:~/Documents$ python3 main.py
{1, 2, 3}
∅
{{1, 2, 3}, ∅}
krzysiek@krzysiek:~/Documents$
```

## METHODS

### MathSet.is_empty()

Returns true if the set is empty and false in any other case.

#### **`main.py`**
```python
from mathset import MathSet
A = MathSet()
print(A.is_empty())
```

```console
krzysiek@krzysiek:~/Documents$ ls
MathSet.py main.py
krzysiek@krzysiek:~/Documents$ python3 main.py
True
krzysiek@krzysiek:~/Documents$
```

### MathSet.is_subset()

Returns true if every element of the first set belongs to the second set.

#### **`main.py`**
```python
from mathset import MathSet
A = MathSet({1, 2, 3})
B = MathSet({2, 3})
C = MathSet({3, 4})
print(B.is_subset(A))
print(C.is_subset(A))
```

```console
krzysiek@krzysiek:~/Documents$ ls
MathSet.py main.py
krzysiek@krzysiek:~/Documents$ python3 main.py
True
False
krzysiek@krzysiek:~/Documents$
```

### MathSet.is_family_of_sets()

Returns true if every element of the set is a set itself.

### MathSet.family_union()

Returns union of all sets in the set. Note that the starting set must be a family of sets.

### MathSet.family_intersection()

Returns intersection of all sets in the set. Note that the starting set must be a non-empty family of sets.

#### **`main.py`**
```python
from mathset import MathSet
A = MathSet({1, 2, 3, 4})
B = MathSet({2, 3, 4, 5})
C = MathSet({2, 3})
D = MathSet([A, B, C])
print(D.is_family_of_sets(), B.is_family_of_sets())
print(D.family_union())
print(D.family_intersection())
```

```console
krzysiek@krzysiek:~/Documents$ ls
MathSet.py main.py
krzysiek@krzysiek:~/Documents$ python3 main.py
True False
{1, 2, 3, 4, 5}
{2, 3}
krzysiek@krzysiek:~/Documents$
```

### MathSet.power_set()

Returns family of all subsets of given set.

#### **`main.py`**
```python
from mathset import MathSet
A = MathSet({1, 2, 3})
B = A.power_set()
print(B)
```

```console
krzysiek@krzysiek:~/Documents$ ls
MathSet.py main.py
krzysiek@krzysiek:~/Documents$ python3 main.py
{{2}, {2, 3}, {1, 2}, {1, 2, 3}, {3}, {1}, ∅, {1, 3}}
krzysiek@krzysiek:~/Documents$
```

### MathSet.cartesian_product(A)

Returns cartesian product of the starting set and set A. As Python has built-in tuples, they are used as ordered pairs in this module.

### MathSet.is_relation()

Returns true if the set is a subset of cartesian product of some two sets.

### MathSet.domain()

Returns domain of the relation. Note that the starting set must be relation.

### MathSet.range()

Returns range of the relation. Note that the starting set must be relation.

#### **`main.py`**
```python
from mathset import MathSet
A = MathSet({0, 1, 2, 3, 4})
B = MathSet({-4, -3, -2, -1, 0, 1, 2, 3, 4})
C = A.cartesian_product(B)
R = MathSet([(a, b) for (a, b) in C if a == abs(b)])
print(R)
print(R.domain())
print(R.range())
```

```console
krzysiek@krzysiek:~/Documents$ ls
MathSet.py main.py
krzysiek@krzysiek:~/Documents$ python3 main.py
{(4, 4), (2, -2), (0, 0), (1, 1), (3, -3), (4, -4), (1, -1), (3, 3), (2, 2)}
{0, 1, 2, 3, 4}
{0, 1, 2, 3, 4, -1, -4, -3, -2}
krzysiek@krzysiek:~/Documents$
```

### MathSet.image(A)

When called on R set, returns image of A under R. Note that R must be relation.

### MathSet.is_function()

Returns true if the set is a function.

### MathSet.value(x)

When called on set f that is a function, returns y such that f(x) = y.

### MathSet.restriction(A)

When called on set f, that is a function from X to Y and A is a subset of X, the method returns restriction of f to A.

#### **`main.py`**
```python
from mathset import MathSet
A = MathSet(range(0, 101))
B = A.cartesian_product(A)
f = MathSet([(x, y) for (x, y) in B if y == x**2])
print(f.is_function())
print(f.image({1, 2, 3, 4}))
print(f.value(7))
g = f.restriction({0, 1, 2})
print(g)
```

```console
krzysiek@krzysiek:~/Documents$ ls
MathSet.py main.py
krzysiek@krzysiek:~/Documents$ python3 main.py
True
{16, 1, 4, 9}
49
{(1, 1), (2, 4), (0, 0)}
krzysiek@krzysiek:~/Documents$
```

### MathSet.is_injection(X, Y)

When called on set f, that is a function from X to Y, the method returns true if f is injection.

### MathSet.is_surjection(X, Y)

When called on set f, that is a function from X to Y, the method returns true if f is surjection.

### MathSet.is_bijection(X, Y)

When called on set f, that is a function from X to Y, the method returns true if f is bijection.

### MathSet.inverse()

When called on relation R, returns the inverse of R.

#### **`main.py`**
```python
from mathset import MathSet
A = MathSet(range(1, 13))
B = A.cartesian_product(A)
f = MathSet([(x, y) for (x, y) in B if x*y % 13 == 1])
print(f.is_injection(A, A))
print(f.is_surjection(A, A))
print(f.is_bijection(A, A))
g = f.inverse()
print(g.value(7))
```

```console
krzysiek@krzysiek:~/Documents$ ls
MathSet.py main.py
krzysiek@krzysiek:~/Documents$ python3 main.py
True
True
True
2
krzysiek@krzysiek:~/Documents$
```

*In this example, A is the multiplicative group of non-zero elements of field of integers modulo 13. f is bijection from A to A. Each element of A is paired with its multiplicative inverse.*

### MathSet.is_reflective(A)

When called on relation R, returns true if R is reflective relation on A.

### MathSet.is_symmetric(A)

When called on relation R, returns true if R is symmetric relation on A.

### MathSet.is_transitive(A)

When called on relation R, returns true if R is transitive relation on A.

### MathSet.is_equivalence(A)

When called on relation R, returns true if R equivalence relation relation on A.

#### **`main.py`**
```python
from mathset import MathSet
A = MathSet(range(-50, 51))
B = A.cartesian_product(A)
R = MathSet([(a, b) for (a, b) in B if a % 10 == b % 10])
print(R.is_reflective(A))
print(R.is_symmetric(A))
print(R.is_transitive(A))
print(R.is_equivalence(A))
print(R.equivalence_class(7))
```

```console
krzysiek@krzysiek:~/Documents$ ls
MathSet.py main.py
krzysiek@krzysiek:~/Documents$ python3 main.py
True
True
True
True
{37, 7, -23, 47, 17, -13, -43, 27, -3, -33}
krzysiek@krzysiek:~/Documents$
```

### MathSet.is_irreflective(A)

When called on relation R, returns true if R is irreflective relation on A.

### MathSet.is_total(A)

When called on relation R, returns true if R is total relation on A.

### MathSet.is_strict_linear_ordering(A)

When called on relation R, returns true if R is is strict linear ordering on A.

#### **`main.py`**
```python
from mathset import MathSet
A = MathSet(range(-10, 11))
B = A.cartesian_product(A)
R1 = MathSet([(a, b) for (a, b) in B if a < b])
R2 = MathSet([(a, b) for (a, b) in B if a <= b])
print(R1.is_strict_linear_ordering(A))
print(R2.is_strict_linear_ordering(A))
```

```console
krzysiek@krzysiek:~/Documents$ ls
MathSet.py main.py
krzysiek@krzysiek:~/Documents$ python3 main.py
True
False
krzysiek@krzysiek:~/Documents$
```

### MathSet.equivalence_class(x)

When called on equivalence relation R, returns equivalence class of element x.

### MathSet.quotients_set(A)

When called on R which is equivalence relation on A, returns quotient set A/R.

### MathSet.is_partition(A)

When called on family of sets B, returns true is B is partition of A.

#### **`main.py`**
```python
from mathset import MathSet
A = MathSet({0, 1, 2, 3, 4, 5})
B = MathSet([{0, 2, 4}, {1, 3, 5}])
C = A.power_set()
print(B.is_partition(A))
print(C.is_partition(A))
```

```console
krzysiek@krzysiek:~/Documents$ ls
MathSet.py main.py
krzysiek@krzysiek:~/Documents$ python3 main.py
True
False
krzysiek@krzysiek:~/Documents$
```

## EXAMPLES

#### **`main.py`**
```python
from mathset import MathSet

def natural_number(n):
	if n == 0:
		return MathSet()
	prev = natural_number(n - 1)
	singleton = MathSet([prev])
	return MathSet(prev.union(singleton))

for i in range(5):
	print(natural_number(i))
```

```console
krzysiek@krzysiek:~/Documents$ ls
MathSet.py main.py
krzysiek@krzysiek:~/Documents$ python3 main.py
∅
{∅}
{∅, {∅}}
{∅, {∅}, {∅, {∅}}}
{∅, {∅}, {∅, {∅}}, {∅, {∅}, {∅, {∅}}}}
krzysiek@krzysiek:~/Documents$
```

*Formal definition of natural numbers*

#### **`main.py`**
```python
from mathset import MathSet

a = lambda b, c : "R is " + c if b else "R is not " + c

A = MathSet({0, 1, 2})
B = A.power_set()
C = B.cartesian_product(B)
R = MathSet([(a, b) for (a, b) in C if MathSet(a).is_subset(b)])
print(a(R.is_reflective(B), "reflective"))
print(a(R.is_symmetric(B), "symmetric"))
print(a(R.is_transitive(B), "transitive"))
print(a(R.is_total(B), "total"))
print(a(R.is_antisymmetric(B), "antisymmetric"))
```

```console
krzysiek@krzysiek:~/Documents$ ls
MathSet.py main.py
krzysiek@krzysiek:~/Documents$ python3 main.py
R is reflective
R is not symmetric
R is transitive
R is not total
R is antisymmetric
krzysiek@krzysiek:~/Documents$
```

*Relation of inclusion is a partial order on the power set*

## ACKNOWLEDGEMENTS

The author thanks Aleksander Bąba for help in this project.

## ABOUT AUTHOR

My name is Krzysztof Karczewski. I am not a professional programmer and I have created this project, as well as the documentation, in my free time. If you want to contact me in the matter of the module or any other, send me an email please. You can find the address on the [homepage](https://kakrzysiek.github.io/mathset) of the mathset python module.
