

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

