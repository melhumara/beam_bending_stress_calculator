# beam bending and stress calculator
# formula: sigma = (m * y) / i

# 1. area moment of inertia calculation
def calculate_area_moment_of_inertia(width, height):
    # calculates moment of inertia for rectangular section
    return (width * (height ** 3)) / 12.0

# 2. maximum bending moment calculation
def calculate_max_bending_moment(force, length):
    # calculates max moment for simply supported beam under point load
    return (force * length) / 4.0

# 3. main function to calculate bending stress
def calculate_bending_stress(force, length, width, height):
    # step a: calculate bending moment (n.mm)
    m = calculate_max_bending_moment(force, length)
    
    # step b: calculate area moment of inertia (mm^4)
    i = calculate_area_moment_of_inertia(width, height)
    
    # step c: distance from neutral axis to outer edge (mm)
    y = height / 2.0
    
    # step d: calculate stress (mpa or n/mm^2)
    sigma = (m * y) / i
    
    return m, i, sigma

# 4. sample execution with example values
if __name__ == "__main__":
    # input parameters
    f = 5000.0      # applied force (n)
    l = 2000.0      # beam length (mm)
    b = 50.0        # cross-section width (mm)
    h = 100.0       # cross-section height (mm)

    # run calculation
    m_max, i_x, sigma_max = calculate_bending_stress(f, l, b, h)

    # print results to console
    print("=" * 45)
    print(" mechanical engineering - beam analysis ")
    print("=" * 45)
    print(f"applied force (f)       : {f} n")
    print(f"beam length (l)         : {l} mm")
    print(f"cross-section (b x h)   : {b} x {h} mm")
    print("-" * 45)
    print(f"max bending moment (m)  : {m_max / 1000:.2f} n.m")
    print(f"moment of inertia (i)   : {i_x:.2f} mm^4")
    print(f"max bending stress (s)  : {sigma_max:.2f} mpa (n/mm²)")
    print("=" * 45)
