import streamlit as st

st.set_page_config(page_title="Floraría Laleaua Alba", page_icon="🌷", layout="wide")

GITHUB_RAW = "https://raw.githubusercontent.com/lunicgeaninaalexandra2-bot/florarie-streamlit/main/"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;600;700&family=Great+Vibes&family=Lato:wght@300;400&display=swap');

*, body { font-family: 'Lato', sans-serif; }

.stApp {
    background-color: #ffffff;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 680 500'%3E%3Cg opacity='0.09'%3E%3Cpath d='M 30 500 C 10 440 -5 370 25 300 C 40 265 55 240 50 200' fill='none' stroke='%234a7a4a' stroke-width='4' stroke-linecap='round'/%3E%3Cpath d='M 28 380 C -15 360 -28 325 -15 295' fill='none' stroke='%235a8a5a' stroke-width='14' stroke-linecap='round' opacity='0.55'/%3E%3Cpath d='M 30 355 C 72 338 88 308 76 278' fill='none' stroke='%235a8a5a' stroke-width='14' stroke-linecap='round' opacity='0.55'/%3E%3Cpath d='M 27 325 C -8 308 -18 278 -5 250' fill='none' stroke='%235a8a5a' stroke-width='11' stroke-linecap='round' opacity='0.45'/%3E%3Cpath d='M 33 302 C 68 290 82 265 72 238' fill='none' stroke='%235a8a5a' stroke-width='11' stroke-linecap='round' opacity='0.45'/%3E%3Cpath d='M 36 278 C 4 262 -4 238 8 215' fill='none' stroke='%236a9a6a' stroke-width='9' stroke-linecap='round' opacity='0.4'/%3E%3Cpath d='M 40 255 C 72 245 83 224 75 200' fill='none' stroke='%236a9a6a' stroke-width='9' stroke-linecap='round' opacity='0.4'/%3E%3Cpath d='M 42 232 C 14 218 8 196 20 174' fill='none' stroke='%237aaa7a' stroke-width='7' stroke-linecap='round' opacity='0.35'/%3E%3Cpath d='M 45 212 C 74 200 84 180 76 158' fill='none' stroke='%237aaa7a' stroke-width='7' stroke-linecap='round' opacity='0.35'/%3E%3C/g%3E%3Cg opacity='0.09'%3E%3Cpath d='M 650 500 C 670 440 685 370 655 300 C 640 265 625 240 630 200' fill='none' stroke='%234a7a4a' stroke-width='4' stroke-linecap='round'/%3E%3Cpath d='M 652 380 C 695 360 708 325 695 295' fill='none' stroke='%235a8a5a' stroke-width='14' stroke-linecap='round' opacity='0.55'/%3E%3Cpath d='M 650 355 C 608 338 592 308 604 278' fill='none' stroke='%235a8a5a' stroke-width='14' stroke-linecap='round' opacity='0.55'/%3E%3Cpath d='M 653 325 C 688 308 698 278 685 250' fill='none' stroke='%235a8a5a' stroke-width='11' stroke-linecap='round' opacity='0.45'/%3E%3Cpath d='M 647 302 C 612 290 598 265 608 238' fill='none' stroke='%235a8a5a' stroke-width='11' stroke-linecap='round' opacity='0.45'/%3E%3Cpath d='M 644 278 C 676 262 684 238 672 215' fill='none' stroke='%236a9a6a' stroke-width='9' stroke-linecap='round' opacity='0.4'/%3E%3Cpath d='M 640 255 C 608 245 597 224 605 200' fill='none' stroke='%236a9a6a' stroke-width='9' stroke-linecap='round' opacity='0.4'/%3E%3Cpath d='M 638 232 C 666 218 672 196 660 174' fill='none' stroke='%237aaa7a' stroke-width='7' stroke-linecap='round' opacity='0.35'/%3E%3Cpath d='M 635 212 C 606 200 596 180 604 158' fill='none' stroke='%237aaa7a' stroke-width='7' stroke-linecap='round' opacity='0.35'/%3E%3C/g%3E%3Cg opacity='0.10'%3E%3Cellipse cx='55' cy='75' rx='18' ry='28' fill='%23e8a0b4' transform='rotate(-15,55,75)'/%3E%3Cellipse cx='55' cy='75' rx='18' ry='28' fill='%23d4607a' transform='rotate(10,55,75)'/%3E%3Cellipse cx='55' cy='75' rx='18' ry='28' fill='%23e8a0b4' transform='rotate(32,55,75)'/%3E%3Cellipse cx='55' cy='75' rx='18' ry='28' fill='%23d4607a' transform='rotate(55,55,75)'/%3E%3Cellipse cx='55' cy='75' rx='18' ry='28' fill='%23e8a0b4' transform='rotate(78,55,75)'/%3E%3Crect x='52' y='78' width='6' height='40' rx='3' fill='%235a8a5a'/%3E%3Cellipse cx='40' cy='100' rx='20' ry='7' fill='%237aba7a' transform='rotate(-30,40,100)'/%3E%3Cellipse cx='70' cy='105' rx='20' ry='7' fill='%237aba7a' transform='rotate(25,70,105)'/%3E%3C/g%3E%3Cg opacity='0.10'%3E%3Cellipse cx='625' cy='65' rx='18' ry='28' fill='%23e8a0b4' transform='rotate(-20,625,65)'/%3E%3Cellipse cx='625' cy='65' rx='18' ry='28' fill='%23d4607a' transform='rotate(5,625,65)'/%3E%3Cellipse cx='625' cy='65' rx='18' ry='28' fill='%23e8a0b4' transform='rotate(30,625,65)'/%3E%3Cellipse cx='625' cy='65' rx='18' ry='28' fill='%23d4607a' transform='rotate(55,625,65)'/%3E%3Cellipse cx='625' cy='65' rx='18' ry='28' fill='%23e8a0b4' transform='rotate(80,625,65)'/%3E%3Crect x='622' y='68' width='6' height='40' rx='3' fill='%235a8a5a'/%3E%3Cellipse cx='610' cy='90' rx='20' ry='7' fill='%237aba7a' transform='rotate(-25,610,90)'/%3E%3Cellipse cx='640' cy='92' rx='20' ry='7' fill='%237aba7a' transform='rotate(28,640,92)'/%3E%3C/g%3E%3Cg opacity='0.09'%3E%3Cellipse cx='160' cy='45' rx='15' ry='24' fill='%23f0b0c8' transform='rotate(-18,160,45)'/%3E%3Cellipse cx='160' cy='45' rx='15' ry='24' fill='%23e07090' transform='rotate(8,160,45)'/%3E%3Cellipse cx='160' cy='45' rx='15' ry='24' fill='%23f0b0c8' transform='rotate(34,160,45)'/%3E%3Cellipse cx='160' cy='45' rx='15' ry='24' fill='%23e07090' transform='rotate(60,160,45)'/%3E%3Crect x='157' y='48' width='5' height='35' rx='2' fill='%235a8a5a'/%3E%3Cellipse cx='148' cy='68' rx='16' ry='6' fill='%237aba7a' transform='rotate(-28,148,68)'/%3E%3Cellipse cx='172' cy='70' rx='16' ry='6' fill='%237aba7a' transform='rotate(22,172,70)'/%3E%3C/g%3E%3Cg opacity='0.09'%3E%3Cellipse cx='520' cy='40' rx='15' ry='24' fill='%23e8a0b4' transform='rotate(-12,520,40)'/%3E%3Cellipse cx='520' cy='40' rx='15' ry='24' fill='%23d4607a' transform='rotate(14,520,40)'/%3E%3Cellipse cx='520' cy='40' rx='15' ry='24' fill='%23e8a0b4' transform='rotate(38,520,40)'/%3E%3Cellipse cx='520' cy='40' rx='15' ry='24' fill='%23d4607a' transform='rotate(62,520,40)'/%3E%3Crect x='517' y='43' width='5' height='35' rx='2' fill='%235a8a5a'/%3E%3Cellipse cx='508' cy='63' rx='16' ry='6' fill='%237aba7a' transform='rotate(-22,508,63)'/%3E%3Cellipse cx='532' cy='65' rx='16' ry='6' fill='%237aba7a' transform='rotate(20,532,65)'/%3E%3C/g%3E%3Cg opacity='0.08'%3E%3Cellipse cx='100' cy='440' rx='16' ry='25' fill='%23e8a0b4' transform='rotate(-15,100,440)'/%3E%3Cellipse cx='100' cy='440' rx='16' ry='25' fill='%23d4607a' transform='rotate(10,100,440)'/%3E%3Cellipse cx='100' cy='440' rx='16' ry='25' fill='%23e8a0b4' transform='rotate(35,100,440)'/%3E%3Cellipse cx='100' cy='440' rx='16' ry='25' fill='%23d4607a' transform='rotate(60,100,440)'/%3E%3Crect x='97' y='443' width='5' height='38' rx='2' fill='%235a8a5a'/%3E%3Cellipse cx='86' cy='465' rx='18' ry='6' fill='%237aba7a' transform='rotate(-25,86,465)'/%3E%3Cellipse cx='114' cy='467' rx='18' ry='6' fill='%237aba7a' transform='rotate(22,114,467)'/%3E%3C/g%3E%3Cg opacity='0.08'%3E%3Cellipse cx='580' cy='450' rx='16' ry='25' fill='%23f0b0c8' transform='rotate(-10,580,450)'/%3E%3Cellipse cx='580' cy='450' rx='16' ry='25' fill='%23e07090' transform='rotate(15,580,450)'/%3E%3Cellipse cx='580' cy='450' rx='16' ry='25' fill='%23f0b0c8' transform='rotate(40,580,450)'/%3E%3Cellipse cx='580' cy='450' rx='16' ry='25' fill='%23e07090' transform='rotate(65,580,450)'/%3E%3Crect x='577' y='453' width='5' height='38' rx='2' fill='%235a8a5a'/%3E%3Cellipse cx='566' cy='474' rx='18' ry='6' fill='%237aba7a' transform='rotate(-20,566,474)'/%3E%3Cellipse cx='594' cy='476' rx='18' ry='6' fill='%237aba7a' transform='rotate(18,594,476)'/%3E%3C/g%3E%3Cg opacity='0.07'%3E%3Cellipse cx='340' cy='25' rx='14' ry='22' fill='%23e8a0b4' transform='rotate(-12,340,25)'/%3E%3Cellipse cx='340' cy='25' rx='14' ry='22' fill='%23d4607a' transform='rotate(14,340,25)'/%3E%3Cellipse cx='340' cy='25' rx='14' ry='22' fill='%23e8a0b4' transform='rotate(38,340,25)'/%3E%3Crect x='337' y='28' width='5' height='32' rx='2' fill='%235a8a5a'/%3E%3C/g%3E%3Cg opacity='0.07'%3E%3Cellipse cx='260' cy='480' rx='13' ry='20' fill='%23f0b0c8' transform='rotate(-15,260,480)'/%3E%3Cellipse cx='260' cy='480' rx='13' ry='20' fill='%23e07090' transform='rotate(12,260,480)'/%3E%3Cellipse cx='260' cy='480' rx='13' ry='20' fill='%23f0b0c8' transform='rotate(38,260,480)'/%3E%3Crect x='257' y='483' width='4' height='28' rx='2' fill='%235a8a5a'/%3E%3C/g%3E%3Cg opacity='0.07'%3E%3Cellipse cx='420' cy='490' rx='13' ry='20' fill='%23e8a0b4' transform='rotate(-10,420,490)'/%3E%3Cellipse cx='420' cy='490' rx='13' ry='20' fill='%23d4607a' transform='rotate(16,420,490)'/%3E%3Cellipse cx='420' cy='490' rx='13' ry='20' fill='%23e8a0b4' transform='rotate(40,420,490)'/%3E%3Crect x='417' y='493' width='4' height='28' rx='2' fill='%235a8a5a'/%3E%3C/g%3E%3C/svg%3E");
    background-repeat: repeat;
    background-size: 680px 500px;
}

/* HEADER cu buchet in spate */
.main-header {
    position: relative;
    text-align: center;
    padding: 3.5rem 2rem 1.5rem;
    border-bottom: 1px solid #e8e8e8;
    margin-bottom: 2rem;
    overflow: hidden;
}
.header-bouquet {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 12rem;
    opacity: 0.06;
    pointer-events: none;
    line-height: 1;
    filter: grayscale(100%);
}
.main-title {
    font-family: 'Great Vibes', cursive !important;
    font-size: 5rem !important;
    font-weight: 400 !important;
    color: #1a1a1a !important;
    letter-spacing: 2px;
    line-height: 1.1;
    margin: 0 !important;
    position: relative;
    z-index: 1;
}
.main-subtitle {
    font-family: 'Dancing Script', cursive;
    color: #999;
    font-size: 1.3rem;
    margin-top: 0.3rem;
    letter-spacing: 1px;
    position: relative;
    z-index: 1;
}
.deco-line {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin: 0.8rem 0 0;
    color: #ccc;
    font-size: 0.72rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    position: relative;
    z-index: 1;
}
.deco-line::before, .deco-line::after {
    content: "";
    flex: 1;
    max-width: 100px;
    height: 1px;
    background: #ddd;
}

/* Produs card */
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
    width: 100%;
    height: 220px;
    object-fit: cover;
    display: block;
}
.prod-info { padding: 14px 16px 10px; }
.prod-cat {
    font-size: 0.65rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #bbb;
    margin-bottom: 4px;
}
.prod-name {
    font-family: 'Dancing Script', cursive;
    font-size: 1.4rem;
    font-weight: 600;
    color: #111;
    margin: 0 0 4px;
}
.prod-desc { font-size: 0.8rem; color: #aaa; margin-bottom: 8px; }
.prod-price {
    font-family: 'Dancing Script', cursive;
    font-size: 1.5rem;
    font-weight: 700;
    color: #111;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #fafafa !important;
    border-right: 1px solid #ebebeb;
}
.sidebar-logo {
    text-align: center;
    padding: 1.5rem 0 1rem;
}
.sidebar-logo .s-title {
    font-family: 'Great Vibes', cursive;
    font-size: 2.2rem;
    color: #111;
    line-height: 1.2;
}
.sidebar-logo .s-sub {
    font-size: 0.65rem;
    letter-spacing: 3px;
    color: #aaa;
    text-transform: uppercase;
    margin-top: 4px;
}

/* Cart */
.cart-title {
    font-family: 'Dancing Script', cursive;
    font-size: 1.5rem;
    font-weight: 700;
    color: #111;
    border-bottom: 1px solid #eee;
    padding-bottom: 8px;
    margin-bottom: 12px;
}
.cart-row {
    padding: 7px 0;
    border-bottom: 1px solid #f5f5f5;
    font-size: 0.83rem;
    color: #444;
}
.cart-total-box {
    background: #111;
    color: #fff;
    padding: 14px 16px;
    margin-top: 12px;
    font-family: 'Dancing Script', cursive;
    font-size: 1.3rem;
    text-align: center;
}
.free-ship { color: #aaa; font-size: 0.72rem; margin-top: 4px; }

/* Review */
.review-card {
    background: #fafafa;
    border: 1px solid #ebebeb;
    border-radius: 4px;
    padding: 18px 20px;
    margin-bottom: 12px;
}
.review-name {
    font-family: 'Dancing Script', cursive;
    font-size: 1.2rem;
    font-weight: 700;
    color: #111;
}
.review-text { color: #777; font-size: 0.85rem; font-style: italic; margin-top: 6px; }

/* Butoane */
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

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-family: 'Dancing Script', cursive !important;
    font-size: 1.2rem !important;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "cart" not in st.session_state:
    st.session_state.cart = {}

# ── Produse ───────────────────────────────────────────────────────────────────
flowers = [
    {"name": "Trandafiri Rosii",   "price": 89,  "desc": "12 trandafiri rosii premium cu iedera",  "cat": "Trandafiri", "img": GITHUB_RAW + "Trandafiri_Rosii.png"},
    {"name": "Trandafiri Rozi",    "price": 95,  "desc": "20 trandafiri roz cu eucalipt",           "cat": "Trandafiri", "img": GITHUB_RAW + "Trandafiri_Rozi.png"},
    {"name": "Trandafiri Albi",    "price": 95,  "desc": "12 trandafiri albi cu funda satinata",    "cat": "Trandafiri", "img": GITHUB_RAW + "Trandafiri_Albi.png"},
    {"name": "Trandafiri Colorati","price": 110, "desc": "Mix de trandafiri multicolori cu eucalipt","cat": "Trandafiri", "img": GITHUB_RAW + "Trandafiri_Colorati.png"},
    {"name": "Lalele Galbene",     "price": 55,  "desc": "15 lalele galbene proaspete",             "cat": "Lalele",     "img": GITHUB_RAW + "Lalele_Galbene.png"},
    {"name": "Lalele Roz",         "price": 55,  "desc": "20 lalele roz delicate",                  "cat": "Lalele",     "img": GITHUB_RAW + "Lalele_Roz.png"},
    {"name": "Lalele Colorate",    "price": 65,  "desc": "Buchet larg de lalele multicolore",       "cat": "Lalele",     "img": GITHUB_RAW + "Lalele_Colorate.png"},
    {"name": "Bujori Roz",         "price": 110, "desc": "Bujori roz luxurianti in ambalaj panza",  "cat": "Bujori",     "img": GITHUB_RAW + "Bujori_Roz.png"},
    {"name": "Bujori Albi",        "price": 115, "desc": "Bujori albi eleganti cu funda argintie",  "cat": "Bujori",     "img": GITHUB_RAW + "Bujori_Albi.png"},
]

reviews = [
    {"name": "Maria D.",    "stars": 5, "text": "Buchetul a ajuns proaspat si superb ambalat. Cu siguranta voi mai comanda!",        "produs": "Trandafiri Rosii"},
    {"name": "Ana P.",      "stars": 5, "text": "Bujori absolut magnifici, exact ca in poza. Livrare rapida, multumesc!",             "produs": "Bujori Roz"},
    {"name": "Elena M.",    "stars": 5, "text": "Lalelele colorate au adus bucurie in casa. Recomand cu caldura.",                    "produs": "Lalele Colorate"},
    {"name": "Ioana C.",    "stars": 4, "text": "Trandafirii rozi au fost o surpriza frumoasa pentru mama. Ii place foarte mult!",    "produs": "Trandafiri Rozi"},
    {"name": "Cristina V.", "stars": 5, "text": "Al treilea buchet comandat si de fiecare data am fost incantata. Calitate excelenta!","produs": "Bujori Albi"},
    {"name": "Raluca N.",   "stars": 5, "text": "Trandafirii albi au fost perfecti pentru nunta. Absolut adorabili.",                "produs": "Trandafiri Albi"},
]

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="s-title">Laleaua Alba</div>
        <div class="s-sub">Florarie Online</div>
    </div>
    <hr style="border:none;border-top:1px solid #eee;margin-bottom:1.2rem;">
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-size:0.68rem;letter-spacing:2px;text-transform:uppercase;color:#bbb;margin-bottom:4px;'>Cauta</p>", unsafe_allow_html=True)
    search = st.text_input("", placeholder="ex: trandafiri, bujori...", label_visibility="collapsed")

    st.markdown("<br><p style='font-size:0.68rem;letter-spacing:2px;text-transform:uppercase;color:#bbb;margin-bottom:4px;'>Categorie</p>", unsafe_allow_html=True)
    categorii = ["Toate"] + sorted(set(f["cat"] for f in flowers))
    cat_sel = st.radio("", categorii, label_visibility="collapsed")

    st.markdown("<br><p style='font-size:0.68rem;letter-spacing:2px;text-transform:uppercase;color:#bbb;margin-bottom:4px;'>Pret maxim (lei)</p>", unsafe_allow_html=True)
    max_price = st.slider("", 40, 150, 150, label_visibility="collapsed")

    st.markdown("<hr style='border:none;border-top:1px solid #eee;margin:1.2rem 0;'>", unsafe_allow_html=True)
    st.markdown("<div class='cart-title'>Cosul tau</div>", unsafe_allow_html=True)

    cart = st.session_state.cart
    if not cart:
        st.markdown("<p style='color:#ccc;font-size:0.85rem;text-align:center;padding:10px 0;'>Cosul este gol</p>", unsafe_allow_html=True)
    else:
        total = 0
        for name, item in list(cart.items()):
            subtotal = item["price"] * item["qty"]
            total += subtotal
            c1, c2 = st.columns([5, 1])
            with c1:
                st.markdown("<div class='cart-row'>" + name[:22] + "<br><small style='color:#bbb'>" + str(item["qty"]) + " x " + str(item["price"]) + " lei = <b>" + str(subtotal) + " lei</b></small></div>", unsafe_allow_html=True)
            with c2:
                if st.button("x", key="del_" + name):
                    del st.session_state.cart[name]
                    st.rerun()
        msg = "Livrare gratuita!" if total >= 150 else "Mai adauga " + str(150 - total) + " lei pt livrare gratuita"
        st.markdown("<div class='cart-total-box'>Total: " + str(total) + " lei<br><span class='free-ship'>" + msg + "</span></div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Goleste cosul", use_container_width=True):
            st.session_state.cart = {}
            st.rerun()

    st.markdown("<hr style='border:none;border-top:1px solid #eee;margin:1.5rem 0 0.5rem;'>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:0.72rem;color:#ccc;text-align:center;line-height:2;'>📞 0721 234 567<br>⏰ Luni-Sam 9-19<br>🚚 Livrare in Bucuresti</p>", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <div class="header-bouquet">💐</div>
    <div class="main-title">Laleaua Alba</div>
    <div class="main-subtitle">Floraríe cu suflet — din 2018</div>
    <div class="deco-line">Arome & Culori pentru sufletul tau</div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["  Produse  ", "  Galerie & Preturi  ", "  Recenzii  "])

# ── TAB 1 ─────────────────────────────────────────────────────────────────────
with tab1:
    filtered = flowers
    if search:
        filtered = [f for f in filtered if search.lower() in f["name"].lower() or search.lower() in f["desc"].lower()]
    if cat_sel != "Toate":
        filtered = [f for f in filtered if f["cat"] == cat_sel]
    filtered = [f for f in filtered if f["price"] <= max_price]

    if not filtered:
        st.markdown("<div style='text-align:center;padding:3rem;color:#bbb;font-size:1.1rem;'>Niciun produs gasit. Incearca alt filtru.</div>", unsafe_allow_html=True)
    else:
        cols = st.columns(3)
        for idx, flower in enumerate(filtered):
            with cols[idx % 3]:
                st.markdown(
                    "<div class='prod-card'>"
                    "<img src='" + flower["img"] + "' alt='" + flower["name"] + "'>"
                    "<div class='prod-info'>"
                    "<div class='prod-cat'>" + flower["cat"] + "</div>"
                    "<div class='prod-name'>" + flower["name"] + "</div>"
                    "<div class='prod-desc'>" + flower["desc"] + "</div>"
                    "<div class='prod-price'>" + str(flower["price"]) + " lei</div>"
                    "<div style='color:#ccc;font-size:0.72rem;margin-top:4px;'>★★★★★</div>"
                    "</div></div>",
                    unsafe_allow_html=True
                )
                qty = st.number_input("Cantitate", min_value=1, max_value=20, value=1,
                                      key="qty_" + flower["name"], label_visibility="collapsed")
                if st.button("+ Adauga in cos", key="btn_" + flower["name"], use_container_width=True):
                    name = flower["name"]
                    if name in st.session_state.cart:
                        st.session_state.cart[name]["qty"] += qty
                    else:
                        st.session_state.cart[name] = {"price": flower["price"], "qty": qty}
                    st.toast(flower["name"] + " adaugat in cos!")

# ── TAB 2 ─────────────────────────────────────────────────────────────────────
with tab2:
    st.markdown("""
    <div style='text-align:center;padding:2rem 0 1.5rem;'>
        <div style='font-family:Great Vibes,cursive;font-size:3rem;color:#111;'>Colectia noastra</div>
        <div style='font-family:Dancing Script,cursive;color:#aaa;font-size:1.1rem;margin-top:0.3rem;font-style:italic;'>
            Fiecare buchet este aranjat cu grija, pentru momentele tale speciale
        </div>
    </div>
    """, unsafe_allow_html=True)

    for i in range(0, len(flowers), 2):
        c1, c2 = st.columns(2, gap="large")
        for col, flower in zip([c1, c2], flowers[i:i+2]):
            with col:
                st.markdown(
                    "<div class='prod-card' style='display:flex;flex-direction:row;height:160px;'>"
                    "<img src='" + flower["img"] + "' style='width:160px;height:160px;object-fit:cover;flex-shrink:0;'>"
                    "<div style='padding:18px 20px;'>"
                    "<div class='prod-cat'>" + flower["cat"] + "</div>"
                    "<div class='prod-name' style='font-size:1.5rem;'>" + flower["name"] + "</div>"
                    "<div class='prod-desc'>" + flower["desc"] + "</div>"
                    "<div class='prod-price'>" + str(flower["price"]) + " lei</div>"
                    "</div></div>",
                    unsafe_allow_html=True
                )
                if st.button("Comanda — " + flower["name"], key="gal_" + flower["name"], use_container_width=True):
                    name = flower["name"]
                    if name in st.session_state.cart:
                        st.session_state.cart[name]["qty"] += 1
                    else:
                        st.session_state.cart[name] = {"price": flower["price"], "qty": 1}
                    st.toast(flower["name"] + " adaugat!")

# ── TAB 3 ─────────────────────────────────────────────────────────────────────
with tab3:
    st.markdown("""
    <div style='text-align:center;padding:2rem 0 1.5rem;'>
        <div style='font-family:Great Vibes,cursive;font-size:3rem;color:#111;'>Ce spun clientii nostri</div>
        <div style='font-family:Dancing Script,cursive;color:#aaa;font-size:1.1rem;font-style:italic;'>Peste 200 de comenzi livrate cu drag</div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    for i, rev in enumerate(reviews):
        col = c1 if i % 2 == 0 else c2
        with col:
            stars = "★" * rev["stars"] + "☆" * (5 - rev["stars"])
            st.markdown(
                "<div class='review-card'>"
                "<div class='review-name'>" + rev["name"] + "</div>"
                "<div style='color:#111;font-size:0.85rem;margin-top:2px;'>" + stars + "</div>"
                "<div class='review-text'>\"" + rev["text"] + "\"</div>"
                "<div style='font-size:0.68rem;color:#ccc;margin-top:8px;letter-spacing:1px;'>PRODUS: " + rev["produs"].upper() + "</div>"
                "</div>",
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='background:#111;color:white;padding:2rem;text-align:center;'><div style='font-family:Great Vibes,cursive;font-size:2rem;'>★★★★★</div><div style='font-family:Dancing Script,cursive;font-size:1rem;margin-top:4px;color:#aaa;'>4.9 / 5 — bazat pe 200+ recenzii verificate</div></div>", unsafe_allow_html=True)

# ── Contact ───────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.divider()
with st.expander("Comanda personalizata sau contacteaza-ne"):
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

        Str. Florilor 12, Bucuresti
        Telefon: 0721 234 567
        Email: comenzi@laleauaalba.ro

        **Program**
        Luni - Vineri: 9:00 - 19:00
        Sambata: 9:00 - 16:00
        Duminica: Inchis

        ---
        Livrare in Bucuresti si Ilfov
        Plata online sau la livrare
        Mesaj cadou personalizat gratuit
        """)

st.markdown("<div style='text-align:center;color:#ccc;font-size:0.75rem;padding:2rem 0 0.5rem;letter-spacing:2px;font-family:Dancing Script,cursive;font-size:1rem;'>© 2025 Floraría Laleaua Alba · Cu dragoste, pentru tine</div>", unsafe_allow_html=True)
