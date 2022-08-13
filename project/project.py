import requests
import json




def main():
    
        
        name = check_name() 
        num = check_num()           
        calories, protein, fat = food_amt(num, data)
        print(f"Nurtrition: {name}\nQuatity: {num} grams\nCalories: {calories}\nProtein: {protein}g\nFat: {fat} \n")      
       
            
                           

def check_name():
    while True:
         name = input("Enter Food: ").strip()
         global data
         data = search_food(name)
         if data == None:
             continue
         return name.capitalize()    

    
 

def check_num():
    while True:
         try:
             num = int(input("How many food do you want? ").strip())
             if num <= 0:
                raise ValueError
         except ValueError:
            continue 
         else:
            return int(num)  
             
         
       
def search_food(name):
    url = 'https://calorieninjas.p.rapidapi.com/v1/nutrition'
    querystring = {"query": name}
    headers = {
    'X-RapidAPI-Key': 'dbc8aa7adfmshee67f7c147807d5p15fa10jsn626149821f72',
    'X-RapidAPI-Host': 'calorieninjas.p.rapidapi.com'
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = json.loads(response.text)
    if len(response["items"]) > 0:
        calories = response["items"][0]["calories"]
        protein = response["items"][0]["protein_g"]
        fat = response["items"][0]["fat_total_g"]
        return {"calories": calories, "protein": protein, "fat":fat}
    return None    
        


   
def food_amt(num, data):
    calories = round(data["calories"] / 100 * num, 1)
    protein = round(data["protein"] / 100 * num, 1)
    fat = round(data["fat"] / 100 * num, 1) 
    
    return calories, protein, fat
    
        

if __name__ == "__main__":
    main()