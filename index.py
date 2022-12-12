import streamlit as st
import datset
import time
import webbrowser

st.set_page_config(
    page_title="",
    page_icon="https://freepngimg.com/save/93231-toy-pubg-mobile-sticker-machine-battlegrounds-playerunknown/512x512",
)

kolom = st.columns((2, 0.48, 2.7))
home = kolom[1].button('Home')
about = kolom[2].button('About')

# home page
if home==False and about==False or home==True and about==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Prediksi Diabetes</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: white; margin:0 ; padding:0;'>WAJIB MENGISI SEMUA KOLOM</h5>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: white; margin:0 ; padding:0;'>Isi 1 jika ya, 0 jika tidak</h6>", unsafe_allow_html=True)

    col1, col2,col3 = st.columns(3)
    with col1:
        nama = st.text_input("Nama", placeholder= 'Nama')
    with col2:
        umur = st.number_input("Age",min_value=0,max_value=120)
    with col3:
        jk = st.selectbox("Gender",('Laki-laki','Perempuan'))
    with col1:
        poliuria = st.number_input("Polyuria",min_value=0,max_value=1)
    with col2:
        polidipsia = st.number_input("Polydipsia",min_value=0,max_value=1)
    with col1:
        lostweight = st.number_input("sudden weight loss",min_value=0,max_value=1)
    with col2:
        poligapia = st.number_input("Polyphagia",max_value=1)
    weakness = st.number_input("weakness",max_value=1)
    Genital_thrush = st.number_input("Genital thrush",max_value=1)
    visual_blurring = st.number_input("visual blurring",max_value=1)
    Itching = st.number_input("Itching",max_value=1)
    Irritability = st.number_input("Irritability",max_value=1)
    delayed_healing = st.number_input("delayed healing",max_value=1)
    partial_paresis	 = st.number_input("partial paresis	",max_value=1)
    Alopecia = st.number_input("Alopecia",max_value=1)
    Obesity = st.number_input("Obesity",max_value=1)

    st.write("""Metode Klasfikasi""")
    model_1 = st.checkbox('K-Nearest Neighbors', value=True)
    model_2 = st.checkbox('Naive Bayes ')
    model_3 = st.checkbox('Decision Tree')


    columns = st.columns((2, 0.6, 2))
    sumbit = columns[1].button("Submit")
    if sumbit and nama != '' and umur != 0 and jk != '':
        if jk == 'Laki-laki':
            jk = 1
        else:
            jk = 0
        # normalisasi data
        data = datset.normalisasi([umur,jk,poliuria,polidipsia,lostweight,poligapia,weakness,Genital_thrush,visual_blurring,Itching,Irritability,delayed_healing,partial_paresis,Alopecia,Obesity])
        # cek jenis kelamin
        #1 = laki-laki
        #0 = perempuan
        if model_1 or model_2 or model_3:
            if model_1:
                # if jk == 'Laki-laki':
                #     jk = 1
                # else:
                #     jk = 0
                prediksi = datset.knn(data)
                # cek prediksi
                with st.spinner("Tunggu Sebentar Masih Proses..."):
                    if prediksi[-1] == 0:
                        time.sleep(1)
                        st.success("Hasil Prediksi Metode KNN: "+nama+" Tidak terkena kencing manis")
                    else:
                        time.sleep(1)
                        st.warning("Hasil Prediksi Metode KNN: "+nama+" Sangat mungkin terkena kencing manis")

            if model_2:
                # if jk == 'Laki-laki':
                #     jk = 1
                # else:
                #     jk = 0
                prediksi = datset.nb(data)  
                # cek prediksi
                with st.spinner("Tunggu Sebentar Masih Proses..."):
                    if prediksi[-1] == 0:
                        time.sleep(1)
                        st.success("Hasil Prediksi Metode Naive Bayes: "+nama+" Tidak terkena kencing manis")
                    else:
                        time.sleep(1)
                        st.warning("Hasil Prediksi Metode Naive Bayes: "+nama+" Sangat mungkin terkena kencing manis")

            if model_3:
                # if jk == 'Laki-laki':
                #     jk = 1
                # else:
                #     jk = 0
                prediksi = datset.dt(data)
                # cek prediksi
                with st.spinner("Tunggu Sebentar Masih Proses..."):
                    if prediksi[-1] == 0:
                        time.sleep(1)
                        st.success("Hasil Prediksi Metode Decision Tree: "+nama+" Tidak terkena kencing manis")
                    else:
                        time.sleep(1)
                        st.warning("Hasil Prediksi Metode Decision Tree: "+nama+" Sangat mungkin terkena kencing manis")
        else:
            st.error("Pilih Salah Satu Metode")

# about page
if about==True and home==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Sistem</h1>", unsafe_allow_html=True)
    st.write('Sistem ini dibuat dengan tujuan untuk memprediksi seseorang apakah terkena penyakit diabetes atau tidak.')
    st.write('Dengan memasukkan fitur yang telah disediakan sistem ini dapat memprediksi apakah pengguna mengalami diabetes atau tidak.')
    st.markdown("<p  color: white;'>SIStem ini menggunakan model KNN ( <i>K-nearest neighbors algorithm</i> ) dengan parameter <b>K = 7</b> . Dataset yang digunakan memiliki <b>7 fitur</b> termasuk kelas.</p>", unsafe_allow_html=True)
    st.write('Alasan menggunakan model KNN dengan parameter k = 7 adalah karena memiliki akurasi yang terbesar dari model lainnya pada dataset ini, sehingga diputuskan untuk menggunakan model tersebut.')
    st.write("Pada fitur weight loss atau kehilangan berat badan yang berlebih mempengaruhi kemungkinan terkena diabetes")
    st.write('Penjelasan tentang tabel/fitur yang di sediakan berikut :')
    st.markdown("<b>-Poliuria</b>, adalah kondisi dimana seseorang mengalami seringnya buang air kecil",unsafe_allow_html=True)
    st.markdown("<b>-Polidipsia</b>, adalah kondisi dimana seseorang mengalami seringnya merasa haus berlebihan",unsafe_allow_html=True)
    st.markdown("<b>-Sudden Weight Loss</b>, adalah kondisi dimana seseorang mengalami penurunan berat badan secara drastis",unsafe_allow_html=True)
    st.markdown("<b>-Poligapia</b>, adalah kondisi dimana seseorang mengalami seringnya merasa lapar berlebihan",unsafe_allow_html=True)

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

