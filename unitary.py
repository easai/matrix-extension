from sympy import Matrix, I, simplify, sqrt


class MatrixExt(Matrix):
    def is_normal(self):
        w, h = self.shape
        if w <= 0 or w != h:
            return False
        adj = self.adjoint()
        product = simplify(self.multiply(adj))
        product_inv = simplify(adj.multiply(self))
        return product == product_inv

    def is_unitary(self):
        if not self.is_normal():
            return False
        w, _ = self.shape
        adj = self.adjoint()
        product = simplify(self.multiply(adj))
        return  product == self.eye(w)


A = 1/2*MatrixExt([[1-I, 1+I], [1+I, 1-I]])
B=1/sqrt(2)*MatrixExt([[-I,1],[I,1]])

# Test 1
print(A.is_unitary())

# Test 2
print(A.is_normal())

# Test 3
print(A.adjoint().is_unitary())

# Test 4
print(B.is_unitary())

# Test 5
print(B.is_normal())
