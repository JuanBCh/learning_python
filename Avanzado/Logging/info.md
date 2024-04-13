El logging es un proceso para obtener logs del programa.
El log es un registro que nos ayuda a entender el comportamiento del programa, ya que al definir un log estamos definiendo la ocurrencia de un evento.
Estos logs tambien nos ayuda a detectar cuando se esta produciendo un error.

Cada log debe ser creado con un nivel de seguridad.
Hay 5 niveles de seguridad:

DEBUG (Informacion detallada, usualmente se usa mientras se esta desarrollando en partes del codigo que tenemos que revisar)

INFO ( Es el reporte de eventos de los cuales se requiere informacion)

WARNING (Reporte de algo inesperado que ha susedido o que va a suceder en el codigo. Aunque no genere ningun error)

ERROR (Reporte de algo que no se puede ejecutar porque ocurrio un error en el codigo)

CRITICAL (Reporte de un error grave, puede indicar que el programa se detendrá por este error)


Por defecto la la libreria logging genera warnings como el primer nivel. Para usar debug e Info es necesario definirlo desde el codigo