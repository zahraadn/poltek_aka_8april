# Library
import streamlit as st

# write
st.title('NYOBA AJA SIH KAYAK W JUGA GA PAHAM')
st.write('hello sayangku')

#INPUT
number1 = st.number_input('masukkan bilangan pertama')
st.write(f'bilangan pertama adalah {number1}')

#INPUT
number2 = st.number_input('masukkan bilangan kedua')
st.write('bilangan kedua adalah', number2)


#HASIL
hasil = number1*number2

if st.button('Hitung'):
    st.write(f'Hasil kali anatara {number1} dan {number2} adalah {hasil}')
else:
    st.write('Silahkan pencet tombol hitung')