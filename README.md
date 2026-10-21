# validador-datos

Generador de archivos de ancho fijo con datos sintéticos de cotizantes, y funciones de validación del dígito verificador del RUT chileno, escritos en Python.

## Contexto

Durante mi trabajo como desarrollador ETL participé en el proceso del Primer Retiro de Fondos de Pensiones (Sura), donde los archivos de entrada llegaban en formato de ancho fijo y debían validarse antes de procesarse.

Este proyecto toma esa idea como punto de partida para practicar Python aplicado a datos: generar un archivo con la misma estructura usando datos ficticios, y validar el RUT con el algoritmo de módulo 11. **No replica el proceso real ni usa datos reales.**

## Estructura

```
validador-datos/
├── src/
│   ├── rut.py            # Cálculo y validación del dígito verificador
│   └── genera_datos.py   # Generador del archivo de cotizantes
└── datos/
    └── cotizantes.txt    # Archivo de ejemplo generado
```

## Layout del archivo

Cada registro tiene **126 caracteres**:

| Campo             | Posición | Largo | Formato                            |
|-------------------|----------|-------|------------------------------------|
| RUT               | 1–12     | 12    | Numérico, con ceros a la izquierda |
| DV                | 13       | 1     | Dígito o `K`                       |
| Nombre            | 14–43    | 30    | Texto alineado a la izquierda      |
| Apellido paterno  | 44–73    | 30    | Texto alineado a la izquierda      |
| Apellido materno  | 74–103   | 30    | Texto alineado a la izquierda      |
| Saldo             | 104–118  | 15    | Numérico, con ceros a la izquierda |
| Fecha             | 119–126  | 8     | `AAAAMMDD`                         |

## Módulos

### `rut.py`

- `calcula_dv(rut)`: calcula el dígito verificador con el algoritmo de módulo 11.
- `valida_DV(rut, dv)`: indica si el dígito verificador corresponde al RUT.

Ambas aceptan el RUT como texto o como número, y normalizan el DV (mayúsculas y espacios).

```python
from src.rut import calcula_dv, valida_DV

calcula_dv("12345678")       # '5'
valida_DV(12345678, "5")     # True
valida_DV("12345678", " k ") # False
```

### `genera_datos.py`

Genera `datos/cotizantes.txt` con registros sintéticos:

- Nombres y apellidos tomados de listas propias.
- RUT al azar con su DV calculado con `rut.py`.
- Saldo y fecha al azar.

## Cómo ejecutarlo

Requiere Python 3.12. No usa librerías externas.

```powershell
git clone https://github.com/pemarfigueroa/validador-datos.git
cd validador-datos
python -m venv .venv
.venv\Scripts\Activate.ps1
python src/genera_datos.py
```

El archivo queda en `datos/cotizantes.txt`.

## Autor

Pedro Figueroa: desarrollador ETL con más de 15 años de experiencia en DataStage, PowerCenter, Oracle y SQL Server.
