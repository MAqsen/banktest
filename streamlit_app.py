import streamlit as st
import pandas as pd

# URL du jeu de données
url = 'https://raw.githubusercontent.com/sdrcr74/bank_nov23/main/bank.csv'

# Chargement du jeu de données
bank = pd.read_csv(url)

# Affichage de l'image et des titres
st.image("https://raw.githubusercontent.com/sdrcr74/bank_nov23/main/logo2.jpeg")
st.markdown("<h1 style='text-align: justify;'>Prédiction du succès d'une campagne de Marketing d’une banque</h1>", unsafe_allow_html=True)
st.subheader("Maxence Malherre, Sophie Dorcier, Stéphane Lascaux, Van-Anh HA")
st.subheader("NOV23_CONTINU_DA - Datascientest", divider='rainbow')

# Titre de la page
st.title("Preprocessing des données bancaires")

# Fonction de prétraitement des données
def preprocess_data(bank):
    st.write("Suite à ces analyses nous pouvons passer au pré-processing du jeu de données.")
    
    st.write("Comme vu précédemment, le jeu de données est propre car il ne contient aucun doublon ni valeurs manquantes. Il dispose malgré tout de nombreuses valeurs insignifiantes tel que 'unknown'(11239) et 'others'(537). Nous avons décidé de supprimer la valeur 'unknown' des variables 'job' et 'education' car cela n'impactera pas le dataset au vu du faible volume de cette valeur.")
    st.write("### Nombre total de lignes avant nettoyage:")
    st.write(bank.shape[0])
    # Suppression des lignes avec les valeurs 'unknown' pour les colonnes 'job' et 'education'
    code = """
# Suppression des lignes avec les valeurs 'unknown' pour les colonnes 'job' et 'education'
bank_cleaned = bank.drop(bank.loc[bank["job"] == "unknown"].index, inplace=False)
bank_cleaned = bank_cleaned.drop(bank_cleaned.loc[bank_cleaned["education"] == "unknown"].index, inplace=False)
    """
    st.code(code, language='python')
    bank_cleaned = bank.drop(bank.loc[bank["job"] == "unknown"].index, inplace=False)
    bank_cleaned = bank_cleaned.drop(bank_cleaned.loc[bank_cleaned["education"] == "unknown"].index, inplace=False)
    st.write(bank_cleaned.head())
     
    st.write("### Distribution de Job après nettoyage:")
    st.write(bank_cleaned['job'].value_counts())
    
    st.write("### Distribution de Education après nettoyage:")
    st.write(bank_cleaned['education'].value_counts())

    st.write("Nous avons eu une réflexion pour certaines variables :")
    
    st.write("- poutcome")
    st.write("Nous avons réfléchis à 3 options :")
    st.write("1. soit nous gardons cette variable dans le dataset et nous supprimons les lignes 'unknown'. Cela a pour conséquence de réduire considérablement la taille de notre dataset. Mais nous serons certainement amenés à le réduire dans tous les cas par la suite.")
    st.write("2. soit nous la gardons telle quelle. Nous pouvons choisir un modèle qui peut être entraîné avec ce type de donnée, et nous verrons l’impact.")
    st.write("3. soit nous supprimons complètement cette colonne car la distribution pourrait impacter négativement notre modèle.")
    st.write("Nous sommes plutôt partis sur la deuxième solution, car outre les 'unknown' et 'other', la distribution de la variable est plutôt bonne.")
    
    st.write("- contact")
    st.write("Nous avons décidé de supprimer cette colonne car sa distribution n’est pas représentative.")
    
    st.write("- pdays")
    st.write("Nous avons décidé de supprimer cette colonne à cause de la valeur -1 sur-représentée et que nous ne sommes pas sûrs de bien interpréter.")
    
    # Suppression des colonnes 'contact' et 'pdays'
    code = """
# Suppression des colonnes 'contact' et 'pdays'
bank_cleaned = bank_cleaned.drop(['contact', 'pdays'], axis=1)
    """
    st.code(code, language='python')
    bank_cleaned = bank_cleaned.drop(['contact', 'pdays'], axis=1)
    st.write(bank_cleaned.head())
    
    st.write("Nous avons également transformé la durée en minute sur Duration.")
    
    # Transformation de la durée en minutes
    code = """
# Transformation de la durée en minutes
bank_cleaned['duration'] = bank_cleaned['duration'] // 60
    """
    st.code(code, language='python')
    bank_cleaned['duration'] = bank_cleaned['duration'] // 60
    st.write(bank_cleaned.head())
    st.write("### Nombre total de lignes après nettoyage:")
    st.write(bank_cleaned.shape[0])
    return bank_cleaned



# Téléchargement du fichier
uploaded_file = st.file_uploader("Choisir un fichier CSV", type="csv")
if uploaded_file is not None:
    bank = pd.read_csv(uploaded_file)
    bank_cleaned = preprocess_data(bank)
   st.write("### Aperçu des premières lignes des données nettoyées:")
    st.write(bank_cleaned.head())

    # Affichage côte à côte des tableaux de statistiques
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Outliers sur la colonne 'previous':")
        st.write(bank_cleaned['previous'].describe())
    
    with col2:
        st.write("### Outliers sur la colonne 'duration':")
        st.write(bank_cleaned['duration'].describe())
else:
    st.write("Veuillez télécharger un fichier CSV pour commencer le prétraitement des données.")
