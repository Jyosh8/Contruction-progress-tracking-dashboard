
# Copyright (c) 2024 Jyosh8
# Licensed under the MIT License (see LICENSE file for details)
import streamlit as st

def app():
    # Title for the Tableau dashboard section
    st.markdown("<h1 style='text-align: center;'>Kanvaz Construction Progress</h1>", unsafe_allow_html=True)


    # Description and Tableau link button
    st.write("Click the button below to open the Tableau visualization in a new tab.")
    st.markdown(
        """
        <a href="https://public.tableau.com/views/HousingConstructionProgress/HousingProgress?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link" target="_blank">
            <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
                Housing & Construction Progress
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

    # Display Image Below the Button
    st.image("data\logo\Housing Progress.png", caption="Housing Progress", use_container_width=True)

if __name__ == "__main__":
    app()
