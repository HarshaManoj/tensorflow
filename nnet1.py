import tensorflow as tf
import numpy
from numpy import exp, array, random, dot
import matplotlib.pyplot as plt
rng = numpy.random
import operator

# In[2]:

# Parameters
learning_rate = 0.01
training_epochs = 1000
display_step = 50


# In[3]:

# Training Data
train_X = array([0.0,5.0,10.0,15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0,75.0,80.0,85.0,90.0])
train_Y = array([0.00, 0.08, 0.17, 0.25, 0.34, 0.42, 0.50, 0.57, 0.64, 0.70, 0.76, 0.81, 0.86, 0.90, 0.93, 0.96, 0.98, 0.99, 1.00])
n_samples = train_X.shape[0]


# In[4]:

# tf Graph Input
X = tf.placeholder("float")
Y = tf.placeholder('float')


# Set model weights
#W = tf.Variable(rng.randn(), name="weight")
#b = tf.Variable(rng.randn(), name="bias")

def neural_network_model(data):
    W1 = tf.Variable(rng.randn(), name="weight")
    b1 = tf.Variable(rng.randn(), name="bias")
    
    W2 = tf.Variable(rng.randn(), name="weight")
    b2 = tf.Variable(rng.randn(), name="bias")
    
    W3 = tf.Variable(rng.randn(), name="weight")
    b3 = tf.Variable(rng.randn(), name="bias")
    
    W = tf.Variable(rng.randn(), name="weight")
    b = tf.Variable(rng.randn(), name="bias")
    
    
    
    
    l1 = operator.add(operator.mul(data, W1), b1)
    l1 = tf.nn.relu(l1)
    
    l2 = operator.add(operator.mul(l1, W2), b2)
    l2 = tf.nn.relu(l2)
    
    l3 = operator.add(operator.mul(l2, W3), b3)
    l3 = tf.nn.relu(l3)
    
    output = operator.add(operator.mul(l3, W), b)
    
    return(output)
# In[5]:

# Construct a linear model
pred = neural_network_model(train_X)


# In[6]:

# Mean squared error
cost = tf.reduce_sum(tf.pow(pred - train_Y, 2))/(2*n_samples)
# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)


# In[7]:

# Initializing the variables
init = tf.global_variables_initializer()


# In[8]:

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        #Display logs per epoch step
        if (epoch+1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_X, Y:train_Y})
            print ("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c))

    print ("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
    print ("Training cost=", training_cost, '\n')

    ip = 45.1
    print (neural_network_model(ip))

    #Graphic display
    #plt.plot(train_X, train_Y, 'ro', label='Original data')
    #plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    #plt.legend()
    #plt.show()


# In[ ]:


#training_set_inputs = array([[0.0], [5.0], [10.0], [15.0], [20.0], [25.0], [30.0], [35.0], [40.0], [45.0], [50.0], [55.0], [60.0], [65.0], [70.0], [75.0], [80.0], [85.0], [90.0]])
#training_set_outputs = array([[0.0000, 0.0872, 0.1736, 0.2588, 0.3420, 0.4226, 0.5000, 0.5736, 0.6428, 0.7071, 0.7660, 0.8191, 0.8660, 0.9063, 0.9397, 0.9659, 0.9848, 0.9962, 1.0000]]).T
