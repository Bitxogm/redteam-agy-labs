# 🔵 CSIRT Informe Técnico: Invernadero (192.168.0.223)

- **Entorno**: Laboratorio local HackMyVM (`192.168.0.223` en `wlan0`)
- **Estado**: 🔍 Análisis técnico de servicios web (`22`, `80`, `8080`)

---

## 🔴 1. Servicios Detectados (`nmap`)
| Puerto | Servicio / Versión | Observaciones |
| :--- | :--- | :--- |
| `22/tcp` | `OpenSSH 10.3 (protocol 2.0)` | SSH activo |
| `80/tcp` | `Apache httpd 2.4.68 ((Unix))` | Página por defecto `It works! Apache httpd` |
| `8080/tcp` | `Werkzeug httpd 3.1.8 (Python 3.9.25)` | Panel `Invernadero IoT` (redirige a `/login`) |

## 🔴 2. Análisis de Rutas y Endpoints (`:8080` y `:80`)
- `/login`: Formulario `POST` (`username`, `password`)
- `/sens`: Estadísticas ESP32
- `/alerts`: Alertas
