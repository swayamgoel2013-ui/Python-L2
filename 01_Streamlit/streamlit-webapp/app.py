import streamlit as st

about_page = st.Page(
    "views/aboutme.py",
    title = "About me",
    icon = ":material/account_circle:",
    default = True,
)

project_1_page = st.Page(
    "views/salesdashboard.py",
    title = "Sales Dashboard",
    icon = ":material/bar_chart:"
)

project_2_page = st.Page(
    "views/chatbot.py",
    title = "Chatbot",
    icon = ":material/smart_toy:"
)


pg = st.navigation(  
{
    "Info":[about_page],
    "Projects":[project_1_page, project_2_page]
}
)

pg.run()