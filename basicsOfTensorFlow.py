import tensorflow as tf

n1=tf.constant(3.0,tf.float32)
n2=tf.constant(4.0,tf.float32)
print(n1,n2) # only address or refrence type something will be print -- not the values

# do all operations in a Session -- tf.Session  or  tf.compat.v1.Session
sess=tf.compat.v1.Session()
print(sess.run([n1,n2])) # we can give only one argument inside run , so give it as list/tuple/string/set
sess.close() # we've to close session after the use

# another method of creating session
with tf.compat.v1.Session() as sess:
    print(sess.run((n1,n2)))
# no need to close 

n3=n1*n2
sess=tf.Session()
print(sess.run((n3)))
sess.close()

# placeholder -- no need to initialize -- just declare -- later assign the value
x=tf.placeholder(tf.float32)
y=tf.placeholder(tf.float32)
z=x+y # z= python variable -- no error when assigning it to placeholder
sess=tf.Session()
print(sess.run(z,{x:[1,5],y:[6,7]}))
sess.close()

# variables -- we've to initialize them
w=tf.Variable([.3],tf.float32)
b=tf.Variable([-.2],tf.float32)

x=tf.placeholder(tf.float32)

linear_model=w*x+b

y=tf.placeholder(tf.float32)

# computing cost
squared_error= tf.square(linear_model-y)
cost=tf.reduce_sum(squared_error)

init = tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)
print(sess.run(cost,{x:[1,2,3,4],y:[0,1,1,0]}))
print(sess.run([w,b]))
sess.close()

# above cost is not optimized 
# linear regression using Tensorflow
# optimizer=tf.train.GradientDescentOptimizer(learning_rate) -- inbuilt fn
# train=optimizer.minimize(cost) 
w=tf.Variable([.3],tf.float32)
b=tf.Variable([-.2],tf.float32)

x=tf.placeholder(tf.float32)

linear_model=w*x+b

y=tf.placeholder(tf.float32)

# computing cost
squared_error= tf.square(linear_model-y)
cost=tf.reduce_sum(squared_error)

optimizer=tf.train.GradientDescentOptimizer(0.01)
training=optimizer.minimize(cost)

init = tf.global_variables_initializer()

sess=tf.Session()
sess.run(init)
for i in range(1000):
    sess.run(training,{x:[1,2,3,4],y:[0,1,1,0]})
# print(sess.run([cost]))
print(sess.run([w,b]))
sess.close()