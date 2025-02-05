# Copyright (c) 2024 Jyosh8
# Licensed under the MIT License (see LICENSE file for details)

import streamlit as st

# ✅ Set the page config FIRST before any other Streamlit commands
st.set_page_config(layout="wide")

from streamlit_option_menu import option_menu
import home
import progress
import elevation
import plan
import tableau_images
import projectdes  # Ensure this module is available

# Sidebar menu
with st.sidebar:
    st.image('data/logo/KANVAZ.png', use_container_width=True)
    
    selected = option_menu(
        menu_title="Menu",
        options=[
            'Home',
            'Progress',
            'Elevation',
            'Floor Plan',
            'Project Descriptions',
            'Project Dashboards'
        ],
        icons=["house", "book", "bar-chart", "camera", "file-check", "file", "tool", "users", "dashboard"],
        default_index=0
    )

    dashboard_option = None
    if selected == 'Project Dashboards':
        dashboard_option = st.radio(
            "Select Dashboard",
            options=[
                "Project Summary",
                "Contract",
                "Land Acquisition",
                "Issue",
                "Safety",
                "Rehabilitation"
            ]
        )

# Main content area
if selected == 'Home':
    home.app()
elif selected == 'Progress':
    progress.app()
elif selected == 'Elevation':
    elevation.app()
elif selected == 'Floor Plan':
    plan.app()    
elif selected == 'Project Descriptions':
    projectdes.app()
elif selected == 'Project Dashboards' and dashboard_option:
    tableau_images.app(dashboard_option)
