import streamlit as st
import requests

# API ma'lumotlari
API_URL = 'https://api.api-ninjas.com/v1/facedetect'
API_KEY = 'zCy1/udLBOpFpnenHh5H5A==OsXjLVUXpi1Q62B4'

def detect_faces(image_file):
    """yuzlarni aniqlash"""
    files = {'image': image_file}
    headers = {'X-Api-Key': API_KEY}
    response = requests.post(API_URL, files=files, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API xatosi: {response.status_code}, {response.text}")
        return None

# Streamlit UI
st.title("Yuzni Aniqlash Dasturi")
st.write("Tasvirni yuklang va yuzlarni aniqlang!")

# Foydalanuvchidan tasvir yuklash
uploaded_file = st.file_uploader("Tasvir yuklash", type=["jpeg", "jpg", "png"])

if uploaded_file is not None:
    # Yuklangan tasvirni ko'rsatish
    st.image(uploaded_file, caption="Yuklangan tasvir", use_container_width=True)
    
    if st.button("Yuzlarni Aniqlash"):
        with st.spinner("Aniqlanmoqda..."):
            result = detect_faces(uploaded_file)
            
            if result:
                # Natijalarni ko'rsatish
                faces = result.get('faces', [])
                if faces:
                    st.success(f"Yuzlar aniqlangan: {len(faces)}")
                    for idx, face in enumerate(faces, start=1):
                        st.write(f"Yuz {idx}:")
                        st.json(face)  # Yuzning batafsil ma'lumotlari
                else:
                    st.warning("Hech qanday yuz aniqlanmadi.")
