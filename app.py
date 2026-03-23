import streamlit as st
import requests
import random

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Penguin AI - Wallpaper Gen",
    page_icon="🐧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. THEME & CSS (KEEPING DARK MODE) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #2E3440;
        color: #88C0D0;
        border-radius: 10px;
        border: 1px solid #88C0D0;
        height: 3em;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #88C0D0;
        color: #2E3440;
    }
    .stTextInput>div>div>input {
        background-color: #1A1C23;
        color: white;
        border: 1px solid #4C566A;
    }
    h1 {
        color: #88C0D0 !important;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. MAIN INTERFACE ---
st.title("🐧 PENGUIN AI")
st.write("<p style='text-align: center; color: #D8DEE9;'>The Ultimate AI Wallpaper Engine</p>", unsafe_allow_html=True)

# Layout for Input
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    prompt = st.text_input("", placeholder="Describe your dream wallpaper (e.g., Cyberpunk Penguin)...", key="user_input")
    
    # Generate Button
    if st.button("Generate Magic ✨"):
        if prompt:
            with st.spinner("Wait bhai... Penguin is painting 🎨"):
                try:
                    seed = random.randint(1, 1000000)
                    # Fixed model to FLUX for stability
                    image_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1280&height=720&seed={seed}&model=flux&nologo=true"
                    
                    # Testing if server is responding
                    st.image(image_url, caption=f"Result: {prompt}", use_container_width=True)
                    
                    # Open/Download Link
                    st.markdown(f'''
                        <a href="{image_url}" target="_blank">
                            <button style="width:100%; background-color:#A3BE8C; color:black; border-radius:10px; padding:10px; border:none; cursor:pointer; font-weight:bold; margin-top:10px;">
                                Open & Save Image 📥
                            </button>
                        </a>
                        ''', unsafe_allow_html=True)
                    st.success("Bhai, wallpaper taiyar hai!")
                        
                except Exception as e:
                    st.error("Connection error! Ek baar phir try karo.")
        else:
            st.warning("Pehle kuch likho toh sahi!")

# --- 4. FOOTER (FIXED SYNTAX) ---
st.markdown("<br><br><hr><p style='text-align: center; color: #4C566A;'>Built with Passion by Agni-India</p>", unsafe_allow_html=True)
