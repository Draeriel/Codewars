idioma = {'english': 'Welcome', 'czech': 'Vitejte', 'danish': 'Velkomst','dutch': 'Welkom', 'estonian': 'Tere tulemast', 'finnish': 'Tervetuloa','flemish': 'Welgekomen', 'french': 'Bienvenue', 'german': 'Willkommen', 'irish': 'Failte', 'italian': 'Benvenuto', 'latvian': 'Gaidits', 'lithuanian': 'Laukiamas', 'polish': 'Witamy', 'spanish': 'Bienvenido', 'swedish': 'Valkommen', 'welsh': 'Croeso'}
def greet(language):
  if language in idioma:
    return idioma[language]
  if language not in idioma:
    return 'Welcome'