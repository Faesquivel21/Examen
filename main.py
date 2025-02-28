"""================================================================================================
Institute....: Universidad Técnica Nacional
Headquarters.: Pacífico
Career.......: Tecnologías de Información
Period.......: 1-2025
Document.....: class_02_02.py
Goals........: Oriented Object Programming, using an external class  for create instance variables
Professor....: Jorge Ruiz (york)
Student......:
================================================================================================"""



from clsTractor import clsTractor
from clsLocomocion import clsLocomocion
from clsAcople import clsAcople
from clsUsoMaquinaria import clsUsoMaquinaria


def main():
    tractores = [
        clsTractor("12354", 5, "VM01", 6, "Diesel", 71, 115, "CH846", "Acero", 5.5, 40, "John Deeere",
                   clsLocomocion("Ruedas", "Frontal", "4x4"), [clsAcople("Arado", False, "Cultivo")],
                   clsUsoMaquinaria("Agricultura", "Plano", 10)),
        clsTractor("4244", 7, "VM222", 4, "Diesel", 41, 70, "CH899", "Acero", 4.0, 35, "Caterpillar",
                   clsLocomocion("Orugas", "Lateral", "2x4"), [clsAcople("Pala", True, "Excavación")],
                   clsUsoMaquinaria("Construcción", "Montañoso", 8)),
        clsTractor("F2123", 8, "VM213", 0, "Electrico", 116, 250, "Ch841", "Acero", 6.2, 50, "Volvo",
                   clsLocomocion("Mixto", "Trasera", "4x4"), [clsAcople("Remolque", False, "Transporte")],
                   clsUsoMaquinaria("Transporte", "Irregular", 15)),
        clsTractor("Y1075", 6, "VM564", 6, "Diesel", 71, 115, "CH5588", "caucho", 5.0, 38, "Massey Ferguson",
                   clsLocomocion("Ruedas", "Frontal", "2x4"), [clsAcople("Cultivador", False, "Siembra")],
                   clsUsoMaquinaria("Agricultura", "Plano", 9)),
        clsTractor("J1011", 9, "VM225", 10, "Gas natural", 116, 250, "CH5485", "Acero", 7.0, 45, "Mach",
                   clsLocomocion("Orugas", "Lateral", "4x4"), [clsAcople("Rotavator", True, "Labranza")],
                   clsUsoMaquinaria("Minería", "Montañoso", 12))
    ]

    for tractor in tractores:
        print(f"Modelo: {tractor.modelo}, Peso: {tractor.peso}T, Velocidad: {tractor.velocidad} km/h")
        print(f"Moto: {tractor.minHP}-{tractor.maxHP} HP, Locomoción: {tractor.locomocion.tipo} ({tractor.locomocion.traccion})")
        print(f"Combustible:{(tractor.combustible)}, Cantidad de Cilindros:{(tractor.cilindros)}, Placa: {(tractor.placa)}")
        print(f"Acoples: {[acople.nombre for acople in tractor.acoples]}")
        print(f"Uso: {tractor.uso.tipo_trabajo} en terreno {tractor.uso.terreno}, con carga máxima {tractor.uso.carga_maxima}T")
        print("-" * 60)


if __name__ == "__main__":
    main()