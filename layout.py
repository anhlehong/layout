import streamlit as st


def layout():
    st.title("Depress Detection")

    input_col, analysis_col = st.columns((1.5, 1))

    with input_col:
        st.header("Input")

        if 'user_input' not in st.session_state:
            st.session_state.user_input = ""
        user_input = st.text_area("", height=300, key="input", value=st.session_state.user_input)

        col1, col2, col3 = st.columns((0.3, 0.5, 0.2))
        with col1:
            detect_pressed = st.button("Detect")
        with col2:
            st.write("")
        with col3:
            reset_pressed = st.button("Reset")
            if reset_pressed:
                st.session_state.user_input = ""
                st.experimental_rerun()

    output_col = st.container()

    with analysis_col:
        st.header("Analysis")

        if detect_pressed:
            st.subheader("Ba từ tiêu cực nhất")
            st.write(user_input)

            st.subheader("Câu tiêu cực nhất")
            st.write(user_input)

            st.subheader("Topic")
            st.write(user_input)

    with output_col:
        if detect_pressed:
            st.subheader("Output")
            st.markdown(user_input)


if __name__ == "__main__":
    layout()
