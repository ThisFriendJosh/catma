import streamlit as st
from catma_core.io_yaml import load_yaml
from catma_core.validate import validate
from catma_core.render import render_graph

st.title("CAT-MA Viewer v0.1")

uploaded = st.file_uploader("Upload CatmaML YAML", type=["yaml","yml"])
if uploaded:
    path = f"/tmp/{uploaded.name}"
    with open(path, "wb") as f: f.write(uploaded.read())
    cat = load_yaml(path)
    st.write(f"Category: **{cat.name}**")
    errs = validate(cat)
    if errs:
        with st.error("Validation issues:"):
            for e in errs:
                st.write(f"- {e}")
    img = render_graph(cat, out_path="/tmp/catma_graph")
    st.image(img, caption="Rendered Category")
