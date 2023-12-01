import copy

class ReportePrototype:
    def clone(self):
        return copy.deepcopy(self)

    def generar_reporte(self, datos):
        raise NotImplementedError("Debe implementarse en la subclase.")

class ReporteAntecedentes(ReportePrototype):
    def __init__(self):
        self.estructura = {
            "titulo": "Reporte de Antecedentes",
            "secciones": ["Datos Personales", "Historial Judicial"],
            "conclusiones": ""
        }

    def generar_reporte(self, datos):
        # Aquí se añadiría la lógica para poblar las secciones con los datos
        self.estructura["conclusiones"] = datos["conclusion"]
        return self.estructura

# Creando y utilizando la plantilla de reporte


if __name__ == "__main__":
    reporte_antecedentes = ReporteAntecedentes()

    # Clonando y personalizando el reporte
    reporte_personalizado = reporte_antecedentes.clone()
    datos = {"conclusion": "No se encontraron antecedentes relevantes."}
    reporte_personalizado.generar_reporte(datos)

    print(reporte_antecedentes.estructura)
    print(reporte_personalizado.estructura)
