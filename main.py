import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import skyfield_data, RK4solver

position_current = skyfield_data.position_nparray
velocity_current = skyfield_data.velocity_nparray
masses = skyfield_data.masses_nparray
names = skyfield_data.names_nparray

dt = 1 # adjust!! (1 = 1 hour)
steps = 3650 # adjust!! (# of calculation)

trajectory = np.zeros((steps, len(masses), 3))

for step in range(steps):
    trajectory[step] = position_current
    position_current, velocity_current = RK4solver.rk4_step(position_current, velocity_current, masses, dt)
    if step%200 == 0: #progress check
      print(step)



plt.figure(figsize=(6, 6))
cmap = cm.get_cmap('rainbow')
colors = cmap(np.linspace(0, 1, len(masses)))

for i in range(len(masses)):
    # 1. 궤도 선에만 label을 붙입니다 (names[i] 사용)
    plt.plot(trajectory[:, i, 0], trajectory[:, i, 1], color=colors[i], label=names[i])
    
    # 2. 끝점 점에는 label을 붙이지 않습니다 (혹은 label='_nolegend_' 사용)
    plt.plot(trajectory[-1, i, 0], trajectory[-1, i, 1], 'o', color=colors[i]) 

plt.title("N-Body Simulation (RK4) - Figure 8 Orbit")
plt.legend() 

plt.grid(True)
plt.axis('equal')
plt.show()
filename = f"planets_{dt}_{steps}steps.png"
plt.savefig(filename, dpi=500)