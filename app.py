import streamlit as st
from dados_api import previsao_temperatura

cidades = {
    "Brașov" : [45.51490235340256, 25.36716381533487],
    "Whitby": [54.48846460127272, -0.6079101284496846],
    "Highgate" : [51.56693877896395, -0.14680768925181267],
    "Edimburgo" : [55.95239217286235, -3.1933411699940777],
    "Paris" : [49.9617, 15.2886],
    "Kutná Hora" : [45.74919, 22.8882]
}

#------------------------------------------------SIDEBAR
st.sidebar.title("Previsão do tempo")
st.sidebar.image("logo.png")

cidade = st.sidebar.selectbox("Escolha a cidade:", cidades.keys())
latitude, longitude = cidades[cidade]

#------------------------------------------------BODY
st.title(f'Previsão do tempo em {cidade} para os próximos 7 dias')

st.markdown("---")

#Previsão de temperatura
dados, temperatura_media = previsao_temperatura(latitude, longitude)

for i,  d in temperatura_media.iterrows():
    with st.container(border=True):
        st.subheader(d['dia_semana'])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric('Data',f'{int(d['dia'])}/{int(d['mes'])}')

        with col2:
            st.metric('Temperatura média', f'{d['temperatura_media']:.2f}º')

        with col3:
            if d['temperatura_media'] < 10: 
                temp = "cold.png"

            elif d['temperatura_media'] < 18:
                temp = "cool.png"

            elif d['temperatura_media'] < 25:
                temp = "comfort.png"

            else:
                temp = "warm.png"

            st.image(temp, width=40)