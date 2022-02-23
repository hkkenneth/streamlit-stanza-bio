import streamlit as st
import stanza
import pandas as pd

stanza.download('en', package='mimic', processors={'ner': 'i2b2'})
st.write('downloaded')
nlp = stanza.Pipeline('en', package='mimic', processors={'ner': 'i2b2'})
st.write('initialized')
doc = nlp('Complete PSG with a digital sleep system using the international 10-20 electrode placement for recording EEG, EOG, EMG from chin, ECG, respiratory effort, oximetry, body position, airflow, snoring sound, pulse rate and limb movement channels.')
st.write('Complete PSG with a digital sleep system using the international 10-20 electrode placement for recording EEG, EOG, EMG from chin, ECG, respiratory effort, oximetry, body position, airflow, snoring sound, pulse rate and limb movement channels.')
df = pd.DataFrame([e.to_dict() for e in doc.entities])
st.write(df)
