"""Programa de finanzas personales.

Registra transacciones de tipo ingreso o egreso y calcula
el balance financiero del periodo registrado.
"""


def calcular_balance(total_ingresos, total_egresos):
    """Calcula el balance a partir de los ingresos y egresos totales."""
    return total_ingresos - total_egresos


def main():
    """Ejecuta el registro de transacciones y muestra el resumen."""
    total_ingresos = 0
    total_egresos = 0
    continuar = "si"

    while continuar == "si":
        monto = float(input("Ingrese el monto: "))
        tipo_movimiento = input(
            "Ingrese el tipo de movimiento (ingreso/egreso): "
        ).strip().lower()

        if tipo_movimiento == "ingreso":
            total_ingresos = total_ingresos + monto
        elif tipo_movimiento == "egreso":
            total_egresos = total_egresos + monto
        else:
            print("Tipo no valido. Escriba 'ingreso' o 'egreso'.")

        continuar = input(
            "Desea registrar otra transaccion? (si/no): "
        ).strip().lower()

    balance = calcular_balance(total_ingresos, total_egresos)

    print("\n--- RESUMEN FINANCIERO ---")
    print(f"Total de ingresos: {total_ingresos}")
    print(f"Total de egresos: {total_egresos}")
    print(f"Balance: {balance}")

    if balance >= 0:
        print("Situacion financiera: Ahorro")
    else:
        print("Situacion financiera: Deficit")


if __name__ == "__main__":
    main()