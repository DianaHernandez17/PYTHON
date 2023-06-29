import datetime

dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Obtener la fecha actual
fecha_actual = datetime.date.today()


numero_dia_semana = fecha_actual.weekday()


dia_actual = dias_semana[numero_dia_semana]

# Muestra el resultado por pantalla
print("HOY ES: ", dia_actual)
