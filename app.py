import streamlit as st

st.set_page_config(page_title="Florăria Online", page_icon="🌷", layout="wide")

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #f5f7fa 0%, #f3e8ff 100%); }
.floral-card { background: white; border-radius: 20px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: center; }
.price { color: #c2185b; font-size: 24px; font-weight: bold; }
h1 { color: #4a154b; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("🌹 Florăria Laleaua Albă 🌸")
st.markdown("<p style='text-align: center; color: #666;'>Arome și culori pentru sufletul tău</p>", unsafe_allow_html=True)
st.divider()

flowers = [
    {"name": "Buchet Trandafiri Roșii", "price": 89, "emoji": "🌹", "desc": "12 trandafiri roșii"},
    {"name": "Lalele Galbene", "price": 55, "emoji": "🌷", "desc": "Buchet de 15 lalele"},
    {"name": "Orhidee Albă", "price": 120, "emoji": "🪷", "desc": "Orhidee Phalaenopsis"},
    {"name": "Buchet Flori de Câmp", "price": 75, "emoji": "🌼", "desc": "Amestec rustic de flori"},
    {"name": "Crin Alb", "price": 65, "emoji": "⚜️", "desc": "3 crini albi parfumați"},
    {"name": "Buchet Roz", "price": 95, "emoji": "🌸", "desc": "Trandafiri roz și eucalipt"},
]

cols = st.columns(3)
for idx, flower in enumerate(flowers):
    with cols[idx % 3]:
        st.markdown(f"<div class='floral-card'><h2>{flower['emoji']}</h2><h3>{flower['name']}</h3><p>{flower['desc']}</p><p class='price'>{flower['price']} lei</p></div>", unsafe_allow_html=True)
        if st.button(f"Comandă {flower['name']}", key=idx):
            st.success(f"✅ {flower['name']} - {flower['price']} lei adăugat!")

st.divider()
with st.expander("📞 Contact și comandă personalizată"):
    with st.form("contact"):
        name = st.text_input("Numele tău")
        phone = st.text_input("Telefon")
        message = st.text_area("Detalii comandă")
        if st.form_submit_button("Trimite"):
            st.success("Mulțumim! Te contactăm în 30 de minute.")

st.markdown("---")
st.markdown("<p style='text-align: center;'>🌻 Program: Luni - Sâmbătă 9-19 | Livrare gratuită peste 150 lei</p>", unsafe_allow_html=True)