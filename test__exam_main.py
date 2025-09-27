import main
from gameplay import Game, Player
from unittest.mock import mock_open, patch

def test_read_file_exists(): # Testa att highscore filen kan läsas så att spelaren kan se tidigare highscores
    game = Game("highscores.txt", 2, False, 0)
    mock_data = "Player:20\nDealer:20\n" #använder mock för att simulera filinnehåll
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = game.read_file("highscores.txt")
    assert result == ["Player:20", "Dealer:20"]

def test_read_file_not_existes():
    game = Game("highscores.txt", "", False, 0)
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = game.read_file("Highscore")
    assert result == []

def test_should_display_menu (capsys): # För att kolla att UI elementen visas för spelaren så att de vet vad de kan göra och så att de kan köra spelet
    start = Game("highscores.txt", "", False, 0)
    start.play_menu()
    captured = capsys.readouterr()
    assert "--- Choices ---" in captured.out
    assert "1. Roll the dice" in captured.out
    assert "2. Stop rolling" in captured.out
    
def test_should_bust_player(): # Testa så att spelarens score kan gå över 21 och att spelaren förlorar om den går över 21 så att spelet inte kan fortsätta om spelaren redan förlorat
    player = Player("Player", 0, 0, False)
    player.increaseScore(22)
    assert player.points == 22
    assert player.isBust == True

def test_should_Draw(capsys): # Test för att kolla om det blir oavgjort när spelaren och dealern har samma värde och att highscore inte uppdateras när det blir oavgjort
    player = Player("Player", 1, 0, False)
    dealer = Player("Dealer", 0, 0, False)
    game = Game("highscores.txt", 2, False, 0)
    player.increaseScore(21)
    dealer.increaseScore(21)
    game.roundEnd(player,dealer)
    captured = capsys.readouterr()
    assert player.points == 21
    assert dealer.points == 21
    assert "Draw!" in captured.out
    assert dealer.highscore == 0
    assert player.highscore == 1
       
        
        