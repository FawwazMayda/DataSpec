from abc import ABC, abstractmethod
import random
import csv

class FieldSpec(ABC):
    def __init__(self,field_name):
        super().__init__()
        self.field_name = field_name
        print(self.field_name)
    @abstractmethod
    def get_field_value():
        pass

class DiscreteField(FieldSpec):
    def __init__(self,field_name,field):
        super().__init__(field_name)
        self.field = field

    def get_field_value(self):
        random_idx = random.randint(0, len(self.field)-1)
        return self.field[random_idx]

class ContinousField(FieldSpec):
    def __init__(self,field_name,lower_bound,upper_bound):
        super().__init__(field_name)
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    def get_field_value(self):
        return random.randint(self.lower_bound, self.upper_bound)

class DatasetSpec():
    def __init__(self,dataset_name,count):
        self.dataset_name = dataset_name
        self.count = count
        self.field_spec_list = []
    
    def add_field(self,f):
        self.field_spec_list.append(f)

    def write_data(self):
        field_names = [f.field_name for f in self.field_spec_list]
        with open(f"{self.dataset_name}.csv","w") as f:
            writer = csv.DictWriter(f, field_names)
            writer.writeheader()
            for i in range(self.count):
                temp_dict = {f.field_name:f.get_field_value() for f in self.field_spec_list}
                writer.writerow(temp_dict)
        f.close()

d1 = DiscreteField("SIM",["SIM A","SIM B"])
d2 = ContinousField("Tahun",2011,2015)

ds = DatasetSpec("coba", 100)
ds.add_field(d1)
ds.add_field(d2)
ds.write_data()