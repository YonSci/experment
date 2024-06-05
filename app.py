import streamlit as st
import netCDF4 as nc
import xarray as xr
import io

# Title
st.title("NetCDF File Uploader")

def load_data():
    uploaded_file = st.file_uploader("Upload a NetCDF file")

    # Check if a file has been uploaded
    if uploaded_file is not None:
        try:
            # Convert the uploaded file to BytesIO
            file = io.BytesIO(uploaded_file.read())
            
            # Use netCDF4 to read the file
            with nc.Dataset('dummy', mode='r', memory=file.read()) as ds:
                # Convert netCDF4 dataset to xarray Dataset
                data = xr.open_dataset(xr.backends.NetCDF4DataStore(ds))

                # Get latitude and longitude variables
                lon = data.coords["Longitude"]
                lat = data.coords["Latitude"]

                # Display latitude and longitude values
                st.write("Longitude values:", lon.values)
                st.write("Latitude values:", lat.values)

        except Exception as e:
            st.error(f"Error opening dataset: {e}")
    else:
        st.info("Please upload a NetCDF file.")

if __name__ == "__main__":
    load_data()
