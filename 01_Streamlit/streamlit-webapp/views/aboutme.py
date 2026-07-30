import streamlit as st


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/Dog.avif", width = 230)
with col2:
    st.title("Dog", anchor=False)
    st.write("A dog is a loyal and friendly domesticated animal kept as a pet or working companion. Dogs are intelligent, playful, and come in many breeds, sizes, and colors. They are known for their strong bond with humans and can help with tasks such as guarding, herding, and providing emotional support."
    )

    if st.button("📧 Contact Me "):
        st.success("Email: swayam.goel2013@gmail.com",
    )
        
st.write("\n")
st.subheader("Positives of Dogs", anchor = False)
st.write(
 """
  - Loyal and faithful companions
  - Friendly and affectionate
  - Intelligent and quick learners
  - Playful and energetic
  - Protective of their owners
  - Great for reducing stress and loneliness
  - Good with families and children
  - Encourage regular exercise through walks
  - Can provide emotional support
  - Adaptable to different environments
"""
  )


st.write("\n")
st.subheader("Skills of Dogs", anchor = False)
st.write(
 """
 - Excellent sense of smell
 - Strong hearing abilities
 - Fast runners with good agility
 - Easy to train for various tasks
 - Can guard homes and property
 - Assist people with disabilities (guide and service dogs)
 - Help police and military detect drugs, explosives, and missing persons
 - Herd livestock on farms
 - Perform search and rescue operations
 - Learn and follow many commands and tricks
"""
  )
