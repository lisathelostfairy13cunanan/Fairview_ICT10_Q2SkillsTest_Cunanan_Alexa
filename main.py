from pyscript import document, display

# Dictionary containing non-metal information
# KEY: Element Symbol
# VALUE: Element Name, Atomic Number, Atomic Mass

non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Se": ("Selenium", 34, 78.971),
    "Cl": ("Chlorine", 17, 35.45),
    "Br": ("Bromine", 35, 79.904),
    "I": ("Iodine", 53, 126.904),
    "He": ("Helium", 2, 4.003),
    "Ne": ("Neon", 10, 20.180),
    "Ar": ("Argon", 18, 39.948),
    "Kr": ("Krypton", 36, 83.798),
    "Xe": ("Xenon", 54, 131.293),
    "Rn": ("Radon", 86, 222)
}


# function to search for a non-metal element
def search_element(e):

    # get the input from HTML
    Element1 = document.getElementById("element1").value.strip().capitalize()

    #rRetrieve information from dictionary
    result = non_metals.get(Element1, ("Element not found", "-", "-"))

    # display the results in HTML
    document.getElementById("symbol").innerText = Element1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]

    # display a message if the element is not found
    if result[0] == "Element not found":
        document.getElementById("message").innerText = "Element does not exist in the non-metals list."
    else:
        document.getElementById("message").innerText = ""


