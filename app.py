import streamlit as st

# 1. Grundkonfiguration und Design
st.set_page_config(page_title="Rezept-Profi", page_icon="👨‍🍳")

# Hier bringen wir Farbe ins Spiel (Gelb/Grün Layout)
st.markdown("""
    <style>
    /* Hintergrundfarbe */
    .stApp {
        background-color: #f7fceb;
    }
    /* Buttons Styling */
    div.stButton > button {
        width: 100%;
        border-radius: 15px;
        height: 3.5em;
        background-color: #d4e157; /* Hellgrün */
        color: #33691e;
        border: 2px solid #9eb23b;
        font-weight: bold;
    }
    /* "Weiter" Button speziell hervorheben */
    div.stButton > button:hover {
        background-color: #fbc02d; /* Gelb beim Hover */
        border-color: #f9a825;
    }
    h1, h2, h3 {
        color: #33691e;
        font-family: 'Arial';
    }
    </style>
    """, unsafe_allow_html=True)

# 2. App-Logik (Speicher für die Auswahl)
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'auswahl' not in st.session_state:
    st.session_state.auswahl = {"gemüse": [], "carbs": "", "protein": "", "sauce": "", "stil": ""}

# Funktionen zum Navigieren
def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

st.title("👨‍🍳 Dein Mahlzeiten-Konfigurator")

# --- SCHRITT 1: GEMÜSE ---
if st.session_state.step == 1:
    st.header("Schritt 1: Wähle dein Gemüse 🥦")
    gemuese_arten = ["🍅 Tomate", "🥒 Zucchini", "🫑 Paprika", "🥦 Brokkoli", "🍃 Spinat", "🥕 Karotten", "🍄 Pilze", "🧅 Zwiebeln", "🌽 Mais", "🍆 Aubergine", "🥦 Blumenkohl", "🥬 Lauch", "🥗 Erbsen", "🧄 Knoblauch", "🎃 Kürbis"]
    
    cols = st.columns(3)
    for idx, g in enumerate(gemuese_arten):
        if cols[idx % 3].button(g):
            if g not in st.session_state.auswahl["gemüse"]:
                st.session_state.auswahl["gemüse"].append(g)
    
    st.info(f"Ausgewählt: {', '.join(st.session_state.auswahl['gemüse']) if st.session_state.auswahl['gemüse'] else 'Nichts'}")
    
    col_a, col_b = st.columns(2)
    if col_a.button("Auswahl löschen"):
        st.session_state.auswahl["gemüse"] = []
        st.rerun()
    if st.session_state.auswahl["gemüse"]:
        if col_b.button("Weiter ➡️"): next_step(); st.rerun()

# --- SCHRITT 2: KOHLENHYDRATE ---
elif st.session_state.step == 2:
    st.header("Schritt 2: Kohlenhydrate 🍝")
    kat = st.radio("Kategorie:", ["Kartoffeln", "Nudeln", "Reis", "Alternative"])
    opts = {
        "Kartoffeln": ["Süßkartoffel", "Festkochend", "Mehlig", "Drillinge"],
        "Nudeln": ["Spaghetti", "Penne", "Fusilli", "Vollkornnudeln"],
        "Reis": ["Basmati", "Wildreis", "Jasmin", "Risotto-Reis"],
        "Alternative": ["Quinoa", "Amaranth", "Couscous", "Hirse", "Steckrübe", "Bulgur"]
    }
    st.session_state.auswahl["carbs"] = st.selectbox("Sorte wählen:", opts[kat])
    
    col1, col2 = st.columns(2)
    if col1.button("⬅️ Zurück"): prev_step(); st.rerun()
    if col2.button("Weiter ➡️"): next_step(); st.rerun()

# --- SCHRITT 3: PROTEIN ---
elif st.session_state.step == 3:
    st.header("Schritt 3: Protein 🥩")
    st.session_state.auswahl["protein"] = st.radio("Was darf es sein?", 
        ["Rind", "Hähnchen", "Schwein", "Lamm", "Fisch", "Garnelen", "Tofu", "Kichererbsen", "Linsen", "Eier", "Kein Tier"])
    
    col1, col2 = st.columns(2)
    if col1.button("⬅️ Zurück"): prev_step(); st.rerun()
    if col2.button("Weiter ➡️"): next_step(); st.rerun()

# --- SCHRITT 4: SAUCE ---
elif st.session_state.step == 4:
    st.header("Schritt 4: Sauce 🥛")
    st.session_state.auswahl["sauce"] = st.radio("Basis:", 
        ["Sahne", "Kokosmilch", "Tomatenpassata", "Gemüsebrühe", "Frischkäse", "Pesto"])
    
    col1, col2 = st.columns(2)
    if col1.button("⬅️ Zurück"): prev_step(); st.rerun()
    if col2.button("Weiter ➡️"): next_step(); st.rerun()

# --- SCHRITT 5: STIL ---
elif st.session_state.step == 5:
    st.header("Schritt 5: Ernährungsstil 🥗")
    st.session_state.auswahl["stil"] = st.radio("Art:", ["Omnivor", "Vegetarisch", "Vegan"])
    
    col1, col2 = st.columns(2)
    if col1.button("⬅️ Zurück"): prev_step(); st.rerun()
    if col2.button("Rezept zeigen ✨"): next_step(); st.rerun()

# --- SCHRITT 6: REZEPT & LISTE ---
elif st.session_state.step == 6:
    a = st.session_state.auswahl
    st.header("🍽️ Dein persönliches Rezept")
    
    st.success(f"**{a['stil']}** mit **{a['protein']}**, **{a['carbs']}** und **{', '.join(a['gemüse'])}**.")
    
    st.markdown("""
    ### 👨‍🍳 Zubereitung
    1. Bereite die Kohlenhydrate nach Packungsanweisung vor.
    2. Brate das Protein und das Gemüse in etwas Öl an.
    3. Lösche alles mit der Saucenbasis ab und würze nach Geschmack.
    """)
    
    st.subheader("🛒 Einkaufsliste")
    for z in a['gemüse'] + [a['carbs'], a['protein'], a['sauce']]:
        if "Kein Tier" not in z:
            st.write(f"- [ ] {z}")
            
    if st.button("🔄 Neues Rezept planen"):
        st.session_state.step = 1
        st.session_state.auswahl = {"gemüse": [], "carbs": "", "protein": "", "sauce": "", "stil": ""}
        st.rerun()
