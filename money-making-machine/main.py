import streamlit as st 
import random 
import time  
import requests  

# Set the title of our web app
st.title("Money Making Machine")


# Function to create random amount of money
def generate_money():
    return random.randint(1, 1000)


# Create a section for generating money
st.subheader("Instant Cash Generator")
if st.button("Generate Money"):  
    st.write("Counting your money...") 
    time.sleep(5) 
    amount = generate_money()  
    st.success(f"You made ${amount}!")


# Function to get side hustle ideas from a server
def fetch_side_hustle():
    try:
        
        response = requests.get(
            "https://fastapi-api.vercel.app/side_hustles"
        )
        if response.status_code == 200:  
            hustles = response.json()  
            return hustles["side_hustle"]  
        else:
            return "Freelancing"  

    except:
        return "Something went wrong!" 


# Create a section for side hustle ideas
st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"):  
    idea = fetch_side_hustle()  
    st.success(idea)  


# Function to get money-related quotes from server
def fetch_money_quote():
    try:
        # Try to get quote from local server or deployed server
        response = requests.get(
            "https://fastapi-api.vercel.app/money_quotes"
        )
        if response.status_code == 200:
            quotes = response.json()  
            return quotes["money_quote"]  
        else:
            return "Money is the root of all evil!" 
    except:
        return "Something went wrong!" 


# Create a section for motivation quotes
st.subheader("Money-Making Motivation")
if st.button("Get Inspired"): 
    quote = fetch_money_quote()  
    st.info(quote)  