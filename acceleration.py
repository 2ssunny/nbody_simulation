import numpy as np

G = 8.6498928e-13  #Unit: km^3 kg^-1 hr^-2

def acc_calculator(r, m):
  """
    r: current postion, m: mass
   """
  dx = r[None, :, :] - r[:, None, :] 

  dist_sq = np.sum(dx**2, axis=-1)

  dist_sq += np.eye(len(r)) 
  
  dist = np.sqrt(dist_sq)

  acc_matrix = G * (m[None, :] / (dist**3))[:, :, None] * dx
  acc = np.sum(acc_matrix, axis=1)

  return acc