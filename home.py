#Home


import streamlit as st

# MUST be the first Streamlit command in your script
st.set_page_config(
    page_title="Custom Layout App",
    page_icon="📊",
    layout="wide",  # Options: "centered" (default) or "wide"
    initial_sidebar_state="expanded" # Options: "auto", "expanded", "collapsed"
)

st.text("")
st.markdown("<h1 style='text-align: center;'>KUMBHFLOW SIMULATION</h1>",unsafe_allow_html=True)
# Centered Subheader
st.markdown("<h3 style='text-align: center;'>Human Behaviour-Based Crowd, Traffic & Parking</h3>",unsafe_allow_html=True)
st.text("")
st.text("")
st.text("")
st.text("")

st.subheader("Map of khumb Mela")
# 1. Display a local image file
st.text("Make it easier to proceed")
image_path = r"E:\Python\Group Project\new try\map.png"
st.image(image_path, caption="Khumb Mela Map", use_container_width=True)

st.text("")
st.text("")
st.text("")
st.text("")
st.title("Simulation Area: Kumbh Mela")
st.text("")
#min value refers to initial value to be entered
#step refers to increment of number by 100 when clicked on + symbol
p = st.number_input("Number of People Registered = ", min_value=0, step=100)
v = st.number_input("Number of Vehicles Registered = ", min_value=0, step=100)
f = st.number_input("Emergency Facilities = ", min_value=0, step=1)
st.text("")
st.text("")

#

st.title("Initial Available Option")
# Equal-width columns
#setting up columns
col1, col2, col3, col4 = st.columns(4)

#selecting first column
with col1:
    st.header("Gate capacity")
    #Gate capacity
    st.text("Capacity of road A from gate A = 100")
    st.text("Capacity of road B from gate B = 100")
    st.text("Capacity of road C from gate C = 500")
    if p > 700:
        st.text("Wait for a while in Waiting Area")

#sselecting second column
with col2:
    st.header("Ground Capacity")
    st.text("Capacity of Ground A = 100")
    st.text("Capacity of Ground B = 500")
    st.text("Capacity of Ground C = 500")

with col3:
    st.header("Parking")
    st.text("Number of Parking Slots = 700" )
    st.text("Capacity of Sloat D = 100 ")
    st.text("Capacity of Sloat E = 100")
    st.text("Capacity of Sloat F = 500")

with col4:
    st.header("Emergency gates available")
    st.text("Emergency Gate G" )
    st.text("Emergency Gate I ")

# Custom-width ratio columns (e.g., 2:1 ratio)
#left_col, right_col = st.columns([2, 1])

#with left_col:
    #st.subheader("Main Content (66% width)")
    #st.line_chart([10, 20, 15, 25])

#with right_col:
    #st.subheader("Sidebar/Controls (33% width)")
    #st.text_input("Filter Data")

st.text("")
st.text("")
st.text("")



#human bihavior
col5, = st.columns(1)
#selecting first column
with col5:
    st.header("Select the Human Behavior:")
    st.write("Enter the serial number in the box at bottom to execute next command")
    st.text("Select Human Behaviour: \n 1. Normal \n 2. Rushed \n 3. Confused \n 4. Emergency/Panic")
st.text("")

#import rushed

#st.text("Available options")
#st.write("Occupied Space in Ground A = ", rushed.r(a), "%")
#st.write("Occupied Space in Ground B = ", b, "%")
#st.write("Occupied Space in Ground C = ", (c/500)*100, "%") 
#st.write("Occupied Space in Vehicle Parking Slot D = ", d, "%")
#st.write("Occupied Space in Vehicle Parking Slot E = ", e, "%")
#st.write("Occupied Space in Vehicle Parking Slot F = ", (f/500)*100, "%")


#import n
#import rushed
#import c
#import g
#import e

st.header("Enter the Serial number of the Human Behavior:")
h = st.number_input("Enter here: ", min_value=1, max_value=4, step=1)
#to include the
if st.button("confirm"):
            st.success("Submitted!")

def f(h):

    if h == 2:
        st.header("========================================================")
        st.header("BEHAVIOUR CHANGED: RUSHED")
        st.header("========================================================")
        import normal
        a = st.number_input("Number of People entered in ground A = ", min_value=0, max_value=100, step=1)
        b = st.number_input("Number of People entered in ground B = ", min_value=0, max_value=100, step=1)
        c = st.number_input("Number of People entered in ground C = ", min_value=0, max_value=500, step=1)    
        d = st.number_input("Number of Vehicles entered in slot D = ", min_value=0, max_value=100, step=1)
        e = st.number_input("Number of Vehicles entered in slot E = ", min_value=0, max_value=100, step=1)
        f = st.number_input("Number of Vehicles entered in slot F = ", min_value=0, max_value=500, step=1)
# Call the function by prefixing it with the module name
        normal.g(a, b, c, d, e, f)

    elif h == 1:
        st.header("========================================================")
        st.header("BEHAVIOUR CHANGED: NORMAL")
        st.header("========================================================")
        import rushed
        a = st.number_input("Number of People entered in ground A = ", min_value=0, max_value=100, step=1)
        b = st.number_input("Number of People entered in ground B = ", min_value=0, max_value=100, step=1)
        c = st.number_input("Number of People entered in ground C = ", min_value=0, max_value=500, step=1)    
        d = st.number_input("Number of Vehicles entered in slot D = ", min_value=0, max_value=100, step=1)
        e = st.number_input("Number of Vehicles entered in slot E = ", min_value=0, max_value=100, step=1)
        f = st.number_input("Number of Vehicles entered in slot F = ", min_value=0, max_value=500, step=1)
         # Call the function by prefixing it with the module name
        rushed.r(a, b, c, d, e, f)
        
    elif h == 3:
        st.header("========================================================")
        st.header("BEHAVIOUR CHANGED: NORMAL")
        st.header("========================================================")
        import confused
        a = st.number_input("Number of People entered in ground A = ", min_value=0, max_value=100, step=1)
        b = st.number_input("Number of People entered in ground B = ", min_value=0, max_value=100, step=1)
        c = st.number_input("Number of People entered in ground C = ", min_value=0, max_value=500, step=1)    
        d = st.number_input("Number of Vehicles entered in slot D = ", min_value=0, max_value=100, step=1)
        e = st.number_input("Number of Vehicles entered in slot E = ", min_value=0, max_value=100, step=1)
        f = st.number_input("Number of Vehicles entered in slot F = ", min_value=0, max_value=500, step=1)
                         # Call the function by prefixing it with the module name
        confused.x(a, b, c, d, e, f)
    elif h == 4:
        st.header("========================================================")
        st.header("BEHAVIOUR CHANGED: NORMAL")
        st.header("========================================================")
        import emergency
        a = st.number_input("Number of People entered in ground A = ", min_value=0, max_value=100, step=1)
        b = st.number_input("Number of People entered in ground B = ", min_value=0, max_value=100, step=1)
        c = st.number_input("Number of People entered in ground C = ", min_value=0, max_value=500, step=1)    
        d = st.number_input("Number of Vehicles entered in slot D = ", min_value=0, max_value=100, step=1)
        e = st.number_input("Number of Vehicles entered in slot E = ", min_value=0, max_value=100, step=1)
        f = st.number_input("Number of Vehicles entered in slot F = ", min_value=0, max_value=500, step=1)
                 # Call the function by prefixing it with the module name
        emergency.z(a, b, c, d, e, f) 

# Call the function and display the result
result = f(h)
if result:
    st.write(result)




st.text("")
st.text("")
st.text("")
st.text("")
st.markdown("<h1 style='text-align: center;'>THANK YOU TO VISIT ON OUR WEBSITE</h1>",unsafe_allow_html=True)
# Centered Subheader
st.text("")
st.markdown("<h1 style='text-align: center;'>Vishwesh Nemade  26BCE10989</h1>",unsafe_allow_html=True)

#
#st.success("Human Behavior is Rushed:")
##now = rushed.r(0,0,0,0,0,0)
#st.write(f"**Run:** {now}")

#
#forms a drop down list

#options = {
  #  "1. Normal": 1,
  #  "2. Rushed": 2,
  # "3. Confused": 3,
  #  "4. Group Movement": 4,
  #  "5. Emergency/Panic": 5
#}

#selected_option = st.selectbox("Select Human Behaviour:", list(options.keys()))
#h = options[selected_option]          


