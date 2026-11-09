# Periodic Table Information Finder
from pyscript import display, document

non_metals = {
    "H": {"name": "Hydrogen", "atomic_num": 1, "atomic_mass": "1.008"},
    "O": {"name": "Oxygen", "atomic_num": 8, "atomic_mass": "15.999"},
    "N": {"name": "Nitrogen", "atomic_num": 7, "atomic_mass": "14.007"},
    "C": {"name": "Carbon", "atomic_num": 6, "atomic_mass": "12.011"},
    "S": {"name": "Sulfur", "atomic_num": 16, "atomic_mass": "32.06"},
    "Cl": {"name": "Chlorine", "atomic_num": 17, "atomic_mass": "35.45"},
    "F": {"name": "Fluorine", "atomic_num": 9, "atomic_mass": "18.998"},
    "P": {"name": "Phosphorus", "atomic_num": 15, "atomic_mass": "30.974"},
    "Br": {"name": "Bromine", "atomic_num": 35, "atomic_mass": "79.904"},
    "I": {"name": "Iodine", "atomic_num": 53, "atomic_mass": "126.90"}
}

def check_element(e):
    document.getElementById("result").innerHTML = ""
    symbol = document.getElementById("element_symbol").value.strip()

    data = non_metals[symbol]
    display(f"Symbol: {symbol}", target="result")
    display(f"Element: {data['name']}", target="result")
    display(f"Atomic Number: {data['atomic_num']}", target="result")
    display(f"Atomic Mass: {data['atomic_mass']}", target="result")