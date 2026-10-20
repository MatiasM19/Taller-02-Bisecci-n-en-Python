def biseccion(f, a, b, TOL=1e-6, N0=100):
    """Devuelve (p, historia), con historia = [(a, b, p) por iteración]."""

    FA = f(a)
    historia = []
    i = 1

    while i <= N0:
        p = a + (b - a) / 2
        FP = f(p)

        historia.append((a, b, p))

        if FP == 0 or (b - a) / 2 < TOL:
            return p, historia

        i = i + 1

        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p

    raise RuntimeError(f"fracasó después de {N0} iteraciones")

def f(x):
    return x**3 + 4*x**2 - 10


p, historia = biseccion(f, 1, 2, TOL=10**-2)

print("Solución aproximada:", p)
print("Historia de la búsqueda:")

for a, b, p in historia:
    print(f"a = {a}, b = {b}, p = {p}")