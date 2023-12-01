# Factory pattern

Factory Method es un patrón de diseño creacional que proporciona una interfaz para crear objetos en una superclase, mientras permite a las subclases alterar el tipo de objetos que se crearán.

El Factory Method es una técnica en programación que usa una clase principal para establecer un método básico de creación de objetos. Las clases derivadas de esta principal pueden cambiar el tipo de objetos que se crean, sin modificar la forma en que se solicitan estos objetos.

Planificación de una comida diaria en casa: Imagina que eres una persona que planea cocinar la cena en casa cada noche. Tienes un método general para preparar la cena, que consiste en decidir el tipo de comida, comprar los ingredientes y cocinarlos. Sin embargo, el tipo específico de cena que preparas puede variar dependiendo del día de la semana (que representaría las subclases). Por ejemplo:

    Lunes (Subclase 1): Decides que los lunes son para comidas saludables, así que sigues tu método general pero preparas una ensalada.
    Martes (Subclase 2): Los martes son para comida rápida, así que utilizas el mismo método general pero preparas hamburguesas.
    Miércoles (Subclase 3): Este día lo dedicas a la comida internacional, por lo que podrías preparar sushi.

En este escenario, la "planificación de la cena" es el método general. No cambia el proceso de planificación, compra y cocina, pero el resultado (el tipo de cena) varía según el día de la semana. Esto es similar al patrón Factory Method, donde tienes un método general para crear un objeto, pero las subclases determinan qué tipo específico de objeto se crea sin cambiar el proceso de creación en sí.