Los errores en tiempo de ejecucion son errores que se generan cuando estamos corriendo el codigo. Estos no ocurren por un solo tipo de error, por lo tranto entener donde y porque sucedio requiere de revisiones cortas o muy exaustiva.

A diferencia de errores que se generan antes de la ejecucion, estos errores ocurren cuando se llega a la linea de codigo que contiene el error. Ahi se levanta una escepcion.

Estos errores pueden ser por dividir entre 0, por usar variables que no estan dentro del scope usado o ejecutar una operacion entre variables incompatibles, etc

Otro error se puede dar por superar el limite de recursiones de una funcion.. El limite por defeco es 1000. Esto lo podemos cambiar con la libreria "sys"