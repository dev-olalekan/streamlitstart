import streamlit as st

st.write("Hello, Streamlit! 1234") 
st.write({"key": "value", "number": 42})
st.write(123)

# https://docs.streamlit.io/develop/quick-reference/cheat-sheet
# https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/llm-quickstart
# https://docs.streamlit.io/develop/api-reference/widgets/st.button

"heloo" if True else "no"
print("hello")
pressed = st.button("Click me", type="primary")
st.write(pressed)

st.title("this is a title")

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.html(
    """
    <div style="text-align:center; padding:20px; background:#f0f0f0;">
        <h2>Hello from HTML</h2>
        <p>This is custom HTML inside Streamlit.</p>
    </div>
    """,
    width="stretch"
) 


st.divider()

st.image("./static/sunrise.avif", caption="Sunrise by the mountains")