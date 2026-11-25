import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)


def calcola_costi(record):
    """Aggiunge a ogni fornitore la chiave 'costo'."""
    for r in record:
        r["costo"] = round(r["distanza_km"] * r["tariffa_km"] * r["volume_m3"], 2)


def fornitore_migliore(record):
    """Restituisce il dizionario del fornitore con costo minimo."""
    migliore = record[0]
    for r in record:
        if r["costo"] < migliore["costo"]:
            migliore = r
    return migliore


df = pd.read_excel("dati/cantieri/villacidro_casa_di_riposo.xlsx")
record = df.to_dict(orient="records")

calcola_costi(record)
m = fornitore_migliore(record)
print("Fornitore più economico:", m["fornitore"], "-", m["costo"], "€")

