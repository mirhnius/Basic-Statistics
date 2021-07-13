import numpy as np

def my_kappa(n_sample, student_id):
    digits = np.array([int(d) for d in str(student_id)])
    c1 = np.random.normal(loc=0, scale=digits[1]+1.0, size=n_sample)
    c2 = np.random.laplace(loc=digits[2]+5, scale=digits[3]*0.3, size=n_sample)
    c3 = np.random.laplace(loc=-digits[2]-5, scale=digits[5]*0.3, size=n_sample)
    res = []
    for i in range(n_sample):
        res.append(
            np.random.choice([c1[i], c2[i], c3[i]])
        )

    return np.array(res)


def my_omicron(student_id):
    digits = np.array([int(d) for d in str(student_id)])
    return np.random.choice(digits, size=1, p=np.flip(digits/np.sum(digits)))

