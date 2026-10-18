#!/usr/bin/env python3
"""
MCP Server con Safety Gate para Laboratorios Locales (DockerLabs, HackMyVM, THM, HTB).
Restringe estrictamente cualquier ejecución a rangos IPv4 privados/locales autorizados.
"""

import ipaddress
import shlex
import subprocess
from urllib.parse import urlparse
try:
    from mcp.server.mcpserver import MCPServer as FastMCP
except ImportError:
    from mcp.server.fastmcp import FastMCP

mcp = FastMCP("redteam-lab-gate")

ALLOWED_LAB_NETWORKS = [
    ipaddress.ip_network("172.16.0.0/12"),   # DockerLabs / Contenedores locales
    ipaddress.ip_network("192.168.0.0/16"),  # HackMyVM / VirtualBox / LAN Laboratorio
    ipaddress.ip_network("10.0.0.0/8"),      # VPNs de CTF (TryHackMe / HackTheBox)
    ipaddress.ip_network("127.0.0.0/8"),     # Loopback local
]


def _is_authorized_lab_ip(host: str) -> tuple[bool, str]:
    """Verifica mediante ipaddress que el host sea una IP dentro de los rangos de laboratorio."""
    try:
        ip_obj = ipaddress.ip_address(host.strip())
    except ValueError:
        return (
            False,
            f"[SAFETY GATE BLOCKED] '{host}' no es una dirección IP literal válida. "
            "Usa únicamente IPs privadas del laboratorio.",
        )

    for net in ALLOWED_LAB_NETWORKS:
        if ip_obj in net:
            return True, str(ip_obj)

    return (
        False,
        f"[SAFETY GATE BLOCKED] La IP '{ip_obj}' está fuera de los rangos privados de laboratorio "
        "(172.16.0.0/12, 192.168.0.0/16, 10.0.0.0/8, 127.0.0.0/8). Ejecución denegada.",
    )


def _extract_and_validate_url_host(target_url: str) -> tuple[bool, str]:
    """Extrae el host de una URL HTTP/HTTPS y valida que pertenezca al laboratorio."""
    parsed = urlparse(target_url.strip())
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        return (
            False,
            f"[SAFETY GATE BLOCKED] URL inválida '{target_url}'. Debe incluir esquema http:// o https:// e IP de laboratorio.",
        )
    return _is_authorized_lab_ip(parsed.hostname)


@mcp.tool()
def lab_nmap_scan(
    target_ip: str,
    ports: str = "-p-",
    extra_flags: str = "-sV -T4 --open",
) -> str:
    """
    Ejecuta nmap contra una IP autorizada del laboratorio local y devuelve el resultado.
    """
    ok, msg = _is_authorized_lab_ip(target_ip)
    if not ok:
        return msg

    cmd = ["nmap", "-n", "-Pn"]
    if ports.strip():
        cmd.extend(shlex.split(ports.strip()))
    if extra_flags.strip():
        cmd.extend(shlex.split(extra_flags.strip()))
    cmd.append(msg)

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
            check=False,
        )
        output = proc.stdout or ""
        if proc.stderr:
            output += f"\n[stderr]\n{proc.stderr}"
        return output.strip() or f"nmap finalizó con código {proc.returncode} sin salida."
    except Exception as exc:
        return f"[ERROR lab_nmap_scan] {exc}"


@mcp.tool()
def lab_web_enum(
    target_url: str,
    wordlist: str = "/usr/share/wordlists/dirb/common.txt",
) -> str:
    """
    Verifica que la URL pertenezca a una IP autorizada del laboratorio y ejecuta gobuster dir.
    """
    ok, msg = _extract_and_validate_url_host(target_url)
    if not ok:
        return msg

    cmd = [
        "gobuster",
        "dir",
        "-u",
        target_url.strip(),
        "-w",
        wordlist.strip(),
        "-q",
        "--no-error",
    ]

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
            check=False,
        )
        output = proc.stdout or ""
        if proc.stderr:
            output += f"\n[stderr]\n{proc.stderr}"
        return output.strip() or "Sin rutas descubiertas por gobuster."
    except Exception as exc:
        return f"[ERROR lab_web_enum] {exc}"


@mcp.tool()
def lab_http_inspect(target_url: str) -> str:
    """
    Verifica que la URL pertenezca al laboratorio y devuelve cabeceras y cuerpo HTTP con curl.
    """
    ok, msg = _extract_and_validate_url_host(target_url)
    if not ok:
        return msg

    cmd = [
        "curl",
        "-i",
        "-s",
        "-L",
        "--max-time",
        "15",
        target_url.strip(),
    ]

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=20,
            check=False,
        )
        output = proc.stdout or ""
        if proc.stderr:
            output += f"\n[stderr]\n{proc.stderr}"
        return output[:15000] if output else f"curl finalizó con código {proc.returncode} sin cuerpo."
    except Exception as exc:
        return f"[ERROR lab_http_inspect] {exc}"


if __name__ == "__main__":
    mcp.run()
