import streamlit as st

def app(dashboard_option):  # Accepts the dashboard_option argument
    st.title("Project Dashboards")

    # File paths for each dashboard image
    image_paths = {
        "Project Summary": "data/shopprogress/PROJECT SUMMARY.png",
        "Contract": "data/shopprogress/CONTRACT.png",
        "Land Acquisition": "data/shopprogress/LAND.png",
        "Issue": "data/shopprogress/ISSUE.png",
        "Safety": "data/shopprogress/SAFETY.png",
        "Rehabilitation": "data/shopprogress/REHABILITATION.png"
    }

    # Display the selected image
    st.image(image_paths[dashboard_option], use_container_width=True)

    # Footer
    st.markdown("<h6 style='text-align: right; color: grey;'></h6>", unsafe_allow_html=True)

