import streamlit as st

# 1. Grundkonfiguration
st.set_page_config(page_title="Rezept-Profi", page_icon="👨‍🍳")

# 2. Besseres Design (Kontrastreiches Gelb-Grün)
st.markdown("""
    <style>
    /* Hintergrund der ganzen App */
    .stApp {
        background-color: #F9FBE7;
    }
    /* Alle Texte auf Dunkelgrün setzen für Lesbarkeit */
    [data-testid="stMarkdownContainer"] p, h1, h2, h3, label {
        color: #1B5E20 !important;
        font-weight: 500;
    }
    /* Buttons Styling */
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #C0CA33; /* Sattes Grün */
        color: white !important;
        border: none;
        font-weight: bold;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover {
        background-color: #FBC02D; /* Warmes Gelb beim Drüberfahren */
        color: #1B5E20 !important;
    }
    /* Radio Buttons und Selectboxen besser lesbar */
    .stRadio label, .stSelectbox label {
        background-color: rgba(255,255,255,0.5);
        padding: 5px 10px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Logik & Speicher
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'auswahl' not in st.session_state:
    st.session_state.auswahl = {"gemüse": [], "carbs": "", "protein": "", "sauce": "", "stil": ""}

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

st.title("👨‍🍳 Mahlzeiten-Konfigurator")

# --- SCHRITTE ---

if st.session_state.step == 1:
    st.header("1. Welches Gemüse hast du?")
    gemuese_arten = ["🍅 Tomate", "🥒 Zucchini", "🫑 Paprika", "🥦 Brokkoli", "🍃 Spinat", "🥕 Karotten", "🍄 Pilze", "🧅 Zwiebeln", "🌽 Mais", "🍆 Aubergine", "🥦 Blumenkohl", "🥬 Lauch", "🥗 Erbsen", "🧄 Knoblauch", "🎃 Kürbis", "🎋 Spargel", "🌱 Bohnen"]
    
    cols = st.columns(3)
    for idx, g in enumerate(gemuese_arten):
        if cols[idx % 3].button(g):
            if g not in st.session_state.auswahl["gemüse"]:
                st.session_state.auswahl["gemüse"].append(g)
    
    st.write("### Ausgewählt:")
    st.info(", ".join(st.session_state.auswahl["gemüse"]) if st.session_state.auswahl["gemüse"] else "Noch nichts gewählt")
    
    c1, c2 = st.columns(2)
    if c1.button("Auswahl leeren"):
        st.session_state.auswahl["gemüse"] = []
        st.rerun()
    if st.session_state.auswahl["gemüse"] and c2.button("Weiter ➡️"):
        next_step()
        st.rerun()

elif st.session_state.step == 2:
    st.header("2. Kohlenhydrate 🍝")
    kat = st.radio("Kategorie wählen:", ["Kartoffeln", "Nudeln", "Reis", "Alternative Getreide"])
    opts = {
        "Kartoffeln": ["Süßkartoffel", "Festkochend", "Mehlig", "Drillinge", "Gnocchi"],
        "Nudeln": ["Spaghetti", "Penne", "Fusilli", "Vollkornnudeln", "Spätzle"],
        "Reis": ["Basmati", "Wildreis", "Jasmin", "Risotto-Reis"],
        "Alternative Getreide": ["Quinoa", "Amaranth", "Couscous", "Hirse", "Bulgur", "Steckrübe"]
    }
    st.session_state.auswahl["carbs"] = st.selectbox("Sorte:", opts[kat])
    
    c1, c2 = st.columns(2)
    if c1.button("⬅️ Zurück"): prev_step(); st.rerun()
    if c2.button("Weiter ➡️"): next_step(); st.rerun()

elif st.session_state.step == 3:
    st.header("3. Protein & Fleisch 🥩")
    st.session_state.auswahl["protein"] = st.radio("Was darf rein?", 
        ["Rind", "Hähnchen", "Schwein", "Lamm", "Fisch", "Garnelen", "Tofu", "Kichererbsen", "Linsen", "Eier", "Kein Tier"])
    
    c1, c2 = st.columns(2)
    if c1.button("⬅️ Zurück"): prev_step(); st.rerun()
    if c2.button("Weiter ➡️"): next_step(); st.rerun()

elif st.session_state.step == 4:
    st.header("4. Die Sauce 🥛")
    st.session_state.auswahl["sauce"] = st.radio("Saucen-Basis:", 
        ["Sahne", "Kokosmilch", "Tomatenpassata", "Gemüsebrühe", "Frischkäse", "Sojasauce", "Pesto"])
    
    c1, c2 = st.columns(2)
    if c1.button("⬅️ Zurück"): prev_step(); st.rerun()
    if c2.button("Weiter ➡️"): next_step(); st.rerun()

elif st.session_state.step == 5:
    st.header("5. Stil wählen 🥗")
    st.session_state.auswahl["stil"] = st.radio("Ernährungstyp:", ["Omnivor", "Vegetarisch", "Vegan"])
    
    c1, c2 = st.columns(2)
    if c1.button("⬅️ Zurück"): prev_step(); st.rerun()
    if c2.button("Rezept erstellen! ✨"): next_step(); st.rerun()

elif st.session_state.step == 6:
    a = st.session_state.auswahl
    st.header("🍽️ Dein fertiges Rezept")
    
    # Dynamisches Rezept
    st.success(f"Heute gibt es: **{a['stil']}e Pfanne** mit **{a['protein']}** und **{a['carbs']}**")
    
    with st.expander("📖 Kochanleitung öffnen", expanded=True):
        st.write(f"""
        1. Koche zuerst die **{a['carbs']}**.
        2. Brate das **{a['protein']}** in einer Pfanne goldbraun an.
        3. Gib das Gemüse (**{', '.join(a['gemüse'])}**) dazu und lass es kurz mitdünsten.
        4. Gieße die **{a['sauce']}** darüber und schmecke alles mit Salz und Pfeffer ab.
        """)
        
    st.subheader("🛒 Deine Einkaufsliste")
    zutaten = a['gemüse'] + [a['carbs'], a['protein'], a['sauce']]
    for z in zutaten:
        if z != "Kein Tier":
            st.write(f"✅ {z}")
            
    if st.button("🔄 Neues Rezept planen"):
        st.session_state.step = 1
        st.session_state.auswahl = {"gemüse": [], "carbs": "", "protein": "", "sauce": "", "stil": ""}
        st.rerun()
