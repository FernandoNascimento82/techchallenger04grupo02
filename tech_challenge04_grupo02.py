# Importe outras bibliotecas necessárias
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
import warnings
import ipeadatapy as ip
from statsmodels.tsa.arima.model import ARIMA
from datetime import date, timedelta
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

st.title('Tech Challenger 4 - Grupo 02')
st.write("***Integrantes:***")
st.write("*Bárbara Pereira Godoi*")
st.write("*Fernando Correia do Nascimento*")
st.write("*Guilherme Gentil Da Silva*")
st.write("*João Vitor Lopes Arruda*")
st.write("*William Fernandes Bento*")

df = ip.metadata()
df['NAME2'] = df['NAME'].str.lower()
df = df[df['NAME2'].str.contains('petróleo')]
df = df[df['NAME2'].str.contains('preço')]
df = df[df['NAME2'].str.contains('brent')]
df = df[df['NAME2'].str.contains('fob')]
df = ip.timeseries('EIA366_PBRENT366')
df = df[df['VALUE (US$)'].notnull()]
df = df[['VALUE (US$)']]
df.rename(columns={'VALUE (US$)': 'VALOR'}, inplace = True)

font_grafico = {'family':'serif','color':'darkred','size':20}

grafico = plt.figure(figsize=(10, 6))
plt.plot(df)
plt.title("Evolução histórica do preço do petróleo", fontdict=font_grafico, weight='bold', style='italic')
plt.legend(bbox_to_anchor = (1.3, 1.3), ncol = 8)
plt.xlabel("Periodo")
plt.ylabel("Valor Total")
plt.xticks(rotation=35)
st.pyplot(grafico) 

st.write("")
st.write("")
st.write("---")
st.write("***Insights***")

df_crise = df[(df.index >= '2007-01-01') & (df.index <= '2008-12-31')]
grafico = plt.figure(figsize=(10, 6))
plt.plot(df_crise)
font_grafico = {'family':'serif','color':'darkred','size':20}
plt.title("A Crise do Petróleo de 2007/2008", fontdict=font_grafico, weight='bold', style='italic')
plt.legend(bbox_to_anchor = (1.3, 1.3), ncol = 8)
plt.xlabel("Periodo")
plt.ylabel("Valor Total")
plt.xticks(rotation=35)
st.pyplot(grafico) 
st.write("\"""... o preço do petróleo vinha aumentando de maneira continua desde 2002. Entretanto, a partir do fim de 2007 até a metade de 2008, a velocidade desse aumento cresceu consideravelmente. O preço do barril atingiu um nível nunca imaginado, ultrapassando a barreira dos US$ 150 em julho de 2008.\"""")
st.write("\"""... o aumento escalar no preço do petróleo em 2008 foi causado por um conjunto de fatores: especulação, forte demanda mundial, baixa capacidade ociosa e um aumento contínuo da importância do “scarcity rent”. O preço desse recurso excede o custo marginal mesmo em um mercado perfeitamente competitivo. Podemos destacar, porém, três pontos chaves que explicam em parte a crise: a baixa elasticidade preço-demanda, o aumento na demanda por petróleo da China, do Oriente Médio e de outros países industrializados, e por último, a baixa capacidade ociosa que dificulta um aumento expressivo na produção. Esses aspectos pressionaram o preço do barril para cima e deslancharam a especulação.\"""")
st.write("*Fonte:* https://www.econ.puc-rio.br/uploads/adm/trabalhos/files/Julia_Fernandes_Ramos.pdf")
st.write("")
st.write("")

df_crise = df[(df.index >= '2014-06-01') & (df.index <= '2016-12-31')]
grafico = plt.figure(figsize=(10, 6))
plt.plot(df_crise)
font_grafico = {'family':'serif','color':'darkred','size':20}
plt.title("Queda no preço do petróleo 2015/2016", fontdict=font_grafico, weight='bold', style='italic')
plt.legend(bbox_to_anchor = (1.3, 1.3), ncol = 8)
plt.xlabel("Periodo")
plt.ylabel("Valor Total")
plt.xticks(rotation=35)
st.pyplot(grafico) 
st.write("\"""... quando atingiu o menor nível desde junho de 2004, o que assustou o mercado foi um intenso e inesperado aumento nos estoques de gasolina dos Estados Unidos. Além disso, tensões geopolíticas após o anúncio de um teste de bomba de hidrogênio pela Coreia do Norte, aliadas a crescentes preocupações sobre a desaceleração da economia da China, contribuíram para o tombo dos preços.\"""")
st.write("\"""... Ao mesmo tempo, a perspectiva de demanda menor da Europa e da Ásia devido ao menor crescimento da economia no mundo também vem contribuindo para a queda.\"""")
st.write("*Fonte:* https://g1.globo.com/economia/mercados/noticia/2016/01/por-que-o-preco-do-petroleo-caiu-tanto-veja-perguntas-e-respostas.html")
st.write("")
st.write("")


df_crise = df[(df.index >= '2020-02-01') & (df.index <= '2020-05-31')]
grafico = plt.figure(figsize=(10, 6))
plt.plot(df_crise)
font_grafico = {'family':'serif','color':'darkred','size':20}
plt.title("Pandemia Coronavirus 2019/2020", fontdict=font_grafico, weight='bold', style='italic')
plt.legend(bbox_to_anchor = (1.3, 1.3), ncol = 8)
plt.xlabel("Periodo")
plt.ylabel("Valor Total")
plt.xticks(rotation=35)
st.pyplot(grafico) 
st.write("\"""... Os preços do petróleo, que já estavam em trajetória de queda em meio ao avanço do novo coronavírus, derreteram neste ano, recuando para mínimas que não eram registradas desde 1999, chegando a cair abaixo de US$ 16.\"""")
st.write("\"""... O tombo é um resultado direto da queda da demanda global, que se acentuou com as medidas de isolamento de governos para conter a pandemia e depois que a Arábia Saudita iniciou uma guerra de preços contra a Rússia.\"""")
st.write("*Fonte:* https://g1.globo.com/economia/noticia/2020/03/09/o-que-explica-o-tombo-do-preco-do-petroleo-e-quais-os-seus-efeitos.ghtml")
st.write("")
st.write("")

df_crise = df[(df.index >= '2023-08-20') & (df.index <= '2023-09-30')]
grafico = plt.figure(figsize=(10, 6))
plt.plot(df_crise)
font_grafico = {'family':'serif','color':'darkred','size':20}
plt.title("Queda no estoque do combustível fóssil eleva preço do petróleo em 2023", fontdict=font_grafico, weight='bold', style='italic')
plt.legend(bbox_to_anchor = (1.3, 1.3), ncol = 8)
plt.xlabel("Periodo")
plt.ylabel("Valor Total")
plt.xticks(rotation=35)
st.pyplot(grafico) 
st.write("\"""... Os preços do petróleo bruto subiram quase de 3%, chegando a atingir US$ 97 por barril. Este é o valor mais alto desde agosto de 2022. A alta se deve à queda nos estoques do combustível fóssil no país. As informações são do Financial Times.\"""")
st.write("\"""... Segundo dados divulgados pela Administração de Informação de Energia norte-americana, os estoques de petróleo bruto dos Estados Unidos caíram 2,2 milhões de barris em set/23 e em contrapartida o preço registrou a maior alta. Desde o inicio do ano, os preços do petróleo nos EUA subiram  cerca de 17%.\"""")
st.write("*Fonte:* https://www.poder360.com.br/internacional/preco-do-petroleo-sobe-para-nivel-mais-alto-de-2023/")
st.write("")
st.write("---")
st.write("")
st.write("")

#Trabalhando com dados dos últimos 365 dias
dt_hoje = date.today()
dt_inicio = pd.to_datetime((dt_hoje + timedelta(-365)))
df_b = df[(df.index >= dt_inicio)]

st.write("***Tech Challenger***")
grafico = plt.figure(figsize=(10, 6))
plt.plot(df_b)
plt.title("Separando os dados dos últimos 365 dias para acompanhamento.", fontdict=font_grafico, weight='bold', style='italic')
plt.legend(bbox_to_anchor = (1.3, 1.3), ncol = 8)
plt.xlabel("Periodo")
plt.ylabel("Valor Total")
plt.xticks(rotation=35)
st.pyplot(grafico) 

# Dividir dados em treinamento e teste
train_size = int(len(df_b) * 0.7)
df_train, df_test = df_b[:train_size], df_b[train_size:]

st.write("---")
st.write("**Dividindo a base em Treino e Teste...**")
st.write("*df_train.shape:* ",df_train.shape," *| df_test.shape:* ",df_test.shape)
st.write("---")

def ehEstacionaria(timeseries):
  dftest = adfuller(timeseries, autolag='AIC')
  dfoutput = pd.Series(dftest[0:4], index=['Estatistica do teste','p-value','O criterio de informação maximizado','Numero de observações usadas'])
  for key,value in dftest[4].items():
    dfoutput['Valor crítico (%s)'%key] = value
  
  if(dfoutput['Estatistica do teste'] < dfoutput['Valor crítico (5%)'] and dfoutput['p-value'] < 0.05):
    st.write(f"**É estacionária.**")
  else:
    st.write(f"**Não é estacionária.**")
    
def test_stationary(timeseries):

  medmov = timeseries.rolling(12).mean() #media movel
  despad = timeseries.rolling(12).std() #desvio movel

  grafico = plt.figure(figsize=(10, 6))
  plt.plot(timeseries, color='blue', label='Valor original')
  plt.plot(medmov, color='red', label='Valor média móvel')
  plt.plot(despad, color='black', label='Desvio móvel')
  plt.legend(loc='best')
  plt.title('Média móvel e desvio padrão', fontdict=font_grafico, weight='bold', style='italic')
  plt.xticks(rotation=35)
  st.pyplot(grafico) 

  st.write("")
  st.write('**Resultado do teste de Dickey Fuller**')
  dftest = adfuller(timeseries, autolag='AIC')
  dfoutput = pd.Series(dftest[0:4], index=['Estatística do teste','p-value','O critério de informação maximizado','Numero de observações usadas'])
  for key,value in dftest[4].items():
    dfoutput['Valor crítico (%s)'%key] = value
  st.write(dfoutput)

  ehEstacionaria(timeseries)
  
st.write("**Verificando se os dados estão em forma estacionária**")
test_stationary(df_train['VALOR'])
st.write("---")

st.write("**Tornando a série estacionária**")
dfdiff = df_train.VALOR.diff()
dfdiff = dfdiff.dropna()
test_stationary(dfdiff)
st.write("---")

st.write("***Determinando os parâmetros ARIMA***")
p = d = q = range(0, 9)
pdq_combinations = list(itertools.product(p, d, q))
menor_aic = float("inf")
melhor_pdq = None
warnings.filterwarnings("ignore")
st.write("Combinações ARIMA(p d q):")

#Professor, comentamos o código abaixo, pois ele irá buscar o melhor parametro
#para o ARIMA, no Colab esse codigo rodou na média em 15 minutos, mas aqui no 
#streamlit demorou bastante, então pegamos o melhor parametro gerado no Colab e forçamos 
#o parametro aqui
#for pdq in pdq_combinations:
#    try:
#        model = ARIMA(df_train['VALOR'].dropna(), order=pdq)
#        results = model.fit()
#        if results.aic < menor_aic:
#            menor_aic = results.aic
#            melhor_pdq = pdq            
#    except:
#        continue
#    st.write('*Identificado a melhor combinação ARIMA(p d q):* ',melhor_pdq)
    
melhor_pdq = (5, 1, 3)
st.write("**-> Melhor combinação ARIMA(p d q):**", melhor_pdq)
st.write("")
st.write("Ajustando o modelo Arima com o melhor parametro pdq")
modelo_arima_otimizado = ARIMA(df_b['VALOR'], order=(melhor_pdq))
modelo_arima_otimizado_fit = modelo_arima_otimizado.fit()
st.write(modelo_arima_otimizado_fit.summary())
st.write("---")
st.write("")

df_b['DATA'] = df_b.index
data_final = df_b['DATA'].iloc[-1]
datas_futuras = pd.date_range(start=data_final, periods=61, inclusive='right')  # 60 dias após a última data

previsoes_futuras = modelo_arima_otimizado_fit.forecast(steps=len(datas_futuras))

#Mostrar no garfico de evolução, 90 dias de historico e 60 dias de previsão
dt_hoje = date.today()
dt_inicio = pd.to_datetime((dt_hoje + timedelta(-90)))

df = df_b[(df_b['DATA'] >= dt_inicio)]
grafico = plt.figure(figsize=(10, 6))
plt.plot(df['DATA'], df['VALOR'], label='Dados Históricos')
plt.plot(datas_futuras, previsoes_futuras, color='red', label='Previsões Futuras')
plt.title('Previsões Futuras de Preço do Petróleo', fontdict=font_grafico, weight='bold', style='italic')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.xticks(rotation=35)
st.pyplot(grafico) 
st.write("")
st.write("---")
st.write("***Conclusão:***")
st.write("")
st.write("A volatilidade no preço do petróleo desde o ano 2000 é inegavelmente influenciada por uma interconexão complexa de fatores. As tensões geopolíticas, como conflitos no Oriente Médio, têm o poder de disparar aumentos abruptos, enquanto crises econômicas impactam a demanda global por energia, provocando flutuações significativas nos valores do petróleo. Além disso, a crescente conscientização ambiental e a transição para fontes de energia alternativas também desempenham um papel crucial na dinâmica desse mercado. Essa interação entre eventos globais, politicas e mudanças na matriz energética destaca a natureza multifacetada e sensível do setor petrolífero, contribuindo para a complexidade das variações de preços ao longo das últimas décadas.")
