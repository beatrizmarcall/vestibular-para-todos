import streamlit as st

st.set_page_config(page_title="Vestibular para Todos", page_icon="🎓", layout="centered")

@st.cache_data
def carregar_conteudo_pesado():
    dados = {
        "provas": {
            2025: {
                "dia1": {"prova": "https://download.inep.gov.br/enem/provas_e_gabaritos/2025_PV_impresso_D1_CD1.pdf", "gab": "https://download.inep.gov.br/enem/provas_e_gabaritos/2025_GB_impresso_D1_CD1.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/enem/provas_e_gabaritos/2025_PV_impresso_D2_CD7.pdf", "gab": "https://download.inep.gov.br/enem/provas_e_gabaritos/2025_GB_impresso_D2_CD7.pdf"}
            },
            2024: {
                "dia1": {"prova": "https://download.inep.gov.br/enem/provas_e_gabaritos/2024_PV_impresso_D1_CD1.pdf", "gab": "https://download.inep.gov.br/enem/provas_e_gabaritos/2024_GB_impresso_D1_CD1.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/enem/provas_e_gabaritos/2024_PV_impresso_D2_CD7.pdf", "gab": "https://download.inep.gov.br/enem/provas_e_gabaritos/2024_GB_impresso_D2_CD7.pdf"}
            },
            2023: {
                "dia1": {"prova": "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D1_CD1.pdf", "gab": "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_GB_impresso_D1_CD1.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD7.pdf", "gab": "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_GB_impresso_D2_CD7.pdf"}
            },
            2022: {
                "dia1": {"prova": "https://download.inep.gov.br/enem/provas_e_gabaritos/2022_PV_impresso_D1_CD1.pdf", "gab": "https://download.inep.gov.br/enem/provas_e_gabaritos/2022_GB_impresso_D1_CD1.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/enem/provas_e_gabaritos/2022_PV_impresso_D2_CD7.pdf", "gab": "https://download.inep.gov.br/enem/provas_e_gabaritos/2022_GB_impresso_D2_CD7.pdf"}
            },
            2021: {
                "dia1": {"prova": "https://download.inep.gov.br/enem/provas_e_gabaritos/2021_PV_impresso_D1_CD1.pdf", "gab": "https://download.inep.gov.br/enem/provas_e_gabaritos/2021_GB_impresso_D1_CD1.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/enem/provas_e_gabaritos/2021_PV_impresso_D2_CD7.pdf", "gab": "https://download.inep.gov.br/enem/provas_e_gabaritos/2021_GB_impresso_D2_CD7.pdf"}
            },
            2020: {
                "dia1": {"prova": "https://download.inep.gov.br/enem/provas_e_gabaritos/2020_PV_impresso_D1_CD1.pdf", "gab": "https://download.inep.gov.br/enem/provas_e_gabaritos/2020_GB_impresso_D1_CD1.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/enem/provas_e_gabaritos/2020_PV_digital_D2_CD7.pdf", "gab": "https://download.inep.gov.br/enem/provas_e_gabaritos/2020_GB_digital_D2_CD7.pdf"}
            },
            2019: {
                "dia1": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2019/2019_PV_impresso_D1_CD1.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2019/gabarito_1_dia_caderno_1_azul_aplicacao_regular.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2019/2019_PV_impresso_D2_CD7.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2019/gabarito_2_dia_caderno_7_azul_aplicacao_regular.pdf"}
            },
            2018: {
                "dia1": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2018/2018_PV_impresso_D1_CD1.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2018/GAB_ENEM_2018_DIA_1_AZUL.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2018/2018_PV_impresso_D2_CD7.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2018/GAB_ENEM_2018_DIA_2_AZUL.pdf"}
            },
            2017: {
                "dia1": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2017/2017_PV_impresso_D1_CD1.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2017/cad_1_gabarito_azul_5112017.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2017/2017_PV_impresso_D2_CD7.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2017/cad_7_gabarito_azul_12112017.pdf"}
            },
            2016: {
                "dia1": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2016/2016_PV_impresso_D1_CD1.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2016/GAB_ENEM_2016_DIA_1_01_AZUL.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2016/2016_PV_impresso_D2_CD7.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2016/GAB_ENEM_2016_DIA_2_07_AZUL.pdf"}
            },
            2015: {
                "dia1": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2015/2015_PV_impresso_D1_CD1.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2015/CADERNO_1_AZUL_SABADO.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2015/2015_PV_impresso_D2_CD7.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2015/CADERNO_7_AZUL_DOMINGO.pdf"}
            },
            2014: {
                "dia1": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2014/2014_PV_impresso_D1_CD1.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2014/CADERNO_1_AZUL_SABADO.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2014/2014_PV_impresso_D2_CD7.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2014/CADERNO_7_AZUL_DOMINGO.pdf"}
            },
            2013: {
                "dia1": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2013/dia1_caderno1_azul.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2013/dia1_azul.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2013/dia2_caderno7_azul.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2013/dia2_azul.pdf"}
            },
            2012: {
                "dia1": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2012/dia1_caderno1_azul.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2012/dia1_azul.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2012/dia2_caderno7_azul.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2012/dia2_azul.pdf"}
            },
            2011: {
                "dia1": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2011/dia1_caderno1_azul.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2011/01_AZUL_GABARITO.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2011/dia2_caderno7_azul.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/gabaritos/2011/07_AZUL_GABARITO.pdf"}
            },
            2010: {
                "dia1": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2010/dia1_caderno1_azul.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/provas/2010/dia1_caderno1_azul_com_gab.pdf"},
                "dia2": {"prova": "https://download.inep.gov.br/educacao_basica/enem/provas/2010/dia2_caderno7_azul.pdf", "gab": "https://download.inep.gov.br/educacao_basica/enem/provas/2010/dia2_caderno7_azul_com_gab.pdf"}
            }
        }
    }
    return dados

# Executa o carregamento e cria a variável que o seu código já usa

conteudo = carregar_conteudo_pesado()
provas_db = conteudo["provas"] 

st.markdown("""
<style>
    .stApp { background-color: white !important; }
    h1, h2, h3, h4, p, li, div, span { color: black !important; }
    
    /* Estilos dos Menus e Botões */
    div[data-baseweb="select"] > div { background-color: white !important; color: black !important; }
    .stButton>button { background-color: #d8c6f7; color: #4a357d; border-radius: 8px; font-weight: 600; }
    .stLinkButton>a { background-color: #e6f0ff !important; color: #004a99 !important; border-radius: 8px !important; font-weight: 600 !important; }
    
    [data-testid="stExpander"] { background-color: #f9f9f9 !important; border: 1px solid #e6e6e6 !important; }
</style>
""", unsafe_allow_html=True)

# Configuração da página
st.set_page_config(page_title="Vestibular para Todos", page_icon="🎓", layout="centered")

st.markdown("""
<style>
    /* 1. Forçar o fundo do app para branco */
    .stApp { background-color: white !important; }
    
    /* 2. Forçar textos gerais para preto */
    h1, h2, h3, h4, p, li, div, span { color: black !important; }

    /* 3. CORREÇÃO COMPLETA DO SELECTBOX (MENU) */
    /* Fundo da caixa fechada */
    div[data-baseweb="select"] > div {
        background-color: white !important;
        color: black !important;
    }
    
    /* Fundo da lista que abre (popover) */
    div[data-baseweb="popover"] div {
        background-color: white !important;
        color: black !important;
    }

    /* Cada item da lista */
    li[role="option"] {
        background-color: white !important;
        color: black !important;
    }

    /* Item quando você passa o mouse */
    li[role="option"]:hover {
        background-color: #d8c6f7 !important;
        color: #4a357d !important;
    }

    /* 4. BOTÕES */
    .stButton>button { background-color: #d8c6f7; color: #4a357d; border: none; border-radius: 8px; font-weight: 600; }
    .stLinkButton>a { background-color: #e6f0ff !important; color: #004a99 !important; border: 1px solid #b3d1ff !important; border-radius: 8px !important; font-weight: 600 !important; text-align: center !important; }
            
            /* Estilo fixo para os Expanders */
    [data-testid="stExpander"] {
        background-color: #f9f9f9 !important;
        border: 1px solid #e6e6e6 !important;
        transition: 0.3s; /* Deixa o efeito suave */
    }

    /* Efeito de passar o mouse (Hover) */
    [data-testid="stExpander"]:hover {
        background-color: #f0f2f6 !important; /* Fica levemente cinza ao passar o mouse */
        border-color: #d8c6f7 !important; /* Borda fica roxinha */
    }

    /* Força o texto dentro do expander */
    [data-testid="stExpander"] * {
        color: black !important;
    }
</style>
""", unsafe_allow_html=True)


conteudo = carregar_conteudo_pesado()
provas_db = conteudo["provas"]

# Cabeçalho
st.markdown('<h1 style="text-align: center;">🎓 Vestibular para Todos</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;">Recursos gratuitos para estudantes de Governador Valadares</p>', unsafe_allow_html=True)

# Menu de Navegação
col1, col2, col3, col4 = st.columns(4)
with col1: inicio = st.button("🏠 Início", use_container_width=True)
with col2: questoes = st.button("📝 Provas", use_container_width=True)
with col3: redacao = st.button("✍️ Redação", use_container_width=True)
with col4: dicas = st.button("💡 Dicas", use_container_width=True)

st.divider()

if 'pagina' not in st.session_state: st.session_state['pagina'] = "inicio"
if inicio: st.session_state['pagina'] = "inicio"
elif questoes: st.session_state['pagina'] = "questoes"
elif redacao: st.session_state['pagina'] = "redacao"
elif dicas: st.session_state['pagina'] = "dicas"

# --- PÁGINA INICIAL ---
if st.session_state['pagina'] == "inicio":
    st.subheader("✨ Bem-vindo(a)!")
    st.write("Selecione uma das opções acima para começar seus estudos. Este portal foi feito para facilitar seu acesso aos materiais oficiais do ENEM.")

# --- PÁGINA DE PROVAS ---

elif st.session_state['pagina'] == "questoes":
    st.subheader("📚 Banco de Provas do ENEM")
    anos_disponiveis = sorted(provas_db.keys(), reverse=True)
    ano_sel = st.selectbox("Escolha o ano do exame:", anos_disponiveis)
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"### 🟦 1º Dia - {ano_sel}")
        st.link_button("📄 Baixar Prova", provas_db[ano_sel]['dia1']['prova'], use_container_width=True)
        st.link_button("✅ Ver Gabarito", provas_db[ano_sel]['dia1']['gab'], use_container_width=True)
    with c2:
        st.markdown(f"### 🟨 2º Dia - {ano_sel}")
        st.link_button("📄 Baixar Prova", provas_db[ano_sel]['dia2']['prova'], use_container_width=True)
        st.link_button("✅ Ver Gabarito", provas_db[ano_sel]['dia2']['gab'], use_container_width=True)

    st.caption("⚠️ Nota: Os arquivos PDF são oficiais do INEP e podem demorar alguns segundos para carregar dependendo do tamanho.")
        

# --- PÁGINA DE REDAÇÃO (VERSÃO COM ABAS) ---
elif st.session_state['pagina'] == "redacao":
    st.subheader("✍️ Oficina de Redação: Rumo ao Nota 1000")
    
    # Criando as abas
    tab_repertorios, tab_estrutura, tab_mil, tab_citacoes = st.tabs([
        "🎞️ Repertórios Culturais", 
        "🏗️ Estrutura do Texto", 
        "🏆 Redações Nota Mil",
        "✍️ Citações Coringa"
    ])

    # --- ABA 1: REPERTÓRIOS ---
    with tab_repertorios:
        st.write("Repertório não é só citação difícil! Use o que você assiste para embasar seus argumentos.")

        # Criando as colunas para as categorias
        cat1, cat2 = st.columns(2)

        with cat1:
            # --- CATEGORIA: ANIMAÇÕES ---
            with st.container(border=True):
                st.markdown("#### 🎨 Animações")
                st.markdown("""
                * **Wall-e:** Nesse filme da Disney Pixar, é abordado temas como consumo desenfreado, degradação ambiental do nosso planeta e a depência tecnológica
                * **Divertidamente:** Também da Disney Pixar, divertidamente aborda temas como psicologia do desenvolvimento, inteligência emocional, a adaptação às mudanças da vida, a gestão de sentimentos em momentos de estresse e a importância da autocompreensão no amadurecimento.
                * **Up: Altas Aventuras:** É uma animação que vira e mexe é muito usada como repertório para o ENEM, pois aborda o etarismo, a solidão na terceira idade, o desenvolvimento urbano desenfreado e a desvalorização da memória afetiva em prol do progresso.
                * **Dica:** Foque na mensagem social por trás do desenho.
                """)
                
                st.divider()


            # --- CATEGORIA: CANAIS DO YOUTUBE ---
            with st.container(border=True):
                st.markdown("#### 📺 Canais do YouTube")
                st.markdown("""* **BBC Brasil:** Canal da BBC Brasil, ótimo para se inpsirar e saber o que está acontecendo no Brasil no momento.""")
                st.link_button("Ir para o canal BBC Brasil", "https://www.youtube.com/@BBCNewsBrasil")
                st.markdown("""* **Rodrigo Barreto:** canal com muitos conteúdos sobre literatura brasileira""")
                st.link_button("Ir para o canal Rodrigo Barreto", "https://www.youtube.com/@o.rodrigo.barreto/videos")
                st.markdown("""* **Brasão de Armas:** canal com vários conteúdos sobre história, guerras e batalhas""")
                st.link_button("Ir para o canal Brasão de Armas", "https://www.youtube.com/@BrasaodeArmas")    
                st.markdown("""* **Ludoviajante:** vídeos que misturam filosofia, psicologia e cultura pop, com reflexões e críticas à vida moderna""")
                st.link_button("Ir para o canal Ludoviajante", "https://www.youtube.com/@ludoviajante/videos")       
                st.markdown("""* **Ciência todo dia:** foca em divulgação científica com abordagem didática e visual, utilizando animações para explicar conceitos complexos de física, astronomia e tecnologia""")
                st.link_button("Ir para o canal Ciência todo dia", "https://www.youtube.com/@CienciaTodoDia/videos")       
                st.markdown("""* **Canal Elementar:** o conteúdo é focado em análises sobre problemáticas do Brasil e do mundo, além de histórias de sucesso, marketing e investigações de mercado""")
                st.link_button("Ir para o canal Elementar", "https://www.youtube.com/@Elementar/videos")


        with cat2:
            # --- CATEGORIA: SÉRIES E FILMES (NETFLIX) ---
            with st.container(border=True):
                st.markdown("#### 🎬 Séries e Filmes (Netflix)")
                st.markdown("""
                * **Série Bridgerton:** aborda nas entrelinhas temas como racismo, machismo, hierarquia de classe e desigualdade e saúde mental
                * **Saga Crepúsculo:** A aclamada saga Crepúsculo, com o primeiro filme lançado em 2008, expõe um tema que até hoje é um problema: a depência emocional/saúde mental
                * **Série Stranger Things:** é retrado na série temas como abuso de Poder e ética científica, saúde mental e trauma, desigualdade e invisibilidade social
                * **Série adolescência:** essa série foi um estrondo quando foi lançada na Netflix, e escancara temas como misoginia digital, cyberbullying e impacto da pornografia
                * **Filme Não Olhe Para Cima:** esse filme foi lançado em 2021, e aborda temas como negacionismo científico e politização da ciência, A "Sociedade do Espetáculo" e mídia superficial, desigualdade e privilégios
                * **Filme O Menino Que Descobriu o Vento:** é um filme baseado em fatos reais, tendo temas como fome e insegurança alimentar, falta de acesso à educação, falta de infraestrutura e recursos
                """)

                st.divider()


            # --- CATEGORIA: DOCUMENTÁRIOS ---
            with st.container(border=True):
                st.markdown("#### 🎥 Documentários (YouTube)")
                st.markdown("""* **Muito Além do Peso:** epidemia infantil de sobrepeso, Consumo Precoce (ex.: consumo de refrigerantes por 56% de bebês com menos de um ano de idade)""")
                st.link_button("Ir para o documentário", "https://www.youtube.com/watch?v=8UGe5GiHCT4")
                st.markdown("""* **Eles Poderiam Estar Vivos:** documentário sobre a COVID-19 no Brasil, abordando negligência de medidas sanitárias recomendadas por especialistas""")
                st.link_button("Ir para o documentário", "https://www.youtube.com/watch?v=RLwaKDJsv88")
                st.markdown("""* **Holocausto Brasileiro:** Baseado no livro de mesmo nome da jornalista Daniela Arbex, o filme retrata a triste história do Hospital Colônia de Barbacena, Minas Gerais.""")
                st.link_button("Ir para o documentário", "https://www.youtube.com/watch?v=jIentTu8nc4")
                st.markdown("""* **O Veneno Está na Nossa Mesa:** A produção questiona o uso abusivo de agrotóxicos na agricultura brasileira. Por meio de entrevistas com especialistas, o documentário mostra o porquê é tão preocupante que o Brasil seja um dos países que mais tem agrotóxicos nos alimentos.""")
                st.link_button("Ir para o documentário", "https://www.youtube.com/watch?v=J-jeukOk7y8")
                st.markdown("""* **A Sombra de Um Delírio Verde:** O documentário retrata a luta da maior população indígena do país para manter seu território diante do avanço de latifúndios de cana de açúcar, chamado de ouro verde.""")
                st.link_button("Ir para o documentário", "https://www.youtube.com/watch?v=2NB61WU1WfM")


        st.divider()


# --- ABA 2: ESTRUTURA ---
    with tab_estrutura:
        st.markdown("### 🏗️ Como organizar seu texto?")
        st.write("A redação do ENEM possui 4 blocos fundamentais:")
        
        with st.container(border=True):
            st.markdown("**1. Introdução (Apresentação)**")
            st.write("Comece com um repertório (ex: Wall-E), apresente o tema e cite duas causas que você vai defender (tese).")
        
        with st.container(border=True):
            st.markdown("**2. Desenvolvimento 1 (Causa 1)**")
            st.write("Use conectivos como 'A princípio' ou 'Em primeira análise'. Foque na falha do Estado ou Silenciamento Social.")
            
        with st.container(border=True):
            st.markdown("**3. Desenvolvimento 2 (Causa 2)**")
            st.write("Use conectivos como 'Ademais' ou 'Outrossim'. Foque na herança cultural ou negligência da sociedade.")

        with st.container(border=True):
            st.markdown("**4. Conclusão (Proposta de Intervenção)**")
            st.write("Responda: Quem vai fazer? O quê? Como? Para quê? + Detalhamento.")



# --- ABA 3: NOTA MIL ---
    with tab_mil:
        st.markdown("### 🏆 Exemplos para se inspirar")
        st.write("Ler textos aprovados ajuda a entender o 'ritmo' da escrita.")
        
        c1, c2 = st.columns(2)
        with c1:
            st.info("📂 **Cartilha do Participante**\nManual oficial do INEP com análises de corretores.")
            st.link_button("Abrir Cartilha 2024", "https://download.inep.gov.br/publicacoes/institucionais/avaliacoes_e_exames_da_educacao_basica/a_redacao_no_enem_2024_cartilha_do_participante.pdf")
        
        with c2:
            st.success("🗞️ **Repositório G1**\nExemplos de textos nota 1000 reais comentados.")
            st.link_button("Ver Redações Nota 1000", "https://g1.globo.com/educacao/enem/2024/noticia/2025/03/14/enem-2024-leia-redacoes-nota-mil.ghtml")


# --- ABA 4: CITAÇÕES ---
    with tab_citacoes:
        st.markdown("### 📝 Citações que cabem em quase tudo")
        st.write("Dica: Não decore apenas a frase, entenda o conceito por trás dela!")

        c1, c2 = st.columns(2)

        with c1:
            with st.container(border=True):
                st.markdown("#### 🏛️ Inércia Estatal / Leis")
                st.write("**Gilberto Dimenstein:**")
                st.info("'O Brasil possui um dos conjuntos de leis mais avançados do mundo, mas que, na prática, não saem do papel.'")
                st.write("**Ariano Suassuna:**")
                st.info("'O que é muito difícil é você vencer a injustiça secular, que dilacera o Brasil em dois países distintos: o país dos privilegiados e o país dos despossuídos.'")
                st.write("**Milton Santos:**")
                st.info("'Existem apenas duas classes sociais, a dos que não comem e a dos que não dormem com medo da revolução dos que não comem.'")
                st.write("**Martin Luther King Jr:**")
                st.info("'Agora é hora de sair do vale escuro e desolado da segregação para o caminho iluminado da justiça racial'")
                st.write("**Jean-Paul Sartre:**")
                st.info("'A violência, seja qual for a maneira como ela se manifesta, é sempre uma derrota.'")   


            with st.container(border=True):
                st.markdown("#### 🎓 Educação")
                st.write("**Paulo Freire:**")
                st.info("'Se a educação sozinha não transforma a sociedade, sem ela tampouco a sociedade muda.'")
                st.write("**Nelson Mandela:**")
                st.info("'A educação é a arma mais poderosa que você pode usar para mudar o mundo.'")    
                st.write("**Simone de Beauvoir:**")
                st.info("'É preciso erguer o povo à altura da cultura e não rebaixar a cultura ao nível do povo.'")    
                st.write("**Voltaire:**")
                st.info("'Preconceito é opinião sem conhecimento.'")   
                st.write("**René Descartes:**")
                st.info("'Ler um bom livro é como conversar com as melhores mentes do passado.'")   



        with c2:

            with st.container(border=True):
                st.markdown("#### 🌍 Comportamento Social")
                st.write("**Arthur Schopenhauer:**")
                st.info("'O maior erro que um homem pode cometer é sacrificar a sua saúde a qualquer outra vantagem.'")
                st.write("**Manuel Castells:**")
                st.info("'A internet é muito mais que uma tecnologia. É um meio de comunicação, de interação e de organização social.'")                   
                st.write("**John Piper:**")
                st.info("'A marca da cultura de consumo é a redução do ‘ser’ para ‘ter’.'")                   
                st.write("**Zygmunt Bauman:**")
                st.info("'Não são as crises que mudam o mundo, e sim nossa reação a elas.'")    

            with st.container(border=True):
                st.markdown("#### 🌍 Meio Ambiente e Sustentabilidade")
                st.write("**Ailton Krenak:**")
                st.info("'Humanidade vive divórcio da vida na Terra.'")
                st.write("**Greta Thunberg:**")
                st.info("'Eu não quero que vocês estejam esperançosos. Quero que vocês estejam em pânico. Quero que ajam como se a casa estivesse pegando fogo, porque ela está'")
                st.write("**Carlos Drummond de Andrade:**")
                st.info("'A natureza não faz milagres, faz revelações.'")
                st.write("**Leonardo da Vinci:**")
                st.info("'A água é o veículo da natureza.'")

        st.divider()
        st.warning("⚠️ **Lembre-se:** A citação deve estar 'abraçada' pelo seu texto. Explique como ela se conecta com o problema do tema!")




# --- PÁGINA DE DICAS ---
elif st.session_state['pagina'] == "dicas":
    st.subheader("💡 Guia do Estudante")
    
    tab_assuntos, tab_cotas, tab_tri, tab_programas = st.tabs([
        "🎯 O que mais cai", 
        "⚖️ Entenda as Cotas", 
        "📊 O que é TRI?", 
        "📅 Programas"
    ])

    with tab_assuntos:
        st.markdown("### 🎯 Onde focar seus esforços?")
        st.write("Segundo nossas pesquisas, esses foram os três temas que mais caíram em cada matéria:")

        col1, col2 = st.columns(2)
        with col1:
            with st.expander("📖 Linguagens e Códigos"):
                st.write("**Português:** Gramática (58%), Interpretação (15%), Teoria Literária (0,5%)")
                st.write("**Literatura:** Teoria (48%), Lit. Brasileira (46%), Lit. Portuguesa (2%)")
                st.caption("📺 Canais: Débora Aladim, PoxaLulu")
            with st.expander("🧪 Exatas e Natureza"):
                st.write("**Matemática:** Aritmética (26%), Funções (10%)")
                st.write("**Biologia:** Ecologia (37%), Citologia (9%)")
                st.write("**Física:** Mecânica (26%), Eletricidade (19%), Ondulatória (14%)")
                st.write("**Química:** Geral (33%), Físico-Química (30%), Orgânica (16%)")
                st.caption("📺 Canais: Ferretto, Professor Boaro, Samuel Cunha")
            
        with col2:
            with st.expander("🌎 Ciências Humanas"):
                st.write("**História:** Brasil (50%), Geral (30%), Temática (13%)")
                st.write("**Filosofia:** Política (25%), Ética (25%), Moderna (12%)")
                st.write("**Geografia:** População (15%), Agrária (13%), Meio Ambiente (13%)")
                st.write("**Sociologia:** Ciência Política (21%), Cultura (18%), Temas Contemporâneos (17%)")                
                st.write("**Artes:** Brasileira (17%), Patrimônio (16%)")
                st.caption("📺 Canais: Débora Aladim, Se Liga, Ricardo Marcílio")

            with st.expander("🌎 Línguas Estrangeiras"):
                st.write("**Inglês:** Interpretação (81%), Vocabulário (11%)")
                st.write("**Espanhol:** Interpretação (73%), História (13%)")

    with tab_tri:
        st.markdown("### 📊 Entendendo a TRI: Por que notas iguais são diferentes?")
        st.write("A **TRI** é o algoritmo que mede a **coerência** do seu conhecimento.")
        
        col_facil, col_dificil = st.columns(2)
        with col_facil:
            st.success("✅ **O acerto coerente:**\nAcertar as fáceis e médias mostra que você domina a base. Sua nota sobe!")
        with col_dificil:
            st.error("⚠️ **O acerto 'chute':**\nAcertar as difíceis e errar as fáceis indica chute. Sua nota sobe menos.")
        
        st.info("💡 **Dica de Ouro:** Vale mais a pena garantir as questões de 'Regra de 3' e 'Ecologia' do que travar em uma impossível de Logaritmo!")

    with tab_cotas:
        st.markdown("### ⚖️ Como funcionam as Cotas?")
        st.write("A Lei de Cotas reserva vagas para quem cursou o **Ensino Médio INTEGRALMENTE em escola pública**.")
        
        col_renda, col_raca = st.columns(2)
        with col_renda:
            st.markdown("#### Por Renda")
            st.write("- **L1:** Renda Baixa\n- **L5:** Renda Independente")
        with col_raca:
            st.markdown("#### Por Raça (PPI)")
            st.write("- **L2:** Renda Baixa + PPI\n- **L6:** Renda Independente + PPI")
        
        st.markdown("> **AC (Ampla Concorrência):** Destinada a quem estudou em escola particular ou não optou pelas cotas.")
        
        with st.expander("🔢 Passo a passo: Cálculo de Renda"):
            st.write("1. Some o salário bruto de todos da casa.\n2. Divida pelo número de moradores.\n3. Resultado ≤ 1 salário mínimo? Você é **Baixa Renda**.")

        with st.expander("📝 Quiz: Em qual cota eu me encaixo?"):
            p1 = st.radio("1. Onde você cursou o Ensino Médio?", ["Escola Pública", "Escola Particular"])
            if p1 == "Escola Particular":
                st.warning("Sua modalidade é: **AC (Ampla Concorrência)**")
            else:
                p2 = st.radio("2. Sua renda familiar por pessoa é maior que 1 salário mínimo?", ["Sim", "Não"])
                p3 = st.radio("3. Você se autodeclara Preto, Pardo, Indígena ou Quilombola?", ["Sim", "Não"])
                
                if p2 == "Não" and p3 == "Sim": res = "L2"
                elif p2 == "Não" and p3 == "Não": res = "L1"
                elif p2 == "Sim" and p3 == "Sim": res = "L6"
                else: res = "L5"
                st.success(f"Sua cota provável é: **{res}**")

        st.markdown("### 📋 Preparação para a Vaga")
        with st.expander("Documentos 'Coringa'"):
            st.write("""
            * **Histórico Escolar:** Comprovando 3 anos de escola pública.
            * **Título e Quitação Eleitoral:** Obrigatório para maiores de 18 anos.
            * **Certificado de Reservista:** Para homens maiores de 18 anos.
            * **Documentos de Renda:** Contracheques ou Folha do CadÚnico.
            """)

        with st.expander("Banca de Heteroidentificação (Cotas PPI)"):
            st.write("Verificação presencial ou online das características físicas para confirmar a autodeclaração e evitar fraudes.")

    with tab_programas:
        st.markdown("### 🎓 Programas de Acesso ao Ensino Superior")
        st.write("Escolha o programa para ver detalhes e notas de corte:")

        # --- EXPANDER SISU ---
        with st.expander("🟦 SiSU - Sistema de Seleção Unificada", expanded=False):
            st.write("**O que é:** Vagas em universidades públicas (como UFJF-GV e IFMG).")
            
            # Notas de Corte de GV que já tínhamos
            notas_gv = {
            "Medicina (UFJF-GV)": 801.98,
            "Direito (UFJF-GV)": 737.82,
            "Odontologia (UFJF-GV)": 747.00,
            "Fisioterapia (UFJF-GV)": 724.14,
            "Administração (UFJF-GV)": 672.74,
            "Ciências Contábeis (UFJF-GV)": 673.20,
            "Ciências Econômicas (UFJF-GV):": 696.94,
            "Educação Física (UFJF-GV)": 669.08,
            "Farmácia (UFJF-GV)": 707.14,
            "Nutrição (UFJF-GV)": 698.98,
            "Engenharia de Produção (IFMG-GV)": 702.90,
            "Engenharia Ambiental e Sanitária(IFMG-GV)": 662.44,
            "Engenharia Civil (IFMG-GV)": 733.14,
            "Gestão Ambiental (IFMG-GV)": 651.36
        }
            
            curso_sel = st.selectbox("Selecione um curso para ver a meta (SiSU GV):", list(notas_gv.keys()), key="sisu_gv")
            st.metric(label=f"Nota de Corte Estimada - {curso_sel}", value=notas_gv[curso_sel])
            st.link_button("Ir para o site do SiSU", "https://acessounico.mec.gov.br/sisu")
            st.link_button("Faculdades e notas de corte", "https://sisu.mec.gov.br/#/vagas")

        # --- EXPANDER PROUNI ---
        with st.expander("🟧 ProUni - Programa Universidade para Todos"):
            st.write("**O que é:** Bolsas de estudo (50% ou 100%) em faculdades particulares.")
            st.markdown("""
            * **Público:** Alunos de escola pública ou bolsistas em particulares.
            * **Critério:** Renda familiar de até 1,5 salário mínimo (integral) ou 3 salários (parcial).
            * **Em GV:** Ótimo para cursos em faculdades como Univale e Pitágoras.
            """)
            st.link_button("Consultar Bolsas ProUni", "https://acessounico.mec.gov.br/busca")

        # --- EXPANDER FIES ---
        with st.expander("🟩 Fies - Fundo de Financiamento Estudantil"):
            st.write("**O que é:** O governo paga sua faculdade particular e você quita a dívida após se formar.")
            st.markdown("""
            * **Vantagem:** Juros zero para quem tem renda baixa.
            * **Exigência:** Mínimo de 450 pontos no ENEM e não ter zerado a redação.
            """)
            st.link_button("Simular Fies", "https://acessounico.mec.gov.br/fies")

# Rodapé
st.markdown('<div style="text-align: center; margin-top: 50px; color: grey; font-size: 0.8rem;">Projeto de Extensão Universitária • Governador Valadares/MG</div>', unsafe_allow_html=True)
