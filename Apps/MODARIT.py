def h():
  print('egcd(a, b): (gcd(a, b), d, n)')
  print('mod(n, m): (remainder)')
  print('modinv(a, m): (remainder)')
  print('mmodinv(M, m): (M^(-1) mod m)^T')
def egcd(a, b):
    if a == 0: return (b, 0, 1)
    else: g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)
def mod(n, m): return n % m
def modinv(a, m):
    if a < 0: a = mod(a, m)
    g, x, y = egcd(a, m)
    if g != 1: raise Exception('modular inverse does not exist (gcd!=1)')
    return x % m
def mmodinv(M, m):
  M = Matrix(M)
  r, c = int(M._width), int(M._width)
  if not (r == c): print('Error: Non square matrix! exiting')
  det = M.determinant()
  detInv = modinv(det, m)
  adj = M.adjoint()._value
  invM = [[j*detInv for j in i] for i in adj]
  invMmod = [[j%m for j in i] for i in invM]
  return invMmod
class Matrix(object):
    def __init__(self, *rows):
        self._width = 0
        self._height = 0
        self._value = list()
        if rows:
            if len(rows) == 1 and type(rows[0]) == type(self):
                for row in rows[0].value:
                    newRow = list()
                    for item in row:
                        newRow.append(item)
                    self.addRow(*newRow)
            elif len(rows) == 1 and type(rows[0]) in (list, tuple) and \
                      type(rows[0][0]) in (list, tuple):
                for row in rows[0]:
                    newRow = list()
                    for item in row:
                        newRow.append(item)
                    self.addRow(*newRow)
            elif ((len(rows) == 2) and (type(rows[0]) in (list, tuple)) and (
                type(rows[1]) in (int,))):
                if (len(rows[0]) % rows[1]): raise ValueError('Invalid list length, must be a multiple of width argument')
                newRow = list()
                for i in range(len(rows[0])):
                    if (i and (not i % rows[1])):
                        self.addRow(*newRow)
                        newRow = list()
                    newRow.append(rows[0][i])
                self.addRow(*newRow)
            else:
                for row in rows:
                    if not (type(row) in (list, tuple)): raise TypeError("Constructor arguments must be of type 'list' or 'tuple'")
                    self.addRow(*row)
    def __getattr__(self, name):
        if name == 'width': return int(self._width)
        if name == 'height': return int(self._height)
        if name == 'value': return list(self._value)
        if name == 'size': return (int(self._width), int(self._height))
    def determinant(self):
        if not self._width == self._height: raise ValueError("Determinant is not defined for non-square matrix")
        if (self._height == 1 and self._width == 1): return self._value[0][0]
        returnvalue = 0
        for i in range(self._width):
            returnvalue += self._value[0][i] * ((-1) ** (0 + i)) * self.minor(0, i)
        return returnvalue
    def minor(self, i, j):
        m = Matrix(self)
        m.deleteRow(i)
        m.deleteColumn(j)
        return m.determinant()
    def deleteColumn(self, column):
        if (column >= self._width or column <= -self._width): raise IndexError('Invalid index, row %d does not exist' % column)
        returnvalue = list()
        self._width -= 1
        for row in self._value: returnvalue.append(row.pop(column))
        return returnvalue
    def deleteRow(self, row):
        if (row >= self._height or row <= -self.height): raise IndexError('Invalid index, row %d does not exist' % row)
        self._height -= 1
        return self._value.pop(row)
    def addRow(self, *row): self.insertRow(self._height, *row)
    def insertRow(self, index, *row):
        if ((len(row) == 1) and (type(row[0]) in (list, tuple))):
            row = row[0]
        if self._width:
            if not (len(row) == self._width): raise ValueError('Improper length for new row: %d, should be %d' % (len(row), self._width))
        else:
            self._width = len(row)
        self._height += 1
        newrow = list()
        for item in row:
            if not (type(item) in (int, float, complex)):
                message = "Values must be of type "
                for t in range(len(('int', 'float', 'complex'))):
                    if t:
                        message += ' or '
                    message += "'%s'" % ('int', 'float', 'complex')[t]
                raise TypeError(message)
            newrow.append(item)
        self._value.insert(index, newrow)
    def adjoint(self): return self.cofactorMatrix()
    def cofactorMatrix(self):
        returnvalue = Matrix()
        for i in range(self._height):
            newRow = list()
            for j in range(self._width):
                newRow.append(((-1) ** (i + j)) * self.minor(i, j))
            returnvalue.addRow(*newRow)
        return returnvalue