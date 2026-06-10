# MacroTracker
This is my first project.  I hope you will like this

# 🍏 MacroTracker: Simple Daily Calorie & Protein Tracker

Welcome to **MacroTracker**! This is a command-line interface (CLI) Python application designed to help users log their daily food intake, track total calories and protein, and build a reusable database of food items. 

This project demonstrates clean modular programming, JSON and CSV file persistence, and robust user-input validation.

---

## 🚀 Key Features

* **Smart Food Memory**: Learns new foods dynamically. If a food doesn't exist in your database (`foods.json`), it asks for its profile once and calculates macros per unit.
* **Persistent Daily Logs**: Saves your total daily breakdown (date, total calories, total protein) into a structured CSV file (`user_history.csv`).
* **History Reviewer**: Includes a built-in terminal reader to let you review your entire historic log at the end of a session.
* **Input Validation**: Safely handles typos, missing data, and invalid string/number conversions without crashing the application.

---

## 🛠️ Project Structure

The project is split into two modules to maintain separation of concerns:
* `main.py` - Manages the core application loop, user decisions, and high-level execution flow.
* `functions.py` - Houses modular helper functions handling calculations, file reading/writing (I/O), and console formatting.

---

## 📋 How It Works

1. **Initialize Date**: Enter the current day and month.
2. **Log Food**: Type in the name of the food item and the amount consumed.
3. **Dynamic Calculations**: The script calculates your scaling macros immediately and gives you a rolling daily total.
4. **Data Preservation**: 
   * Updates your global food library to `foods.json`.
   * Appends your daily total summary to `user_history.csv`.
5. **View History**: Choose whether to print all past historical logs directly to your terminal.

---

## ⚙️ Technologies Used

* **Language**: Python 3.x
* **Data Storage**: JSON (for structural object mapping) & CSV (for linear history tracking)
* **Core Modules**: `json`, `csv`, `os`
