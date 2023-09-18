# Copyright (c) 2023 Krzysztof Karczewski
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Hashable

ERRORS = [
    "Unknown error occured",
    "This operation is defined only for a set",
    "This operation is defined only for a family of sets",
    "The intersection is not defined for an empty family",
    "This operation is defined only for a relation",
    "This operation is defined only for a function",
    "The function is defined on its domain only",
    "The equivalence class is defined only for elements of domain"
    "This operation is defined only for an equivalence relation",
    "Found unhashable object that is not a set"
]

def _str_tuple(arg):
    result = ["("]
    for i in arg:
        if type(i) in [set, frozenset, MathSet]:
            result.append(str(MathSet(i)))
        elif type(i) is tuple:
            result.append(_str_tuple(i))
        else:
            result.append(str(i))
        result.append(", ")
    result.pop()
    return "".join(result + [")"])

class MathSetException(Exception):
    pass

class MathSet(set):
    def __init__(self, args = []):
        frozen_args = []
        for i in args:
            if type(i) in [set, MathSet]:
                frozen_args.append(frozenset(i))
            elif not isinstance(i, Hashable):
                raise MathSetException(ERRORS[9])
            else:
                frozen_args.append(i)
        super().__init__(frozen_args)

    def __str__(self):
        if self in [MathSet(), set(), frozenset()]:
            return "\u2205"
        result = ["{"]
        for i in self:
            if type(i) in [set, MathSet, frozenset]:
                result.append(str(MathSet(i)))
            elif type(i) is tuple:
                result.append(_str_tuple(i))
            else:
                result.append(str(i))
            result.append(", ")
        result.pop()
        return "".join(result + ["}"])

    # Private
    def __args_check(self, condition, error):
        if not condition:
            index = error if error in range(len(ERRORS)) else 0
            raise MathSetException(ERRORS[index])

    # Methods
    def is_empty(self):
        return self == MathSet()

    def is_subset(self, A):
        self.__args_check(type(A) in [set, frozenset, MathSet], 1)
        return self.issubset(MathSet(A))

    def is_family_of_sets(self):
        for i in self:
            if not isinstance(i, frozenset):
                return False
        return True

    def family_union(self):
        self.__args_check(self.is_family_of_sets(), 2)
        result = MathSet()
        for i in self:
            result = result.union(i)
        return result

    def power_set(self):
        n = len(self)
        binary = []
        for i in range(2**n):
            binary.append(bin(i)[2:].rjust(n, "0"))
        sequence = list(self)
        result = []
        for i in binary:
            subset = [sequence[j] for j in range(n) if i[j] == "1"]
            result.append(frozenset(subset))
        return MathSet(result)

    def cartesian_product(self, A):
        self.__args_check(type(A) in [set, frozenset, MathSet], 2)
        result = []
        for i in self:
            for j in A:
                result.append((i, j))
        return MathSet(result)

    def family_intersection(self):
        self.__args_check(not self.is_empty(), 3)
        self.__args_check(self.is_family_of_sets(), 2)
        sequence = list(self)
        result = set(sequence[0])
        for i in sequence[1:]:
            result = result.intersection(i)
            if result == set():
                return MathSet(result)
        return MathSet(result)

    def is_relation(self):
        for i in self:
            if isinstance(i, tuple):
                if not len(i) == 2:
                    return False
            else:
                return False
            return True

    def domain(self):
        self.__args_check(self.is_relation(), 4)
        result = []
        for (a, b) in self:
            result.append(a)
        return MathSet(result)

    def range(self):
        self.__args_check(self.is_relation(), 4)
        result = []
        for (a, b) in self:
            result.append(b)
        return MathSet(result)

    def image(self, A):
        self.__args_check(self.is_relation(), 4)
        self.__args_check(type(A) in [set, frozenset, MathSet], 1)
        result = []
        for (a, b) in self:
            if a in A:
                result.append(b)
        return MathSet(result)

    def is_function(self):
        if not self.is_relation():
            return False
        X = self.domain()
        for x in X:
            if len([b for (a, b) in self if a == x]) > 1:
                return False
        return True

    def restriction(self, A):
        self.__args_check(self.is_function(), 5)
        self.__args_check(type(A) in [set, frozenset, MathSet], 1)
        return MathSet((a, b) for (a, b) in self if a in A)

    def value(self, x):
        self.__args_check(self.is_function(), 5)
        self.__args_check(x in self.domain(), 6)
        for (a, b) in self:
            if a == x:
                return b

    def is_injection(self, X, Y):
        self.__args_check(self.is_function(), 5)
        self.__args_check(type(X) in [set, frozenset, MathSet], 1)
        self.__args_check(type(Y) in [set, frozenset, MathSet], 1)
        for y in Y:
            if len([a for (a, b) in self if b == y]) > 1:
                return False
        return True

    def is_surjection(self, X, Y):
        self.__args_check(self.is_function(), 5)
        self.__args_check(type(X) in [set, frozenset, MathSet], 1)
        self.__args_check(type(Y) in [set, frozenset, MathSet], 1)
        for y in Y:
            if not any(self.value(x) == y for x in X):
                return False
        return True

    def is_bijection(self, X, Y):
        self.__args_check(self.is_function(), 5)
        self.__args_check(type(X) in [set, frozenset, MathSet], 1)
        self.__args_check(type(Y) in [set, frozenset, MathSet], 1)
        return self.is_injection(X, Y) and self.is_surjection(X, Y)

    def inverse(self):
        self.__args_check(self.is_relation(), 4)
        return MathSet((b, a) for (a, b) in self)

    def is_reflective(self, A):
        self.__args_check(self.is_relation(), 4)
        self.__args_check(type(A) in [set, frozenset, MathSet], 1)
        for x in A:
            if not (x, x) in self:
                return False
        return True

    def is_symmetric(self, A):
        self.__args_check(self.is_relation(), 4)
        self.__args_check(type(A) in [set, frozenset, MathSet], 1)
        for (a, b) in self:
            if not (b, a) in self:
                return False
        return True

    def is_transitive(self, A):
        self.__args_check(self.is_relation(), 4)
        self.__args_check(type(A) in [set, frozenset, MathSet], 1)
        for (x, y) in self:
            for (a, b) in self:
                if y == b and not (x, b) in self:
                    return False
        return True

    def is_equivalence(self, A):
        self.__args_check(self.is_relation(), 4)
        self.__args_check(type(A) in [set, frozenset, MathSet], 1)
        conditions = [self.is_reflective(A),
                    self.is_symmetric(A),
                    self.is_transitive(A)]
        return all(conditions)

    def is_irreflective(self, A):
        self.__args_check(self.is_relation(), 4)
        self.__args_check(type(A) in [set, frozenset, MathSet], 1)
        for x in A:
            if (x, x) in self:
                return False
        return True

    def is_total(self, A):
        self.__args_check(self.is_relation(), 4)
        self.__args_check(type(A) in [set, frozenset, MathSet], 1)
        for i in A:
            for j in A:
                if i == j:
                    continue
                if not ((i, j) in self or (j, i) in self):
                    return False
        return True

    def is_antisymmetric(self, A):
        self.__args_check(self.is_relation(), 4)
        self.__args_check(type(A) in [set, frozenset, MathSet], 1)
        for (a, b) in self:
            if (b, a) in self and not a == b:
                return False
        return True

    def is_strict_linear_ordering(self, A):
        self.__args_check(self.is_relation(), 4)
        self.__args_check(type(A) in [set, frozenset, MathSet], 1)
        conditions = [self.is_irreflective(A),
                    self.is_transitive(A),
                    self.is_total(A)]
        return all(conditions)

    def equivalence_class(self, x):
        self.__args_check(self.is_relation(), 4)
        A = self.domain()
        self.__args_check(x in A, 7)
        self.__args_check(self.is_equivalence(A), 8)
        return MathSet(y for y in A if (x, y) in self)

    def quotient_set(self, A):
        self.__args_check(type(A) in [set, frozenset, MathSet], 1)
        self.__args_check(self.is_equivalence(A), 8)
        result = MathSet()
        used = set()
        for i in self:
            if i in used:
                continue
            current = A.equivalence_class(i)
            result.update({frozenset(current)})
            used = used.union(current)
        return result

    def is_partition(self, A):
        self.__args_check(self.is_family_of_sets(), 2)
        if not self.family_union() == A:
            return False
        for i in self:
            if i == MathSet():
                return False
            for j in self:
                if not i.isdisjoint(j) and not i == j:
                    return False
        return True
