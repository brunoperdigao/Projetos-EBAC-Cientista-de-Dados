import pandas as pd
import streamlit as st

from io import BytesIO
from sklearn.preprocessing import StandardScaler
from pycaret.classification import *

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

@st.cache_data
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def main():
    st.set_page_config(page_title = 'Projeto Final',
        layout="wide",
        initial_sidebar_state='expanded'
    )

    st.write('## Avaliando o modelo gerado no Pycaret')
    st.markdown('---')

    st.sidebar.write('## Suba o arquivo')
    data_file_1 = st.sidebar.file_uploader('Bank Credit Dataset', type=['csv', 'ftr'])

    if (data_file_1 is not None):
        df_credit = pd.read_feather(data_file_1)    
        df_credit = df_credit.sample(50000)
        df_credit['bom'] = 1-df_credit.mau

        
        setup = setup(
            data = df_credit,
            target = 'mau',
            numeric_imputation='mean',
            normalize=True,           
            remove_outliers=True,     
            pca=True,                 
            pca_components=5,
            normalize_method='zscore', 
            transformation=True,
            transformation_method = 'quantile',
            fix_imbalance=True
            )
        )

        model_saved = load_model('../models/pycaret_model')
        predict = predict_model(model_saved, data=setup.X)

        df_xlsx = to_excel(predict)
        st.download_button(
            label='Download',
            data=df_xlsx,
            file_name='predict.xlxs'
        )

if __name__ == '__main__':
    main()
