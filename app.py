import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import urllib.parse
import random

# --- Configuration & Custom CSS ---
st.set_page_config(page_title="Penguin AI", page_icon="🐧", layout="centered")

def inject_custom_css():
    """Injects custom CSS for a premium dark theme and footer."""
    st.markdown(
        """
        <style>
        /* Premium Dark Theme Adjustments */
        .stApp {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        /* Custom Button Styling */
        .stButton>button {
            border-radius: 8px;
            border: 1px solid #4CAF50;
            transition: 0.3s;
            font-weight: 600;
        }
        .stButton>button:hover {
            border: 1px solid #00E676;
            color: #00E676;
            box-shadow: 0 4px 12px rgba(0, 230, 118, 0.2);
        }
        /* Sticky Footer */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            padding: 12px;
            font-size: 14px;
            color: #A0A0A0;
            background: rgba(14, 17, 23, 0.95);
            z-index: 100;
            border-top: 1px solid #2e2e2e;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# --- Session State Management ---
if "history" not in st.session_state:
    st.session_state.history = []
if "prompt_input" not in st.session_state:
    st.session_state.prompt_input = ""

# --- Core Logic ---
def generate_image_with_fallback(prompt, max_retries=4):
    """
    Robust image generation attempting multiple models and seeds.
    Validates image bytes to ensure no broken images are returned.
    """
    encoded_prompt = urllib.parse.quote(prompt)
    models = ["flux", "sana", "turbo"]
    
    for attempt in range(max_retries):
        model = random.choice(models)
        seed = random.randint(1, 999999)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?seed={seed}&width=1024&height=1024&nologo=true&model={model}"
        
        try:
            # 15-second timeout to prevent infinite hanging
            response = requests.get(url, timeout=15) 
            
            if response.status_code == 200:
                try:
                    # Validate that the byte stream is a legitimate, unbroken image
                    image_bytes = BytesIO(response.content)
                    img = Image.open(image_bytes)
                    img.verify() # Checks for broken file headers
                    
                    # Re-open because verify() closes the stream state
                    valid_image = Image.open(BytesIO(response.content))
                    return valid_image
                except Exception:
                    # Catch PIL Image loading errors (broken image)
                    continue 
        except requests.exceptions.RequestException:
            # Catch network errors, timeouts, and connection drops
            continue 
            
    # Return None if all retries are exhausted
    return None

# --- UI Layout ---
inject_custom_css()

st.title("🐧 Penguin AI")
st.markdown("### High-End Image Generation Engine")

# "Surprise Me" Data
surprise_prompts = [
    "A cyberpunk penguin hacker typing on a neon keyboard, 8k resolution, unreal engine 5",
    "A majestic floating castle inside a giant glass bottle, ethereal lighting",
    "A futuristic racing car drifting on a glowing bioluminescent track, synthwave style",
    "Macro photography of a tiny glowing mushroom forest in a terrarium, highly detailed"
]

# Prompt Input Area
col1, col2 = st.columns([4, 1])
with col1:
    user_prompt = st.text_input("Describe your vision:", value=st.session_state.prompt_input, key="prompt_widget")
with col2:
    st.write("") # Vertical alignment padding
    st.write("")
    if st.button("Surprise Me ✨"):
        st.session_state.prompt_input = random.choice(surprise_prompts)
        st.rerun()

# Generation Execution
if st.button("Generate Image 🚀", use_container_width=True):
    if not user_prompt.strip():
        st.warning("Please enter a prompt to get started.")
    else:
        with st.spinner("Connecting to neural nodes... Crafting your masterpiece..."):
            img = generate_image_with_fallback(user_prompt)
            
            if img:
                st.success("Masterpiece generated successfully!")
                st.image(img, use_container_width=True)
                
                # Prepare image for download
                buf = BytesIO()
                img.save(buf, format="PNG")
                byte_im = buf.getvalue()
                
                st.download_button(
                    label="Download High-Res Image ⬇️",
                    data=byte_im,
                    file_name="penguin_ai_masterpiece.png",
                    mime="image/png",
                    use_container_width=True
                )
                
                # Update Session History
                st.session_state.history.insert(0, {"prompt": user_prompt, "image": img})
            else:
                st.error("⚠️ All generation attempts failed. The servers might be overloaded. Please try a different prompt or wait a moment.")

# --- History Gallery ---
if st.session_state.history:
    st.markdown("---")
    st.markdown("### 🕒 Session Gallery")
    # Create rows of 3 columns for the gallery
    cols = st.columns(3)
    # Display up to the last 9 images
    for idx, item in enumerate(st.session_state.history[:9]): 
        with cols[idx % 3]:
            st.image(item["image"], caption=item["prompt"][:40] + "...", use_container_width=True)

# --- Footer ---
st.markdown('<div class="footer">Built with Passion by Agni-India</div>', unsafe_allow_html=True)
