from streamlit_extras.grid import grid
import streamlit as st

# ALL FLAG

show_type_output = False

# DEFAULT SET UP PAGE
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":smiley:",
    layout="wide"  

)

# APP
col_left, col_right = st.columns([1,3])

with col_left:
    # PROJECT BOX
    col_left_prj_grid = grid(1,2,2,2,vertical_align="top")
    # Row 1:
    col_left_prj_grid.header("Project")
    # Row 2:
    col_left_prj_grid.text_input("Model Code")
    col_left_prj_grid.selectbox("PowerTrain",[])
    # Row 3:
    col_left_prj_grid.selectbox("Case",[])
    col_left_prj_grid.selectbox("Plant",[])
    # Row 4:
    col_left_prj_grid.selectbox("Dev",[])
    col_left_prj_grid.selectbox("Lot",[])

    # SPEC BOX
    # Row 1:
    st.header("SPEC")
    # Row 2:
    st.file_uploader("",accept_multiple_files=True)  
    # Row 3:
    col_left_spec_grid = grid(2,2,vertical_align="top")
    col_left_spec_grid.button("1. CADIS 項目作成", use_container_width=True)
    col_left_spec_grid.button("2. Create Output", use_container_width=True)


with col_right:
    # BANNER RIGHT
    col_r1, col_r2 = st.columns([2,1])
    with col_r1:
        st.image("img/banner.png",width=500)

    with col_r2:
        st.markdown('<p style="text-align: center;">AVATAR.</p>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center;">KNT19203.</p>', unsafe_allow_html=True)

    # Create button select output : Cadis or 5 output
    button_select_caout_grid = grid(1,1,4,vertical_align="top")
    selected_option_output_select = button_select_caout_grid.selectbox("SELECT OUTPUT",["CADIS 項目","Car配車要望表","WTC仕様用途一覧表","WTC要望集約兼チェックリスト","実験部品","特性管理部品リスト"])
    
    # area for table output
    if selected_option_output_select == "CADIS 項目":
        button_select_caout_grid.text_area("",value="CADIS 項目", height=400)
    if selected_option_output_select == "Car配車要望表":
        button_select_caout_grid.text_area("",value="Car配車要望表", height=400)
    if selected_option_output_select == "WTC仕様用途一覧表":
        button_select_caout_grid.text_area("",value="WTC仕様用途一覧表", height=400)
    if selected_option_output_select == "WTC要望集約兼チェックリスト":
        button_select_caout_grid.text_area("",value="WTC要望集約兼チェックリスト", height=400)
    if selected_option_output_select == "実験部品":
        button_select_caout_grid.text_area("",value="実験部品", height=400)
    if selected_option_output_select == "特性管理部品リスト":
        button_select_caout_grid.text_area("",value="特性管理部品リスト", height=400)        

    # button save and download
    button_select_caout_grid.header("")
    button_select_caout_grid.header("")
    button_select_caout_grid.button("SAVE", use_container_width=True)
    button_select_caout_grid.button("DOWNLOAD FILE", use_container_width=True)


