import streamlit as st
import datset
import time
import webbrowser

st.set_page_config(
    page_title="",
    page_icon="https://freepngimg.com/save/93231-toy-pubg-mobile-sticker-machine-battlegrounds-playerunknown/512x512",
)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



kolom = st.columns((2, 0.48, 2.7))
home = kolom[1].button('Home')
about = kolom[2].button('About')

# home page
if home==False and about==False or home==True and about==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Prediksi Diabetes</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: white; margin:0 ; padding:0;'>WAJIB MENGISI SEMUA KOLOM</h5>", unsafe_allow_html=True)

    col1, col2,col3 = st.columns(3)
    with col1:
        nama = st.text_input("Nama", placeholder= 'Nama')
    with col2:
        umur = st.number_input("Age",min_value=0,max_value=120)
    with col3:
        jk = st.selectbox("Gender",('Laki-laki','Perempuan'))
    st.write("Isi 0 jika positif")
    poliuria = st.number_input("Polyuria",min_value=0,max_value=999)
    polidipsia = st.number_input("Polydipsia",min_value=0,max_value=999)
    lostweight = st.number_input("sudden weight loss",min_value=0,max_value=999)
    poligapia = st.number_input("Polyphagia",max_value=999)
    columns = st.columns((2, 0.6, 2))
    sumbit = columns[1].button("Submit")
    if sumbit and nama != '' and umur != 0 and jk != '':
        # cek jenis kelamin
        #0 = laki-laki
        #1 = perempuan
        if jk == 'Laki-laki':
            jk = 0
        else:
            jk = 1
        # normalisasi data
        data = datset.normalisasi([umur,jk,poliuria,polidipsia,lostweight,poligapia])
        # prediksi data
        prediksi = datset.knn(data)    
        # cek prediksi
        with st.spinner("Tunggu Sebentar Masih Proses..."):
            if prediksi[-1]== 0:
                time.sleep(1)
                st.success("Hasil Prediksi : "+nama+" - Positive, Terkena penyakit diabetes")
            else :  
                time.sleep(1)
                st.warning("Hasil Prediksi : "+nama+" - Negative, tidak terkena penyakit diabetes")

st.write('Another :')
colum = st.columns((0.1,0.2,1))
url = 'https://github.com/AlifianNaufaldyPranzah/ProjectDatamining'

if colum[1].button('GitHub'):
    webbrowser.open_new_tab(url)

link = 'https://alifiannaufaldypranzah.github.io/Datamining/Project.html?highlight=project'

if colum[2].button('Jupyter'):
    webbrowser.open_new_tab(link)
# colum = st.columns((0.1,10,1.5))
# github= colum[1].button("check out this [link]()")
# jupyter = colum[2].button("")


st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# about page
if about==True and home==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Sistem</h1>", unsafe_allow_html=True)
    st.write('Sistem ini dibuat dengan tujuan untuk memprediksi seseorang apakah terkena penyakit diabetes atau tidak.')
    st.write('Dengan memasukkan fitur yang telah disediakan sistem ini dapat memprediksi apakah pengguna mengalami diabetes atau tidak.')
    st.markdown("<p  color: white;'>SIStem ini menggunakan model KNN ( <i>K-nearest neighbors algorithm</i> ) dengan parameter <b>K = 7</b> . Dataset yang digunakan memiliki <b>7 fitur</b> termasuk kelas.</p>", unsafe_allow_html=True)
    st.write('Alasan menggunakan model KNN dengan parameter k = 7 adalah karena memiliki akurasi yang terbesar dari model lainnya pada dataset ini, sehingga diputuskan untuk menggunakan model tersebut.')
    st.write("Pada fitur weight loss atau kehilangan berat badan yang berlebih mempengaruhi kemungkinan terkena diabetes")
    st.markdown("<b>Alanine transminase (ALT), yaitu enzim yang mengubah protein menjadi energi untuk digunakan oleh sel-sel hati<b>",unsafe_allow_html=True)
    st.markdown("<b>Alanine transminase (ALT), yaitu enzim yang mengubah protein menjadi energi untuk digunakan oleh sel-sel hati<b>",unsafe_allow_html=True)
