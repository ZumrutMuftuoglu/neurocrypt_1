# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:50:58 2019

@author: User
"""

#2 TPM oluşturduk
import time
import sys

#Machine parameters
k = 3
n = 4
d = 6

#Update rule
rule = ['hebbian']
rule = rule[0]

#Create 2 machines : Alice and Bob.
print("Creating machines : k=" + str(k) + ", n=" + str(n) + ", d=" + str(n))
print("Using " + rule + " update rule.")
Alice = Machine(k, n, d)
Bob = Machine(k, n, d)
#Eve = Machine(k, n, d)

#Random number generator
def random():
    return np.random.randint(-d, d + 1, [k, n])
    
#Function to evaluate the synchronization score between two machines.
def sync_score(m1, m2):
    return 1.0 - np.average(1.0 * np.abs(m1.W - m2.W)/(2 * d))

#Synchronize weights

sync = False # Flag to check if weights are sync
nb_updates = 0 # Update counter
nb_eve_updates = 0 # To count the number of times eve updated
start_time = time.time() # Start time
sync_history = [] # to store the sync score after every update

while(not sync):

    X = random() # Create random vector of dimensions [k, n]

    tauA = Alice(X) # Get output from Alice
    tauB = Bob(X) # Get output from Bob
#    tauE = Eve(X) # Get output from Eve

    Alice.update(tauB, rule) # Update Alice with Bob's output
    Bob.update(tauA, rule) # Update Bob with Alice's output

    #Eve would update only if tauA = tauB = tauE
    if tauA == tauB :
#        Eve.update(tauA, rule)
        nb_eve_updates += 1

    nb_updates += 1

    score = 100 * sync_score(Alice, Bob) # Calculate the synchronization of the 2 machines

    sync_history.append(score) # Add sync score to history, so that we can plot a graph later.

    sys.stdout.write('\r' + "Synchronization = " + str(int(score)) + "%   /  Updates = " + str(nb_updates) ) 
    if score == 100: # If synchronization score is 100%, set sync flag = True
        sync = True

end_time = time.time()
time_taken = end_time - start_time # Calculate time taken

#Print results
print ('\nMachines have been synchronized.')
print ('Time taken = ' + str(time_taken)+ " seconds.")
print ('Updates = ' + str(nb_updates) + ".")
print(X)
#print(tauA)#sonradan yazdım
#print (tauB)#sonradan yazdım
#print( nb_updates)#sonradan yazdım

print(np.average)


#Plot graph 
import matplotlib.pyplot as mpl
mpl.plot(sync_history)
mpl.show()

