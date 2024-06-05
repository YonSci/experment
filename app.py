import h5netcdf

import streamlit as st
import xarray as xr
import h5netcdf
import netCDF4
import h5py
import io

# Print versions to verify installation
st.write("xarray version:", xr.__version__)
st.write("h5netcdf version:", h5netcdf.__version__)
st.write("netCDF4 version:", netCDF4.__version__)
st.write("h5py version:", h5py.__version__)

# Print available backends to verify installation
st.write("Available xarray backends:", xr.backends.list_engines())

# Title
st.title("NetCDF File Uploader")

def load_data():
    uploaded_file = st.file_uploader("Upload a NetCDF file")

    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Convert the uploaded file to BytesIO
        file = io.BytesIO(uploaded_file.read())
        
        try:
            # Open the file with xarray using the h5netcdf backend
            data = xr.open_dataset(file, engine='h5netcdf')

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
