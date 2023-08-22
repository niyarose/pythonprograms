from json import load 
with open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\restCountries\\rest.json",encoding="UTF-8") as f:
    data=load(f)
    

# print(len(data))

#print all country name 


# country_names=[u.get("name") for u in data]
# print(country_names)


#print all region names

# region_name={r.get("region") for r in data}    # set {} to remove duplication
# print(region_name)


# print asian country names

# asian_country=[a.get("name") for a in data if a.get("region")=="Asia"]
# print(asian_country)



# print population of afganistan


# pop_afganistan=[p.get("population") for p in data if p.get("name")=="Afghanistan"]
# print(pop_afganistan)



# print indian boards

# indian_boards=[p.get("borders") for p in data if p.get("name")=="India"][0]
# print(indian_boards)

# country_boarders_name=[p.get("name") for p in data if p.get("alpha3Code") in indian_boards ]
# print(country_boarders_name)

# print currency code 
# currency_code={c.get("cuurencies") for c in data if c.get("name")=="India"}
# print(currency_code)

# country with highest population 
high_pop=[for p in data if p.get("population")]
