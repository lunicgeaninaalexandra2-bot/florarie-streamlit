import streamlit as st

st.set_page_config(page_title="Floraría Laleaua Alba", page_icon="🌷", layout="wide")

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #fff8f9 0%, #fde8f0 100%); }
.floral-card { background: white; border-radius: 20px; padding: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: center; margin-bottom: 10px; }
.price { color: #c2185b; font-size: 24px; font-weight: bold; }
h1 { color: #4a154b; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("🌹 Floraría Laleaua Alba 🌸")
st.markdown("<p style='text-align:center;color:#666'>Arome si culori pentru sufletul tau</p>", unsafe_allow_html=True)
st.divider()

if "cart" not in st.session_state:
    st.session_state.cart = {}

flowers = [
    {"name": "Buchet Trandafiri Rosii", "price": 89,  "emoji": "🌹", "desc": "12 trandafiri rosii", "cat": "Buchete"},
    {"name": "Lalele Galbene",          "price": 55,  "emoji": "🌷", "desc": "Buchet de 15 lalele",  "cat": "Buchete"},
    {"name": "Orhidee Alba",            "price": 120, "emoji": "🪷", "desc": "Orhidee Phalaenopsis", "cat": "Plante"},
    {"name": "Flori de Camp",           "price": 75,  "emoji": "🌼", "desc": "Amestec rustic",       "cat": "Buchete"},
    {"name": "Crin Alb",                "price": 65,  "emoji": "⚜️", "desc": "3 crini parfumati",   "cat": "Flori"},
    {"name": "Buchet Roz",              "price": 95,  "emoji": "🌸", "desc": "Trandafiri roz",       "cat": "Buchete"},
    {"name": "Lavanda",                 "price": 45,  "emoji": "💜", "desc": "Snop de lavanda",      "cat": "Flori"},
    {"name": "Suculent",                "price": 80,  "emoji": "🌵", "desc": "Terarium minimalist",  "cat": "Plante"},
    {"name": "Bujori Roz",             "price": 110, "emoji": "🌺", "desc": "7 bujori proaspeti",   "cat": "Flori"},
]

categorii = ["Toate"] + sorted(set(f["cat"] for f in flowers))

main_col, cart_col = st.columns([3, 1], gap="large")

with main_col:
    cat_sel = st.radio("Categorie:", categorii, horizontal=True)
    st.markdown("<br>", unsafe_allow_html=True)
    filtered = flowers if cat_sel == "Toate" else [f for f in flowers if f["cat"] == cat_sel]
    cols = st.columns(3)
    for idx, flower in enumerate(filtered):
        with cols[idx % 3]:
            st.markdown(
                "<div class='floral-card'>"
                "<h2>" + flower["emoji"] + "</h2>"
                "<h3>" + flower["name"] + "</h3>"
                "<p>" + flower["desc"] + "</p>"
                "<p class='price'>" + str(flower["price"]) + " lei</p>"
                "</div>",
                unsafe_allow_html=True
            )
            qty = st.number_input("Cantitate", min_value=1, max_value=20, value=1,
                                  key="qty_" + flower["name"], label_visibility="collapsed")
            if st.button("🛒 Adauga", key="btn_" + flower["name"], use_container_width=True):
                name = flower["name"]
                if name in st.session_state.cart:
                    st.session_state.cart[name]["qty"] += qty
                else:
                    st.session_state.cart[name] = {"price": flower["price"], "qty": qty, "emoji": flower["emoji"]}
                st.toast(flower["name"] + " adaugat!", icon="✅")

with cart_col:
    st.markdown("### 🛍️ Cosul tau")
    cart = st.session_state.cart
    if not cart:
        st.info("Cosul este gol 🌷")
    else:
        total = 0
        for name, item in list(cart.items()):
            subtotal = item["price"] * item["qty"]
            total += subtotal
            col_a, col_b = st.columns([4, 1])
            with col_a:
                st.write(item["emoji"] + " " + name + " x" + str(item["qty"]) + " = " + str(subtotal) + " lei")
            with col_b:
                if st.button("x", key="del_" + name):
                    del st.session_state.cart[name]
                    st.rerun()
        if total >= 150:
            st.success("Total: " + str(total) + " lei - Livrare gratuita!")
        else:
            st.warning("Total: " + str(total) + " lei - Mai adauga " + str(150 - total) + " lei pt livrare gratuita")
        if st.button("Goleste cosul", use_container_width=True):
            st.session_state.cart = {}
            st.rerun()

st.divider()
with st.expander("📞 Comanda personalizata"):
    with st.form("contact"):
        name = st.text_input("Numele tau")
        phone = st.text_input("Telefon")
        message = st.text_area("Detalii comanda")
        if st.form_submit_button("Trimite"):
            if name and phone:
                st.success("Multumim " + name + "! Te contactam in 30 minute.")
            else:
                st.warning("Completeaza numele si telefonul.")

st.markdown("---")
st.markdown("<p style='text-align:center'>🌻 Program: Luni-Sambata 9-19 | Livrare gratuita peste 150 lei</p>", unsafe_allow_html=True)