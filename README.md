# Simulador de Plantas y Control PID

Este el código en Python que crea la interfaz gráfica para ingresar datos y desplegar las gráficas del comportamiento de la planta especificada.

## Pasos para ejecutar el programa
Ubicar el programa en el folder donde fue descargado.
Ejecutar con el comando:

```
python ProyectoFinalCtrlComp_Equipo10.py
```

## Uso del programa
1. Acomodar la ventana de datos y la ventana de gráficas para poder visualizar ambas de manera adecuada.
2. Ingresar los datos en los espacios correspondientes
    - Los espacios sin llenar se tomarán como 0 (a excepción del intervalo de muestreo).
3. Seleccionar los modos de operación deseados
4. Hacer click en el botón _Start/Update_ para comenzar la simulación
    - Volver a hacer click en este botón después de modificar los datos y/o los modos de operación.
5. Hacer click en el botón _Stop/Reset_ para detener el programa y/o resetear las condiciones de la planta.
6. Cerrar ambas ventanas del programa y teclear _Control+C_ en la terminal donde se ejecutó el programa
    - También se puede cerrar la terminal para cancelar la ejecución.