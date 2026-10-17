# 🛡️ Red Team & CTF Workspace (Antigravity / Gemini)

Espacio de trabajo exclusivo para **Antigravity (`agy` / App / IDE)** dedicado a laboratorios de Hacking Ético (**DockerLabs, HackMyVM, TryHackMe, HackTheBox**).

## 👥 Equipo Activo Automáticamente (`GEMINI.md`)
- **🎯 Team Lead**: Estrategia, priorización (`RCE > Credenciales > Web/LFI/SQLi > SUID/Sudo/Capabilities`) y bitácora `notes.md`.
- **🔍 Recon & Enum**: Descubrimiento de red, `nmap`, fuzzing web (`ffuf`, `gobuster`), VHosts y enumeración de servicios.
- **💥 Exploit & Web/AD**: Explotación web/servicios, payloads, cracking de hashes y acceso inicial (reverse shell).
- **👑 PrivEsc & Post-Exploit**: Escalada de privilegios a `root`, GTFOBins, SUID, `sudo -l`, capabilities, cronjobs y pivoting.

## 📂 Estructura del Repositorio (`redteam-agy-labs`)
- [`GEMINI.md`](./GEMINI.md): Reglas y protocolo del equipo ofensivo (cargado automáticamente por Antigravity al entrar aquí).
- [`.agents/skills/pentest-team/SKILL.md`](./.agents/skills/pentest-team/SKILL.md): Flujo de trabajo para crear carpetas de máquinas, coordinar al equipo y generar writeups.
- [`.agents/agents/`](./.agents/agents/): Definiciones de los especialistas (`recon-enum`, `exploit-specialist`, `privesc-post`).
- [`machines/`](./machines/): Directorio de trabajo técnico de cada máquina (`machines/<nombre>/{nmap,web,exploits,loot,notes.md}`).
- [`writeups/`](./writeups/): Writeups completos paso a paso (con pistas para desatascarse, credenciales y flags incluidas para ayudar a la comunidad):
  - 🐳 [**Writeups de DockerLabs**](./writeups/dockerlabs/README.md)
  - 虚拟机 [**Writeups de HackMyVM**](./writeups/hackmyvm/README.md)

