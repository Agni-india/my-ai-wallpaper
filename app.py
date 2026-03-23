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

# --- 2. THEME & CSS (KEEPING IT AS YOU LIKED) ---
st.markdown("""
    <style>
    /* Dark Theme Force */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    /* Button Styling */
    .stButton>button {
        background-color: #2E3440;
        color: #88C0D0;
        border-radius: 10px;
        border: 1px solid #88C0D0;
        height: 3em;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #88C0D0;
        color: #2E3440;
    }
    /* Input Box Styling */
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
    /* Hide default menu */
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
    prompt = st.text_input("", placeholder="Describe your dream wallpaper (e.g., Cyberpunk Penguin in Tokyo)...")
    
    # Generate Button
    if st.button("Generate Magic ✨"):
        if prompt:
            with st.spinner("Wait bhai... Penguin is painting your imagination 🎨"):
                try:
                    # Using 'flux' model for higher stability and fewer errors
                    seed = random.randint(1, 1000000)
                    image_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1280&height=720&seed={seed}&model=flux&nologo=true"
                    
                    # Verifying if image is accessible
                    response = requests.get(image_url, timeout=15)
                    
                    if response.status_code == 200:
                        st.image(image_url, caption=f"Result: {prompt}", use_container_width=True)
                        
                        # Download Link Button
                        st.markdown(f'''
                            <a href="{image_url}" target="_blank">
                                <button style="width:100%; background-color:#A3BE8C; color:black; border-radius:10px; padding:10px; border:none; cursor:pointer; font-weight:bold; margin-top:10px;">
                                    Open & Save Image 📥
                                </button>
                            </a>
                            ''', unsafe_allow_html=True)
                        st.success("Bhai, wallpaper taiyar hai!")
                    else:
                        st.error("Server thoda busy hai, 2-3 second baad phir se 'Generate' dabao!")
                        
                except Exception as e:
                    st.error("Internal connection error! Ek baar phir try karo.")
        else:
            st.warning("Bhai, pehle kuch likho toh sahi!")

# --- 4. FOOTER ---
st.markdown("<br><br><hr><p style='text-align: center; color: #
