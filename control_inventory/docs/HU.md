

# Historias de Usuario – Gestión de Inventarios

---

### **HU-01: Agregar Producto**
**Como** encargado del inventario  
**Quiero** agregar nuevos productos al sistema  
**Para** mantener actualizado el catálogo de productos disponibles  

**Criterios de aceptación:**
- Se debe ingresar: nombre, categoría, precio y cantidad del producto.  
- El sistema confirma cuando el producto se agrega exitosamente.  

---

### **HU-02: Listar Productos**
**Como** usuario del sistema  
**Quiero** ver todos los productos del inventario  
**Para** conocer qué productos están disponibles  

**Criterios de aceptación:**
- El sistema muestra todos los productos en formato:  
  `Nombre | Categoría | Precio | Stock`  
- Si el inventario está vacío, muestra el mensaje:  
  `"Inventario vacío."`

---

### **HU-03: Buscar Producto por Nombre**
**Como** usuario del sistema  
**Quiero** buscar un producto específico por su nombre  
**Para** obtener información detallada de ese producto  

**Criterios de aceptación:**
- Si el producto existe, el sistema muestra su información completa.  
- Si el producto no existe, muestra `"Producto no encontrado."`

---

### **HU-04: Actualizar Cantidad de Producto**
**Como** encargado de inventario  
**Quiero** actualizar la cantidad de un producto existente  
**Para** reflejar cambios en el stock (ventas, devoluciones, nuevas compras)  

**Criterios de aceptación:**
- Si el producto no existe, muestra `"Producto no encontrado."`  
- No permite cantidades negativas.  
- Si la cantidad es `0`, muestra `"Sin stock!"`  
- Si ingreso datos inválidos, muestra `"Cantidad inválida."`

---

### **HU-05: Verificar Estado del Stock**
**Como** gerente de inventario  
**Quiero** ver un resumen del estado del stock de todos los productos  
**Para** identificar rápidamente productos que necesitan reabastecimiento  

**Criterios de aceptación:**
- El sistema clasifica productos en tres categorías:  
  - **SIN STOCK**: cantidad = 0  
  - **STOCK BAJO**: cantidad < 5  
  - **STOCK NORMAL**: cantidad ≥ 5  
- Lista los nombres de productos en cada categoría.  
- Si el inventario está vacío, muestra `"Inventario vacío."`

---

### **HU-06: Filtrar productos por categoría**
**Como** usario del sistema  
**Quiero** ver solo los productos de una categoría específica  
**Para** facilitar la búsqueda de productos similares  

**Criterios de aceptación:**  
- pruedo ingresar el nombre de una categoría.
- el sistema debe tener la capacidad de ignorar mayúsculas/minúsculas

---

### **HU-07: Salir del Sistema**
**Como** usuario del sistema  
**Quiero** poder cerrar la aplicación  
**Para** finalizar mi sesión de trabajo  

**Criterios de aceptación:**  
- La aplicación se debe cerrar correctamente.


---

### **HU-08: Filtrar productos por rango de precio**
**Como** usuario del sistema  
**Quiero** ver solo los productos dentro de un rango de precios  
**Para** comparar opciones según mi presupuesto  

**Criterios de aceptación:**
- Puedo ingresar precio mínimo y máximo.  
- Si ambos valores son válidos, el sistema lista los productos dentro del rango.  
- Si no hay coincidencias, muestra: "No hay productos en ese rango".  

---

### **HU-09: Eliminar producto**
**Como** encargado del inventario  
**Quiero** eliminar un producto por su nombre  
**Para** mantener el inventario limpio y actualizado  

**Criterios de aceptación:**
- Si el producto existe, se elimina y muestra: "Producto eliminado: 'nombre'".  
- Si el producto no existe, muestra: "Producto no encontrado."  

---

### **HU-10: Calcular valor total del inventario**
**Como** gerente  
**Quiero** conocer el valor monetario total del inventario  
**Para** tomar decisiones financieras  

**Criterios de aceptación:**
- El sistema calcula la suma de (precio x cantidad) de todos los productos usando Decimal.  
- Muestra el total con el formato: "Valor total: 'monto'".  

---

### **HU-11: Registrar una venta**
**Como** vendedor  
**Quiero** registrar la venta de un producto  
**Para** descontar stock y dejar historial de ventas  

**Criterios de aceptación:**
- Debo ingresar nombre del producto y cantidad a vender.  
- Si el producto no existe, informa y no realiza la venta.  
- Si la cantidad es <= 0, muestra: "Error: La cantidad debe ser mayor a cero."  
- Si no hay stock suficiente, muestra el disponible: "Error: Stock insuficiente. Disponible: X"  
- Si la venta es válida, descuenta stock y registra la venta con total = precio x cantidad.  
- Si el stock queda en 0, muestra alerta de sin stock; si es menor a 5, muestra advertencia de stock bajo.  

---

### **HU-12: Ver productos más vendidos**
**Como** gerente  
**Quiero** ver un ranking de los productos más vendidos  
**Para** identificar tendencias y tomar decisiones de compra  

**Criterios de aceptación:**
- El sistema muestra un top (por defecto 5) basado en el historial de ventas.  
- Para cada producto, se muestra nombre, unidades vendidas y stock actual.  
- Si no hay ventas registradas, muestra: "No hay ventas registradas."  

---

### **HU-13: Reporte de ventas**
**Como** analista  
**Quiero** ver un reporte con el historial de ventas  
**Para** conocer ingresos y unidades vendidas  

**Criterios de aceptación:**
- Se listan las ventas con fecha, producto, cantidad y total.  
- Se muestran totales al final: número de ventas, unidades vendidas e ingresos totales.  
- Si no hay ventas, muestra: "No hay ventas registradas."  

---

### **HU-14: Ver gráfica de inventario (ASCII)**
**Como** usuario del sistema  
**Quiero** ver una representación visual simple del stock  
**Para** entender rápidamente el estado del inventario  

**Criterios de aceptación:**
- Se muestra una barra proporcional para cada producto (máximo 50 caracteres).  
- Si todos los productos tienen 0, muestra: "Todos los productos sin stock."  
- Incluye una escala aproximada al final.  

---

### **HU-15: Guardar datos (inventario y ventas)**
**Como** usuario del sistema  
**Quiero** guardar los datos actuales a archivos JSON  
**Para** no perder información al cerrar la aplicación  

**Criterios de aceptación:**
- Los productos se guardan en `inventario.json`; las ventas en `ventas.json`.  
- Se serializan correctamente tipos especiales: Decimal (como string) y datetime (ISO 8601).  
- Muestra mensajes de confirmación al guardar.  
- Maneja y reporta errores de guardado.  

---

### **HU-16: Cargar datos (inventario y ventas)**
**Como** usuario del sistema  
**Quiero** cargar datos previamente guardados  
**Para** continuar trabajando desde donde lo dejé  

**Criterios de aceptación:**
- Carga `inventario.json` y `ventas.json` si existen.  
- Reconstruye tipos correctamente: Decimal desde string y datetime desde ISO.  
- Si no existen archivos, informa y continúa con listas vacías.  
- Maneja y reporta errores de lectura de JSON.  

---

### **HU-17: Carga automática al iniciar**
**Como** usuario frecuente  
**Quiero** que el sistema cargue datos automáticamente al iniciar  
**Para** ahorrar tiempo y continuar rápidamente  

**Criterios de aceptación:**
- Al iniciar la aplicación, intenta cargar `inventario.json` y `ventas.json`.  
- Si no existen, el sistema continúa sin error, con inventario/ventas vacíos.  

---

### **HU-18: Confirmación de guardado al salir**
**Como** usuario del sistema  
**Quiero** que al salir se me pregunte si deseo guardar  
**Para** evitar perder cambios por accidente  

**Criterios de aceptación:**
- Al seleccionar "Salir", el sistema pregunta: ¿Deseas guardar antes de salir? (s/n)  
- Si respondo "s", guarda inventario y ventas antes de cerrar.  
- Si respondo "n", sale sin guardar.  

---

### **HU-19: Ver fecha y hora de alta del producto**
**Como** usuario del sistema  
**Quiero** ver cuándo fue agregado cada producto  
**Para** tener trazabilidad básica  

**Criterios de aceptación:**
- Al listar productos, se muestra la fecha y hora con formato legible (dd/mm/aaaa HH:MM:SS).  
- La fecha se guarda internamente en formato ISO para persistencia.  

