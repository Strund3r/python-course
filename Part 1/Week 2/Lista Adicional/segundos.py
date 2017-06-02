segundos_input = input("Por favor, entre com o número de segundos que deseja converter: ")

segundos_int = int(segundos_input)

horas = segundos_int // 3600
dias = horas // 24
segundos_restantes = segundos_int % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

if (horas >= 24):
	dias = int(horas / 24)
	horas = int(horas % 24)

if (dias == 0 or dias > 1):
	dias_texto = "dias,"
else:
	dias_texto = "dia,"

if (horas == 0 or horas > 1):
	horas_texto = "horas,"
else:
	horas_texto = "hora,"

if (minutos == 0 or minutos > 1):
	minutos_texto = "minutos e"
else:
	minutos_texto = "minuto e"

if (segundos == 0 or segundos > 1):
	segundos_texto = "segundos."
else:
	segundos_texto = "segundo."

print(dias, dias_texto, horas, horas_texto, minutos, minutos_texto, segundos, segundos_texto)
