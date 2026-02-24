import streamlit as st

st.set_page_config(page_title="Rezept-Profi", page_icon="👨‍🍳", layout="wide")

# Styling für die Buttons
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("👨‍🍳 Dein smarter Rezept-Planer")

if 'auswahl' not in st.session_state:
    st.session_state.auswahl = {"gemüse": [], "carbs": "", "protein": "", "sauce": "", "stil": ""}

# Navigation oben
step = st.select_slider("Schritt für Schritt zum Essen", options=["Gemüse", "Kohlenhydrate", "Protein", "Sauce", "Stil", "Rezept"])

# --- 1. GEMÜSE RASTER ---
if step == "Gemüse":
    st.header("🥦 Welches Gemüse hast du?")
    gemuese_arten = ["🍅 Tomate", "🥒 Zucchini", "🫑 Paprika", "🥦 Brokkoli", "🍃 Spinat", "🥕 Karotten", "🍄 Pilze", "🧅 Zwiebeln", "🌽 Mais", "🍆 Aubergine", "🥦 Blumenkohl", "🥬 Lauch", "🥗 Erbsen", "🧄 Knoblauch", "🎃 Kürbis"]
    
    # Erstellt ein Raster mit 3 Spalten
    cols = st.columns(3)
    for idx, g in enumerate(gemuese_arten):
        if cols[idx % 3].button(g):
            if g not in st.session_state.auswahl["gemüse"]:
                st.session_state.auswahl["gemüse"].append(g)
                st.toast(f"{g} hinzugefügt!")
    
    st.write("### Deine Auswahl:", ", ".join(st.session_state.auswahl["gemüse"]))
    if st.button("Auswahl löschen"):
        st.session_state.auswahl["gemüse"] = []
        st.rerun()

# --- 2. KOHLENHYDRATE ---
elif step == "Kohlenhydrate":
    st.header("🍝 Kohlenhydrate")
    kat = st.radio("Kategorie wählen:", ["Kartoffeln", "Nudeln", "Reis", "Alternative"])
    
    opts = {
        "Kartoffeln": ["Süßkartoffel", "Festkochend", "Mehlig", "Drillinge", "Pommes-Kartoffeln"],
        "Nudeln": ["Spaghetti", "Penne", "Fusilli", "Tagliatelle", "Vollkornnudeln", "Glasnudeln"],
        "Reis": ["Basmati", "Wildreis", "Jasmin", "Risotto-Reis", "Sushi-Reis"],
        "Alternative": ["Quinoa", "Amaranth", "Couscous", "Hirse", "Steckrübe", "Bulgur", "Polenta", "Linsen-Pasta"]
    }
    st.session_state.auswahl["carbs"] = st.selectbox("Sorte wählen:", opts[kat])

# --- 3. PROTEIN ---
elif step == "Protein":
    st.header("🥩 Protein")
    st.session_state.auswahl["protein"] = st.radio("Was darf es sein?", 
        ["Rind", "Hähnchen", "Schwein", "Lamm", "Lachs", "Kabeljau", "Garnelen", "Tofu", "Kichererbsen", "Linsen", "Eier", "Kein Tier"])

# --- 4. SAUCE ---
elif step == "Sauce":
    st.header("🥛 Saucenbasis")
    st.session_state.auswahl["sauce"] = st.radio("Basis:", 
        ["Sahne", "Kokosmilch", "Tomatenpassata", "Gemüsebrühe", "Frischkäse", "Pesto", "Sojasauce", "Weißwein-Sud"])

# --- 5. STIL ---
elif step == "Stil":
    st.header("🥗 Ernährungsstil")
    st.session_state.auswahl["stil"] = st.radio("Art:", ["Omnivor (Alles)", "Vegetarisch", "Vegan"])

# --- 6. ERGEBNIS & REZEPT ---
elif step == "Rezept":
    a = st.session_state.auswahl
    if not a["gemüse"]:
        st.warning("Bitte wähle zuerst Gemüse aus!")
    else:
        st.header("🍽️ Dein persönliches Rezept")
        
        # Simuliertes Rezept (Logik)
        titel = f"{a['stil']}e Pfanne mit {a['protein']} und {a['carbs']}"
        st.subheader(titel)
        
        st.markdown(f"""
        **Zutaten:**
        * {', '.join(a['gemüse'])}
        * {a['carbs']}
        * {a['protein']}
        * Basis: {a['sauce']}
        * Gewürze: Salz, Pfeffer, Kräuter der Saison
        
        **Zubereitung:**
        1. {a['carbs']} nach Packungsanweisung kochen.
        2. {a['protein']} in einer Pfanne scharf anbraten, dann herausnehmen.
        3. Das Gemüse ({', '.join(a['gemüse'])}) in derselben Pfanne dünsten.
        4. Mit {a['sauce']} ablöschen und kurz köcheln lassen.
        5. Alles vermengen und genießen!
        """)
        
        st.subheader("🛒 Einkaufsliste")
        for z in a['gemüse'] + [a['carbs'], a['protein'], a['sauce']]:
            if "Kein Tier" not in z:
                st.write(f"- [ ] {z}")
