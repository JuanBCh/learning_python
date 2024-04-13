from modelos import Departamento, Empleado
from conexion import engine, ModeloBase, session

def guardar_datos():
    contabilidad = Departamento("Contabilidad")
    session.add(contabilidad)

    tecnologia = Departamento("Tecnologia")
    session.add(tecnologia)

    session.commit()

    emilio = Empleado("Emilio", "Tafur", "184723", contabilidad.id)
    session.add(emilio)

    javier = Empleado("Javier", "Quinionez", "134213", tecnologia.id)
    session.add(javier)

    session.commit()

    print(contabilidad.id)

def hacer_consultas():
    dep_id_1 = session.get(Departamento, 1)
    print(dep_id_1)

    cantidad_empleados = session.query(Empleado).count()
    print(cantidad_empleados, "Empleados")

    empleado_contab = session.query(Empleado).filter_by(
        id_departamento = dep_id_1.id
    ).all() # => Si lo cambiamos por .first() nos da el primer elemento de la lista
    
    for empleado in empleado_contab:
        print(empleado)

if __name__ == "__main__":
    ModeloBase.metadata.create_all(engine)
    # guardar_datos()
    hacer_consultas()
