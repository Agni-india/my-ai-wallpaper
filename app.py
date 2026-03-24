import streamlit as st
import random
import urllib.parse

# --- 1. PAGE CONFIG (Locked) ---
st.set_page_config(page_title="Penguin AI", page_icon="🐧", layout="centered")

# --- 2. SESSION STATE (Locked) ---
if "p_val" not in st.session_state: st.session_state.p_val = ""
if "gen_url" not in st.session_state: st.session_state.gen_url = None

# --- 3. UI & GLOW CSS (Locked & Improved) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    
    /* Locked Glow Buttons */
    .stButton>button { 
        border-radius: 12px; border: 1px solid #4CAF50; background-color: #1A1C23;
        color: white; font-weight: bold; width: 100%; padding: 12px;
        box-shadow: 0 0 5px rgba(76, 175, 80, 0.2); transition: 0.3s;
    }
    .stButton>button:hover { 
        border-color: #00E676; color: #00E676; 
        box-shadow: 0 0 20px rgba(0, 230, 118, 0.5); 
    }

    /* Loader Styling */
    .loader-box { display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px; }
    .penguin-gif { width: 180px; border-radius: 50%; }
    
    /* Footer Locked */
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; text-align: center; padding: 10px; background: #0E1117; border-top: 1px solid #2e2e2e; color: gray; }
    </style>
    """, unsafe_allow_html=True)

st.title("🐧 Penguin AI")
st.write("<p style='text-align: center; color: #88C0D0;'>Pro Art Engine • Optimized Experience</p>", unsafe_allow_html=True)

# --- 4. INPUT AREA ---
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_input("Enter your creative prompt:", value=st.session_state.p_val)
with col2:
    st.write("<br>", unsafe_allow_html=True)
    if st.button("✨"):
        st.session_state.p_val = random.choice(["Cyberpunk Penguin", "Neon Lion", "Space Castle", "Ice Dragon"])
        st.rerun()

# --- 5. GENERATION & NEW PAGE LOGIC ---
if st.button("Generate Masterpiece 🚀", use_container_width=True):
    if user_input:
        st.session_state.p_val = user_input
        
        # DISPLAY DANCING PENGUIN (The UX you wanted)
        with st.container():
            st.markdown(f'''
                <div class="loader-box">
                    <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXF3eXNueXNueXNueXNueXNueXNueXNueXNueXNueXNueSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/v8Y3G96J6qXGf2E5uE/giphy.gif" class="penguin-gif">
                    <h3 style="color:#00E676;">Penguin is Dancing...</h3>
                    <p>Creating your image in the background</p>
                </div>
            ''', unsafe_allow_html=True)
            
            # Generating the URL (Using a more stable universal source)
            seed = random.randint(1, 1000000)
            encoded = urllib.parse.quote(user_input)
            
            # Fixed Source to prevent 404
            final_url = f"https://image.pollinations.ai/prompt/{encoded}?seed={seed}&nologo=true"
            st.session_state.gen_url = final_url

            # SHOW DOWNLOAD BUTTON THAT OPENS IN NEW PAGE (Your Idea)
            st.write("---")
            st.success("Your image is ready to view!")
            st.markdown(f'''
                <a href="{final_url}" target="_blank" style="text-decoration: none;">
                    <button style="width:100%; background: linear-gradient(90deg, #4CAF50, #00E676); color:white; padding:15px; border-radius:12px; border:none; cursor:pointer; font-weight:bold; font-size:18px; box-shadow: 0 4px 15px rgba(0,230,118,0.3);">
                        VIEW & DOWNLOAD IMAGE 📥
                    </button>
                </a>
                <p style="text-align:center; font-size:12px; margin-top:10px;">(Clicking will open the image in a high-quality new tab)</p>
            ''', unsafe_allow_html=True)
    else:
        st.warning("Prompt likho pehle!")

st.markdown('<div class="footer">Built with Passion by Agni-India | 2026</div>', unsafe_allow_html=True)
