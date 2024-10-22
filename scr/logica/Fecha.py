class Fecha:

    def validaFecha(self,dia, mes, anio):
        if (dia < 1) or (dia > 31):
            return False

        if (mes < 1) or (mes > 12):
            return False

        # determinamos la cantidad de días del mes
        diasMes = 0
        if mes in (1, 3, 5, 7, 8, 10, 12):
            diasMes = 31
        elif mes in (4, 6, 9, 11):
            diasMes = 30
        elif mes == 2:
            # verificación de año bisiesto
            if ((anio % 400 == 0) or ((anio % 4 == 0) and (anio % 100 != 0))):
                diasMes = 29
            else:
                diasMes = 28

        if (dia > diasMes):
            return False
        else:
            return True

if __name__ == '__main__':
    fecha = Fecha()
    if (fecha.validaFecha(29, 2, 2024)):
        print("fecha es valida")
    else:
        print("La fecha no es valida")
