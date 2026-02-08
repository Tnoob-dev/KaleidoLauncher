from typing import Dict

class Langs:
    langsDict: Dict[str, Dict[str, str]] = {
        # Dashboard
        "welcome": {
            "en": "\t   Welcome {username}\n",
            "es": "\t   ¡Bienvenido {username}!\n"
        },
        "versionSelected": {
            "en": "Version: {version} API: {api}\n{ascii_art}\n",
            "es": "Versión: {version} API: {api}\n{ascii_art}\n"
        },
        "minecraftInstallationPath": {
            "en": "Minecraft path: {path}",
            "es": "Ruta de Minecraft: {path}"
        },
        "goBackButton": {
            "en": "Go Back",
            "es": "Volver"
        },
        "deleteProfileButton": {
            "en": "Delete Profile",
            "es": "Eliminar Perfil"
        },
        "installButton": {
            "en": "Install",
            "es": "Instalar"
        },
        "startingInstallationStatus": {
            "en": "Starting installation of Minecraft v{version}",
            "es": "Iniciando instalación de Minecraft v{version}"
        },
        "installingStatus": {
            "en": "Installing...",
            "es": "Instalando..."
        },
        "installedStatus": {
            "en": "Installed",
            "es": "Instalado"
        },
        "playButton": {
            "en": "Play!",
            "es": "¡Jugar!"
        },
        "executingStatus": {
            "en": "Executing Minecraft v{version}",
            "es": "Ejecutando Minecraft v{version}"
        },
        "closedStatus": {
            "en": "Minecraft Closed",
            "es": "Minecraft Cerrado"
        },
        
        # Profile Creation
        "profileUsernameLabel": {
            "en": "Profile username:",
            "es": "Nombre del perfil:"
        },
        "pathLabel": {
            "en": "Path:",
            "es": "Ruta:"
        },
        "versionLabel": {
            "en": "Version",
            "es": "Versión"
        },
        "retryButton": {
            "en": "Retry",
            "es": "Reintentar"
        },
        "createButton": {
            "en": "Create",
            "es": "Crear"
        },
        
        # Profile
        "newProfileButton": {
            "en": "New Profile",
            "es": "Nuevo Perfil"
        },
        
        # Errors
        "errorOpening": {
            "en": "Error starting Minecraft -> {error}",
            "es": "Error al iniciar Minecraft -> {error}"
        },
        "connectionError": {
            "en": "Cannot establish connection with Mojang Servers. Check your internet connection.",
            "es": "No se puede establecer conexión con los servidores de Mojang. Verifica tu conexión a internet."
        },
        "connectionErrorSeveral": {
            "en": "Cannot establish connection -> {error}",
            "es": "No se puede establecer conexión -> {error}"
        },
        
        # Notifications
        "readyToPlayNotification": {
            "en": "🎮 Minecraft v{version} ready to play!",
            "es": "🎮 ¡Minecraft v{version} listo para jugar!"
        },
        "profileRemovedNotification": {
            "en": "Profile Removed",
            "es": "Perfil Eliminado"
        }
    }