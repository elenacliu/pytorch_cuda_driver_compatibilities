import sqlite3
import streamlit as st
import pandas as pd
import natsort

conn = sqlite3.connect('version.db')

st.title('PyTorch (on Linux64) Installation Environment Selection')


pytorch_versions = ['null',
    '1.0.0', '1.0.1', '1.1.0', '1.2.0', '1.2.0+cu92', '1.3.0', '1.3.1', '1.4.0', '1.5.0', '1.5.1', 
    '1.6.0', '1.7.0', '1.7.1', '1.8.0', '1.8.1', '1.9.0', '1.9.1', '1.10.0', '1.10.1', '1.10.2',
    '1.11.0', '1.12.0', '1.12.1', '1.13.0', '1.13.1', '2.0.0']
python_versions = ['null', '3.6', '3.7', '3.8', '3.9', '3.10']
cuda_versions = ['null', 
                '9.2', 
                '10.0', '10.1', '10.2', 
                '11.0', '11.1', '11.3', '11.5', '11.6', '11.7', '11.8']
sm_versions = ['null', 'sm_20', 'sm_35', 'sm_37', 'sm_50', 'sm_60', 'sm_61', 'sm_70', 'sm_75', 'sm_80', 'sm_86', 'sm_90']
st.markdown('## Please select the software version and/or compute capability of your NVIDIA GPU')

col1, col2, col3, col4 = st.columns(4)
with col1:
    option_pytorch = st.selectbox(label='PyTorch Version', options=pytorch_versions)
with col2:
    option_python = st.selectbox(label='Python Version', options=python_versions)
with col3:
    option_cuda = st.selectbox(label='CUDAToolkit Version', options=cuda_versions)
with col4:
    option_sm = st.selectbox(label='SM Version', options=sm_versions)

def main():
    cur = conn.cursor()

    sql = 'SELECT * FROM pytorch'
    data = []
    cond = ''
    if option_pytorch != 'null':
        cond += f' AND pytorch = ?'
        data.append(option_pytorch)
    if option_python != 'null':
        cond += f' AND python = ?'
        data.append(option_python)
    if option_cuda != 'null':
        cond += f' AND cuda like ?'
        data.append(option_cuda+'%')
    if option_sm != 'null':
        cond += f' AND sm = ?'
        data.append(option_sm[3:])
    if cond != '':
        sql = sql + ' WHERE ' + cond[4:]
    cur = cur.execute(sql, data)

    df = pd.DataFrame(cur.fetchall(), columns=['PyTorch', 'Python', 'CUDA', 'cuDNN', 'SM'])
    df = df.sort_values(by=['PyTorch', 'Python', 'CUDA', 'cuDNN', 'SM'], ignore_index=True, key=natsort.natsort_keygen(alg=natsort.ns.LOCALEALPHA))
    # for tup in cur.fetchall()[:20]:
    # return cur.fetchall()
    st.table(df)


main()