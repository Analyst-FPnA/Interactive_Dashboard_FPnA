import streamlit as st

# Judul Dashboard
st.title("Interactive Dashboard")

# Deskripsi
st.markdown("### Klik pada kotak di bawah untuk menuju ke halaman tertentu!")

# Layout kotak interaktif
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<a href="https://www.google.com" target="_blank" style="text-decoration:none;">'
        '<div style="background-color:#ffcccb;padding:20px;text-align:center;border-radius:10px;">'
        '<strong>Google</strong></div>'
        '</a>',
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        '<a href="https://www.youtube.com" target="_blank" style="text-decoration:none;">'
        '<div style="background-color:#add8e6;padding:20px;text-align:center;border-radius:10px;">'
        '<strong>YouTube</strong></div>'
        '</a>',
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        '<a href="https://github.com" target="_blank" style="text-decoration:none;">'
        '<div style="background-color:#90ee90;padding:20px;text-align:center;border-radius:10px;">'
        '<strong>GitHub</strong></div>'
        '</a>',
        unsafe_allow_html=True,
    )

# Baris kedua
col4, col5 = st.columns(2)

with col4:
    st.markdown(
        '<a href="https://www.linkedin.com" target="_blank" style="text-decoration:none;">'
        '<div style="background-color:#ffe4b5;padding:20px;text-align:center;border-radius:10px;">'
        '<strong>LinkedIn</strong></div>'
        '</a>',
        unsafe_allow_html=True,
    )

with col5:
    st.markdown(
        '<a href="https://twitter.com" target="_blank" style="text-decoration:none;">'
        '<div style="background-color:#d8bfd8;padding:20px;text-align:center;border-radius:10px;">'
        '<strong>Twitter</strong></div>'
        '</a>',
        unsafe_allow_html=True,
    )
