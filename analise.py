import pandas as pd
import streamlit as st


def main():
    st.title('Analisando Dados Covid19')
    # st.image('imagens/python.png')
    file = st.file_uploader('Choose your file :', type='csv')
    if file is not None:
        st.success('Carregado com sucesso !')
        slider = st.slider('Valores', 1, 1000)
        df = pd.read_csv(file)
        covid_ref = df[
            ['date', 'city', 'confirmed', 'deaths', 'estimated_population_2019', 'confirmed_per_100k_inhabitants']]
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
            st.write(len(covid))

        colunas = st.sidebar.checkbox('Colunas')
        if colunas is not False:
            st.markdown('Conhecendo as colunas do Dataset :')
            st.write(covid.columns)

        st.subheader('Buscando dados por cidade')
        covid_cidade = covid.query("cidade=='Sabará'")
        covid_casos_cidade = covid_cidade[["data", "casos", "mortes"]]
        st.table(covid_casos_cidade.head())

        # plotando grafico
        covid_casos_cidade = covid_casos_cidade.sort_values(by="data")
        covid_casos_cidade.plot.area(x="data", y=["mortes", "casos"], figsize=(15, 10), title="Covid Sabará", grid=True)
        st.pyplot_chart(covid_cidade)
        #st.pyplot(covid_cidade)

    # if st.sidebar.button('Contatos'):
    st.text('GitHub: https://github.com/silenozlt')
    st.text('linkedin : https://www.linkedin.com/in/cassio-placido-4a950261/')
    # else:
    #    st.text(' ')


if __name__ == '__main__':
    main()
