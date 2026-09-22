
import streamlit as st

def z(a,b,c,d,e,f):
    st.text("")
    st.text("")
    st.text("")
    st.title("Condition for Human Behavior to be Emergency:")
    st.text("")
    st.text("")
    st.title("let's see for crowd Manageent")
    col5, = st.columns(1)
    #selecting first column
    with col5:
        st.subheader("Seat occupied")
        st.write("occupied seat in ground A = ", a,"%")
        st.write("occupied seat in ground B = ", b,"%")
        st.write("occupied seat in ground c = ", (c/500)*100,"%")
        st.write("occupied seat in ground D = ", a,"%")
        st.write("occupied seat in ground E = ", b,"%")
        st.write("occupied seat in ground F = ", (c/500)*100,"%")
        st.text("")   
    st.text("")



    st.text("")
    st.text("")
    st.text("")
    st.title("let's see for crowd Manageent")    
    st.text("")
    
#u = st.radio("Weather the peson can enter from Gate A:", ["pass", "fail"], key="person_entry_a")
#Basic radio button
#choice = st.radio("Select an option:", ["Option 1", "Option 2", "Option 3"])
# if u == "pass":
# Combination 1
#Combination 1: Order a -> b -> c
# a = available seats in Ground A
# b = available seats in Ground B
# c = available seats in Ground C

    if a >= 95 and b >= 95 and c >= 450:
        st.success("The most preffered Exit Gate G ")
        st.success("GATE D -> GROUND A -> EXIT GATE G")

    elif a >= 95 and b >= 95 and c < 450:
        st.success("The most preffered Exit Gate G ") 
        st.success("GATE D -> GROUND A -> EXIT GATE G")

    elif a < 95 and b >= 95 and c >= 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE E -> GROUND B -> EXIT GATE I")

    elif a >= 95 and b < 95 and c >= 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE F -> GROUND C -> EXIT GATE I")
        

    elif a < 95 and b < 95 and c >= 450:
        st.success("The most preffered Exit Gate i ")
        st.success("GATE F -> GROUND C -> EXIT GATE I")

    elif a >= 95 and b < 95 and c < 450:
        st.success("The most preffered Exit Gate G")
        st.success("GATE D -> GROUND A -> EXIT GATE G")


    elif a < 95 and b >= 95 and c < 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE E -> GROUND B -> EXIT GATE I")

    elif a < 95 and b < 95 and c < 450:
        st.success("The most preffered Exit Gate I ")
        st.info("GATE E -> GROUND B -> EXIT GATE I")

    elif a >= 95 and b >= 95 and c >= 450:
        st.success("The most preffered Exit Gate G ")
        st.success("GATE D -> GROUND A -> EXIT GATE G")
        st.success("The most preffered Exit Gate G ")

    elif a >= 95 and b >= 95 and c < 450:
        st.success("The most preffered Exit Gate G ")
        st.success("GATE D -> GROUND A -> EXIT GATE G")
        
    elif a >= 95 and b < 95 and c >= 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE F -> GROUND C -> EXIT GATE I")
    

    elif a >= 95 and b < 95 and c < 450:
        st.success("The most preffered Exit Gate G ")
        st.success("GATE D -> GROUND A -> EXIT GATE G")
  
    elif a < 95 and b >= 95 and c >= 450:
        st.success("The most preffered Exit Gate i ")
        st.success("GATE E -> GROUND B -> EXIT GATE I")

    elif a < 95 and b >= 95 and c < 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE E -> GROUND B -> EXIT GATE I")

    elif a < 95 and b < 95 and c >= 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE F -> GROUND C -> EXIT GATE I")

    elif a < 95 and b < 95 and c < 450:
        st.success("The most preffered Exit Gate I ")
        st.info("GATE E -> GROUND B -> EXIT GATE I")

    elif a >= b and a >= c:
        st.success("The most preffered Exit Gate G ")
        st.success("GATE D -> GROUND A -> EXIT GATE G")

    elif b >= a and b >= c:
        st.success("The most preffered Exit Gate I")
        st.success("GATE E -> GROUND B -> EXIT GATE I")

    elif c >= a and c >= b:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE F -> GROUND C -> EXIT GATE I")    


    st.text("")
    st.text("")
    st.title("let's see for Vehicle Manageent")
    st.text("")
    st.text("")



    if d >= 95 and e >= 95 and f >= 450:
        st.success("The most preffered Exit Gate G ")
        st.success("GATE D -> GROUND D -> EXIT GATE G")
        
    elif d >= 95 and e >= 95 and f < 450:
        st.success("The most preffered Exit Gate G ")
        st.success("GATE D -> GROUND D -> EXIT GATE G")

    elif d < 95 and e >= 95 and f >= 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE E -> GROUND E -> EXIT GATE I")

    elif d >= 95 and e < 95 and f >= 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE F -> GROUND F -> EXIT GATE I")
        
    elif d < 95 and e < 95 and f >= 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE F -> GROUND F -> EXIT GATE I")


    elif d >= 95 and e < 95 and f < 450:
        st.success("The most preffered Exit Gate G ")
        st.success("GATE D -> GROUND D -> EXIT GATE G")

    elif d < 95 and e >= 95 and f < 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE E -> GROUND E -> EXIT GATE I")

    elif d < 95 and e < 95 and f < 450:
        st.success("The most preffered Exit Gate I ")
        st.info("GATE E -> GROUND E -> EXIT GATE I")

    elif d >= 95 and e >= 95 and f < 450:
        st.success("The most preffered Exit Gate G ")
        st.success("GATE D -> GROUND D -> EXIT GATE G")

    elif d >= 95 and e < 95 and f >= 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE F -> GROUND F -> EXIT GATE I")
        
    elif d >= 95 and e < 95 and f < 450:
        st.success("The most preffered Exit Gate G ")
        st.success("GATE D -> GROUND D -> EXIT GATE G")

    elif d < 95 and e >= 95 and f >= 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE E -> GROUND E -> EXIT GATE I")

    elif d < 95 and e >= 95 and f < 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE E -> GROUND E -> EXIT GATE I")

    elif d < 95 and e < 95 and f >= 450:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE F -> GROUND F -> EXIT GATE I")

    elif d < 95 and e < 95 and f < 450:
        st.success("The most preffered Exit Gate I")
        st.info("GATE E -> GROUND E -> EXIT GATE I")

    elif d >= e and d >= f:
        st.success("The most preffered Exit Gate G ")
        st.success("GATE D -> GROUND D -> EXIT GATE G")

    elif e >= d and e >= f:
        st.success("The most preffered Exit Gate I ")
        st.success("GATE E -> GROUND E -> EXIT GATE I")

    elif f >= d and f >= e:
        st.success("The most preffered Exit Gate I")
        st.success("GATE F -> GROUND F -> EXIT GATE I")
                           
