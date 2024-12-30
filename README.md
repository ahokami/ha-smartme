# Smart-me Integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

This integration allows you to monitor your Smart-me energy meters in Home Assistant.

[Version française](#intégration-smart-me-pour-home-assistant)

## Features

- Easy configuration through the UI
- Automatic device discovery
- Support for multiple meters
- Real-time power consumption monitoring
- Detailed energy statistics
- Support for three-phase measurements

## Installation

### HACS Installation (Recommended)

1. Open HACS in your Home Assistant instance
2. Click on "Integrations"
3. Click the three dots in the top right corner
4. Select "Custom repositories"
5. Add this repository URL and select "Integration" as the category
6. Click "Add"
7. Search for "Smart-me" in HACS
8. Click "Install"
9. Restart Home Assistant

### Manual Installation

1. Copy the `custom_components/smartme` directory to your Home Assistant's `custom_components` directory
2. Restart Home Assistant

## Configuration

1. Go to Settings -> Devices & Services
2. Click "Add Integration"
3. Search for "Smart-me"
4. Enter your Smart-me credentials (username and password)
5. Select the meters you want to monitor
6. Click "Submit"

## Available Sensors

Each meter will create a device with the following sensors:

- Active Power (total and per phase)
- Counter Reading (total, T1, T2, import, export)
- Voltage (total and per phase)
- Current (per phase)
- Power Factor (total and per phase)
- Digital Output Status
- Last Update Timestamp

## Troubleshooting

If you encounter any issues:

1. Check your credentials
2. Verify your internet connection
3. Ensure your Smart-me devices are online
4. Check the Home Assistant logs for any error messages

---

# Intégration Smart-me pour Home Assistant

## Fonctionnalités

- Configuration facile via l'interface utilisateur
- Découverte automatique des appareils
- Support de plusieurs compteurs
- Surveillance en temps réel de la consommation d'énergie
- Statistiques énergétiques détaillées
- Support des mesures triphasées

## Installation

### Installation via HACS (Recommandée)

1. Ouvrez HACS dans votre instance Home Assistant
2. Cliquez sur "Intégrations"
3. Cliquez sur les trois points en haut à droite
4. Sélectionnez "Dépôts personnalisés"
5. Ajoutez l'URL de ce dépôt et sélectionnez "Integration" comme catégorie
6. Cliquez sur "Ajouter"
7. Recherchez "Smart-me" dans HACS
8. Cliquez sur "Installer"
9. Redémarrez Home Assistant

### Installation Manuelle

1. Copiez le répertoire `custom_components/smartme` dans votre dossier `custom_components` de Home Assistant
2. Redémarrez Home Assistant

## Configuration

1. Allez dans Paramètres -> Appareils et Services
2. Cliquez sur "Ajouter une intégration"
3. Recherchez "Smart-me"
4. Entrez vos identifiants Smart-me (nom d'utilisateur et mot de passe)
5. Sélectionnez les compteurs que vous souhaitez surveiller
6. Cliquez sur "Soumettre"

## Capteurs Disponibles

Chaque compteur créera un appareil avec les capteurs suivants :

- Puissance Active (totale et par phase)
- Relevé de Compteur (total, T1, T2, import, export)
- Tension (totale et par phase)
- Courant (par phase)
- Facteur de Puissance (total et par phase)
- État de la Sortie Digitale
- Horodatage de la Dernière Mise à Jour

## Dépannage

Si vous rencontrez des problèmes :

1. Vérifiez vos identifiants
2. Vérifiez votre connexion internet
3. Assurez-vous que vos appareils Smart-me sont en ligne
4. Consultez les logs de Home Assistant pour les messages d'erreur