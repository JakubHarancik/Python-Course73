def country_capital(country_name, capital_name):
    """ Return a formatted name like Czech Republic, Prague  """
    return f"{country_name},{ capital_name}"

formatted_name = country_capital('Germany','Berlin')
print(formatted_name)