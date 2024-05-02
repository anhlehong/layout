import streamlit as st


def layout():
    st.title("Depress Detection")

    input_col, analysis_col = st.columns((2, 1))

    with input_col:
        st.header("Input")

        if st.session_state.get("reset"):
            st.session_state.user_input = ""

        st.text_area("", height=350, key="user_input")

        col1, col2, col3 = st.columns((0.2, 0.55, 0.15))
        with col1:
            st.button("Detect", key="detect")
        with col2:
            st.write("")
        with col3:
            st.button("Reset", key="reset")

    output_col = st.container()

    if st.session_state.get("detect") and st.session_state.get("user_input"):
        with analysis_col:
            st.header("Analysis")
            st.write("")

            st.subheader("Ba từ tiêu cực nhất")
            st.write(st.session_state.get("user_input"))

            st.subheader("Câu tiêu cực nhất")
            st.write(st.session_state.get("user_input"))

            st.subheader("Topic")
            st.write(st.session_state.get("user_input"))

        with output_col:
            st.subheader("Output")
            st.write(st.session_state.get("user_input"))


if __name__ == "__main__":
    layout()
