import streamlit as st
import requests
import io
from PIL import Image
import time
import random

# --- 1. CONFIG & AUTH (Locked) ---
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer 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"}

st.set_page_config(page_title="Penguin AI", page_icon="🐧", layout="centered")

# --- 2. SESSION STATE ---
if "p_val" not in st.session_state: st.session_state.p_val = ""
if "generated_image" not in st.session_state: st.session_state.generated_image = None

# --- 3. UI & GLOW CSS (LOCKED UX) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { 
        border-radius: 12px; border: 1px solid #4CAF50; background-color: #1A1C23;
        color: white; font-weight: bold; width: 100%; padding: 15px;
        box-shadow: 0 0 5px rgba(76, 175, 80, 0.2); transition: 0.3s;
    }
    .stButton>button:hover { 
        border-color: #00E676; color: #00E676; 
        box-shadow: 0 0 20px rgba(0, 230, 118, 0.5); 
    }
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; text-align: center; padding: 10px; background: #0E1117; border-top: 1px solid #2e2e2e; color: gray; }
    img { border-radius: 15px; border: 1px solid #333; box-shadow: 0 0 20px rgba(0,0,0,0.5); }
    </style>
    """, unsafe_allow_html=True)

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

st.title("🐧 Penguin AI")
st.write("<p style='text-align: center; color: #88C0D0;'>Powered by Hugging Face • High-Res Wallpapers</p>", unsafe_allow_html=True)

# --- 4. INPUT AREA ---
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_input("Describe your vision:", value=st.session_state.p_val, placeholder="E.g. A futuristic cyberpunk city, 8k, cinematic...")
with col2:
    st.write("<br>", unsafe_allow_html=True)
    if st.button("✨"):
        ideas = ["Neon Samurai Penguin", "Galaxy in a Bottle", "Viking Warrior 8k", "Cyberpunk Mumbai 2077"]
        st.session_state.p_val = random.choice(ideas)
        st.rerun()

# --- 5. GENERATION LOGIC (The New Engine) ---
if st.button("Generate Masterpiece 🚀", use_container_width=True):
    if user_input:
        st.session_state.p_val = user_input
        with st.status("Connecting to Hugging Face GPUs...", expanded=True) as status:
            st.write("🎨 Rendering your wallpaper...")
            
            # Adding "Wallpaper" quality keywords automatically
            full_prompt = f"{user_input}, high resolution, 8k, highly detailed, masterpiece, cinematic lighting"
            
            image_bytes = query({"inputs": full_prompt})
            
            try:
                image = Image.open(io.BytesIO(image_bytes))
                st.session_state.generated_image = image
                status.update(label="Art Generated Successfully!", state="complete", expanded=False)
            except:
                st.error("Model is loading... Please wait 30 seconds and try again. (Hugging Face is waking up the GPU)")
    else:
        st.warning("Prompt likho pehle bhai!")

# --- 6. DISPLAY & DOWNLOAD ---
if st.session_state.generated_image:
    st.image(st.session_state.generated_image, use_container_width=True)
    
    # Download Button Logic
    buf = io.BytesIO()
    st.session_state.generated_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="📥 Download Wallpaper",
        data=byte_im,
        file_name="penguin_ai_wallpaper.png",
        mime="image/png",
        use_container_width=True
    )

st.markdown('<div class="footer">Built with Passion by Agni-India • 2026</div>', unsafe_allow_html=True)
