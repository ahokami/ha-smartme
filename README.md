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

### HACS Installation (Custom Repository)

1. Open HACS in your Home Assistant instance
2. Click on the three dots in the top right corner
3. Select "Custom repositories"
4. Add this repository URL: `https://github.com/ahokami/ha-smartme`
5. Select "Integration" as the category
6. Click "Add"
7. Click on "Smart-me" in the integration list
8. Click "Download"
9. Restart Home Assistant

### Manual Installation

1. Copy the `custom_components/smartme` directory to your Home Assistant's `custom_components` directory
2. Restart Home Assistant

## Configuration

1. Go to Settings -> Devices & Services
2. Click "Add Integration"
3. Search for "Smart-me"
4. Enter your Smart-me credentials (username and password)
5. Click "Submit"

## Available Sensors

Each meter will create a device with the following sensors:

### Power Measurements
- Active Power (total)
- Active Power L1, L2, L3 (per phase)

### Energy Readings
- Counter Reading (total)
- Counter Reading T1, T2 (tariff periods)
- Counter Reading Import/Export

### Voltage Measurements
- Voltage (total)
- Voltage L1, L2, L3 (per phase)

### Current Measurements
- Current L1, L2, L3 (per phase)

### Power Factor
- Power Factor (total)
- Power Factor L1, L2, L3 (per phase)

### Other
- Digital Output Status
- Last Update Timestamp

## Troubleshooting

If you encounter any issues:

1. Check your credentials
2. Verify your internet connection
3. Ensure your Smart-me devices are online
4. Check the Home Assistant logs for any error messages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

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

### Installation via HACS (Dépôt Personnalisé)

1. Ouvrez HACS dans votre instance Home Assistant
2. Cliquez sur les trois points en haut à droite
3. Sélectionnez "Dépôts personnalisés"
4. Ajoutez l'URL du dépôt : `https://github.com/ahokami/ha-smartme`
5. Sélectionnez "Integration" comme catégorie
6. Cliquez sur "Ajouter"
7. Cliquez sur "Smart-me" dans la liste des intégrations
8. Cliquez sur "Télécharger"
9. Redémarrez Home Assistant

### Installation Manuelle

1. Copiez le répertoire `custom_components/smartme` dans votre dossier `custom_components` de Home Assistant
2. Redémarrez Home Assistant

## Configuration

1. Allez dans Paramètres -> Appareils et Services
2. Cliquez sur "Ajouter une intégration"
3. Recherchez "Smart-me"
4. Entrez vos identifiants Smart-me (nom d'utilisateur et mot de passe)
5. Cliquez sur "Soumettre"

## Capteurs Disponibles

Chaque compteur créera un appareil avec les capteurs suivants :

### Mesures de Puissance
- Puissance Active (totale)
- Puissance Active L1, L2, L3 (par phase)

### Relevés d'Énergie
- Relevé de Compteur (total)
- Relevé de Compteur T1, T2 (périodes tarifaires)
- Relevé de Compteur Import/Export

### Mesures de Tension
- Tension (totale)
- Tension L1, L2, L3 (par phase)

### Mesures de Courant
- Courant L1, L2, L3 (par phase)

### Facteur de Puissance
- Facteur de Puissance (total)
- Facteur de Puissance L1, L2, L3 (par phase)

### Autres
- État de la Sortie Digitale
- Horodatage de la Dernière Mise à Jour

## Dépannage

Si vous rencontrez des problèmes :

1. Vérifiez vos identifiants
2. Vérifiez votre connexion internet
3. Assurez-vous que vos appareils Smart-me sont en ligne
4. Consultez les logs de Home Assistant pour les messages d'erreur

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à soumettre une Pull Request.