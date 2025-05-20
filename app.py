import streamlit as st

st.title('Unit Converter')

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def sq_meters_to_sq_feet(sq_meters):
    return sq_meters * 10.7639

def sq_feet_to_sq_meters(sq_feet):
    return sq_feet / 10.7639

def gb_to_mb(gb):
    return gb * 1024

def mb_to_gb(mb):
    return mb / 1024

option = st.selectbox('Select a measurement type:', ('Length', 'Area', 'Digital Storage'))

if option == 'Length':
    conversion = st.selectbox('Select conversion:', ('Meters to Feet', 'Feet to Meters'))
    if conversion == 'Meters to Feet':
        value = st.number_input('Enter value in meters:', value=0.0, key='meters')
        if st.button('Calculate'):
            result = meters_to_feet(value)
            st.write(f'{value} meters is equal to {result:.2f} feet')
    else:
        value = st.number_input('Enter value in feet:', value=0.0, key='feet')
        if st.button('Calculate'):
            result = feet_to_meters(value)
            st.write(f'{value} feet is equal to {result:.2f} meters')
elif option == 'Area':
    conversion = st.selectbox('Select conversion:', ('Square Meters to Square Feet', 'Square Feet to Square Meters'))
    if conversion == 'Square Meters to Square Feet':
        value = st.number_input('Enter value in square meters:', value=0.0, key='sq_meters')
        if st.button('Calculate'):
            result = sq_meters_to_sq_feet(value)
            st.write(f'{value} square meters is equal to {result:.2f} square feet')
    else:
        value = st.number_input('Enter value in square feet:', value=0.0, key='sq_feet')
        if st.button('Calculate'):
            result = sq_feet_to_sq_meters(value)
            st.write(f'{value} square feet is equal to {result:.2f} square meters')
elif option == 'Digital Storage':
    conversion = st.selectbox('Select conversion:', ('Gigabytes to Megabytes', 'Megabytes to Gigabytes'))
    if conversion == 'Gigabytes to Megabytes':
        value = st.number_input('Enter value in gigabytes:', value=0.0, key='gb')
        if st.button('Calculate'):
            result = gb_to_mb(value)
            st.write(f'{value} gigabytes is equal to {result:.2f} megabytes')
    else:
        value = st.number_input('Enter value in megabytes:', value=0.0, key='mb')
        if st.button('Calculate'):
            result = mb_to_gb(value)
            st.write(f'{value} megabytes is equal to {result:.2f} gigabytes')