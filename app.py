import streamlit as st
import math

st.set_page_config(page_title="MKJY VIP Predictor", page_icon="⚽")
st.title("⚽ MKJY - VIP Score Predictor")

def poisson(l, x):
    return (math.exp(-l) * (l**x)) / math.factorial(x)

st.sidebar.header("Réglages Match")
h_team = st.sidebar.text_input("Domicile", "GAIS")
a_team = st.sidebar.text_input("Extérieur", "Mjällby")
h_xg = st.sidebar.slider(f"Force {h_team}", 0.0, 5.0, 1.45)
a_xg = st.sidebar.slider(f"Force {a_team}", 0.0, 5.0, 1.10)

if st.button("LANCER L'ANALYSE VIP 💎"):
    res = []
    for h in range(5):
        for a in range(5):
            p = poisson(h_xg, h) * poisson(a_xg, a) * 100
            res.append((f"{h} - {a}", p))
    res.sort(key=lambda x: x[1], reverse=True)
    st.write(f"### Top Scores : {h_team} vs {a_team}")
    for i in range(3):
        s, prob = res[i]
        st.success(f"**{s}** | {prob:.2f}%")
          
