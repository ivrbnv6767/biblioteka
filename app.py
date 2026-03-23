import streamlit as st
st.title("Galeriq ot igri")
if "games" not in st.session_state:
  st.session_state.games = []

st.header("Dobavi nova igra")
name = st.text_input("ime na igra")
description = st.text_area("Opisanie")
image_url = st.text_input("URL na kartinka")

if st.button ("dobavi"):
  if name and description and image_url:
    st.session_state.games.append({
      "ime" : name,
      "opisanie" : description,
      "kartinka" : image_url
    })
  else:
    st.warning("Populnete vsichki poleta")


if st.session_state.games:
  st.header("Premahni igra")
  name=[]
  for a in st.session_state.games:
    name.append(a["ime"])

remove_name = st.selectbox("Premahni igra",name)
if st.button("Premahni"):
  for a in st.session_state.games:
    if a["ime"] == remove_name:
      st.session_state.games.remove(a)
      break

st.header("Galeriq")
if st.session_state.games:
  cols = st.colums(3)
  for idx, igra in enumerate(st.session_state.games):
    with cols[idx % 3]:
      st.subheader(igra["ime"])
      st.image(igra["kartina"],use_colums_width=True)
      st.write(igra["opisanie"])
else:
      st.info("Galeriqta e prazna. Dobavi igra!")
      

