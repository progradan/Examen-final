import json  
import os   

def crear_archivo_inventario():  
    if not os.path.exists("inventario.json"):  
        with open("inventario.json", "w") as file:  
            json.dump([], file)  
        print("Archivo inventario.json creado.")  

def cargar_inventario():  
    with open("inventario.json", "r") as file:  
        return json.load(file)  

def guardar_inventario(inventario):  
    with open("inventario.json", "w") as file:  
        json.dump(inventario, file, indent=4)  

def comparar_producto(inventario, nombre):
    for i, producto in enumerate(inventario):
        if producto["nombre"]==nombre:
            return i
    return None
                      
def crear_producto(inventario):  
    nombre = input("Ingrese el nombre del producto: ").lower() 
    if comparar_producto(inventario, nombre) is None:
        cantidad = int(input("Ingrese la cantidad del producto: "))  
        costo = float(input("Ingrese el precio del producto: "))  
        inventario.append({"nombre": nombre, "cantidad": cantidad, "costo": costo})  
        guardar_inventario(inventario)  
        print("El producto se agregó con éxito.") 
    else:
        print("el producto ya existe en el inventario") 
    

def mostrar_productos(inventario):  
    if not inventario:  
        print("No hay nada en el inventario.")  
        return  
    for producto in inventario:  
        print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Costo: {producto['costo']}")  

def mostrar_producto(inventario):  
    nombre = input("Ingrese el nombre del producto que quiere buscar: ").lower()  
    for producto in inventario:  
        if producto["nombre"] == nombre:  
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Costo: {producto['costo']}")  
            return  
    print("No se encontró el producto que busca.")  

def actualizar_producto(inventario):  
    nombre = input("Ingrese el nombre del producto que desea actualizar: ").lower()  
    for producto in inventario:  
        if producto["nombre"] == nombre:  
            new_costo = float(input("Ingrese el nuevo precio: "))  
            new_cantidad = int(input("Ingrese la nueva cantidad del producto: "))  
            producto["costo"] = new_costo  
            producto["cantidad"] = new_cantidad  
            guardar_inventario(inventario)  
            print("Producto actualizado con éxito.")  
            return  
    print("Producto no encontrado.")  

def eliminar_producto(inventario):  
    nombre = input("Ingrese el nombre del producto que desea eliminar: ").lower()  
    for i, producto in enumerate(inventario):  
        if producto["nombre"] == nombre:  
            del inventario[i]  
            guardar_inventario(inventario)  
            print("Producto eliminado con éxito.")  
            return  
    print("Producto no encontrado.")  

def main():  
    crear_archivo_inventario()   
    inventario = cargar_inventario()  
    while True:  
        print("----- Gestión de Inventarios -----")  
        print(' 1) Crear Producto \n 2) Mostrar Productos\n 3) Mostrar Producto\n 4) Actualizar Producto\n 5) Eliminar Producto\n 6) Salir')  
        escoger = int(input("Ingrese una opción: ")) 
        if escoger == 1:  
            crear_producto(inventario)  
        elif escoger == 2:  
            mostrar_productos(inventario)  
        elif escoger == 3:  
            mostrar_producto(inventario)  
        elif escoger == 4:  
            actualizar_producto(inventario)  
        elif escoger == 5:  
            eliminar_producto(inventario)  
        elif escoger == 6:  
            break  
        else:  
            print("Ingreso un número no válido.")  



if __name__ == "__main__":  
    main()
    
    
    

   
    

            
    
    
    



    
    
    
    
    