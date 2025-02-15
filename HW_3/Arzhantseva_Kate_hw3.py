class cyan_solute:
    def __init__(self, concentration: float = 0, purity_perc: float = 0 , solute: str = "NaCN"):
        self.__concentration = concentration
        self.__purity_perc = purity_perc
        self.__solute = solute

    def get_purity_perc(self):
        return self._purity_perc

    def get_concentration(self):
        return self._concentration
    
    def get_solute(self):
        return self._solute
    
    def set_purity_perc(self, purity_perc):
        self._purity_perc = purity_perc

    def set_concentration(self, concentration):
        self._concentration = concentration
    
    def set_solute(self, solute):
        self._solute = solute 

    #Дальше геттеры и сеттеры прописывать не буду они делаются ровно так же

    def check_purity(self):
        return self.get_purity_perc() < 1

    def check_conc(self):
        return self.get_concentration() <= 100 and self.get_concentration() >= 50

class catalyst:
    def __init__(self, concentration: float, purity: float, type: str = "Fe(SO4)3"):
        self._catal: str = 'Fe(SO4)3'
        self._concentration: float
        self._purity: float

    def set_atribute(self):
        pass 

    def get_atribute(self):
        pass


class clean_filter:
    def __init__(self, perc_wear: float = 0, type: str = 'A', firm: str = ''):
        self._perc_wear = perc_wear
        self._type = type
        self._firm = firm

    def set_atribute(self):
        pass 

    def get_atribute(self):
        pass

    def check_wear(self):
        return self.get_perc_wear() <= 80 

class batch:
    def __init__(self, material: str, fraction: float, solute : cyan_solute, catalyst: catalyst, filter: clean_filter):
        self.__material = material
        self.__fraction = fraction
        self.__solute = solute
        self.__catalyst = catalyst
        self.__filter = filter

    def set_atribute(self):
        pass 

    def get_atribute(self):
        pass

    def cyanidation(self):
        if self.get_solute().check_purity() == 1 and self.get_solute().check_conc() == 1:
            pass  # Implementation cyanidation process and returning a new batch
    
    def catalisation(self):
        pass  # Implementation catalisation process and returning a new batch

    def clean(self):
        if self.get_filter().check_wear() == 1:
            batch.set_fraction(self.get_material())
            used_wear = lambda solute, catalyst, filter: #Некоторая функция показывает как влиея чистка на износ фильтра
            new_filter = self.get_filter().set_wear(used_wear(self.get_solute(), self.get_catalyst(), self.get_filter()))
            self.set_filter(new_filter)
            pass  # Clean and returning a new batch


class crushing_corp:
    def __init__(self, material : str):
        self.__material = material

    def set_atribute(self):
        pass 

    def get_atribute(self):
        pass

    def change_fraction(self, batch: batch):
        if self.check_material() == 1:
            fraction = lambda x: #Некоторая функция, где x это материал
            batch.set_fraction(self.get_material())
        else: 
            raise ValueError(f"Неподходящий материал")

    def check_material(self):
        '''
        Checked if the material is apropriate for fraction
        '''
        return bool