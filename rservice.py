import streamlit as st
from data import DATABASE, DIAGNOSTIC_DATABASE, NON_ENGINE_DATABASE

st.set_page_config(page_title="R-Service", page_icon=("🔧"))

st.markdown("""
    <style>
    /* 1. Centrează textul din input-uri și titluri */
    .stMarkdown, .stText, h1, h2, h3, p {
        text-align: center;
    }

    /* 2. Centrează Label-urile de la Selectbox și Radio */
    div[data-testid="stWidgetLabel"] {
        text-align: center !important;
        display: block;
    }

    /* 3. Centrează butoanele radio (opțiunile orizontale) */
    div[data-testid="stHorizontalBlock"] {
        justify-content: center;
    }

    /* 4. Centrează mesajele de succes/info */
    div[data-testid="stNotificationContent"] {
        text-align: center;
    }
    
    /* 5. Dacă vrei ca butonul "Continue" să fie centrat dar nu pe toată lățimea */
    div.stButton {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

if 'app_state' not in st.session_state:
    st.session_state.app_state = {
        'stage': 'welcome',
        'car_data': {},
        'diagnostics': []
    }

def set_stage(new_stage):
    st.session_state.app_state['stage'] = new_stage
    st.rerun()

if st.session_state.app_state['stage'] == 'welcome':
    st.title("R-service 🔧")
    st.markdown("---")
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("Enter workshop 🔧"):
            set_stage('vehicle_config')

elif st.session_state.app_state['stage'] == 'vehicle_config':
    st.header("⚙️ Vehicle config")
    st.markdown("---")
    empty_l, center_col, empty_r = st.columns([0.5, 2, 0.5])

    with center_col:
        st.markdown("### 🏷️ Brand")
        make = st.selectbox("Brand", ["BMW", "AUDI", "MERCEDES"], label_visibility="hidden")
        
        st.markdown("### 📂 Series")
        model = st.text_input("Model line", placeholder="e.x. e60", label_visibility="hidden").strip().lower()
        
        engine_to_save = "Unknown Engine"

        car_key = None

        if make == "BMW":
            if model == "e60":
                car_key = "BMW E60 (2003-2010)"
            elif model !="":
                st.warning("Please enter the right model (e.x. e60) ⚠️")
        elif make == "AUDI":
            if model == "a6":
                car_key = "Audi A6 C6 (2004-2011)"
            elif model !="":
                st.warning("Please enter the right model (e.x. a6) ⚠️")
        elif make == "MERCEDES":
            if model == "w211":
                car_key = "Mercedes E-Class W211 (2002-2009)"
            elif model !="":
                st.warning("Please enter the right model (e.x. w211) ⚠️")


        if car_key:
            st.success(f"{model.upper()} Database found! ✅")

            fuel_options = list(DATABASE[car_key].keys())
            fuel = st.radio("Fuel Type", fuel_options, horizontal=True)

            c1, c2 = st.columns(2)
            with c1:
                variant_list = list(DATABASE[car_key][fuel].keys())
                selected_variant = st.selectbox("Variant", variant_list)

            with c2:
                engine_options = DATABASE[car_key][fuel][selected_variant]
                selected_year = st.selectbox("Year & Engine", list(engine_options.keys()))
        
            engine_to_save = engine_options[selected_year]
            st.info(f"Selected: {selected_variant} - {engine_to_save}")

        with st.expander("Why do I need to be precise?"):
            st.write("Precision helps our logic find the right parts for your car.")

    with st.sidebar:
        st.title("Help center")
        st.markdown("---")
        st.write("**If you have any issues you can contact us bellow on our email adress.**")
        st.markdown("---")
        st.write("**Contact: nrarress@gmail.com**")

    with center_col:
        if car_key:
            if st.button("Continue to symptoms ➡️", use_container_width=True):
                st.session_state.app_state['car_data'] = {
                    'make': make,
                    'model': model,
                    'engine': engine_to_save
                }
                set_stage('symptoms_input')

        else:
            st.button("Continue to symptoms ➡️", use_container_width=True, disabled=True, help="Plese enter a valid model.")

elif st.session_state.app_state['stage'] == 'symptoms_input':
    car = st.session_state.app_state['car_data']
    st.title("Symptoms Diagnostic")
    st.markdown("---")
    st.write(f"### Analyzing: {car['make']} {car['model'].upper()} ( {car[ 'engine' ]} )")


    with st.expander("Describe us your car symptoms", expanded=True):
        symptoms = st.text_area("Input", placeholder="e.x. My car burns oil.", label_visibility="collapsed")
        submit = st.button("Start AI Analysis")

    if submit and symptoms:
        st.session_state.app_state['symptoms'] = symptoms
        
        engine_code = car['engine'].split(" ")[0]
        make = car['make'].upper()
        user_input = symptoms.lower()
        results = []

        if engine_code in DIAGNOSTIC_DATABASE:
            for entry in DIAGNOSTIC_DATABASE[engine_code]:
                if any(key in user_input for key in entry['keywords']):
                    results.append({"type": "Engine", "data": entry})


        if make in NON_ENGINE_DATABASE:
            for entry in NON_ENGINE_DATABASE[make]:
                if any(key in user_input for key in entry['keywords']):
                    results.append({"type": "Chassis/General", "data": entry})

        st.markdown("### 🛠️ Potential Issues Detected: ")
        if results:
            for res in results:
                with st.container():
                    st.error(f"**{res['type']}: {res['data']['issue']}**")
                    st.info(f"💡 **Expert Solution:** {res['data']['solution']}")
                    st.markdown("---")
        else:
            st.warning("No specific matches found in our database for these keyword. Try 'smoke', 'rattle', 'leak', or 'clutch'.")

    if st.button("Back to garage"):
        set_stage('vehicle_config')