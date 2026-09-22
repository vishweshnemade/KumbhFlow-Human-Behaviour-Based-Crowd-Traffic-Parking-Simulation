import streamlit as st

def r(a, b, c, d, e, f):
    st.text("")
    st.text("")
    st.title("let's see for crowd Manageent")    
    st.text("")

    col5, = st.columns(1)
#selecting first column
    with col5:
        st.subheader("Seat occupied")
        st.write("occupied seat in ground A = ", a,"%")
        st.write("occupied seat in ground B = ", b,"%")
        st.write("occupied seat in ground D = ", (c/500)*100,"%")
        st.text("")
    
    u = st.radio("Weather the peson can enter from Gate A:", ["pass", "fail"], key="person_entry_a")
#Basic radio button
#choice = st.radio("Select an option:", ["Option 1", "Option 2", "Option 3"])
    if u == "pass":
        if a < 100:
#it do not has return it has write or success option only
            st.success("Allow people to enter from Gate A")
            st.info(a + 1)
        if a >= 100:
            st.warning("Please select fail option to proceed")    
#In Streamlit, st.info() creates a styled, blue alert box on the webpage used to display informational messages or status updates to the user.
    if u != "pass":
        st.warning("⚠ High crowd density detected near Gate A")
        if b < 100:
            st.success("Allow people to move from Gate B")
        if c < 500:
            st.success("Allow people to move from Gate C")
    st.write(f"Occupied space in Gate A: {a}%")
    st.write(f"Occupied space in Gate B: {b}%")
    st.write(f"Occupied space in Gate C: {(c / 500) * 100:.1f}%")
# : — Indicates that formatting options follow.
# .1 — Specifies that exactly 1 digit should appear after the decimal point.
# f — Stands for fixed-point float (a standard number format, not scientific notation). 
# val = 66.666666
#print(f"{val:.1f}%")
# Output: 66.7%  (rounds up to 1 decimal place)

    if not u == "pass":
        global v  # Explicitly declare it as global
        v = st.radio("Weather the peson can enter from Gate B:", ["pass", "fail"], key="person_entry_b")
        #Basic radio button
        #choice = st.radio("Select an option:", ["Option 1", "Option 2", "Option 3"])
        if v == "pass":
            if b < 100:
                st.success("Allow people to enter from Gate B")
                st.info(b + 1)
            if b >= 100:
                st.warning("Please select fail option to proceed")     
    if v != "pass":
        st.warning("⚠ High crowd density detected near Gate B")
        if a < 100:
            st.success("Allow people to move from Gate A")
        if c < 500:
            st.success("Allow people to move from Gate C")
    st.write("Occupied space in A = ", (a/100)*100, "%")
    st.write("Occupied space in B = ", (b/100)*100, "%")
    st.write("Occupied space in C = ", (c/500)*100, "%")

    if not u == "pass":
        if not v == "pass":
            w = st.radio("Weather the peson can enter from Gate C:", ["pass", "fail"], key="person_entry_c")
    #Basic radio button
    #choice = st.radio("Select an option:", ["Option 1", "Option 2", "Option 3"])
            if w == "pass":
                if c < 500:
                    st.success("Allow people to enter from Gate C")
                    st.info(c + 1)
                if c >= 500:
                    st.warning("Please select fail option to proceed")     
            if w != "pass":
                st.warning("⚠ High crowd density detected near Gate C")
                if a < 100:
                    st.success("Allow people to move from Gate A")
                if b < 100:
                    st.success("Allow people to move from Gate B") 
            st.write("Occupied space in A = ", (a/100)*100, "%")
            st.write("Occupied space in B = ", (b/100)*100, "%") 
            st.write("Occupied space in C = ", (c/500)*100, "%") 
    st.text("")
    st.text("")
    st.title("let's see for Vehicle Manageent")
 # for vehicles   
    d = st.number_input("Number of Vehicles entered in Gate E = ", min_value=0, max_value=100, step=1)
    e = st.number_input("Number of Vehicles entered in Gate F = ", min_value=0, max_value=100, step=1)
    f = st.number_input("Number of Vehicles entered in Gate G = ", min_value=0, max_value=500, step=1)
    st.text("")

    col6, = st.columns(1)
#selecting first column
    with col6:
        st.subheader("Seat occupied")
        st.write("occupied seat in Slot D = ", d,"%")
        st.write("occupied seat in Slot E = ", e,"%")
        st.write("occupied seat in Slot F = ", (f/500)*100,"%")
        st.text("")

    t = st.radio("Can vehicles enter from Slot D", ["pass", "fail"], key="vehicle_entry_d")
    if t == "pass":
        if d < 100:
            st.success("Allow Vehicle to enter from Slot D")
            st.info(d + 1)
        if d >= 100:
            st.warning("Please select fail option to proceed")     
    if t != "pass":
        st.warning("⚠ No Paeking Space detected near Slot D")
        if e < 100:
            st.success( "Allow Vehicle to move from Slot E")
        if f < 500:
                    st.success("Allow Vehicle to move from Slot F")
    st.write("Occupied space in D = ", (d/100)*100, "%")
    st.write("Occupied space in E = ", (e/100)*100, "%") 
    st.write("Occupied space in F = ", (f/500)*100, "%") 

    if not t == "pass":
        s = st.radio("Can vehicles enter from Slot E", ["pass", "fail"], key="vehicle_entry_e")
        if s == "pass":
            if e < 100:
                st.success("Allow Vehicle to enter from Slot E")
                st.info(e + 1)
            if e >= 100:
                st.warning("Please select fail option to proceed") 
        else:
            st.warning("⚠ No Paeking Space detected near Slot E")
            if d < 100:
                st.success("Allow Vehicle to move from Slot D")
            if f < 500:
                st.success("Allow Vehicle to move from Slot F")
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%") 
        st.write("Occupied space in F = ", (f/500)*100, "%") 

        if not t == "pass":
            if not s == "pass":
                i = st.radio("Can vehicles enter from Slot F", ["pass", "fail"], key="vehicle_entry_f")
                if i == "pass": 
                    if f < 500:
                        st.success("Allow Vehicle to enter from Gate F")
                        st.info(f + 1)
                    if f >= 500:
                        st.warning("Please select fail option to proceed")     
                else:
                    st.warning("⚠ High crowd density detected near Gate F")
                    if d < 100:
                            st.success("Allow Vehicle to move from Gate A")
                    if e < 100:
                            st.success("Allow Vehicle to move from Gate B") 
                st.write("Occupied space in D = ", (d/100)*100, "%")
                st.write("Occupied space in E = ", (e/100)*100, "%") 
                st.write("Occupied space in F = ", (f/500)*100, "%") 

            
#result = r(54, 65, 45, 52, 45, 45)

# Display option 1: Simple text output
#st.write(f"**Result:** {result}")