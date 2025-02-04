import streamlit as st
import pandas as pd

# File path for the Excel file
file_path = "data/1.xlsx"

# Function to generate a dummy .xer file (replace with actual logic if needed)
def generate_xer():
    xer_content = "Sample Primavera .xer file content"
    return xer_content.encode("utf-8")

def app():
    # Set the title of the Streamlit app
    st.title("📊 Progress Dashboard")

    # Display download buttons at the top
    st.subheader("📥 Download Files")

    # Download button for the Excel file
    with open(file_path, "rb") as f:
        st.download_button(
            label="📥 Click to Download Excel File",
            data=f,
            file_name="progress.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    # Download button for the .xer file (Primavera format)
    st.download_button(
        label="📥 Click to Download Primavera (.xer) File",
        data=generate_xer(),
        file_name="progress.xer",
        mime="application/octet-stream"
    )

    # Load the Excel file
    try:
        xls = pd.ExcelFile(file_path)
        sheet_names = xls.sheet_names

        # Display available sheets
        st.write("### Available Sheets:")
        for sheet in sheet_names:
            st.write(f"- {sheet}")
        
        # Let the user select a sheet to display
        selected_sheet = st.selectbox("Select a sheet to display:", sheet_names)
        
        # Load and display the selected sheet
        df = pd.read_excel(xls, sheet_name=selected_sheet)
        st.write(f"### Displaying Sheet: {selected_sheet}")
        st.dataframe(df)

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Run the app
if __name__ == "__main__":
    app()
