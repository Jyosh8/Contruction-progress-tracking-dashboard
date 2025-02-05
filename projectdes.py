# Copyright (c) 2024 Jyosh8
# Licensed under the MIT License (see LICENSE file for details)

import streamlit as st
import pandas as pd
from datetime import datetime

def app():
    # Title for the page
    st.title("Project Descriptions")

    # Data containing the project details
    data = {
        "Description": [
            "Project Name", 
            "Building Description", 
            "Scope of Work", 
            "Contract Sum", 
            "Owner", 
            "Consultant", 
            "Architect Designer", 
            "Structure Designer", 
            "Electrical Designer", 
            "Sanitary Designer", 
            "A/C & Ventilation Designer", 
            "Construction Time", 
            "Start Date", 
            "Finish Date", 
            "Time Passed",
            "Project Manager"
        ],
        "Details": [
            "KANVAZ CONSTRUCTION",  # Updated Project Name
            "A brief overview of the building, including its size, number of floors, intended use (single-family residence, duplex, etc.), and any unique features (e.g., modern design, energy-efficient systems).",  # Updated Building Description
            "Description of the work to be completed, including site preparation, foundation work, structural framing, roofing, interior and exterior finishes, plumbing, electrical installation, HVAC, landscaping, and any other specialized tasks like smart home installations.",  # Updated Scope of Work
            "1,234,590,456,789 USD",  # Updated Contract Sum
            "XAXAXA XAXA", 
            "KIARA", 
            "RAGHU", 
            "JAY", 
            "SYNERGIZ", 
            "MITRA", 
            "RAJIV", 
            "30 Months", 
            "10 Aug 2023",  # Start Date
            "2 Jan 2026",  # Finish Date
            "",  # Placeholder for Time Passed
            "SHLAGHANA"  # Project Manager
        ]
    }

    # Extract the start date from the data and calculate time passed
    start_date_str = data["Details"][12]  # Get the start date from the data
    start_date = datetime.strptime(start_date_str, "%d %b %Y")
    today = datetime.today()

    # Calculate the time passed in months
    time_passed = (today.year - start_date.year) * 12 + today.month - start_date.month

    # Update the "Time Passed" value in the data
    data["Details"][14] = f"{time_passed} Months"

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Apply custom CSS for responsiveness (making the table fit the container, and wrapping text)
    st.markdown("""
        <style>
            .stDataFrame {
                width: 100% !important;
                overflow-x: auto;
                table-layout: fixed;
            }
            .stTable {
                table-layout: fixed;
                width: 100%;
            }
            .stTable td {
                word-wrap: break-word;
                white-space: normal;
            }
            .stDataFrame tbody {
                font-size: 14px;
                line-height: 1.5;
            }
            .stDataFrame .stTable th, .stDataFrame .stTable td {
                padding: 10px;
                text-align: left;
            }
        </style>
    """, unsafe_allow_html=True)

    # Create 2 columns layout for data
    cols = st.columns(2)

    # Display the data in 2 columns
    for idx, row in enumerate(df.iterrows()):
        _, row_data = row
        with cols[idx % 2]:
            st.subheader(row_data["Description"])
            st.write(row_data["Details"])

    # Footer
    st.markdown("<h6 style='text-align: right; color: grey;'>Project Management - 2025</h6>", unsafe_allow_html=True)

