import streamlit as st

# Website ki settings
st.set_page_config(page_title="Agni AI Wallpaper", page_icon="🎨")

# Main Page ki Heading
st.title("🔥 Agni AI: Unlimited Wallpaper Gen")
st.write("Class 10th Project - Unlimited & Free Wallpapers")

# Prompt box jahan user likhega
prompt = st.text_input("Enter your idea (Example: 'Realistic Dragon' or 'Cyberpunk Car'):")

if st.button("Generate Wallpaper"):
    if prompt:
        # AI ko batana ki kya image banani hai
        # Humne resolution 1080x1920 rakha hai jo phone ke liye best hai
        image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width=1080&height=1920&nologo=true"
        
        # Image dikhana
        st.image(image_url, caption=f"Result for: {prompt}", use_column_width=True)
        
        # Download button/link
        st.markdown(f"### [📥 Download Image]({image_url})")
    else:
        st.warning("Bhai, pehle kuch likho toh sahi!")
