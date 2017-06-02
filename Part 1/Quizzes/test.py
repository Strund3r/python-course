segundos_input = input("Por favor, entre com o número de segundos que deseja converter: ")

segundos_int = int(segundos_input)

dias = horas // 24
horas = segundos_int // 3600
segundos_restantes = segundos_int % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(dias, "dias, ", horas, "horas, ", minutos, "minutos e ", segundos, "segundos.")
