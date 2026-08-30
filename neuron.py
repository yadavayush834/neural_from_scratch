
def relu(x):
    if x>0 : 
        return x 
    else :
        return 0 




def layer(inputs, weights, biases):
    outputs = []

    for i in range(len(weights)):
        total = 0

        for j in range(len(inputs)):
            total += inputs[j] * weights[i][j]

        total += biases[i]

        outputs.append(relu(total))

    return outputs

inputs = [2, 3]

weights = [
    [0.5, -0.2],   
    [0.1, 0.4],    
    [-0.3, 0.8]    
]

biases = [0.1, 0.2, -0.1]

outputs = layer(inputs, weights, biases)

print(outputs)