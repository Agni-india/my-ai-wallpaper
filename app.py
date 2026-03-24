import streamlit as st
import random
import urllib.parse

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Penguin AI", page_icon="🐧", layout="centered")

# --- 2. SESSION STATE ---
if "p_val" not in st.session_state:
    st.session_state.p_val = ""
if "history" not in st.session_state:
    st.session_state.history = []

# --- 3. PREMIUM DARK CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { 
        border-radius: 12px; border: 1px solid #4CAF50; background-color: #1A1C23;
        color: white; font-weight: bold; width: 100%; padding: 10px;
    }
    .stButton>button:hover { border-color: #00E676; color: #00E676; box-shadow: 0 0 15px rgba(0, 230, 118, 0.4); }
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; text-align: center; padding: 10px; background: #0E1117; border-top: 1px solid #2e2e2e; color: gray; z-index: 99; }
    .main-img { width: 100%; border-radius: 20px; border: 2px solid #2e2e2e; margin-top: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    .hist-img { width: 100%; border-radius: 10px; margin-bottom: 10px; transition: 0.3s; }
    .hist-img:hover { transform: scale(1.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("🐧 Penguin AI")
st.write("<p style='text-align: center; color: #88C0D0; margin-top: -15px;'>High-End Image Generation Engine</p>", unsafe_allow_html=True)

# --- 4. SURPRISE ME DATA ---
surprise_list = [
    "A cyberpunk penguin with glowing blue eyes, futuristic city background",
    "A majestic lion made of fire and ice, cinematic lighting, 8k",
    "A surreal portal to another galaxy inside a deep forest",
    "An astronaut penguin walking on the moon, earth in background"
]

# --- 5. UI LAYOUT ---
col1, col2 = st.columns([4, 1])

with col1:
    # Capturing input and linking it to session state
    u_input = st.text_input("Describe your vision:", value=st.session_state.p_val, placeholder="E.g. A magic penguin...")

with col2:
    st.write("<br>", unsafe_allow_html=True)
    if st.button("Surprise ✨"):
        st.session_state.p_val = random.choice(surprise_list)
        st.rerun()

# Execute Generation
if st.button("Generate Masterpiece 🚀", use_container_width=True):
    if u_input:
        st.session_state.p_val = u_input # Ensure current input is saved
        with st.spinner("Wait... Penguin is painting 🎨"):
            seed = random.randint(1, 999999)
            encoded = urllib.parse.quote(u_input)
            
            # THE FIX: Direct HTML URL that works 100%
            img_url = f"https://pollinations.ai/p/{encoded}?seed={seed}&width=1024&height=1024&model=flux&nologo=true"
            
            # Displaying via Markdown to avoid Streamlit's internal image failures
            st.markdown(f'<img src="{img_url}" class="main-img">', unsafe_allow_html=True)
            
            # Professional Action Buttons
            st.write("<br>", unsafe_allow_html=True)
            st.markdown(f'''
                <a href="{img_url}" target="_blank">
                    <button style="width:100%; background-color:#4CAF50; color:white; padding:15px; border-radius:12px; border:none; cursor:pointer; font-weight:bold; font-size:16px;">
                        Download High-Res (Full HD) 📥
                    </button>
                </a>
            ''', unsafe_allow_html=True)
            
            # Save to History
            if {"p": u_input, "u": img_url} not in st.session_state.history:
                st.session_state.history.insert(0, {"p": u_input, "u": img_url})
    else:
        st.warning("Prompt likho pehle!")

# --- 6. HISTORY GALLERY ---
if st.session_state.history:
    st.write("---")
    st.subheader("🕒 Recent Creations")
    h_cols = st.columns(3)
    for i, item in enumerate(st.session_state.history[:6]):
        with h_cols[i % 3]:
            st.markdown(f'<img src="{item["u"]}" class="hist-img">', unsafe_allow_html=True)

st.markdown('<div class="footer">Built with Passion by Agni-India | © 2026</div>', unsafe_allow_html=True)
