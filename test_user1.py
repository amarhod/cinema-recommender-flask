import database_handler as db


my_movies = [{'Actors': ' George Mackay, Dean-Charles Chapman, Richard Madden, Benedict '
            'Cumberbatch, Colin Firth, Mark Strong',
  'Date': ' 31 jan 2020',
  'Description': 'Två brittiska soldater får i uppdrag att ta sig långt in '
                 'bakom fiendelinjen för att varna ett regemente för ett '
                 'bakhåll som tyskarna planerar.',
  'Directors': ' Sam Mendes',
  'Genre': 'Drama, Krig',
  'Original_language': ' Engelska ',
  'Original_title': '1917',
  'Rating': 1},
 {'Actors': ' Christos Loulis, Ulrich Tukur',
  'Date': ' 10 jul 2020',
  'Description': 'I kölvattnet av börskraschen som startade i USA 2007 är '
                 'Grekland 2015 ett land på ruinens brant. Bakom lyckta dörrar '
                 'försöker landets finansminister Gianis Varoufakis rädda vad '
                 'som räddas kan genom hårda åtstramningsförslag. Allt för att ' 'Grekland inte ska knuffas ut ur EU och ned i en evig '
                 'skuldfälla...',
  'Directors': ' Costa-Gavras ',
  'Genre': 'Drama, Thriller',
  'Original_language': ' Franska,  Tyska,  Engelska,  Grekiska ',
  'Original_title': 'Adults in the Room',
  'Rating': -1},
 {'Actors': ' Will Smith, Martin Lawrence',
  'Date': ' 17 jan 2020',
  'Description': 'Poliserna Mike Lowrey och Marcus Burnett är tillbaka en '
                 'sista gång i "Bad Boys for Life".',
  'Directors': ' Adil El Arbi, Bilall Fallah',
  'Genre': 'Action, Komedi',
  'Original_language': ' Engelska ',
  'Original_title': 'Bad Boys for Life',
  'Rating': -1},
 {'Actors': ' Christian Bale, Michael Caine, Ken Watanabe, Liam Neeson, Katie '
            'Holmes, Gary Oldman, Rutger Hauer, Morgan Freeman',
  'Date': ' 24 jun 2020',
  'Description': 'Den ursprungliga berättelsen om hur Bruce Wayne bestämmer '
                 'sig för det goda och sitt alter ego Batman. Bruce Wayne ser '
                 'sina föräldrar mördas och vill hämnas på förövaren. Men - '
                 'han inser att hämnd inte löser något, utan blir i stället '
                 'Batman.',
  'Directors': ' Christopher Nolan',
  'Genre': 'Action, Äventyr',
  'Original_language': ' Engelska ',
  'Original_title': 'Batman Begins',
  'Rating': -1}]
def test_user(name="user1"):
  handler = db.DatabaseHandler(name)
  #handler.clear_table()
  handler.create_table(name)
  for movie in my_movies:
    handler.store(movie)
  handler.print_table()
  print(handler.get_rating("Bad Boys for Life"))
  handler.close_connection()


if __name__ == "__main__":
  test_user()
