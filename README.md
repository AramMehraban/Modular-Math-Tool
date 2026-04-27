# Modular Math Tool 

![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Ein modulares Python-Projekt für Grundrechenarten mit **User Input** und **Unit Tests**.


## Features
- Addition, Subtraction, Multiplication, Division
- Unterstützung für Benutzereingaben
- Handling von Division durch Null
- Unit Tests inklusive
- Modularer Aufbau für einfache Erweiterung


## Installation

```bash
git clone https://github.com/AramMehraban/modular-math-tool.git
cd modular-math-tool
pip install -r requirements.txt
```
Hinweis: Für dieses Projekt werden nur Standard-Python-Bibliotheken verwendet, daher ist requirements.txt optional.


## Usage

```bash
python main.py
```

### Beispiel:
```
Willkommen beim Modular Math Tool 
Gib die erste Zahl ein: 10
Gib die zweite Zahl ein: 5
10.0 + 5.0 = 15.0
10.0 - 5.0 = 5.0
10.0 * 5.0 = 50.0
10.0 / 5.0 = 2.0
```

## Testing

```bash
pytest tests/
```

Alle Unit Tests werden automatisch ausgeführt, um die Funktionen zu überprüfen.


## Project Structure
```
modular-math-tool/
│── main.py
│── math_operations.py
│── tests/
│   └── test_math_operations.py
│── requirements.txt
│── README.md
│── LICENSE
│── .gitignore
```


## Future Improvements

- Weitere mathematische Funktionen hinzufügen (z.B. Potenz, Quadratwurzel)
- GUI oder Web-Interface
- Erweiterte Eingabevalidierung und Fehlermanagement
- Continuous Integration (CI) mit GitHub Actions


## Author
Aram Mehraban 
- Beispielprojekt für modulares Python-Design

