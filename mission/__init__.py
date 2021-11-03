import lxml.etree as ET
import xmltodict
import csv

MISSION_FIELDS = ['Horodate_debut_mission','Nbre_Mesures','Nbre_Mesures_RAPP','Nbre_Mesures_ELOI',\
                  'Nbre_Infractions','Nbre_Infractions_RAPP','Nbre_Infractions_ELOI','Duree_mission',\
                  'Horodate_fin_mission','ID_Miss','Mode_Controle']

MESURES_FIELDS = ['Horodate', 'PositionGeoLtt', 'PositionGeoLgt','Infraction','Porteur','Cible',\
                    'Mesure','Direction','Limite']

class Mission:
    all_mission = []

    def __init__(self, file_path):
        self._file_path = file_path
        self._list_mesures = self.extract_mesures_fields()
        self._list_mission = self.extract_mission_fields()
        self._id_mission, self._nb_mesures, self._nb_infractions  = self.extract_details()
        self.__class__.all_mission.append(self)
        
        
    def extract_details(self):
        dom = ET.parse(self._file_path)
        return dom.find(".//ID_Miss").text, int(dom.find(".//Nbre_Mesures").text), int(dom.find(".//Nbre_Infractions").text)
    
    def extract_mission_fields(self):    
        dom = ET.parse(self._file_path) 
        mesure_et = dom.findall('.//Mission')
        
        list_mesures = []
        
        for mesure in mesure_et:
            values = [mesure.find(f).text for f in MISSION_FIELDS]
            list_mesures.append(values)
        
        return list_mesures

    def extract_mesures_fields(self):
        dom = ET.parse(self._file_path) 
        mesure_et = dom.findall('.//Vitesse')
        mission_id = dom.find(".//ID_Miss")
        
        list_mesures = []
        
        for mesure in mesure_et:
            values = [mesure.find(f).text for f in MESURES_FIELDS]
            values.insert(0, mission_id.text)
            list_mesures.append(values)
        
        return list_mesures

    

    @classmethod
    def total_nb_mesures(cls):
        total = 0
        for m in cls.all_mission:
            total = total + m._nb_mesures
        return total

    @classmethod
    def total_nb_infractions(cls):
        total = 0
        for m in cls.all_mission:
            total = total + m._nb_infractions
        return total
