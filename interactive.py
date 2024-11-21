import streamlit as st

# Judul Dashboard
st.title("Interactive Dashboard FPnA")

# Deskripsi
st.markdown("### Klik pada kotak di bawah untuk menuju ke halaman tertentu!")

# Deskripsi
st.markdown("DASHBOARD")

# Layout kotak interaktif
col1, col2= st.columns(2)

with col1:
    st.markdown(
        "<a href='https://leadtime.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>LEADTIME REPLENISHMENT</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        "<a href='https://dashboard-harga-barang.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>ANALISA PEMBELIAN BARANG</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

# Baris kedua
col3, col4 = st.columns(2)

with col3:
    st.markdown(
        "<a href='https://dashboard-safetystock.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>SAFETY STOCK & MOVEMENT</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        "<a href='https://dashboard-inventaris.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>INVENTORY CONTROL</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

# Baris ketiga
col5, col6 = st.columns(2)

with col5:
    st.markdown(
        "<a href='https://https://dashboard-selisih-ojol.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>REKAP SELISIH OJOL</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

with col6:
    st.markdown(
        "<a href='https://dashboard-promix.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>PRODUCT MIX</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )