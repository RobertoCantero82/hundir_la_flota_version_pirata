<p align="center">
  <img src="https://raw.githubusercontent.com/tu-usuario/tu-repo/main/reports/figures/battleship_banner.png" alt="Battleship Coding The Deep Banner" width="100%">
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python Version">
    <img src="https://img.shields.io/badge/Status-Project%20Delivered-green.svg" alt="Project Status">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
    <a href="https://linkedin.com/in/tu-perfil"><img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555" alt="LinkedIn"></a>
</p>

<h1 align="center">⚓ Battleship: Coding the Deep ⚓</h1>

<p align="center">
  <b>Simulador de estrategia naval desarrollado en Python para el Bootcamp de Data Science de The Bridge.</b>
</p>

---

## 📖 Misión y Objetivos

Este proyecto no es solo una recreación del clásico juego de mesa. Es un desafío de ingeniería para construir un **motor de lógica de juego robusto** basado en Programación Orientada a Objetos (POO). El objetivo fue desarrollar un sistema capaz de gestionar:

1.  **Lógica Compleja de Tableros:** Colocación validada de flotas y gestión de estados de casillas (Agua/Tocado/Hundido).
2.  **Un Oponente Táctico:** Implementación de una IA que no solo dispara al azar, sino que toma decisiones basadas en el historial de combate.
3.  **Flujo de Turnos Asíncrono:** Gestión limpia del bucle de juego Jugador vs. Máquina.

---

## 👁️ Visualización del Combate

<p align="center">
  <img src="https://raw.githubusercontent.com/tu-usuario/tu-repo/main/reports/figures/gameplay_demo.gif" alt="Gameplay Demo" width="70%">
  <br>
  <i>Vista del puente de mando: Tablero táctico en consola con feedback visual de impactos.</i>
</p>

---

## 🏗️ Arquitectura del Sistema (Diagrama)

Para este proyecto, decidí utilizar un enfoque de **Programación Orientada a Objetos (POO)** para asegurar la escalabilidad del código. Aquí puedes ver cómo interactúan las clases principales:

```mermaid
classDiagram
    class GameEngine {
        +Player human
        +Player ai
        +start_game()
        +game_loop()
    }
    class Player {
        +Board board
        +Fleet fleet
        +string name
        +attack(coordinate)
    }
    class AIOponent {
        +list attack_history
        +strategy_level
        +make_decision()
    }
    class Board {
        +matrix grid
        +place_ship(ship, coord)
        +receive_shot(coord)
    }
    class Ship {
        +string type
        +int size
        +int hits
        +is_sunk()
    }

    GameEngine --> Player : manages
    Player <|-- AIOponent : inherits
    Player --> Board : owns
    Board --> Ship : contains
