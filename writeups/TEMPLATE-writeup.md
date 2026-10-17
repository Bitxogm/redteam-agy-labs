# 🏴‍☠️ Writeup: <NOMBRE_MAQUINA> (<PLATAFORMA>)

- **Plataforma:** DockerLabs / HackMyVM
- **Dificultad:** Fácil / Media / Difícil
- **IP de Laboratorio:** `<IP>`
- **Autor:** [Bitxogm](https://github.com/Bitxogm) (con el Equipo RedTeam de Antigravity)

---

## 📋 Resumen Rápido (Para quien se haya quedado atascado)
- **Vector de Entrada (Foothold):** 
- **Escalada de Privilegios (Root):** 
- **💡 Pista clave / Rabbit Hole a evitar:** 

---

## 🔍 1. Reconocimiento y Enumeración (`Recon & Enum`)

### Escaneo de Puertos (`nmap`)
```bash
nmap -p- --open -sS --min-rate 5000 -n -Pn <IP>
nmap -sCV -p<PUERTOS> <IP>
```

### Enumeración Web / Servicios
```bash
# Comandos utilizados (gobuster, ffuf, whatweb, etc.)
```

---

## 💥 2. Explotación y Acceso Inicial (`Exploit Specialist`)

Explicación paso a paso de cómo conseguir la primera shell:

```bash
# Comandos / Payload utilizado
```

- **Usuario obtenido:** ``
- ** Credenciales encontradas:** ``

---

## 👑 3. Escalada de Privilegios a Root (`PrivEsc Specialist`)

Enumeración interna (`sudo -l`, SUID, Capabilities, Cronjobs) y comando exacto para obtener `root`:

```bash
# Comandos de escalada
```

---

## 🏆 4. Flags y Credenciales (Ayuda para la Comunidad)
- **User Flag (`user.txt`):** ``
- **Root Flag (`root.txt`):** ``
- **Usuarios / Contraseñas del Lab:**
  - `` : ``
