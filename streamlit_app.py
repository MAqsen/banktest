import streamlit as st
import pandas as pd

# Fonction de prétraitement des données
def preprocess_data(bank):
    st.write("Suite à ces analyses nous pouvons passer au pré-processing du jeu de données.")
    
    st.write("Comme vu précédemment, le jeu de données est propre car il ne contient aucun doublon ni valeurs manquantes. Il dispose malgré tout de nombreuses valeurs insignifiantes tel que 'unknown'(11239) et 'others'(537). Nous avons décidé de supprimer la valeur 'unknown' des variables 'job' et 'education' car cela n'impactera pas le dataset au vu du faible volume de cette valeur.")
    
    # Suppression des lignes avec les valeurs 'unknown' pour les colonnes 'job' et 'education'
    bank_cleaned = bank.drop(bank.loc[bank["job"] == "unknown"].index, inplace=False)
    bank_cleaned = bank_cleaned.drop(bank_cleaned.loc[bank_cleaned["education"] == "unknown"].index, inplace=False)
    display(bank_cleaned)

    st.write("Nous avons eu une réflexion pour certaines variables :")
    
    st.write("- poutcome")
    st.write("Nous avons réfléchis à 3 options :")
    st.write("1. soit nous gardons cette variable dans le dataset et nous supprimons les lignes 'unknown'. Cela a pour conséquence de réduire considérablement la taille de notre dataset. Mais nous serons certainement amenés à le réduire dans tous les cas par la suite.")
    st.write("2. soit nous la gardons telle quelle. Nous pouvons choisir un modèle qui peut être entraîné avec ce type de donnée, et nous verrons l’impact.")
    st.write("3. soit nous supprimons complètement cette colonne car la distribution pourrait impacter négativement notre modèle.")
    st.write("Nous sommes plutôt partis sur la deuxième solution, car outre les 'unknown' et 'other', la distribution de la variable est plutôt bonne..")

    st.write("- contact")
    st.write("Nous avons décidé de supprimer cette colonne car sa distribution n’est pas représentative.")

    st.write("- pdays")
    st.write("Nous avons décidé de supprimer cette colonne à cause de la valeur -1 sur-représentée et que nous ne sommes pas sûrs de bien interpréter.")
    
    st.write("Suppression des colonnes 'contact' et 'pdays' car non significatives")
    bank_cleaned = bank_cleaned.drop(['contact', 'pdays'], axis=1)
    
    st.write("Nous avons également transformé la durée en minute sur Duration.")
    # Transformation de la durée en minutes
    bank_cleaned['duration'] = bank_cleaned['duration'] // 60
    
    return bank_cleaned

# Chargement des données
st.title("Prétraitement des données bancaires")

uploaded_file = st.file_uploader("Choisir un fichier CSV", type="csv")
if uploaded_file is not None:
    bank = pd.read_csv(uploaded_file)
    bank_cleaned = preprocess_data(bank)
    
    st.write("### Distribution des emplois après nettoyage:")
    st.write(bank_cleaned['job'].value_counts())
    
    st.write("### Distribution des niveaux d'éducation après nettoyage:")
    st.write(bank_cleaned['education'].value_counts())

    st.write("### Nombre total de lignes après nettoyage:")
    st.write(bank_cleaned.value_counts().sum())
    
    st.write("### Statistiques sur la colonne 'previous':")
    st.write(bank_cleaned['previous'].describe())
    
    st.write("### Statistiques sur la colonne 'duration':")
    st.write(bank_cleaned['duration'].describe())

    st.write("### Aperçu des premières lignes des données nettoyées:")
    st.write(bank_cleaned.head())


