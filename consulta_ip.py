import requests
import json

def checar_ip(ip):
    link = "http://ip-api.com/json/" + ip
    r = requests.get(link)
    
    if r.status_code == 200:
        info = r.json()
        
        if info["status"] == "success":
            datos = {
                "ip": ip,
                "pais": info["country"],
                "region": info["regionName"],
                "compania_internet": info["isp"],
                "lat": info["lat"],
                "lon": info["lon"]
            }
            return datos
        else:
            return {"ip": ip, "error": "No se encontró info"}
    else:
        return {"ip": ip, "error": "No se pudo hacer la consulta"}

def principal():
    todo = []
    
    while True:
        ip = input("Pon una IP pública (o escribe 'exit' pa terminar): ")
        if ip.lower() == "exit":
            break
        
        resultado = checar_ip(ip)
        print(json.dumps(resultado, indent=4))
        todo.append(resultado)
    
    archivo = open("datos_guardados.json", "w")
    json.dump(todo, archivo, indent=4)
    archivo.close()
    
    print("Listo! Se guardó todo en datos_guardados.json")

if __name__ == "__main__":
    principal()
