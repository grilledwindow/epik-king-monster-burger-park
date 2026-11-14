from typing import Literal
import streamlit as st

date_ph_dict = dict()
with open('./data/PublicHolidaysfor2026-2027.csv', 'r') as f:
    f.readline()

    for line in f.readlines():
        line = line.strip()
        if line == '': break
        [date, day, holiday] = line.split(sep=',')
        date_ph_dict[date] = holiday

    f.close()
        
session = st.session_state

st.write("# Epik King Monster Burger Park")

ticket_prices = {
    'weekday': {
        'young-child': 0,
        'child': 30,
        'adult': 50,
        'senior': 30
    },
    'weekend': {
        'young-child': 0,
        'child': 40,
        'adult': 60,
        'senior': 40
    }
}

def get_ticket_price_display(price):
    return 'Free' if price == 0 else f'${price}'

def create_ticket_price_column(ticket_prices, day):
    return [get_ticket_price_display(p) for p in ticket_prices[day].values()]

ticket_table_data = {
    'Age group': ['Child (<5 y/o)', 'Child (<12 y/o)', 'Normal (<60 y/o)', 'Senior (60 y/o & above)'],
    'Weekday': create_ticket_price_column(ticket_prices, 'weekday'), 
    'Weekend/PH': create_ticket_price_column(ticket_prices, 'weekend'), 
}

st.write('## Ticket prices')
st.table(ticket_table_data)
