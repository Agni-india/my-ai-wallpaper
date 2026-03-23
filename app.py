import streamlit as st
import random

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Penguin AI", page_icon="🐧", layout="wide")

# --- 2. SESSION STATE (For History) ---
if 'history' not in st.session_state:
    st.session_state.history = []

# --- 3. CSS (DESIGN LOCK) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { 
        background-color: #2E3440; color: #88C0D0; 
        border-radius: 10px; border: 1px solid #88C0D0; width: 100%; font-weight: bold;
    }
    .stButton>button:hover { background-color: #88C0D0; color: #2E3440; }
    h1 { color: #88C0D0 !important; text-align: center; }
    .history-card { border: 1px solid #4C566A; border-radius: 5px; padding: 5px; margin: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🐧 PENGUIN AI")

# --- 4. GENERATION AREA ---
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    prompt = st.text_input("Describe your masterpiece:", placeholder="e.g. Iron Man Penguin on Ice...")
    
    if st.button("Generate Magic ✨"):
        if prompt:
            with st.spinner("Wait... Penguin is painting 🎨"):
                seed = random.randint(1, 1000000)
                # Hum image URL ko "Verified" format mein dalenge
                image_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed={seed}&model=flux"
                
                # Main Image Display
                st.image(image_url, caption="Your Generated Art", use_container_width=True)
                
                # History mein save karo
                st.session_state.history.insert(0, image_url)
                
                # Download Button
                st.markdown(f'<a href="{image_url}" target="_blank"><button style="width:100%; background-color:#A3BE8C; color:black; border-radius:10px; padding:10px; border:none; cursor:pointer; font-weight:bold;">Open & Save High-Res 📥</button></a>', unsafe_allow_html=True)
        else:
            st.warning("Prompt toh dalo bhai!")

# --- 5. HISTORY SECTION (YE HAI NAYA MAST FEATURE) ---
if st.session_state.history:
    st.write("---")
    st.subheader("Your Recent Creations 🎨")
    h_cols = st.columns(4) # 4 images ek line mein
    for i, h_url in enumerate(st.session_state.history[:8]): # Sirf last 8 dikhayega
        with h_cols[i % 4]:
            st.image(h_url, use_container_width=True)
            st.caption(f"Art #{i+1}")

st.markdown("<br><hr><p style='text-align: center; color: #4C566A;'>Built with Passion by Agni-India</p>", unsafe_allow_html=True)
