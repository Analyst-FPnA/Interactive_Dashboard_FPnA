import streamlit as st

# Judul Dashboard
st.title("Interactive Dashboard FPnA")

# Deskripsi
st.markdown("### Klik pada kotak di bawah untuk menuju ke halaman tertentu!")

# Deskripsi
st.markdown("# DASHBOARD")

# Layout kotak interaktif
app1, app2= st.columns(2)

with app1:
    st.markdown(
        "<a href='https://leadtime.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>LEADTIME REPLENISHMENT</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

with app2:
    st.markdown(
        "<a href='https://dashboard-harga-barang.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>ANALISA PEMBELIAN BARANG</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

# Baris kedua
app3, app4 = st.columns(2)

with app3:
    st.markdown(
        "<a href='https://dashboard-safetystock.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>SAFETY STOCK & MOVEMENT</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

with app4:
    st.markdown(
        "<a href='https://dashboard-inventaris.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>INVENTORY CONTROL</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

# Baris ketiga
app5, app6 = st.columns(2)

with app5:
    st.markdown(
        "<a href='https://https://dashboard-selisih-ojol.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>REKAP SELISIH OJOL</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

with app6:
    st.markdown(
        "<a href='https://dashboard-promix.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>PRODUCT MIX</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

# Deskripsi
st.markdown("# TOOLS")

# Layout kotak interaktif
tool1, tool2= st.columns(2)

with tool1:
    st.markdown(
        "<a href='https://leadtime.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>LEADTIME REPLENISHMENT</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

with tool2:
    st.markdown(
        "<a href='https://dashboard-harga-barang.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#800000;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>ANALISA PEMBELIAN BARANG</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )
