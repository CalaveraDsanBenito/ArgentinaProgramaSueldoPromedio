# Definir los sueldos de Juan en cada mes
sueldos_por_mes = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]

# Calcular el sueldo total y promedio
sueldo_total = sum(sueldos_por_mes)
sueldo_promedio = sueldo_total / len(sueldos_por_mes)

# Determinar la categoría de sueldo
if sueldo_promedio < 300:
    categoria = "Sueldo bajo"
elif sueldo_promedio <= 900:
    categoria = "Sueldo normal"
else:
    categoria = "Sueldo mejor de lo normal"

# Imprimir los resultados
print(f"El sueldo promedio de Juan es ${sueldo_promedio:.2f}")
print(f"Categoría de sueldo: {categoria}")
