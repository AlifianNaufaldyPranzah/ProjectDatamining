import streamlit as st

st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Average Status Pemain</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: white; margin:0 ; padding:0;'>WAJIB MENGISI SEMUA KOLOM</h5>", unsafe_allow_html=True)

st.text_input("Masukkan Nama",placeholder='Nama pemain')
st.number_input("Masukkan Umur",max_value=100)
st.selectbox("Jenis Kelamin",('Laki-laki','Perempuan'))
st.number_input("Total Permainan",min_value=0,max_value=1000)
st.number_input("Total Menang",min_value=0,max_value=1000)
st.number_input("Total Kalah",min_value=0,max_value=1000)
st.button("submit")