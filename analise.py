import streamlit as st
import pandas as pd
import base64
import seaborn as sns


def main():
    st.title('Analisando Dados Covid19')
    st.image('imagens/python.png')
    file = st.file_uploader('Choose your file :', type='csv')
    if file is not None:
        st.success('Carregado com sucesso !')
        slider = st.slider('Valores', 1, 1000)
        df = pd.read_csv(file)
        covid_ref = df[['date', 'city', 'confirmed', 'deaths', 'estimated_population_2019', 'confirmed_per_100k_inhabitants']]
        covid_ref.columns = ['data', 'cidade', 'casos', 'mortes', 'populacao', 'habitantes_por_100k']
        covid = covid_ref.dropna()
        st.markdown('Selecione a quantidade de linhas para visualizar: ')
        # st.dataframe(df.head(slider))
        # st.markdown('Dados apresenteados formato tabela')
        st.table(covid.head(slider))


        # AQUI TUDO QUE FOR FICAR DENTRO DO SIDEBAR
        st.sidebar.subheader('Selecione como conhecer os dados:')
        linhas = st.sidebar.checkbox('Linhas do dataset : ')
        if linhas is not False:
            st.markdown('Quantidade de linhas: ')
            st.write(len(df))

        colunas = st.sidebar.checkbox('Colunas')
        if colunas is not False:
            st.markdown('Conhecendo as colunas do Dataset :')
            st.write(df.columns)


#teste

    if st.sidebar.button('Contatos'):
        st.write('GitHub: https://github.com/silenozlt')
        st.write(('linkedin : https://www.linkedin.com/in/cassio-placido-4a950261/'))
    else:
        st.text(' ')


if __name__ == '__main__':
    main()
