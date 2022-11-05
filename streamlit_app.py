import streamlit as st
import numpy as np
from PIL import Image,ImageDraw


import streamlit as st

from bokeh.models.widgets import Div

st.set_page_config(
    page_title="Portifólio do Pedro",
    page_icon=":robot_face:"
)


with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# **Pedro Andrietta Chagas**
##### *Este portifólio em si é um projeto de webapp no Streamlit Cloud!* 
''')

image = Image.open('profile.png')

def round_image(image):
  height,width = image.size
  lum_image = Image.new('L', [height,width] , 0)
    
  draw = ImageDraw.Draw(lum_image)
  draw.pieslice([(0,0), (height,width)], 0, 360, 
                fill = 255, outline = "white")
  image_arr =np.array(image)
  lum_image_arr =np.array(lum_image)
  final_image_arr = np.dstack((image_arr,lum_image_arr))
  return final_image_arr


image = round_image(image)

st.image(image, width=150)

st.markdown('## Quem sou eu', unsafe_allow_html=True)
st.info('''
- Duplo-graduado em Engenheria de Produção pela UFRJ e pela ENSAM Paristech (Bolsista Honorário BRAFITEC) :mortar_board:
- Apaixonado por Ciência de Dados e Machine Learning :robot_face:
- Em constante busca de conhecimento :brain:
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #cc4915;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/pedroachagas/" target="_blank">Pedro Chagas</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Início <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Educação">Educação</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Projetos</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Educação
''')

txt('**Universidade Federal do Rio de Janeiro**, Graduação em Engenharia de Produção',
'2015-2022')
st.markdown('''
Trabalho de conclusão de curso voltado à aplicação de técnicas de Data Mining e algoritmos de Machine Learning na gestão da UFRJ, especialmente quanto a previsão de alunos em risco de evasão.
''')

txt('**Arts et Métiers ParisTech - École Nationale Supérieure dArts et Métiers**, Master of Engineering - MEng, Engenharia e Gestão Industrial',
'2015-2022')
st.markdown('''
- Bolsista Honorário BRAFITEC: cobrimento completo dos custos dos 2 anos de intercâmbio em Paris, França
- Especialização em Gestão Industrial 4.0: experiência com robôs colaborativos, IoT e gestão da inovação.
''')


#####################


with st.container():
    st.markdown('''
    ## Projetos
    ''')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(Image.open('images/rossmann_cover.png'))
        st.subheader("Rossmann Sales Prediction")
        st.write("Previsão de vendas de rede farmacêutica implementada como bot do Telegram")
        if st.button('Testar bot!', key="ews_enter"):
            js = "window.open('https://github.com/pedroachagas')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="ews_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/pedroachagas/rossmann_sales_forecasting')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

#####################
st.markdown('''
## Competências técnicas
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`,`Keras`')
txt3('Web development', '`Flask`, `HTML`, `CSS`, `Gunicorn`')
txt3('Model deployment', '`streamlit`, `gradio`, `Heroku`, `AWS`, `Azure`')

#####################
st.markdown('''
## Me encontre também em
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/pedroachagas/')
txt2('GitHub', 'https://github.com/pedroachagas')
