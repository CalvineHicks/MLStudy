import numpy

def experiment1():
    return numpy.random.normal(5, 1)
def experiment2():
    return numpy.random.normal(5.3, 1)
def experiment3():
    return numpy.random.normal(4, 1)

def customExperiment(mean, sigma):
     return numpy.random.normal(mean, sigma)

#populate initial values
arr1 = []
arr2 = []
arr3 = []
result = [0, 0, 0]

for i in range(3):
    arr1.append(experiment1())
    arr2.append(experiment2())
    arr3.append(experiment3())

#experiment a number of times
#could DEFINITELY be optimized (store total additive val, number of arr elements, etc)
for i in range(500):
    arr1Mean = numpy.mean(arr1)
    arr2Mean = numpy.mean(arr2)
    arr3Mean = numpy.mean(arr3)

    arr1Sigma = numpy.std(arr1)
    arr2Sigma = numpy.std(arr2)
    arr3Sigma = numpy.std(arr3)

    val1 = customExperiment(arr1Mean, arr1Sigma)
    val2 = customExperiment(arr2Mean, arr2Sigma)
    val3 = customExperiment(arr3Mean, arr3Sigma)

    maxVal = numpy.amax([val1, val2, val3])
    
    if maxVal == val1:
        arr1.append(experiment1())
        result[0] = result[0] + 1
        print('EXPERIMENT 1 maxVal value was: ', val1)
    if maxVal == val2:
        arr2.append(experiment2())
        result[1] = result[1] + 1
        print('EXPERIMENT 2 maxVal value was: ', val2)
    if maxVal == val3:
        arr3.append(experiment3())
        result[2] = result[2] + 1
        print('EXPERIMENT 3 maxVal value was: ', val3)

print("result was: ", result)
print("max was: ", numpy.amax(result))