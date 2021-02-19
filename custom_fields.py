import looker_sdk

sdk=looker_sdk.init31()

#USE CASE
#Customer has a dashboard that crashes their browser due to an overwhelming number of custom fields. 
#Because they can't render the dashboard in the UI, they need a way to see which tile(s) are overwhelming the browser and causing the issue.
#This script allows the user to see which dashboard elements have custom fields, the number of custom fields per element, and the definitions of those fields should they want to recreate/recover them.


#Enter the dashboard you want to inspect here:
dashboard='1247'

#Stores all dashboard element ids and queries for the given dashboard
elements=sdk.dashboard_dashboard_elements(dashboard_id=dashboard, fields='id, query')

#Gets the number of elements on the dashboard
number_of_elements=len(elements)

#Iterates over each dashboard element to find the custom fields. Notes queries without custom fields and text tiles. 
def custom_fields_of_elements():
    i=0
    while i<number_of_elements:
        element_id=elements[i].id
        if elements[i].query is not None:
            custom_fields_element=elements[i].query.dynamic_fields
            if custom_fields_element is not None:
                formatted_custom_fields=custom_fields_element[2:len(custom_fields_element)-2].split('},{')
                number_of_fields=len(formatted_custom_fields)
                j=0
                print(f"Dashboard element {element_id} has {number_of_fields} custom field(s):")
                while j<number_of_fields:
                    current_tile=formatted_custom_fields[j]
                    if current_tile[1:8]=="measure":
                        print(f"   Custom measure defined as:\n {current_tile}")
                    elif current_tile[1:10]=="dimension":
                        print(f"   Custom dimension defind as:\n {current_tile}")
                    else: print(f"   Table calculation defined as:\n {current_tile}")
                    j+=1
                print("\n")
            else: print(f"Dashboard element {element_id} has no custom fields.\n")
        else:
            print(f"Dashboard element {element_id} is a text tile with no custom fields.\n")
        i+=1

custom_fields_of_elements()
