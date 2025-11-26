import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
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
print('Simulation finished')


fig = plt.figure(figsize=(10, 10)) # 3D는 조금 더 크게 보는 게 좋습니다.
ax = fig.add_subplot(111, projection='3d') # 3D 축(Axes) 생성

cmap = cm.get_cmap('rainbow')
# Matplotlib 버전 이슈로 경고가 뜰 경우 아래 코드로 대체 가능:
# cmap = matplotlib.colormaps['rainbow'] 
colors = cmap(np.linspace(0, 1, len(masses)))

for i in range(len(masses)):
    # X, Y, Z 좌표 데이터 추출
    xs = trajectory[:, i, 0]
    ys = trajectory[:, i, 1]
    zs = trajectory[:, i, 2] # --- [변경됨] Z축 데이터 추가 ---
    
    # 1. 궤도 선 그리기 (ax.plot 사용 및 z 인자 추가)
    # lw=linewidth, 너무 두꺼우면 겹쳐 보이니 조절하세요.
    ax.plot(xs, ys, zs, color=colors[i], label=names[i], lw=1) 
    
    # 2. 끝점 그리기 (3D에서는 scatter가 더 깔끔합니다)
    ax.scatter(xs[-1], ys[-1], zs[-1], color=colors[i], s=30, marker='o')


# --- [변경됨] 3. 그래프 꾸미기 및 비율 설정 ---
ax.set_title(f"N-Body Simulation (RK4) - 3D View (dt={dt}, steps={steps})")
ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_zlabel('Z (km)')
ax.legend()

# 우주 느낌을 위한 배경색 설정 (선택사항)
# ax.set_facecolor('black')
# fig.patch.set_facecolor('black')
# ax.grid(False)
# ax.xaxis.label.set_color('white') 
# (등등... 필요하면 추가하세요)


# [중요] 3D 축 비율 맞추기 (Equal Aspect Ratio Trick)
# Matplotlib 3D는 axis='equal'이 제대로 작동하지 않아 수동으로 박스를 맞춰야 찌그러지지 않습니다.
X_all = trajectory[:, :, 0]
Y_all = trajectory[:, :, 1]
Z_all = trajectory[:, :, 2]

max_range = np.array([X_all.max()-X_all.min(), 
                      Y_all.max()-Y_all.min(), 
                      Z_all.max()-Z_all.min()]).max() / 2.0

mid_x = (X_all.max()+X_all.min()) * 0.5
mid_y = (Y_all.max()+Y_all.min()) * 0.5
mid_z = (Z_all.max()+Z_all.min()) * 0.5

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)


plt.title("N-Body Simulation (RK4) - Figure 8 Orbit")
plt.legend() 

plt.grid(True)
plt.axis('equal')
plt.show()
filename = f"planets_{dt}_{steps}steps.png"
plt.savefig(filename, dpi=500)