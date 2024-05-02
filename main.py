import streamlit as st
import datetime

st.header('Aguinaldo Calculator')
st.subheader('Enter your gross salary of each month')
st.caption('In each of the following boxes, you must enter the gross salary earned in each month as appropriate (Gross Salary: Salary that includes overtime, commissions, bonuses, without reductions in social charges or income).')

current_month = datetime.datetime.now().month

months = [
    'December (2023)', 'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November'
]

num_months = len(months)
months_per_col = num_months // 2

col1, col2 = st.columns(2)

salaries = {}

for i, month in enumerate(months):
    if i < months_per_col:
        disabled = False if i <= current_month else True
        salary = col1.text_input(f'{month}:', disabled=disabled)
        salaries[month] = salary
    else:
        disabled = False if i <= current_month else True
        salary = col2.text_input(f'{month}:', disabled=disabled)
        salaries[month] = salary

total_salary = (sum(float(salary)
                for salary in salaries.values() if salary)) / 12

st.write('Based on the data provided, your Aguinaldo should be:')
st.info(f'## {total_salary}')