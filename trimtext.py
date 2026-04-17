import pyclip

st: str = pyclip.paste(text=True)
st = st.replace(" ", "")
pyclip.copy(st)
