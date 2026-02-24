import streamlit as st

st.set_page_config(page_title="Rezept-Planer", page_icon="🍳")
st.title("🍳 Dein persönlicher Mahlzeiten-Planer")

# Auswahl-Speicher vorbereiten
if 'auswahl' not in st.session_state:
    st.session_state.auswahl = {"gemüse": [], "carbs": "", "protein": "", "sauce": "", "stil": ""}

# Navigation
step = st.sidebar.radio("Navigation", ["1. Gemüse", "2. Kohlenhydrate", "3. Protein", "4. Sauce", "5. Stil", "6. Ergebnis"])

if step == "1. Gemüse":
    st.header("🥦 Wähle dein Gemüse")
    gemuese_liste = ["Tomaten", "Zucchini", "Paprika", "Brokkoli", "Spinat", "Karotten", "Pilze", "Zwiebeln", "Lauch", "Auberginen"]
    st.session_state.auswahl["gemüse"] = st.multiselect("Was hast du da?", gemuese_liste)

elif step == "2. Kohlenhydrate":
    st.header("🍝 Kohlenhydrate")
    kategorie = st.selectbox("Kategorie", ["Kartoffeln", "Nudeln", "Reis", "Alternative"])
    options = {
        "Kartoffeln": ["Süßkartoffel", "Festkochend", "Mehlig"],
        "Nudeln": ["Spaghetti", "Penne", "Fusilli"],
        "Reis": ["Basmati", "Wildreis", "Jasmin"],
        "Alternative": ["Quinoa", "Couscous", "Hirse", "Steckrübe"]
    }
    st.session_state.auswahl["carbs"] = st.selectbox("Welche Sorte?", options[kategorie])

elif step == "3. Protein":
    st.header("🥩 Protein-Quelle")
    st.session_state.auswahl["protein"] = st.radio("Was wählst du?", ["Rind", "Hähnchen", "Fisch", "Tofu", "Linsen", "Kein Tier"])

elif step == "4. Sauce":
    st.header("🥛 Saucenbasis")
    st.session_state.auswahl["sauce"] = st.radio("Basis:", ["Sahne", "Kokosmilch", "Tomatenpassata", "Gemüsebrühe"])

elif step == "5. Stil":
    st.header("🥗 Ernährungsstil")
    st.session_state.auswahl["stil"] = st.radio("Wie soll es sein?", ["Omnivor", "Vegetarisch", "Vegan"])

elif step == "6. Ergebnis":
    st.header("🍽️ Dein Plan & Einkaufsliste")
    a = st.session_state.auswahl
    st.success(f"Bereit für ein {a['stil']}es Gericht!")
    st.write(f"Kombination: **{a['protein']}** mit **{a['carbs']}** und **{', '.join(a['gemüse'])}**.")
    
    st.subheader("🛒 Einkaufsliste")
    zutaten = a['gemüse'] + [a['carbs'], a['protein'], a['sauce']]
    for z in zutaten:
        if z != "Kein Tier":
            st.write(f"- [ ] {z}")
