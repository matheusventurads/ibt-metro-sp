import streamlit as st
import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt

st.set_page_config(
    page_title='Interval Between Trains - Omdena São Paulo Brazil Chapter',
    layout='wide',
)

@st.cache_data
def get_data():
    df = pd.read_csv('data/publiclines_ibt_complete.csv')
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df.dropna(inplace=True)

    return df


def dashboard(df):

    st.write('# :train: Interval Between Trains Per Line')

    st.markdown("""
    This page display information about the public subway system of São Paulo.

    :large_blue_square: Line 1 - Blue (Azul)
    
    :large_green_square: Line 2 - Green (Verde)

    :large_red_square: Line 3 - Red (Vermelha)

    :black_square_button: Line 15 - Silver (Prata)
    """)


    st.subheader("Choose train line:")
    line = st.radio(
        label="Select the line to show its information:",  
        options=df['line'].unique(),
        index=0, 
        horizontal=True, 
        label_visibility="visible"
        )
    
    line = int(line)
    
    df1 = df[df['line'] == line][['date', 'interval']]

    fig = plt.figure()
    sns.lineplot(df1, x='date', y='interval')
    plt.xticks(rotation=45)
    plt.ylabel('Interval between trains in seconds')
    plt.xlabel('Year-Month')

    st.pyplot(fig)

if __name__ == '__main__':
    data = get_data()

    dashboard(data)
