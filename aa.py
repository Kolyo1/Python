import sympy as sp

# Уравнения на правите h и m (параметрична форма):
# h: x = 3 + t, y = t, z = t
# m: x = -4 + 2s, y = -9 + s, z = 5 + s

# Параметри на правите
t, s = sp.symbols('t s')

# Параметрични уравнения на h и m
x_h, y_h, z_h = 3 + t, t, t
x_m, y_m, z_m = -4 + 2*s, -9 + s, 5 + s

# Уравнение на равнината \lambda: 5x + 2y + 3z + 5 = 0
plane_eq = 5*sp.Symbol('x') + 2*sp.Symbol('y') + 3*sp.Symbol('z') + 5

# 1. Проверка дали правите се пресичат
# Решаваме системата x_h = x_m, y_h = y_m, z_h = z_m
intersection = sp.solve([
    x_h - x_m, y_h - y_m, z_h - z_m
], (t, s))

if intersection:
    result = "Правите се пресичат в точка: " + str(intersection)
else:
    result = "Правите не се пресичат (скръстени). Продължаваме с намиране на точки D и G."

# 2. Намиране на точки D и G, лежащи на равнината
# Заместваме параметричните уравнения на h и m в равнината, за да намерим t и s, където h и m пресичат равнината
plane_h = plane_eq.subs({'x': x_h, 'y': y_h, 'z': z_h})
plane_m = plane_eq.subs({'x': x_m, 'y': y_m, 'z': z_m})

t_d = sp.solve(plane_h, t)  # t за точката D
s_g = sp.solve(plane_m, s)  # s за точката G

if t_d and s_g:
    # Намираме координатите на D и G
    t_d = t_d[0]
    s_g = s_g[0]
    D = (x_h.subs(t, t_d), y_h.subs(t, t_d), z_h.subs(t, t_d))
    G = (x_m.subs(s, s_g), y_m.subs(s, s_g), z_m.subs(s, s_g))
    
    # 3. Уравнение на равнината, симетрична спрямо D и G
    center = [(D[i] + G[i]) / 2 for i in range(3)]  # Център на симетрията
    normal_vector = [D[i] - G[i] for i in range(3)]  # Нормален вектор на равнината
    symmetric_plane = f"{normal_vector[0]}*(x - {center[0]}) + {normal_vector[1]}*(y - {center[1]}) + {normal_vector[2]}*(z - {center[2]}) = 0"

    result += f"\nТочка D: {D}\nТочка G: {G}\nСиметрична равнина: {symmetric_plane}"

result
