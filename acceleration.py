import numpy as np

G = 8.6498928e-13 #Unit: km^3 kg^-1 hr^-2

def acc_calculator(r, m):
  """
    r: current postion, m: mass
   """
  N = len(m) #number of celestial objects
  acc = np.zeros_like(r)

  for i in range(N):
    for j in range(N):
      if i!=j:
        dr = r[j]-r[i]
        dist = np.sqrt(np.sum(dr**2))
        acc[i] += G * m[j] * dr / (dist**3)
  return acc