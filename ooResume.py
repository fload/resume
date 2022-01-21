import streamlit as st
from data import mapping_sample, skills_df, Jobs
import plotly.express as px
import pydeck as pdk

class Jesse:
    #Holds and Builds the data for my resume.

    def __init__(self):
        self.name = "Jesse Ferguson"
        self.phone = ':phone: [213-447-7170](213-447-7170)' #:emoji:
        self.location = ':house: Crestline, California'
        self.email = ':email: [ifload@gmail.com](mailto:ifload@gmail.com?subject=We%20need%20you%20on%20our%20team!)'
        self.map_data = mapping_sample
        self.skillset = skills_df
        self.jobs = Jobs
        self.map = None
        self.heatmap()

    def heatmap(self):
        "Creates Map."
        self.map = pdk.Deck(
            map_style="mapbox://styles/mapbox/satellite-streets-v11", 
            initial_view_state=pdk.ViewState(-117.816, 34.192, 9),
            layers=[
                pdk.Layer(
                    "HeatmapLayer",
                    data=self.map_data,
                    get_position=["lon", "lat"],
                    radius=100,
                    elevation_range=[0,3000],
                    pickable=True,
                    extruded=True,
                ),
            ]
        )

    def skill_plot(self):
        'Creates a Plotly chart.'
        template = 'ggplot2'
        fig = px.scatter(self.skillset, x="Skill", y="Experience_years",
                size="Use", color="Skill", labels=None, width=1200, height=700, template=template, )
        st.plotly_chart(fig)

    def sidebar_data(self):
        st.markdown("<h1 style='text-align: center; color: white;'>Jesse Ferguson</h1>", unsafe_allow_html=True)
        st.image('me.png')
        st.header("Contact")
        st.markdown(':phone: [213-447-7170](213-447-7170)')
        st.markdown(':house: Crestline, California')
        st.markdown(':email: [ifload@gmail.com](mailto:ifload@gmail.com?subject=We%20need%20you%20on%20our%20team!)')

    def run(self):
        st.set_page_config(page_title='Jesse Ferguson', page_icon="random",layout="wide")

        st.title = self.name

        with st.sidebar:
            self.sidebar_data()

        with st.expander("Python Developer", expanded=True):
            st.write('7 years experience with python, 1 year of full-stack development with the Django framework on google cloud. My experience with development has been mostly solo projects so I am excited for any opportunity to work with a team and learn new technologies.')

        with st.expander("Skills"):
            self.skill_plot()

        with st.expander("Experience"):
            st.markdown(self.jobs)

        with st.expander("Education/Certifications"):
            st.write('''- Udacity Machine Learning  
- TWIC Security access  
- California weights and measurement agent  
- Chevron Leadership Award  
- Aera Energy Safety and Compliance cert  
- Centennial High School – 2003''')

        with st.expander("Map"):
            st.write("A sample of my personal google gps data")
            st.write(self.map)

me = Jesse()
me.run()


