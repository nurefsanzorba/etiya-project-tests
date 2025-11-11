import json
import os
from typing import List, Dict, Any

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # dosyanın tam konumunu alır, iki üst dizine çıkar(os.path.dirname) klasör kök dizini olarak belirler yani(etiya-project-test dizini)
DATA_PATH = os.path.join(BASE_DIR, 'data', 'login_data.json') # etiya-project-test dizini içinde data klasöründeki login_data.json dosyasını açar


def get_login_scenarios(key_name: str) -> List[Dict[str, Any]]: # verilen string key değerine göre json içindeki verileri temelde bir listeye dönüştürür ve liste içindeki veriler json tipinde yani pythondaki dict yapısında belirtilmeli 
                                                                # Dict yapısında key ve value yapıları mevcut key değerimiz string, value değerimiz herhangi bir tipte değişken olabilir(any)
    
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            all_data = json.load(f)
            
    except FileNotFoundError:
        print(f"HATA: {DATA_PATH} dosyası bulunamadı. Lütfen yolu kontrol edin.")
        return []
    except json.JSONDecodeError:
        print(f"HATA: JSON formatı geçersiz.")
        return []

   
    return all_data.get(key_name, [])


"""
if __name__ == '__main__':
    ui_data = get_login_scenarios('ui_validations')
    
    print("\n--- UI Validasyon Verileri ---")
    #print(ui_data)
    for i in ui_data:
        if(i['scenario_name'] == "Login Buton Status (Less than 2 character entered to the both input areas)"):
            print(i)
"""
