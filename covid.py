#pip install covid

from covid import Covid
covid=Covid()
india=covid.get_status_by_country_name("india")
print(india)
