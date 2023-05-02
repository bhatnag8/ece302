import numpy as np
import matplotlib.pyplot as plt
import math


def question1():
    print("=================================")
    print("Question 1 : ")
    print("Generating 5000 samples of zero-mean, unit-variance Gaussian random variable.")
    samples = np.random.normal(0, 1, 5000)
    total = 0
    for i in samples:
        total += i

    mean = total / 5000
    plt.hist(samples, 30, density=True, label='Samples')
    var = "The mean for this random set is " + str(mean)
    plt.axvline(x=mean, color='red', linestyle='--', label=var)
    plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc='lower left', ncols=1, mode="expand", borderaxespad=0.)
    plt.ylabel('f(X)')
    plt.xlabel('X')
    plt.show()
    return samples


def question2():
    print("=================================")
    print("Question 2 : ")
    print("Generating 50, 100, 1000, and 5000 samples of a uniform random variable on the interval [−1, 1].")
    samples_50 = np.random.uniform(-1, 1, 50)
    samples_100 = np.random.uniform(-1, 1, 100)
    samples_1000 = np.random.uniform(-1, 1, 1000)
    samples_5000 = np.random.uniform(-1, 1, 5000)
    c50 = samples_50
    c100 = samples_100
    c1000 = samples_1000
    c5000 = samples_5000
    sum50, sum100, sum1000, sum5000 = 0, 0, 0, 0

    for i in range(50):
        c50[i] = math.tan(math.pi * samples_50[i])
        sum50 += c50[i]

    for i in range(100):
        c100[i] = math.tan(math.pi * samples_100[i])
        sum100 += c100[i]

    for i in range(1000):
        c1000[i] = math.tan(math.pi * samples_1000[i])
        sum1000 += c1000[i]

    for i in range(5000):
        c5000[i] = math.tan(math.pi * samples_5000[i])
        sum5000 += c5000[i]

    mean50 = sum50 / 50
    mean100 = sum100 / 100
    mean1000 = sum1000 / 1000
    mean5000 = sum5000 / 5000

    plt.figure(figsize=(11.5, 8.5))
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    plt.subplot(2, 2, 1)
    plt.hist(c50, 15, density=True, label='50 Samples')
    var50 = "The mean for 50 is " + str(mean50)
    plt.axvline(x=mean50, color='red', linestyle='--', label=var50)
    plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc='lower left', ncols=1, mode="expand", borderaxespad=0.)
    plt.ylabel('C(U)')
    plt.xlabel('U, n=50')

    plt.subplot(2, 2, 2)
    plt.hist(c100, 15, density=True, label='100 Samples')
    var100 = "The mean for 100 is " + str(mean100)
    plt.axvline(x=mean100, color='red', linestyle='--', label=var100)
    plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc='lower left', ncols=1, mode="expand", borderaxespad=0.)
    plt.ylabel('C(U)')
    plt.xlabel('U, n=100')

    plt.subplot(2, 2, 3)
    plt.hist(c1000, 15, density=True, label='1000 Samples')
    var1000 = "The mean for 1000 is " + str(mean1000)
    plt.axvline(x=mean1000, color='red', linestyle='--', label=var1000)
    plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc='lower left', ncols=1, mode="expand", borderaxespad=0.)
    plt.ylabel('C(U)')
    plt.xlabel('U, n=1000')

    plt.subplot(2, 2, 4)
    plt.hist(c5000, 15, density=True, label='5000 Samples')
    var5000 = "The mean for 5000 is " + str(mean5000)
    plt.axvline(x=mean5000, color='red', linestyle='--', label=var5000)
    plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc='lower left', ncols=1, mode="expand", borderaxespad=0.)
    plt.ylabel('C(U)')
    plt.xlabel('U, n=5000')

    plt.show()


def question3(samples):
    print("=================================")
    print("Question 3 : ")
    print("Generating 5000 samples of a zero-mean, unit-variance Gaussian random variable.")
    y_samples = np.random.normal(0, 1, 5000)
    z_50 = [0] * 50
    z_100 = [0] * 100
    z_1000 = [0] * 1000
    z_5000 = [0] * 5000
    sum50, sum100, sum1000, sum5000 = 0, 0, 0, 0

    for i in range(50):
        z_50[i] = samples[i] / y_samples[i]
        sum50 += z_50[i]

    for i in range(100):
        z_100[i] = samples[i] / y_samples[i]
        sum100 += z_100[i]

    for i in range(1000):
        z_1000[i] = samples[i] / y_samples[i]
        sum1000 += z_1000[i]

    for i in range(5000):
        z_5000[i] = samples[i] / y_samples[i]
        sum5000 += z_5000[i]

    mean50 = sum50 / 50
    mean100 = sum100 / 100
    mean1000 = sum1000 / 1000
    mean5000 = sum5000 / 5000

    plt.figure(figsize=(11.5, 8.5))
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    plt.subplot(2, 2, 1)
    plt.hist(z_50, 15, density=True, label='50 Samples')
    var50 = "The mean for 50 is " + str(mean50)
    plt.axvline(x=mean50, color='red', linestyle='--', label=var50)
    plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc='lower left', ncols=1, mode="expand", borderaxespad=0.)
    plt.ylabel('Z(n)')
    plt.xlabel('n, n=50')

    plt.subplot(2, 2, 2)
    plt.hist(z_100, 15, density=True, label='100 Samples')
    var100 = "The mean for 100 is " + str(mean100)
    plt.axvline(x=mean100, color='red', linestyle='--', label=var100)
    plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc='lower left', ncols=1, mode="expand", borderaxespad=0.)
    plt.ylabel('Z(n)')
    plt.xlabel('n, n=100')

    plt.subplot(2, 2, 3)
    plt.hist(z_1000, 15, density=True, label='1000 Samples')
    var1000 = "The mean for 1000 is " + str(mean1000)
    plt.axvline(x=mean1000, color='red', linestyle='--', label=var1000)
    plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc='lower left', ncols=1, mode="expand", borderaxespad=0.)
    plt.ylabel('Z(n)')
    plt.xlabel('n, n=1000')

    plt.subplot(2, 2, 4)
    plt.hist(z_5000, 15, density=True, label='5000 Samples')
    var5000 = "The mean for 5000 is " + str(mean5000)
    plt.axvline(x=mean5000, color='red', linestyle='--', label=var5000)
    plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc='lower left', ncols=1, mode="expand", borderaxespad=0.)
    plt.ylabel('Z(n)')
    plt.xlabel('n, n=5000')

    plt.show()

    return


if __name__ == '__main__':
    samples_q1 = question1()
    question2()
    question3(samples_q1)

