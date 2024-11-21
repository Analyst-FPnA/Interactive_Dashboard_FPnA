import streamlit as st

# Judul Dashboard
st.title("Interactive Dashboard FPnA")

# Deskripsi
st.markdown("### Klik pada kotak di bawah untuk menuju ke halaman tertentu!")

# Layout kotak interaktif
col1, col2= st.columns(2)

with col1:
    st.markdown(
        "<a href='https://leadtime.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 20px;'>"
        "<strong style='color: black !important;'>LEADTIME REPLENISHMENT</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        '<a href="https://dashboard-safetystock.streamlit.app/" target="_blank" style="text-decoration:none;">'
        '<div style="background-color:#add8e6;padding:20px;text-align:center;border-radius:10px;">'
        '<strong>Safety Stock & Movement Monitoring</strong></div>'
        '</a>',
        unsafe_allow_html=True,
    )

# Baris kedua
col3, col4 = st.columns(2)

with col3:
    st.markdown(
        '<a href="https://dashboard-inventaris.streamlit.app/" target="_blank" style="text-decoration:none;">'
        '<div style="background-color:#90ee90;padding:20px;text-align:center;border-radius:10px;">'
        '<strong>INVENTARIS CONTROL</strong></div>'
        '</a>',
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        '<a href="https://dashboard-harga-barang.streamlit.app/" target="_blank" style="text-decoration:none;">'
        '<div style="background-color:#d8bfd8;padding:20px;text-align:center;border-radius:10px;">'
        '<strong>Harga Barang</strong></div>'
        '</a>',
        unsafe_allow_html=True,
    )
