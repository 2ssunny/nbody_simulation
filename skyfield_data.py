from skyfield.api import load
import numpy as np

# load skyfield data
planets = load('de421.bsp')
ts = load.timescale()
now = ts.now()

# set up celestial objects
BODY_INFO = {
    'Sun': 10,
    'Mercury': 1,
    'Venus': 2,
    'Earth': 399,
    'Mars': 4,
    'Jupiter': 5,
    'Saturn': 6,
    'Uranus': 7,
    'Neptune': 8,
    'Pluto': 9
}

MASSES_KG = {
    'Sun': 1.989e30,
    'Mercury': 3.302e23,
    'Venus': 4.869e24,
    'Earth': 5.972e24,
    'Mars': 6.417e23,
    'Jupiter': 1.899e27,
    'Saturn': 5.685e26,
    'Uranus': 8.682e25,
    'Neptune': 1.024e26,
    'Pluto': 1.309e22
}

# function to extract data based on SSB (in km, hr)
def get_state(body_id, time):
	target = planets[body_id]
	barycentric = target.at(time)
	
	pos_km = barycentric.position.km
	vel_km_s = barycentric.velocity.km_per_s
	vel_km_hr = vel_km_s * 3600.0
	
	return pos_km, vel_km_hr


y0_list = []      # position/velocity
masses_list = []
names_list = []
position_list=[]
velocity_list = []

print(now.utc_strftime('%Y-%m-%d %H:%M:%S'))
print("-" * 40)

for name, body_id in BODY_INFO.items():
	# use extraction function
	position, velocity = get_state(body_id, now)
	
	# extend list to 1D list
	# y0_list.extend(position) # x, y, z
	# y0_list.extend(velocity) # vx, vy, vz
	
	position_list.append(position)
	velocity_list.append(velocity)
	masses_list.append(MASSES_KG[name])
	names_list.append(name)
	
	print(f"Loaded: {name:<12} | ID: {body_id}")

# Numpy array for simulation
# y0 = np.array(y0_list)

position_nparray = np.array(position_list)
velocity_nparray = np.array(velocity_list)
masses_nparray = np.array(masses_list)
names_nparray = np.array(names_list)

print(position_nparray)