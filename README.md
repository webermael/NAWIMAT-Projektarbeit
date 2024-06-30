# NAWIMAT-Projektarbeit

## Implementation

### Backend

#### Welt
- Klasse World (Gesamte Welt, bestehend aus Feldern)
- Klasse Tile (einzelnes Feld)
    - Kann "Umweltfaktoren" enthalten

#### Organismus
- Klasse Organismus
    - Methode move() (wird so programmiert, dass später Outputs vom neuronalen Netz als Inputs genutzt werden können)
    - Einzelne Methoden für jeweilige Sensoren
    - Attribute:
        - Lebendig / Tot (mehrere "Leben?")
        - weitere?

#### Neuronales Netz
- Eigenständige Klasse oder als Teil des Orgnismus
- Wandelt Inputs von Sensoren in Outputs in Form von Bewegung um


### Frontend (wird während der Backendentwicklung noch genauer definiert)
- Darstellung der Welt
- Darstellung der Organismen
- Inputmöglichkeiten von Benutzer


## Installation
-> `docs/installation.md`

## Usage
-> `docs/usage.md`
