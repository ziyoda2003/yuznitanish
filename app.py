import streamlit as st
import requests
import pandas as pd

# API ma'lumotlari
API_URL = 'https://api.api-ninjas.com/v1/facedetect'
API_KEY = 'zCy1/udLBOpFpnenHh5H5A==OsXjLVUXpi1Q62B4'

def detect_faces(image_file):
    """API orqali yuzlarni aniqlash"""
    files = {'image': image_file}
    headers = {'X-Api-Key': API_KEY}
    response = requests.post(API_URL, files=files, headers=headers)
    if response.status_code == 200:
        return response.json()  # JSON javob qaytariladi
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
            
            if result is not None:  # result mavjudligini tekshirish
                if isinstance(result, list) and len(result) > 0:  # Javob `list` formatida bo'lsa
                    st.success(f"Yuzlar aniqlangan: {len(result)}")
                    
                    # Natijalarni DataFrame ko'rinishida tayyorlash
                    face_data = []
                    for idx, face in enumerate(result, start=1):
                        face_data.append({
                            "Yuz raqami": idx,
                            "Top (yuqori)": face.get('top'),
                            "Left (chap)": face.get('left'),
                            "Width (eni)": face.get('width'),
                            "Height (bo'yi)": face.get('height')
                        })
                    
                    # Pandas DataFrame yaratish
                    df = pd.DataFrame(face_data)
                    
                    # Jadvalni ko'rsatish
                    st.dataframe(df)
                else:
                    st.warning("Hech qanday yuz aniqlanmadi.")
            else:
                st.error("API dan hech qanday ma'lumot qaytarilmadi.")



# import streamlit as st
# import requests

# # API ma'lumotlari
# API_URL = 'https://api.api-ninjas.com/v1/facedetect'
# API_KEY = 'zCy1/udLBOpFpnenHh5H5A==OsXjLVUXpi1Q62B4'

# def detect_faces(image_file):
#     """API orqali yuzlarni aniqlash"""
#     files = {'image': image_file}
#     headers = {'X-Api-Key': API_KEY}
#     response = requests.post(API_URL, files=files, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         st.error(f"API xatosi: {response.status_code}, {response.text}")
#         return None

# # Streamlit UI
# st.title("Yuzni Aniqlash Dasturi")
# st.write("Tasvirni yuklang va yuzlarni aniqlang!")

# # Foydalanuvchidan tasvir yuklash
# uploaded_file = st.file_uploader("Tasvir yuklash", type=["jpeg", "jpg", "png"])

# if uploaded_file is not None:
#     # Yuklangan tasvirni ko'rsatish
#     st.image(uploaded_file, caption="Yuklangan tasvir", use_container_width=True)
    
#     if st.button("Yuzlarni Aniqlash"):
#         with st.spinner("Aniqlanmoqda..."):
#             result = detect_faces(uploaded_file)
            
#             if result is not None:  # result mavjudligini tekshirish
#                 faces = result.get('faces', [])
#                 if faces:
#                     st.success(f"Yuzlar aniqlangan: {len(faces)}")
#                     for idx, face in enumerate(faces, start=1):
#                         st.write(f"Yuz {idx}:")
#                         st.json(face)  # Yuzning batafsil ma'lumotlari
#                 else:
#                     st.warning("Hech qanday yuz aniqlanmadi.")
#             else:
#                 st.error("API dan hech qanday ma'lumot qaytarilmadi.")


# import streamlit as st
# import requests

# # API ma'lumotlari
# API_URL = 'https://api.api-ninjas.com/v1/facedetect'
# API_KEY = 'zCy1/udLBOpFpnenHh5H5A==OsXjLVUXpi1Q62B4'

# def detect_faces(image_file):
#     """yuzlarni aniqlash"""
#     files = {'image': image_file}
#     headers = {'X-Api-Key': API_KEY}
#     response = requests.post(API_URL, files=files, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         st.error(f"API xatosi: {response.status_code}, {response.text}")
#         return None

# # Streamlit UI
# st.title("Yuzni Aniqlash Dasturi")
# st.write("Tasvirni yuklang va yuzlarni aniqlang!")

# # Foydalanuvchidan tasvir yuklash
# uploaded_file = st.file_uploader("Tasvir yuklash", type=["jpeg", "jpg", "png"])

# if uploaded_file is not None:
#     # Yuklangan tasvirni ko'rsatish
#     st.image(uploaded_file, caption="Yuklangan tasvir", use_container_width=True)
    
#     if st.button("Yuzlarni Aniqlash"):
#         with st.spinner("Aniqlanmoqda..."):
#             result = detect_faces(uploaded_file)
            
#             if result:
#                 # Natijalarni ko'rsatish
#                 faces = result.get('faces', [])
#                 if faces:
#                     st.success(f"Yuzlar aniqlangan: {len(faces)}")
#                     for idx, face in enumerate(faces, start=1):
#                         st.write(f"Yuz {idx}:")
#                         st.json(face)  # Yuzning batafsil ma'lumotlari
#                 else:
#                     st.warning("Hech qanday yuz aniqlanmadi.")
