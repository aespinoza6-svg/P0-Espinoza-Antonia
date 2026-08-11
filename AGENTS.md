# AGENTS.md

Instrucciones basicas para OpenCode al trabajar en este repositorio.

## Proposito del proyecto
Implementar una funcion propia de multiplicacion de matrices (`mimatmul`) en Python puro, medir su rendimiento y compararla con NumPy (`A @ B`). Evaluaciones P0E1 (configuracion e inicio) y P0E2 (benchmark, grafico y documentacion final).

## Reglas
- Mantener el codigo sencillo y legible.
- No inventar mediciones ni resultados: todos los datos deben generarse ejecutando el codigo.
- `mimatmul` debe usar ciclos explicitos de Python y no `A @ B`, `np.matmul`, `np.dot` ni `np.einsum`.
- No ejecutar comandos destructivos de Git (por ejemplo, `reset --hard`, `rebase`, `push --force`).
- No subir credenciales ni secretos al repositorio.
- Ejecutar las pruebas despues de modificar codigo:
  ```
  pytest
  ```
- Regenerar los datos y el grafico despues de cambiar el benchmark:
  ```
  python src/benchmark.py
  ```
