import streamlit as st
import sqlalchemy
from sqlalchemy import text

engine = sqlalchemy.create_engine("postgresql://postgres:Iceburg1209@database-2.ct2imowo41nh.ap-south-1.rds.amazonaws.com:5432/postgres")

st.subheader(":blue[Population of each district]")
with engine.connect() as con:
    rs1 = con.execute(text("SELECT District, SUM(CASE WHEN Population='Nan' THEN 0 ELSE Population END) AS Total_Population FROM cenus_data GROUP BY District ORDER BY Total_Population DESC"))
    for row in rs1:
        st.write(row)

st.subheader(":orange[literate males and females of each district]")
with engine.connect() as con:
    rs2 = con.execute(text("SELECT District, SUM(CASE WHEN Literate_Male='Nan' THEN 0 ELSE Literate_Male END) AS Literate_Male, SUM(Literate_Female) AS Literate_Female FROM cenus_data  GROUP BY District"))
    for row1 in rs2:
        st.write(row1)

st.subheader(":green[percentage of workers in each district]")
with engine.connect() as con:
    rs3 = con.execute(text("SELECT District, (CASE WHEN Workers='Nan' THEN 0 ELSE Workers END) / (CASE WHEN Population='Nan' OR Population = 0 THEN 1 ELSE Population END) * 100 AS Percentage_of_Workers FROM public.cenus_data"))
    for rows in rs3:
        st.write(rows)

st.subheader(":green[households with access to LPG or PNG as cooking fuel]")
with engine.connect() as con:
    rs4 = con.execute(text("SELECT District, SUM(CASE WHEN LPG_or_PNG_Households='Nan' THEN 0 ELSE LPG_or_PNG_Households END) AS Total_Households_with_LPG_or_PNG FROM cenus_data GROUP BY District"))
    for i in rs4:
        st.write(i)

st.subheader(":blue[Religious composition of each district]")
with engine.connect() as con:
    rs5 = con.execute(text("SELECT District, SUM(CASE WHEN Hindus='Nan' THEN 0 ELSE Hindus END) AS Hindus, SUM(CASE WHEN Muslims='Nan' THEN 0 ELSE Muslims END) AS Muslims, SUM(CASE WHEN Christians='Nan' THEN 0 ELSE Christians END) AS Christians, SUM(CASE WHEN Sikhs='Nan' THEN 0 ELSE Sikhs END) AS Sikhs, SUM(CASE WHEN Buddhists='Nan' THEN 0 ELSE Buddhists END) AS Buddhists, SUM(CASE WHEN Jains='Nan' THEN 0 ELSE Jains END) AS Jains, SUM(CASE WHEN Others_Religions='Nan' THEN 0 ELSE Others_Religions END) AS Others_Religions, SUM(CASE WHEN Religion_Not_Stated='Nan' THEN 0 ELSE Religion_Not_Stated END) AS Religion_Not_Stated FROM cenus_data GROUP BY District"))
    for i in rs5:
        st.write(i)

st.subheader(":blue[households with internet access in each district]")
with engine.connect() as con:
    rs9 = con.execute(text("SELECT District, SUM(CASE WHEN Households_with_Internet='Nan' THEN 0 ELSE Households_with_Internet END) AS Total_Households_with_Internet FROM cenus_data GROUP BY District"))
    for row in rs9:
        st.write(row)

st.subheader(":blue[education attainment in each district]")
with engine.connect() as con:
    rs9 = con.execute(text("SELECT District, SUM(CASE WHEN Below_Primary_Education='Nan' THEN 0 ELSE Below_Primary_Education END) AS Below_Primary, SUM(CASE WHEN Primary_Education='Nan' THEN 0 ELSE Primary_Education END) AS Primary, SUM(CASE WHEN Middle_Education='Nan' THEN 0 ELSE Middle_Education END) AS Middle, SUM(CASE WHEN Secondary_Education='Nan' THEN 0 ELSE Secondary_Education END) AS Secondary, SUM(CASE WHEN Higher_Education='Nan' THEN 0 ELSE Higher_Education END) AS Higher, SUM(CASE WHEN Graduate_Education='Nan' THEN 0 ELSE Graduate_Education END) AS Graduate, SUM(CASE WHEN Other_Education='Nan' THEN 0 ELSE Other_Education END) AS Other, SUM(CASE WHEN Literate_Education='Nan' THEN 0 ELSE Literate_Education END) AS Literate, SUM(CASE WHEN Illiterate_Education='Nan' THEN 0 ELSE Illiterate_Education END) AS Illiterate, SUM(CASE WHEN Total_Education='Nan' THEN 0 ELSE Total_Education END) AS Total FROM cenus_data GROUP BY District"))
    for row in rs9:
        st.write(row)

st.subheader(":red[households with various transportation modes]")
with engine.connect() as con:
     res10 = con.execute(text("SELECT District,SUM(CASE WHEN Households_with_Bicycle='Nan' THEN 0 ELSE Households_with_Bicycle END) AS Bicycle,SUM(CASE WHEN Households_with_Car_Jeep_Van='Nan' THEN 0 ELSE Households_with_Car_Jeep_Van END) AS Car_Jeep_Van, SUM(CASE WHEN Households_with_Radio_Transistor='Nan' THEN 0 ELSE Households_with_Radio_Transistor END) AS Radio_Transistor,SUM(CASE WHEN Households_with_Television='Nan' THEN 0 ELSE Households_with_Television END) AS Television,SUM(CASE WHEN Households_with_Scooter_Motorcycle_Moped='Nan' THEN 0 ELSE Households_with_Scooter_Motorcycle_Moped END) AS Scooter_Motorcycle_Moped,SUM(CASE WHEN Households_with_Telephone_Mobile_Phone_Landline_only='Nan' THEN 0 ELSE Households_with_Telephone_Mobile_Phone_Landline_only END) AS Telephone_Mobile_Phone_Landline_only,SUM(CASE WHEN Households_with_Telephone_Mobile_Phone_Mobile_only='Nan' THEN 0 ELSE Households_with_Telephone_Mobile_Phone_Mobile_only END) AS Telephone_Mobile_Phone_Mobile_only,SUM(CASE WHEN Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car='Nan' THEN 0 ELSE Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car END) AS TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car FROM cenus_data GROUP BY District"))
     for row in res10:
         st.write(row)

st.subheader(":red[condition of occupied census houses]")
with engine.connect() as con:
    res11 = con.execute(text("SELECT District,SUM(CASE WHEN Condition_of_occupied_census_houses_Dilapidated_Households='Nan' THEN 0 ELSE Condition_of_occupied_census_houses_Dilapidated_Households END) AS Dilapidated_Households,SUM(CASE WHEN Households_with_separate_kitchen_Cooking_inside_house='Nan' THEN 0 ELSE Households_with_separate_kitchen_Cooking_inside_house END) AS Separate_Kitchen,SUM(CASE WHEN Having_bathing_facility_Total_Households='Nan' THEN 0 ELSE Having_bathing_facility_Total_Households END) AS Bathing_Facility,SUM(CASE WHEN Having_latrine_facility_within_the_premises_Total_Households='Nan' THEN 0 ELSE Having_latrine_facility_within_the_premises_Total_Households END) AS Latrine_Facility FROM cenus_data GROUP BY District"))
    for row in res11:
        st.write(row)

st.subheader(":green[household size distribution in each district]")
with engine.connect() as con:
    res12 = con.execute(text("SELECT District,SUM(CASE WHEN Household_size_1_person_Households='Nan' THEN 0 ELSE Household_size_1_person_Households END) AS Household_size_1_Person, SUM(CASE WHEN Household_size_2_persons_Households='Nan' THEN 0 ELSE Household_size_2_persons_Households END) AS Household_size_2_Persons,SUM(CASE WHEN Household_size_3_to_5_persons_Households='Nan' THEN 0 ELSE Household_size_3_to_5_persons_Households END) AS Household_size_3_5_Persons FROM  cenus_data GROUP BY  District"))
    for i in res12:
     st.write(i)

st.subheader(":blue[total no.of households in each state]")
with engine.connect() as con:
    res13 = con.execute(text("SELECT State_UT,SUM(CASE WHEN Households='Nan' THEN 0 ELSE Households END) AS Total_Households FROM cenus_data GROUP BY State_UT "))
    for i in res13:
     st.write(i)

st.subheader(":green[households having access to latrine in each state]")
with engine.connect() as con:
    res14 = con.execute(text("SELECT State_UT,SUM(CASE WHEN Having_latrine_facility_within_the_premises_Total_Households='Nan' THEN 0 ELSE Having_latrine_facility_within_the_premises_Total_Households END) AS Latrine_Facility_within_the_premises FROM  cenus_data GROUP BY State_UT "))
    for i in res14:
     st.write(i)

st.subheader(":green[average household size in each state]")
with engine.connect() as con:
    res15 = con.execute(text("SELECT State_UT,AVG(CASE WHEN Households='Nan' THEN 0 ELSE Households END) AS Total_Households FROM cenus_data GROUP BY State_UT"))
    for i in res15:
     st.write(i)

st.subheader(":red[own households vs rented households in each state]")
with engine.connect() as con:
    res16 = con.execute(text("SELECT State_UT,SUM(CASE WHEN Ownership_Owned_Households='Nan' THEN 0 ELSE Ownership_Owned_Households END) AS Owned_Households,SUM(CASE WHEN Ownership_Rented_Households='Nan' THEN 0 ELSE Ownership_Rented_Households END) AS Rented_Households FROM  cenus_data GROUP BY State_UT"))
    for i in res16:
     st.write(i)

st.subheader(":red[distribution of different latrine types]")
with engine.connect() as con:
    res17 = con.execute(text("SELECT State_UT,SUM(CASE WHEN Type_of_latrine_facility_Pit_latrine_Households='Nan' THEN 0 ELSE Type_of_latrine_facility_Pit_latrine_Households END) AS Pit_Latrine,SUM(CASE WHEN Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households='Nan' THEN 0 ELSE Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households END) AS Flush_Latrine,SUM(CASE WHEN Type_of_latrine_facility_Other_latrine_Households='Nan' THEN 0 ELSE Type_of_latrine_facility_Other_latrine_Households END) AS Other_Latrine FROM  cenus_data GROUP BY State_UT"))
    for i in res17:
     st.write(i)

st.subheader(":red[Access to drinking water near premises in each state]")
with engine.connect() as con:
    res18 = con.execute(text("SELECT State_UT,SUM(CASE WHEN location_of_drinking_water_source_near_the_premises_households='Nan' THEN 0 ELSE location_of_drinking_water_source_near_the_premises_households END) AS Access_to_Drinking_near_Premises FROM  cenus_data GROUP BY  State_UT"))
    for i in res18:
     st.write(i)

st.subheader(":red[Income distribution in each state based on power parity]")
with engine.connect() as con:
    res19 = con.execute(text("SELECT State_UT,AVG(CASE WHEN total_power_parity='Nan' THEN 0 ELSE total_power_parity END) AS Avg_Power_parity FROM  cenus_data GROUP BY State_UT"))
    for i in res19:
     st.write(i)

st.subheader(":blue[percent of married couple with different household sizes]")
with engine.connect() as con:
    res20 = con.execute(text("SELECT State_UT,((CASE WHEN Married_couples_1_Households='Nan' THEN 0 ELSE Married_couples_1_Households END) / NULLIF((CASE WHEN Married_couples_1_Households='Nan' THEN 0 ELSE Married_couples_1_Households END) + (CASE WHEN Married_couples_2_Households='Nan' THEN 0 ELSE Married_couples_2_Households END) + (CASE WHEN Married_couples_3_Households='Nan' THEN 0 ELSE Married_couples_3_Households END) + (CASE WHEN Married_couples_3_or_more_Households='Nan' THEN 0 ELSE Married_couples_3_or_more_Households END), 0)) * 100 AS Percent_Married_1_Person,((CASE WHEN Married_couples_2_Households='Nan' THEN 0 ELSE Married_couples_2_Households END) / NULLIF((CASE WHEN Married_couples_1_Households='Nan' THEN 0 ELSE Married_couples_1_Households END) + (CASE WHEN Married_couples_2_Households='Nan' THEN 0 ELSE Married_couples_2_Households END) + (CASE WHEN Married_couples_3_Households='Nan' THEN 0 ELSE Married_couples_3_Households END) + (CASE WHEN Married_couples_3_or_more_Households='Nan' THEN 0 ELSE Married_couples_3_or_more_Households END), 0)) * 100 AS Percent_Married_2_Persons,((CASE WHEN Married_couples_3_Households='Nan' THEN 0 ELSE Married_couples_3_Households END) / NULLIF((CASE WHEN Married_couples_1_Households='Nan' THEN 0 ELSE Married_couples_1_Households END) + (CASE WHEN Married_couples_2_Households='Nan' THEN 0 ELSE Married_couples_2_Households END) + (CASE WHEN Married_couples_3_Households='Nan' THEN 0 ELSE Married_couples_3_Households END) + (CASE WHEN Married_couples_3_or_more_Households='Nan' THEN 0 ELSE Married_couples_3_or_more_Households END), 0)) * 100 AS Percent_Married_3_Persons,((CASE WHEN Married_couples_3_or_more_Households='Nan' THEN 0 ELSE Married_couples_3_or_more_Households END) / NULLIF((CASE WHEN Married_couples_1_Households='Nan' THEN 0 ELSE Married_couples_1_Households END) + (CASE WHEN Married_couples_2_Households='Nan' THEN 0 ELSE Married_couples_2_Households END) + (CASE WHEN Married_couples_3_Households='Nan' THEN 0 ELSE Married_couples_3_Households END) + (CASE WHEN Married_couples_3_or_more_Households='Nan' THEN 0 ELSE Married_couples_3_or_more_Households END), 0)) * 100 AS Percent_Married_3_or_More_Persons FROM cenus_data"))
    for i in res20:
     st.write(i)

st.subheader(":blue[below poverty line based on power parity in each state]")
with engine.connect() as con:
    res21 = con.execute(text("SELECT State_UT,SUM(CASE WHEN power_parity_less_than_rs_45000='Nan' THEN 0 ELSE power_parity_less_than_rs_45000 END) AS households_below_poverty_line  FROM  cenus_data GROUP BY State_UT"))
    for i in res21:
     st.write(i)

st.subheader(":blue[percent of literacy rate in each state]")
with engine.connect() as con:
    res22 = con.execute(text("SELECT State_UT,AVG(CASE WHEN literate='Nan' THEN 0 ELSE literate END) * 100 AS literacy_percent FROM cenus_data GROUP BY  State_UT"))
    for i in res22:
     st.write(i)
