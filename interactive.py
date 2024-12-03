import streamlit as st

# Judul Dashboard
st.title("Interactive Dashboard FPnA")

# Deskripsi dengan font khusus
st.markdown(
    "<h1 style='font-family:Roboto,sans-serif; font-size:25px; color:#FFF5E4;'>DASHBOARD</h1>", 
    unsafe_allow_html=True
)

# Layout kotak interaktif
app1, app2= st.columns(2)

with app1:
    st.markdown(
        "<a href='https://leadtime.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#982B1C;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>LEADTIME REPLENISHMENT</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

with app2:
    st.markdown(
        "<a href='https://dashboard-harga-barang.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#982B1C;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>ANALISA PEMBELIAN BARANG</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

# Baris kedua
app3, app4 = st.columns(2)

with app3:
    st.markdown(
        "<a href='https://dashboard-safetystock.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#982B1C;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>SAFETY STOCK & MOVEMENT</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

with app4:
    st.markdown(
        "<a href='https://dashboard-inventaris.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#982B1C;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>INVENTORY CONTROL</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

# Baris ketiga
app5, app6 = st.columns(2)

with app5:
    st.markdown(
        "<a href='https://dashboard-selisih-ojol.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#982B1C;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>REKAP SELISIH OJOL</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

with app6:
    st.markdown(
        "<a href='https://dashboard-promix.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#982B1C;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 16px;'>"
        "<strong style='color:white;'>PRODUCT MIX</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

# Deskripsi
st.markdown(
    "<h1 style='font-family:Roboto,sans-serif; font-size:25px; color:#FFF5E4;'>TOOLS</h1>", 
    unsafe_allow_html=True
)

# Layout kotak interaktif
tool1, tool2, tool3= st.columns(3)

with tool1:
    st.markdown(
        "<a href='https://abo-analyst.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#982B1C;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 12px;'>"
        "<strong style='color:white;'>Automatic Breakdown Ojol</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

with tool2:
    st.markdown(
        "<a href='https://dashboard-gis-cleaning-and-rekap-scm.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#982B1C;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 12px;'>"
        "<strong style='color:white;'>GIS Cleaning & REKAP SCM</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )

with tool3:
    st.markdown(
        "<a href='https://9901-error-checking.streamlit.app/' target='_blank' style='text-decoration:none;'>"
        "<div style='background-color:#982B1C;padding:20px;text-align:center;border-radius:10px;color:black; font-family:Roboto,sans-serif; font-size: 11px;'>"
        "<strong style='color:white;'>Automate Error Checking (99.01)</strong></div>"
        "</a>",
        unsafe_allow_html=True,
    )
