
def relu(x):
    if x>0 : 
        return x 
    else :
        return 0 

def neuron(input,weights,bias):
    total = 0 


    for i in range(len(input)):
        total += weights[i] * input[i]


    total += bias
    return total 

input = [2,4]
weights = [0.5,-0.2]

bias = 0.1 

output = relu(neuron(input ,weights,bias))
print(output)

