import streamlit as st
import xarray as xr
import io

# Title
st.title("NetCDF File Uploader")

def load_data():
    uploaded_file = st.file_uploader("Upload a NetCDF file")
    # function to read netCDF file
        # Convert the uploaded file to BytesIO
    file = io.BytesIO(uploaded_file.read())
    
    # Open the file with xarray
    data = xr.open_dataset(file)

    # Get latitude and longitude variables
    lon = data.coords["Longitude"]
    lat = data.coords["Latitude"]

    # st.write(data)
    st.write(lon.values)
    st.write(lat.values)



#  # File upload sidebar
#     

#     if uploaded_file is not None:
#         # Read the NetCDF data
#         data = xr.open_dataset(uploaded_file)

#         st.write(data)

        # # Get latitude and longitude variables
        # lon = data.coords["longitude"]
        # lat = data.coords["latitude"]

        # # Select a variable to plot
        # variable_to_plot = st.sidebar.selectbox(
        #     "Select a variable to plot", data.data_vars.keys()
        # )

        # # Plot the data on a map
        # st.map(data[variable_to_plot].values, lon=lon.values, lat=lat.values)

if __name__ == "__main__":
    load_data()