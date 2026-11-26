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

#ticket categories:
YOUNG_CHILD = 'young-child'
CHILD = 'child'
ADULT = 'adult'
SENIOR = 'senior'

ticket_prices = {
    'weekday': {
        YOUNG_CHILD: 0,
        CHILD: 30,
        ADULT: 50,
        SENIOR: 30
    },
    'weekend': {
        YOUNG_CHILD: 0,
        CHILD: 40,
        ADULT: 60,
        SENIOR: 40
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
st.write('## Book tickets') 

#cvhoose age group
age_groups = {
    'Child (<5 y/o)': YOUNG_CHILD,
    'Child (<12 y/o)': CHILD,
    'Normal (<60 y/o)': ADULT,
    'Senior (60 y/o & above)': SENIOR,
}

age_label = st.selectbox('Select your age group', list(age_groups.keys()))
age_group = age_groups[age_label]
quantity = st.number_input('Number of tickets', min_value=1, max_value=50, value=1, step=1)

#calendar booking app interface
visit_date = st.date_input('Choose your visiting date')

#day type for ticket price calcs (weekday, weekend, public holiday)
def get_day_type(visit_date):
    date_str = visit_date.strftime('%Y-%m-%d')

    if date_str in date_ph_dict:
        return 'public holiday'

    if visit_date.weekday() >= 5:
        return 'weekend'

    else :
        return 'weekday'

day_type = get_day_type(visit_date)
if day_type == 'weekday':
    price_column = 'weekday'
else:
    price_column = 'weekend'

#web part for ticket selection
price = ticket_prices[price_column][age_group]
price_text = get_ticket_price_display(price)
nice_date = visit_date.strftime('%A, %d %B %Y')

#day type display
if day_type == 'public holiday':
    holiday_name = date_ph_dict[visit_date.strftime('%Y-%m-%d')]
    st.info(f'{nice_date} is **{holiday_name}**, so the ticket price is: {price_text}')
elif day_type == 'weekend':
    st.info(f'{nice_date} is a weekend, so the ticket price is: {price_text}')
else:
    st.info(f'{nice_date} is a weekday, so the ticket price is: {price_text}')

#total price display
total = price * quantity
total_text = get_ticket_price_display(total)

st.write(f'### Total: {total_text}')
#book button
if st.button('Book now'):
    st.success(f'Booked {quantity} x {age_label} ticket(s) for {nice_date}. Total: {total_text}')st.write('## gyat')