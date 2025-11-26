import acceleration

def rk4_step(r, v, m, h):
    """
    r: current postion, v: current velocity, m: mass, h: time step
    """
    # k1
    v1 = v
    a1 = acceleration.acc_calculator(r, m)
    
    # k2
    r_mid1 = r + v1 * 0.5 * h
    v_mid1 = v + a1 * 0.5 * h
    v2 = v_mid1
    a2 = acceleration.acc_calculator(r_mid1, m)
    
    # k3
    r_mid2 = r + v2 * 0.5 * h
    v_mid2 = v + a2 * 0.5 * h
    v3 = v_mid2
    a3 = acceleration.acc_calculator(r_mid2, m)
    
    # k4
    r_end = r + v3 * h
    v_end = v + a3 * h
    v4 = v_end
    a4 = acceleration.acc_calculator(r_end, m)
    
    r_next = r + (h/6.0) * (v1 + 2*v2 + 2*v3 + v4)
    v_next = v + (h/6.0) * (a1 + 2*a2 + 2*a3 + a4)
    
    return r_next, v_next