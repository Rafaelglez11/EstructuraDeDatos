alumnos_tiempo = [-2, -1, 0, 1, 2]
umbral = 3
alumnos_puntuales = 0
alumnos_impuntuales = 0

for i in range(len(alumnos_tiempo)):
    if alumnos_tiempo[i] < 0:
        alumnos_puntuales += 1
    elif alumnos_tiempo[i] >= 0:
        alumnos_impuntuales += 1

if alumnos_puntuales >= 3:
    print("\nLa clase puede iniciar.")
    print(f"\nLlegaron a timepo {alumnos_puntuales} alumnos.")
    print("\nEl profesor esta feliz :)")
elif alumnos_puntuales < 3:
    print("\nLa clase no puede iniciar.")
    print(f"{alumnos_impuntuales} alumnos van retrasados.")
    print("\nEl profesor está enojado >:c")


