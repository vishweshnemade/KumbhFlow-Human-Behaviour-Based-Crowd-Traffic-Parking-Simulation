
import streamlit as st

def g(a,b,c,d,e,f):
    st.text("")
    st.text("")
    st.text("")
    st.title("Condition for Human Behavior to be Rushed:")
    st.text("Average Walking Speed is Increased \nCrowd Concentration is Increased \nRoad Congestion is Increased \nParking Demand is Increased")
    st.text("")
    st.text("")
    st.title("let's see for crowd Manageent")
    #a = st.number_input("Number of People entered in ground A = ", min_value=0, max_value=100, step=1)
    #b = st.number_input("Number of People entered in ground B = ", min_value=0, max_value=100, step=1)
    #c = st.number_input("Number of People entered in ground C = ", min_value=0, max_value=500, step=1)    
    st.text("")



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
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%") 
        st.success("GATE D -> GROUND A -> EXIT GATE G")
        st.warning("NO space Available to visit any Ground")

    elif a >= 95 and b >= 95 and c < 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")    
        st.success("GATE D -> GROUND A -> EXIT GATE G")
        st.success("If you want you can go to Ground c")

    elif a < 95 and b >= 95 and c >= 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE E -> GROUND B -> EXIT GATE I")
        st.success("If you want you can go to Ground A")

    elif a >= 95 and b < 95 and c >= 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE F -> GROUND C -> EXIT GATE I")
        st.success("If you want you can go to Ground B")

    elif a < 95 and b < 95 and c >= 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE F -> GROUND C -> EXIT GATE I")
        st.success("If you want you can go to Ground A")
        st.success("If you want you can go to Ground B")

    elif a >= 95 and b < 95 and c < 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE D -> GROUND A -> EXIT GATE G")
        st.success("If you want you can go to Ground B")
        st.success("If you want you can go to Ground c")

    elif a < 95 and b >= 95 and c < 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE E -> GROUND B -> EXIT GATE I")
        st.success("If you want you can go to Ground c")
        st.success("If you want you can go to Ground A")

    elif a < 95 and b < 95 and c < 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("ALL GROUNDS HAVE AVAILABILITY")
        st.info("GATE E -> GROUND B -> EXIT GATE I")

    elif a >= 95 and b >= 95 and c >= 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE D -> GROUND A -> EXIT GATE G")
        st.warning("NO space Available to visit any Ground")

    elif a >= 95 and b >= 95 and c < 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE D -> GROUND A -> EXIT GATE G")
        st.success("If you want you can go to Ground C")

    elif a >= 95 and b < 95 and c >= 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE F -> GROUND C -> EXIT GATE I")
        st.success("If you want you can go to Ground B")
    

    elif a >= 95 and b < 95 and c < 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE D -> GROUND A -> EXIT GATE G")
        st.success("If you want you can go to Ground B")
        st.success("If you want you can go to Ground C")
    
    elif a < 95 and b >= 95 and c >= 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE E -> GROUND B -> EXIT GATE I")
        st.success("If you want you can go to Ground A")

    elif a < 95 and b >= 95 and c < 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE E -> GROUND B -> EXIT GATE I")
        st.success("If you want you can go to Ground C")
        st.success("If you want you can go to Ground A")

    elif a < 95 and b < 95 and c >= 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE F -> GROUND C -> EXIT GATE I")
        st.success("If you want you can go to Ground A")
        st.success("If you want you can go to Ground B")

    elif a < 95 and b < 95 and c < 450:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.warning("GROUNDS A, B AND C ARE NEAR CAPACITY")
        st.info("GATE E -> GROUND B -> EXIT GATE I")

    elif a >= b and a >= c:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE D -> GROUND A -> EXIT GATE G")

    elif b >= a and b >= c:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE E -> GROUND B -> EXIT GATE I")

    elif c >= a and c >= b:
        st.write("Occupied space in A = ", (a/100)*100, "%")
        st.write("Occupied space in B = ", (b/100)*100, "%") 
        st.write("Occupied space in C = ", (c/500)*100, "%")
        st.success("GATE F -> GROUND C -> EXIT GATE I")    



    st.text("")
    st.text("")
    st.title("let's see for Vehicle Manageent")
    st.text("")
    st.text("")


    if d >= 95 and e >= 95 and f >= 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE D -> GROUND D -> EXIT GATE G")
        st.warning("NO space Available to visit any Ground")

    elif d >= 95 and e >= 95 and f < 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE D -> GROUND D -> EXIT GATE G")
        st.success("If you want you can go to Ground F")

    elif d < 95 and e >= 95 and f >= 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE E -> GROUND E -> EXIT GATE I")
        st.success("If you want you can go to Ground D")

    elif d >= 95 and e < 95 and f >= 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE F -> GROUND F -> EXIT GATE I")
        st.success("If you want you can go to Ground E")

    elif d < 95 and e < 95 and f >= 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE F -> GROUND F -> EXIT GATE I")
        st.success("If you want you can go to Ground D")
        st.success("If you want you can go to Ground E")

    elif d >= 95 and e < 95 and f < 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE D -> GROUND D -> EXIT GATE G")
        st.success("If you want you can go to Ground E")
        st.success("If you want you can go to Ground F")

    elif d < 95 and e >= 95 and f < 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE E -> GROUND E -> EXIT GATE I")
        st.success("If you want you can go to Ground F")
        st.success("If you want you can go to Ground D")

    elif d < 95 and e < 95 and f < 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("ALL GROUNDS HAVE AVAILABILITY")
        st.info("GATE E -> GROUND E -> EXIT GATE I")

    elif d >= 95 and e >= 95 and f < 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE D -> GROUND D -> EXIT GATE G")
        st.success("If you want you can go to Ground F")

    elif d >= 95 and e < 95 and f >= 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE F -> GROUND F -> EXIT GATE I")
        st.success("If you want you can go to Ground E")

    elif d >= 95 and e < 95 and f < 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE D -> GROUND D -> EXIT GATE G")
        st.success("If you want you can go to Ground E")
        st.success("If you want you can go to Ground F")

    elif d < 95 and e >= 95 and f >= 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE E -> GROUND E -> EXIT GATE I")
        st.success("If you want you can go to Ground D")

    elif d < 95 and e >= 95 and f < 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE E -> GROUND E -> EXIT GATE I")
        st.success("If you want you can go to Ground F")
        st.success("If you want you can go to Ground D")

    elif d < 95 and e < 95 and f >= 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE F -> GROUND F -> EXIT GATE I")
        st.success("If you want you can go to Ground D")
        st.success("If you want you can go to Ground E")

    elif d < 95 and e < 95 and f < 450:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.warning("GROUNDS D, E AND F ARE NEAR CAPACITY")
        st.info("GATE E -> GROUND E -> EXIT GATE I")

    elif d >= e and d >= f:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE D -> GROUND D -> EXIT GATE G")

    elif e >= d and e >= f:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE E -> GROUND E -> EXIT GATE I")

    elif f >= d and f >= e:
        st.write("Occupied space in D = ", (d/100)*100, "%")
        st.write("Occupied space in E = ", (e/100)*100, "%")
        st.write("Occupied space in F = ", (f/500)*100, "%")
        st.success("GATE F -> GROUND F -> EXIT GATE I")
                           
