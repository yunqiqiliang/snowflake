# streamlit_app.py

from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit Snowflake Sample!
"""
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.experimental_connection('snowflake', type='sql')

# Perform query.
df = conn.query('SELECT * from AMPLITUDE_EVENT;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")

