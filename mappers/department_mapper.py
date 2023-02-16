from models.Deparment import Deparment


def department_mapper(data: dict):
    return Deparment(       
        id=data['id'],
        name=data['name'],
        description=data['descripton'],
        municipalities=data['municipalities'],
        surface=data['surface'],
        population=data['population'],
        phone_prefix=data['phonePrefix'],
    )


dict = [
    {
        "id": 9,
        "name": "Caquetá",
        "description": "Caquetá es uno de los treinta y dos departamentos que, junto con Bogotá, Distrito Capital, forman la República de Colombia. Su capital es Florencia. Está ubicado al sur del país, en la región Amazonia, limitando al norte con Meta y Guaviare, al noreste con Vaupés, al sur con Amazonas y Putumayo, y al oeste con Cauca y Huila. Con 88 965 km² es el tercer departamento más extenso —por detrás de Amazonas y Vichada—. Todos sus municipios forman parte de los territorios focalizados",
        "cityCapitalId": 364,
        "municipalities": 16,
        "surface": 88965,
        "population": 419275,
        "phonePrefix": "8",
        "countryId": 1,
        "cityCapital": None,
        "country": None,
        "cities": None
    },
    {
        "id": 10,
        "name": "Casanare",
        "description": "Casanare es uno de los treinta y dos departamentos que, junto con Bogotá, Distrito Capital, forman la República de Colombia. Su capital es Yopal. Está ubicado en la región Orinoquía, limitando al norte con Arauca, al este con Vichada, al sur con Meta y al oeste con Boyacá. Con 44 490 km² es el décimo departamento más extenso —por detrás de Amazonas, Vichada",
        "cityCapitalId": 380,
        "municipalities": 19,
        "surface": 44640,
        "population": 442068,
        "phonePrefix": "8",
        "countryId": 1,
        "cityCapital": None,
        "country": None,
        "cities": None
    },
    {
        "id": 11,
        "name": "Cauca",
        "description": "Cauca es uno de los treinta y dos departamentos que, junto al Distrito Capital de Bogotá, conforman la República de Colombia. Su capital y ciudad más poblada es Popayán. Está ubicado al suroccidente del país entre las regiones andina y pacífica, limitando al norte con Valle del Cauca y Tolima, al oriente con Huila, al suroriente con Caquetá, al sur con Putumayo y Nariño, y al noroccidente con el océano Pacífico",
        "cityCapitalId": 399,
        "municipalities": 41,
        "surface": 29308,
        "population": 1516018,
        "phonePrefix": "2",
        "countryId": 1,
        "cityCapital": None,
        "country": None,
        "cities": None
    },
]
