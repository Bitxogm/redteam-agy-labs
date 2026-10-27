# RED TEAM & CTF PENTESTING WORKSPACE

> **Workspace de pentest/CTF/laboratorio en `~/redteam`.** El equipo CSIRT y los especialistas ofensivos están definidos globalmente en `~/.claude/agents/` (ver `~/.claude/CLAUDE.md`). Este fichero añade únicamente **contexto específico del proyecto**: estructura de carpetas por máquina y formato de respuesta cuando se opera en este workspace.
>
> **Objetivo**: Resolución ofensiva y metódica de laboratorios de Hacking Ético y CTFs (**DockerLabs, HackMyVM, TryHackMe, HackTheBox**) desde **Kali Linux**.
>
> **MCP server**: `csirt-lab-gate` registrado globalmente, con herramientas `lab_nmap_scan`, `lab_web_enum`, `lab_http_inspect` (Safety Gate para rangos IPv4 privados). Preferir siempre sobre terminal cruda cuando el objetivo encaje.

---

## 1. Estructura de Trabajo por Máquina y Writeups para GitHub

Cada laboratorio o máquina se trabaja en `machines/` y, al completarla (o durante el proceso), el **🎯 Líder** coordina al agente `writeup` para generar el Writeup completo para la comunidad en `writeups/`:
```text
~/redteam/
├── machines/<plataforma>-<nombre>/
│   ├── nmap/        # Escaneos de puertos y servicios (ports.nmap, targeted.nmap)
│   ├── web/         # Resultados de fuzzing (ffuf, gobuster, código descargado)
│   ├── exploits/    # Scripts, payloads, webshells, PoCs modificados
│   ├── loot/        # Hashes, credenciales, claves SSH, flags encontradas
│   └── notes.md     # Bitácora viva gestionada por el Líder
└── writeups/
    ├── dockerlabs/  # Writeups públicos paso a paso de DockerLabs
    └── hackmyvm/    # Writeups públicos paso a paso de HackMyVM
```
- **Regla de Comunidad en Writeups (`writeups/`)**: Incluye siempre el paso a paso claro, los comandos exactos, las **credenciales encontradas**, las **flags (`user.txt` y `root.txt`)** y un apartado de *"💡 Pista clave / Dónde es fácil atascarse"* para ayudar a cualquiera de la comunidad que se quede bloqueado, usando la plantilla [`writeups/TEMPLATE-writeup.md`](file:///home/ladybaba2000/redteam/writeups/TEMPLATE-writeup.md).

---

## 2. Formato de Respuesta del Equipo

Cuando trabajes en una máquina dentro de `~/redteam`, estructura siempre tus avances separando claramente qué miembro del equipo interviene según la fase actual:
- **🎯 [LÍDER]**: Estado actual de la máquina, hipótesis principal y qué descartamos.
- **🔍 [RECON & ENUM]** *(si estamos enumerando o descubriendo vectores)*: Comandos exactos y análisis de salidas.
- **💥 [EXPLOIT]** *(si hay vector de entrada o ataque web/servicio)*: Payload, comando o ajuste del exploit para lograr shell.
- **👑 [PRIVESC]** *(una vez dentro de la máquina)*: Enumeración interna y vector de escalada a `root`.
