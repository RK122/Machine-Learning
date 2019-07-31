# numPy = scientific library/module 
import numpy as np

# array creation methods

# 1. np.array(list) -- converts a list into an array
a=np.array([1,2,3])
print(a)
print(type(a)) # type = numpy.ndarray
# var.ndim -- for the dimension of array
print(a.ndim)
# var.shape -- returns shape -- in 1-D returns col -- in 2-D reutuns (row,col)
print(a.shape)
# len(var) -- returns -- in 1-D col -- in 2-D rows
print(len(a))
# 2. 2-D array -- pass 2-D list
a=np.array([[1,2,3],[4,5,6]])
print(a)
print(a.ndim)
print(a.shape)
print(len(a))

# 3. np.arange(start,stop,step) -- creates a array containing no from start to stop-1 with a diff of step
a=np.arange(10)
print(a)

# 4. np.linspace(start,end,n) -- from start to end(inclusive) it will returns n numbers
# diff b/w each no is equal -- means no random no. 
a=np.linspace(0,1,7)
print(a)

# 5. np.ones((row,col)) -- matrix of ones 
# note tuple containing row & col
# type(each values) = float
a=np.ones((3,3))
print(a)
print(type(a[0][0]))
# var.astype(type_u_want) -- to convert a var in the type u want
print(a.astype(int)) # type(of all matrix values) = int

# 6. np.zeros((row,col)) -- matrix of zeros 
# note tuple containing row & col
# type(each values) = float
a=np.zeros((3,3))
print(a)

# 8. np.eye(size) -- identity matrix of given size (square matrix)
a=np.eye(3)
# eye(row,col) -- identity matrix of row , col
a=np.eye(3,2)
# np.diag(mat) -- returns diagonal of given matrix
print(np.diag(a))

# 9. np.diag(list) -- returns a diagonal mat -- all elements = 0 except diagonal elements -- diagonal elements = list elements
a=np.diag([1,2,3,4])
print(a)
print(np.diag(a)) # still returns diagonal of matrix a

# 10. np.random.rand(size_of_array) -- returns a array of given size -- with elements b/w 0 & 1
a=np.random.rand(4)
print(a)


# dtype -- it's same as type but in numpy


# indexing
 
# 1. array[index] -- for 1-D array
a=np.array([1,2,3])
print(a)
print(a[1])
# -ve indexing also works -- same as string
print(a[-1])

# 2. array[row][col]  or  array[row , col] -- for 2-D array
a=np.diag([1,2,3,4])
print(a[1][1])
print(a[1,1])
# -ve indexing also works -- same as string
print(a[-1][-1])

# 3. multiple indices accessing
a=np.array([1,2,3,4,5])
b=np.array([0,2,4])
print(a[b]) # every element of j = index of a -- one by one 

# slicing -- same as string
a=np.arange(10)
print(a)
a[5:] = np.arange(100,105) # from index = 5 to last -- elements will be replaced by 100 to 105 -- no. of elements should match on both side
print(a)


# mask method 
a=np.arange(1,11)
mask=(a%2==0) # now in mask all elements are even(indexes actually not elements)
print(a[mask])
# if we manipulate mask then same elements will also be modified in the original array
a[mask]=-1 # now all even = -1 
print(a) 
print(a[mask])


# for algebra -- do same as octave -- once u created numpy array -- then do all operations on that array same as octave -- without numpy
a=np.array([1,2,3,4])
print(a+1)
print(a**2)

# matrix multiplication
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])
print(a*b) # this will do elements wise multiplication
# for element wise multi -- *
# for real/normal product -- mat1.dot(mat2)
b=np.array([[1,2],[3,4],[5,6]])
print(a.dot(b)) # both matrix won't be change

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a>5) # true / false matrix

# to compare two arrays -- dimensions must be same
b=np.array([[1,1,3],[4,5,40],[70,80,9]])
print(a==b) # but this will return mat of true / false -- element wise checking
# np.array_equal(mat1,mat2) -- returns true if all elements are same else false 
print(np.array_equal(a,b)) 

# logical operations
a=np.array([1,1,0,0],dtype=bool) # means this means is now true/false mat
print(a) 
b=np.array([0,1,0,1],dtype=bool) 
# np.logical_or(a,b)
print(np.logical_or(a,b)) 
# np.logical_and(a,b)
print(np.logical_and(a,b))


# np.sin(mat) -- convert all values into their sins -- similary all triagnometric expression
# np.log(mat) -- convert all values into their log
# np.exp(mat) -- convert all values into their exp
# np.abs(mat) -- covert all values into their absolute value

# np.sum(mat)  or  mat.sum()  -- returns sum of elements -- for 1-D
a=np.array([1,1,1,1])
print(a.sum())
print(np.sum(a))
# for 2-D 
# mat.sum(axis=1) -- for row-wise multi
a=np.array([[1,2,3],[4,5,6]])
print(a.sum(axis=1))
# mat.sum(axis=0) -- for col-wise
print(a.sum(axis=0))

# mat.max() -- returns max element -- for both 1-D & 2-D
print(a.max())
# mat.min() -- returns min element -- for both 1-D & 2-D
print(a.min())
# mat.argmax() -- returns position of max element -- for both 1-D & 2-D -- 0th indexed position
print(a.argmax()) # position = 5
# mat.argmin() -- returns position of min element -- for both 1-D & 2-D -- 0th indexed position
print(a.argmin()) # position = 0
# use axis = 1 -- for row-wise
# use axis = 0 -- for col-wise



# np.all(array) -- returns true if all values > 0 
a=np.zeros((2,2))
print(np.all(a))
a=np.ones((2,2))
print(np.all(a))

# np.any(array) -- returns true if any of the values > 0 
a=np.zeros((2,2))
print(np.any(a))
a[0][0]=1
print(np.any(a))


# mat.T -- transpose -- only for matrix -- not for 1-D array
a=np.array([1,2,3,4])
print(a.T)
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a.T)



# broadcasting -- algebra of matrices of diff sizes

# 1. element wise addition -- mat1 + mat2 -- size must be same
# 2. element wise multi -- mat1 * mat2 -- size must be same

# 3. mat + 1-D array
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([10,20,30])
print(a+b)  # it will add b in all row of a 
# it is like -- first it will convert b's size equal to a -- with all rows = same = b -- now b & a have same dim -- so add

# 4. vector + 1-D array -- vector = 1-D array
a=np.array([1,2,3])
b=np.array([1,2,3])
# first we've to convert a into 2-D array -- for that we've to change its dim
# a[:,np.newaxis] -- to add one dim
print(a.shape)
a=a[:,np.newaxis]
print(a.shape)
# after 2-D -- now when we add a & b -- it will make sizes of both equal
# now a = mat & b = array -- so it's like 3rd pt now
print(a+b)


# np.tile(array/mat,(row,col)) -- it will replicate array/mat = row & col  times with replication of elements
a=np.tile([1,2,3],(3,1)) # make rows = 1*3 (all rows same as first row) & col = 3*1 
print(a) 
a=np.tile(a,(3,3)) # rows = 3*3 (every next 3 rows = first 3 rows) & col = 3*3 
print(a)


# mat.ravel() -- convert any-D array to 1-D array
b=a.ravel()
print(b)
# mat.flatten() -- does same 
print(a.flatten())

# mat.reshape(row,col) -- to change dim of mat to row,col -- row & col must be valid & that can fit
print(b.reshape(9,9))


# 3-D array -- (n,row,col) -- order -- n = no of mat & size of each mat = row * col
a=np.arange(4*3*2).reshape(4,3,2) # no. of mat = 4 with size = 3*2
print(a)
# a[n,row,col] -- to access nth index mat -- with rowth index & colth index element
print(a[1,1,1])


# sorting

# 1. np.sort(mat) -- it will return sorted mat not actually sort that
a=np.array([[5,4,6],[3,1,7]])
b=np.sort(a)
print(b)
# row-wise sorting -- np.sort(mat)  or np.sort(mat, axis=1)
b=np.sort(a,axis=1)
print(b)
# col-wise sorting -- np.sort(mat,axis=0)  
b=np.sort(a,axis=0)
print(b)

# 2. mat.sort(axis = 0/1) -- to actually sort
a.sort(axis=0)
print(a)

# 3. np.argsort(array) -- returns index array of sorted array
a=np.array([4,3,1,2])
b=np.argsort(a) # a is now sorted
print(b) 
print(a[b]) # to get sorted array
# use this only for array

# more ways to access and algebra
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print(a)

# mat[[r1,r2],:]   or   mat[[r1,r2]]  -- to access row r1 & r2 at a time
print(a[[0,2],:])
print(a[[0,2]])

# mat[:,c] -- to access a particular col
print(a[:,2])
# mat[:,[c1,c2]] -- to access multi col
print(a[:,[0,2]])

# mat[r1:r2] -- to access rows from r1 to r2 (both inclusive)
print(a[0:3])
print(a[1:5])
# if r1/r2 > total_rows -- NO ERRORS -- upto last row
print(a[2:10])

# mat[:,c1:c2] -- to access col from c1 to c2(exclusive) -- from c1 to c2-1 
print("hello")
print(a[:,1:2])
print(a[:,1:3])
print(a[:,0:4])
# if c1/c2 > total_cols -- NO ERRORS -- upto last col
print(a[:,1:10])

# mat[r1:r2,c1:c2] -- from rows r1 to r2 & cols c1 to c2
print(a[1:4,1:4])

# application
a[0]=np.array([70,80,90])
print(a)
a[:,1]=np.array([100,200,300,400,500])
print(a)

# np.c_[mat,col] -- to add a col in mat -- dim must match
print(np.c_[a,np.ones(5)]) # hstack -- adds after a
print(np.c_[np.ones(5),a]) # adds before a
print(np.c_[np.ones(5),a,np.ones(5)]) # we can add multiple cols also

# np.r_[mat,[[row]]] -- to add a row in mat -- dim must match
print(np.r_[a,[[10,20,30]]]) # vstack -- adds at bottom
print(np.r_[[[10,20,30]],a]) # adds at top
print(np.r_[[[10,20,30]],a,[[10,20,30]]]) # multiple rows addition

# np.insert(mat, col_no, n/col, axis=1) 
# if n is given -- then it will create a col of all n & add that col at given col_no
# if col is given -- add that col at given col_no
# all col after that will move right by one place
print(np.insert(a,1,10,axis=1))
print(np.insert(a,1,[1,2,3,4,5],axis=1))

# np.insert(mat, row_no, n/row, axis=0) -- same as above -- axis = 0 for row addition
print(np.insert(a,2,10,axis=0))
print(np.insert(a,1,[1,2,3],axis=0))

# basic algebra
a=np.array([[1,2,3],[4,5,6]])
print(a**2) # square of each element
print(1/a) # reciprocal of each element
print(a/5) # float division
print(a//5) # int division

# mat.prod() -- returns product of all elements
print(a.prod()) # product of all    
print(a.prod(axis=0)) # col-wise
print(a.prod(axis=1)) # row-wise

# mat.mean() -- returns mean of all elements
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a.mean())
print(a.mean(axis=0)) # col-wise
print(a.mean(axis=1)) # row-wise

# np.round(mat) -- 0 if value<=0.5 else 1 
a=np.array([0.1,0.499999,0.52,0.533929202,0.9,1.1,1.3,1.58,1.8,1.6,1.4])
print(np.round(a))

# to shuffle a mat 
m=5
a=np.random.randn(3,3,4,5)
# per=list(np.random.permutation(m))
# print(per)
# print(a[:,per])
a=np.max([1,3])
print(a)

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
