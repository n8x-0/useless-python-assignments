import streamlit as st
import pandas as pd
import os  
from io import BytesIO  

# Setup for Streamlit app
st.set_page_config(page_title="Data Sweeper", layout="wide")  
st.title("Data Sweeper")

# App Description
st.markdown("### Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

# File uploader
uploaded_files = st.file_uploader(
    "📤 Upload your file (CSV or Excel):", 
    type=["csv", "xlsx"], 
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files: 
        file_ext = os.path.splitext(file.name)[1].lower()  # Fixed index usage
        st.write(f"📂 **Uploaded File:** {file.name} ({file_ext})")  

        # Read file based on extension
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file, engine="openpyxl")  # Ensure openpyxl is used
            else:
                st.error(f"❌ Unsupported file type: {file_ext}")
                continue  

            # Display file size
            file_size = len(file.getvalue()) / 1024  
            st.write(f"📏 **File Size:** {file_size:.2f} KB")

            # Show preview of data
            st.write("🔍 **Preview of the Data:**")
            st.dataframe(df.head())

            # Data Cleaning Options
            st.subheader("🛠️ Data Cleaning Options")

            # Remove missing values
            if st.checkbox(f"Remove missing values (NaN) from {file.name}"):
                df.dropna(inplace=True)
                st.success("✅ Missing values removed!")

            # Remove duplicate rows
            if st.checkbox(f"Remove duplicate rows from {file.name}"):
                df.drop_duplicates(inplace=True)
                st.success("✅ Duplicate rows removed!")

            # Select columns to keep
            all_columns = df.columns.tolist()
            selected_columns = st.multiselect(f"Select columns to keep from {file.name}:", all_columns, default=all_columns)
            if selected_columns:
                df = df[selected_columns]
                st.success("✅ Columns updated!")

            # Show cleaned data
            st.write("📌 **Cleaned Data Preview:**")
            st.dataframe(df.head())

            # Visualization Section
            st.subheader(f"📊 Data Visualization for {file.name}")
            if st.checkbox(f"Show Visualization for {file.name}"):
                numeric_cols = df.select_dtypes(include="number").columns.tolist()
                if len(numeric_cols) >= 2:
                    st.bar_chart(df[numeric_cols].iloc[:, :2])
                elif len(numeric_cols) == 1:
                    st.line_chart(df[numeric_cols])
                else:
                    st.warning("⚠️ Not enough numeric columns for visualization.")

            # File Conversion
            st.subheader(f"🔄 Convert {file.name} to CSV or Excel")
            conversion_type = st.radio(
                f"Convert {file.name} to:",
                ["CSV", "Excel"],
                key=file.name  # Fixed key usage
            )

            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                new_file_name = file.name.rsplit(".", 1)[0]  

                try:
                    if conversion_type == "CSV":
                        df.to_csv(buffer, index=False, encoding="utf-8-sig")  # Fixed encoding
                        new_file_name += ".csv"
                        mime_type = "text/csv"
                    else:
                        with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
                            df.to_excel(writer, index=False, sheet_name="Sheet1")
                        new_file_name += ".xlsx"
                        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                    buffer.seek(0)  # Reset buffer position for download

                    st.download_button(
                        label=f"📥 Download {new_file_name}",
                        data=buffer,
                        file_name=new_file_name,
                        mime=mime_type
                    )
                    st.success(f"✅ {new_file_name} is ready for download!")

                except Exception as e:
                    st.error(f"⚠️ Error converting {file.name}: {e}")

        except Exception as e:
            st.error(f"⚠️ Error processing file {file.name}: {e}")

    st.success("✅ All files successfully processed!")
