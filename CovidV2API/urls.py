BASE_URL = 'https://coronavirus-tracker-api.herokuapp.com/v2'

latest = BASE_URL + '/latest'
sources = BASE_URL + '/sources'
locations = BASE_URL + '/locations'
locations_by_id = lambda id: BASE_URL + f'/locations/{id}'
