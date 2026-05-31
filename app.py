import streamlit as st

st.set_page_config(page_title="Floraría Laleaua Alba", page_icon="🌷", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400;1,600&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Lato:wght@300;400&display=swap');

*, body { font-family: 'Lato', sans-serif; }
h1, h2, h3, .display { font-family: 'Cormorant Garamond', serif; }

.stApp {
    background-color: #ffffff;
    background-image:
        radial-gradient(circle at 5% 10%, rgba(0,0,0,0.03) 0%, transparent 50%),
        radial-gradient(circle at 95% 90%, rgba(0,0,0,0.03) 0%, transparent 50%);
}

/* Floral SVG background decoration */
.floral-bg {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    pointer-events: none; z-index: 0; opacity: 0.04;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='400'%3E%3Ctext x='20' y='80' font-size='60' opacity='0.5'%3E🌸%3C/text%3E%3Ctext x='300' y='150' font-size='40'%3E🌿%3C/text%3E%3Ctext x='100' y='300' font-size='50'%3E🌹%3C/text%3E%3Ctext x='320' y='360' font-size='55'%3E🌷%3C/text%3E%3C/svg%3E");
    background-size: 400px 400px;
}

/* Header */
.main-header {
    text-align: center;
    padding: 3rem 2rem 1rem;
    border-bottom: 1px solid #e8e8e8;
    margin-bottom: 2rem;
    position: relative;
}
.main-header::before, .main-header::after {
    content: "✦";
    font-size: 1.2rem;
    color: #aaa;
    margin: 0 1rem;
}
.main-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 3.8rem !important;
    font-weight: 300 !important;
    color: #111 !important;
    letter-spacing: 4px;
    line-height: 1.1;
    margin: 0 !important;
}
.main-subtitle {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    color: #888;
    font-size: 1.2rem;
    margin-top: 0.3rem;
    letter-spacing: 2px;
}
.deco-line {
    display: flex; align-items: center; justify-content: center; gap: 1rem;
    margin: 1rem 0 0;
    color: #bbb; font-size: 0.75rem; letter-spacing: 3px; text-transform: uppercase;
}
.deco-line::before, .deco-line::after {
    content: ""; flex: 1; max-width: 120px; height: 1px; background: #ddd;
}

/* Product card */
.prod-card {
    background: #fff;
    border: 1px solid #ebebeb;
    border-radius: 4px;
    overflow: hidden;
    transition: box-shadow 0.3s, transform 0.3s;
    margin-bottom: 16px;
}
.prod-card:hover {
    box-shadow: 0 12px 40px rgba(0,0,0,0.1);
    transform: translateY(-3px);
}
.prod-card img {
    width: 100%; height: 220px; object-fit: cover;
    display: block; filter: grayscale(15%);
    transition: filter 0.3s;
}
.prod-card:hover img { filter: grayscale(0%); }
.prod-info { padding: 14px 16px 10px; }
.prod-cat {
    font-size: 0.65rem; letter-spacing: 3px; text-transform: uppercase;
    color: #999; margin-bottom: 4px;
}
.prod-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.25rem; font-weight: 600; color: #111;
    margin: 0 0 4px;
}
.prod-desc { font-size: 0.8rem; color: #aaa; margin-bottom: 8px; }
.prod-price {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.4rem; font-weight: 600; color: #111;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #fafafa !important;
    border-right: 1px solid #ebebeb;
}
section[data-testid="stSidebar"] .stTextInput input {
    border-radius: 0 !important;
    border: 1px solid #ddd !important;
    font-family: 'Lato', sans-serif;
}

/* Cart */
.cart-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.4rem; font-weight: 600; color: #111;
    border-bottom: 1px solid #eee; padding-bottom: 8px; margin-bottom: 12px;
}
.cart-row {
    display: flex; justify-content: space-between; align-items: center;
    padding: 8px 0; border-bottom: 1px solid #f5f5f5;
    font-size: 0.85rem; color: #333;
}
.cart-total-box {
    background: #111; color: #fff;
    padding: 14px 16px; margin-top: 12px;
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.2rem; text-align: center;
}
.free-ship { color: #aaa; font-size: 0.75rem; margin-top: 4px; }

/* Review card */
.review-card {
    background: #fafafa; border: 1px solid #ebebeb;
    border-radius: 4px; padding: 18px 20px; margin-bottom: 12px;
}
.review-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.05rem; font-weight: 600; color: #111;
}
.review-stars { color: #111; font-size: 0.9rem; margin: 2px 0 6px; }
.review-text { color: #666; font-size: 0.85rem; font-style: italic; }

/* Buttons */
.stButton > button {
    border-radius: 0 !important;
    border: 1px solid #111 !important;
    background: #111 !important;
    color: white !important;
    font-family: 'Lato', sans-serif !important;
    letter-spacing: 1px !important;
    font-size: 0.78rem !important;
    text-transform: uppercase !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: white !important;
    color: #111 !important;
}

/* Nav tabs */
.stTabs [data-baseweb="tab"] {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.1rem !important;
    letter-spacing: 1px;
}
</style>
<div class="floral-bg"></div>
""", unsafe_allow_html=True)

# ── Data ──────────────────────────────────────────────────────────────────────
flowers = [
    {"name": "Buchet Trandafiri Rosii",  "price": 89,  "emoji": "🌹", "desc": "12 trandafiri rosii premium", "cat": "Buchete",
     "img": "https://images.unsplash.com/photo-1518621736915-f3b1c41bfd00?w=600&q=80",
     "review_count": 48},
    {"name": "Lalele Galbene",           "price": 55,  "emoji": "🌷", "desc": "Buchet de 15 lalele proaspete", "cat": "Buchete",
     "img": "https://images.unsplash.com/photo-1490750967868-88df5691cc9f?w=600&q=80",
     "review_count": 31},
    {"name": "Orhidee Alba",             "price": 120, "emoji": "🪷", "desc": "Orhidee Phalaenopsis in ghiveci", "cat": "Plante",
     "img": "https://images.unsplash.com/photo-1566913485365-3a6cd87d7ff1?w=600&q=80",
     "review_count": 27},
    {"name": "Flori de Camp",            "price": 75,  "emoji": "🌼", "desc": "Amestec rustic si colorat", "cat": "Buchete",
     "img": "https://images.unsplash.com/photo-1462275646964-a0e3386b89fa?w=600&q=80",
     "review_count": 19},
    {"name": "Crin Alb Parfumat",        "price": 65,  "emoji": "⚜️", "desc": "3 crini albi, parfum intens", "cat": "Flori",
     "img": "https://images.unsplash.com/photo-1455659817273-f96807779a8a?w=600&q=80",
     "review_count": 22},
    {"name": "Buchet Roz Delicat",       "price": 95,  "emoji": "🌸", "desc": "Trandafiri roz si eucalipt", "cat": "Buchete",
     "img": "https://images.unsplash.com/photo-1561181286-d3fee7d55364?w=600&q=80",
     "review_count": 55},
    {"name": "Lavanda Provensala",       "price": 45,  "emoji": "💜", "desc": "Snop de lavanda uscata", "cat": "Flori",
     "img": "https://images.unsplash.com/photo-1499578124509-1611b77778c8?w=600&q=80",
     "review_count": 38},
    {"name": "Suculent Terarium",        "price": 80,  "emoji": "🌵", "desc": "Aranjament terarium minimalist", "cat": "Plante",
     "img": "https://images.unsplash.com/photo-1459411552884-841db9b3cc2a?w=600&q=80",
     "review_count": 14},
    {"name": "Bujori Roz",              "price": 110, "emoji": "🌺", "desc": "7 bujori proaspeti sezonieri", "cat": "Flori",
     "img": "https://images.unsplash.com/photo-1588196749597-9ff075ee6b5b?w=600&q=80",
     "review_count": 42},
]

reviews = [
    {"name": "Maria D.", "stars": 5, "text": "Buchetul a ajuns proaspat si superb ambalat. Cu siguranta voi mai comanda!", "produs": "Buchet Trandafiri Rosii"},
    {"name": "Ana P.",   "stars": 5, "text": "Orhideea e magnifica, exact ca in poza. Livrare rapida, multumesc!", "produs": "Orhidee Alba"},
    {"name": "Elena M.", "stars": 5, "text": "Lavanda e parfumata si arata minunat in living. Recomand cu caldura.", "produs": "Lavanda Provensala"},
    {"name": "Ioana C.", "stars": 4, "text": "Buchetul roz a fost o surpriza frumoasa pentru mama. Ii place foarte mult!", "produs": "Buchet Roz Delicat"},
    {"name": "Cristina V.", "stars": 5, "text": "Al treilea buchet comandat si de fiecare data am fost incantata. Calitate excelenta!", "produs": "Bujori Roz"},
    {"name": "Raluca N.", "stars": 5, "text": "Florile de camp au adus un strop de natura in casa. Absolut adorabile.", "produs": "Flori de Camp"},
]

# ── Session state ─────────────────────────────────────────────────────────────
if "cart" not in st.session_state:
    st.session_state.cart = {}

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1.5rem 0 1rem;'>
        <div style='font-family:Cormorant Garamond,serif; font-size:1.8rem; font-weight:300; color:#111; letter-spacing:3px;'>
            ✦ LALEAUA <br>ALBA ✦
        </div>
        <div style='font-size:0.7rem; letter-spacing:3px; color:#aaa; text-transform:uppercase; margin-top:6px;'>
            Florarie Online
        </div>
    </div>
    <hr style='border:none; border-top:1px solid #eee; margin-bottom:1.2rem;'>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;color:#999;'>Cauta</p>", unsafe_allow_html=True)
    search = st.text_input("", placeholder="ex: trandafiri, orhidee...", label_visibility="collapsed")

    st.markdown("<br><p style='font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;color:#999;'>Categorie</p>", unsafe_allow_html=True)
    categorii = ["Toate"] + sorted(set(f["cat"] for f in flowers))
    cat_sel = st.radio("", categorii, label_visibility="collapsed")

    st.markdown("<br><p style='font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;color:#999;'>Pret maxim (lei)</p>", unsafe_allow_html=True)
    max_price = st.slider("", 40, 150, 150, label_visibility="collapsed")

    st.markdown("<hr style='border:none;border-top:1px solid #eee;margin:1.2rem 0;'>", unsafe_allow_html=True)

    # Cart in sidebar
    st.markdown("<div class='cart-title'>Cosul tau</div>", unsafe_allow_html=True)
    cart = st.session_state.cart
    if not cart:
        st.markdown("<p style='color:#bbb;font-size:0.85rem;text-align:center;padding:10px 0;'>Cosul este gol 🌷</p>", unsafe_allow_html=True)
    else:
        total = 0
        for name, item in list(cart.items()):
            subtotal = item["price"] * item["qty"]
            total += subtotal
            c1, c2 = st.columns([5, 1])
            with c1:
                st.markdown(f"<div class='cart-row'><span>{item['emoji']} {name[:18]}<br><small style='color:#aaa'>{item['qty']} x {item['price']} lei</small></span><span style='font-weight:600'>{subtotal} lei</span></div>", unsafe_allow_html=True)
            with c2:
                if st.button("✕", key="del_" + name, help="Sterge"):
                    del st.session_state.cart[name]
                    st.rerun()

        msg = "Livrare gratuita!" if total >= 150 else f"Mai adauga {150-total} lei pt livrare gratuita"
        st.markdown(f"<div class='cart-total-box'>TOTAL: {total} LEI<br><span class='free-ship'>{msg}</span></div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Goleste cosul", use_container_width=True):
            st.session_state.cart = {}
            st.rerun()

    st.markdown("<hr style='border:none;border-top:1px solid #eee;margin:1.5rem 0 0.5rem;'>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:0.72rem;color:#bbb;text-align:center;line-height:1.8;'>📞 0721 234 567<br>⏰ Luni–Sam 9–19<br>🚚 Livrare in Bucuresti</p>", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <div class="main-title">🌹 Laleaua Albă 🌸</div>
    <div class="main-subtitle">Florărie cu suflet — din 2018</div>
    <div class="deco-line">Arome & Culori pentru sufletul tău</div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["✦  Produse", "✦  Buchete — Galerie & Preturi", "✦  Recenzii"])

# ── TAB 1: Produse ────────────────────────────────────────────────────────────
with tab1:
    # Filter
    filtered = flowers
    if search:
        filtered = [f for f in filtered if search.lower() in f["name"].lower() or search.lower() in f["desc"].lower()]
    if cat_sel != "Toate":
        filtered = [f for f in filtered if f["cat"] == cat_sel]
    filtered = [f for f in filtered if f["price"] <= max_price]

    if not filtered:
        st.markdown("<div style='text-align:center;padding:3rem;color:#aaa;font-size:1.1rem;'>Niciun produs gasit. Incearca alt filtru 🌷</div>", unsafe_allow_html=True)
    else:
        cols = st.columns(3)
        for idx, flower in enumerate(filtered):
            with cols[idx % 3]:
                st.markdown(f"""
                <div class="prod-card">
                    <img src="{flower['img']}" alt="{flower['name']}">
                    <div class="prod-info">
                        <div class="prod-cat">{flower['cat']}</div>
                        <div class="prod-name">{flower['name']}</div>
                        <div class="prod-desc">{flower['desc']}</div>
                        <div class="prod-price">{flower['price']} lei</div>
                        <div style="color:#aaa;font-size:0.72rem;margin-top:4px;">★★★★★ ({flower['review_count']} recenzii)</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                qty = st.number_input("Cantitate", min_value=1, max_value=20, value=1,
                                      key="qty_" + flower["name"], label_visibility="collapsed")
                if st.button("+ Adauga in cos", key="btn_" + flower["name"], use_container_width=True):
                    name = flower["name"]
                    if name in st.session_state.cart:
                        st.session_state.cart[name]["qty"] += qty
                    else:
                        st.session_state.cart[name] = {"price": flower["price"], "qty": qty, "emoji": flower["emoji"]}
                    st.toast(flower["name"] + " adaugat in cos!", icon="🌸")

# ── TAB 2: Galerie Buchete ────────────────────────────────────────────────────
with tab2:
    st.markdown("""
    <div style='text-align:center;padding:2rem 0 1.5rem;'>
        <div style='font-family:Cormorant Garamond,serif;font-size:2.2rem;font-weight:300;color:#111;letter-spacing:2px;'>
            Colectia noastra de Buchete
        </div>
        <div style='font-family:Cormorant Garamond,serif;font-style:italic;color:#aaa;font-size:1rem;margin-top:0.3rem;'>
            Fiecare buchet este aranjat cu grija, pentru momentele tale speciale
        </div>
    </div>
    """, unsafe_allow_html=True)

    buchete = [f for f in flowers if f["cat"] == "Buchete"]

    for i in range(0, len(buchete), 2):
        c1, c2 = st.columns(2, gap="large")
        for col, flower in zip([c1, c2], buchete[i:i+2]):
            with col:
                st.markdown(f"""
                <div class="prod-card" style="display:flex;flex-direction:row;height:180px;">
                    <img src="{flower['img']}" style="width:180px;height:180px;object-fit:cover;flex-shrink:0;filter:grayscale(10%);">
                    <div style="padding:20px 22px;">
                        <div class="prod-cat">{flower['cat']}</div>
                        <div class="prod-name" style="font-size:1.4rem;">{flower['name']}</div>
                        <div class="prod-desc" style="margin:6px 0;">{flower['desc']}</div>
                        <div class="prod-price">{flower['price']} lei</div>
                        <div style="color:#aaa;font-size:0.72rem;margin-top:4px;">★★★★★ ({flower['review_count']} recenzii)</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                if st.button("Comanda acum — " + flower["name"], key="gal_" + flower["name"], use_container_width=True):
                    name = flower["name"]
                    if name in st.session_state.cart:
                        st.session_state.cart[name]["qty"] += 1
                    else:
                        st.session_state.cart[name] = {"price": flower["price"], "qty": 1, "emoji": flower["emoji"]}
                    st.toast(flower["name"] + " adaugat!", icon="🌸")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background:#fafafa;border:1px solid #ebebeb;padding:2rem;text-align:center;margin-top:1rem;'>
        <div style='font-family:Cormorant Garamond,serif;font-size:1.5rem;color:#111;'>Vrei un buchet personalizat?</div>
        <div style='color:#999;font-size:0.85rem;margin-top:6px;'>Contacteaza-ne si cream aranjamentul perfect pentru tine</div>
    </div>
    """, unsafe_allow_html=True)

# ── TAB 3: Recenzii ───────────────────────────────────────────────────────────
with tab3:
    st.markdown("""
    <div style='text-align:center;padding:2rem 0 1.5rem;'>
        <div style='font-family:Cormorant Garamond,serif;font-size:2.2rem;font-weight:300;color:#111;letter-spacing:2px;'>
            Ce spun clientii nostri
        </div>
        <div style='font-family:Cormorant Garamond,serif;font-style:italic;color:#aaa;font-size:1rem;margin-top:0.3rem;'>
            Peste 200 de comenzi livrate cu drag
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    for i, rev in enumerate(reviews):
        col = c1 if i % 2 == 0 else c2
        with col:
            stars = "★" * rev["stars"] + "☆" * (5 - rev["stars"])
            st.markdown(f"""
            <div class="review-card">
                <div class="review-name">{rev['name']}</div>
                <div class="review-stars">{stars}</div>
                <div class="review-text">"{rev['text']}"</div>
                <div style="font-size:0.7rem;color:#ccc;margin-top:8px;letter-spacing:1px;">PRODUS: {rev['produs'].upper()}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background:#111;color:white;padding:2rem;text-align:center;'>
        <div style='font-family:Cormorant Garamond,serif;font-size:1.4rem;letter-spacing:2px;'>★★★★★</div>
        <div style='font-family:Cormorant Garamond,serif;font-size:1rem;margin-top:4px;color:#aaa;font-style:italic;'>
            4.9 / 5 — bazat pe 200+ recenzii verificate
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Contact expander ──────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.divider()
with st.expander("✦  Comanda personalizata sau contacteaza-ne"):
    f1, f2 = st.columns(2)
    with f1:
        with st.form("contact"):
            name_inp = st.text_input("Numele tau")
            phone_inp = st.text_input("Telefon")
            data_inp = st.date_input("Data dorita pentru livrare")
            msg_inp = st.text_area("Detalii comanda (culori, ocazie, buget)")
            if st.form_submit_button("Trimite cererea", use_container_width=True):
                if name_inp and phone_inp:
                    st.success("Multumim, " + name_inp + "! Te contactam in 30 de minute.")
                else:
                    st.warning("Te rugam completeaza numele si telefonul.")
    with f2:
        st.markdown("""
        **Informatii contact**

        📍 Str. Florilor 12, Bucuresti  
        📞 0721 234 567  
        📧 comenzi@laleauaalba.ro  

        **Program**  
        Luni – Vineri: 9:00 – 19:00  
        Sambata: 9:00 – 16:00  
        Duminica: Inchis  

        ---
        🚚 Livrare in Bucuresti si Ilfov  
        💳 Plata online sau la livrare  
        🎁 Mesaj cadou personalizat gratuit  
        """)

st.markdown("<div style='text-align:center;color:#ccc;font-size:0.75rem;padding:2rem 0 0.5rem;letter-spacing:2px;'>© 2025 FLORARÍA LALEAUA ALBA · CU DRAGOSTE, PENTRU TINE</div>", unsafe_allow_html=True)
