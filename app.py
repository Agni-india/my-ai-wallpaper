import streamlit as st
import random
import time
import urllib.parse

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Penguin AI", page_icon="🐧", layout="centered")

# --- 2. SESSION STATE ---
if "p_val" not in st.session_state: st.session_state.p_val = ""
if "history" not in st.session_state: st.session_state.history = []

# --- 3. PREMIUM CSS (Animations & Theme) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { 
        border-radius: 12px; border: 1px solid #4CAF50; background-color: #1A1C23;
        color: white; font-weight: bold; width: 100%; padding: 12px;
    }
    .stButton>button:hover { border-color: #00E676; box-shadow: 0 0 20px rgba(0, 230, 118, 0.4); }
    
    /* Center the Dancing Penguin */
    .loader-container { display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px; }
    .penguin-loader { width: 150px; }
    
    .final-img { width: 100%; border-radius: 20px; border: 2px solid #2e2e2e; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; text-align: center; padding: 10px; background: #0E1117; border-top: 1px solid #2e2e2e; color: gray; }
    </style>
    """, unsafe_allow_html=True)

st.title("🐧 Penguin AI")
st.write("<p style='text-align: center; color: #88C0D0;'>Multi-Node AI Art Engine • No Limits</p>", unsafe_allow_html=True)

# --- 4. UI INPUT ---
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_input("What should the Penguin create?", value=st.session_state.p_val)
with col2:
    st.write("<br>", unsafe_allow_html=True)
    if st.button("✨"):
        st.session_state.p_val = random.choice(["Cyberpunk Penguin", "Neon Lion", "Space Castle", "Ice Dragon"])
        st.rerun()

# --- 5. THE MAGIC GENERATOR ---
if st.button("Generate Masterpiece 🚀", use_container_width=True):
    if user_input:
        # STEP 1: SHOW DANCING PENGUIN LOADER
        loader_placeholder = st.empty()
        with loader_placeholder.container():
            st.markdown(f'''
                <div class="loader-container">
                    <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXF3eXNueXNueXNueXNueXNueXNueXNueXNueXNueXNueSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/v8Y3G96J6qXGf2E5uE/giphy.gif" class="penguin-loader">
                    <p>Penguin is dancing while AI is thinking... 🎨</p>
                </div>
            ''', unsafe_allow_html=True)
        
        # Artificial delay for the "feel" (Optional)
        time.sleep(3) 

        # STEP 2: MULTI-SOURCE LOGIC (Aggregator)
        seed = random.randint(1, 1000000)
        encoded = urllib.parse.quote(user_input)
        
        # Hum 3 alag-alag backup sources rakhte hain
        sources = [
            f"https://image.pollinations.ai/prompt/{encoded}?seed={seed}&width=1024&height=1024&nologo=true",
            f"https://api.dicebear.com/7.x/identicon/svg?seed={seed}", # Backup if AI fails
            f"https://picsum.photos/seed/{seed}/1024/1024" # Ultimate backup
        ]
        
        # Primary Image URL
        final_url = sources[0] 

        # STEP 3: REPLACE LOADER WITH IMAGE
        loader_placeholder.empty()
        st.markdown(f'<img src="{final_url}" class="final-img">', unsafe_allow_html=True)
        
        # Download Button
        st.write("<br>", unsafe_allow_html=True)
        st.markdown(f'''
            <a href="{final_url}" target="_blank">
                <button style="width:100%; background-color:#4CAF50; color:white; padding:15px; border-radius:12px; border:none; cursor:pointer; font-weight:bold;">
                    Download High-Res 📥
                </button>
            </a>
        ''', unsafe_allow_html=True)
        
        # Save to history
        st.session_state.history.insert(0, final_url)
    else:
        st.warning("Prompt likh de bhai!")

# --- 6. HISTORY ---
if st.session_state.history:
    st.write("---")
    st.subheader("🕒 Recent Art")
    h_cols = st.columns(3)
    for i, url in enumerate(st.session_state.history[:6]):
        with h_cols[i % 3]:
            st.image(url, use_container_width=True)

st.markdown('<div class="footer">Built with Passion by Agni-India</div>', unsafe_allow_html=True)
