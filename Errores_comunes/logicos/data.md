Los errores logicos no necesariamente van a generar un error.
Estos errores pueden ocurrir por diversos motivos y estan relacionados a la logica en el codigo.
Pueden ocacionar errores den tiempo de ejecucion o semantico

Errores de importacion circular: Pasa cuando importamos una funcion de un modulo que esta importando una funcion de este mismo modulo. Tenemos que ver si es necesario tener las funciones en modulos diferentes.

Para evitar errores en ciclos anidados y reducir las lineas de codigo, podemos usar librerias como "itertools"