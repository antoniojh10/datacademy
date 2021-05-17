def rock_paper_scissors(player_one, player_two):
    options_to_string = player_one + player_two

    initial_message = f"{player_one} vs {player_two}."

    player_one_wins = ["piedratijeras", "tijeraspapel", "papelpiedra"]
    player_two_wins = ["papeltijeras", "piedrapapel", "tijeraspiedra"]

    if options_to_string in player_one_wins:
        return initial_message + "El ganador es el jugador 1"
    if options_to_string in player_two_wins:
        return initial_message + "El ganador es el jugador 2"

    return initial_message + "Empate"


def get_player_option(player_num):
    options_dict = {1: "piedra", 2: "papel", 3: "tijeras"}

    while True:
        player_input = input(f"Escribe la opción del jugador {player_num}: ")

        try:
            assert player_input.isnumeric(), "Error. Escribe 1, 2, 3"
            player_input = int(player_input)
            assert player_input in [1, 2, 3], "Error. Escribe 1, 2, 3"
        except AssertionError as ae:
            print(ae)
        else:
            break

    return options_dict[player_input]


def run():
    print(
        f"""
        Escribe el número de la opción
            1 - Piedra
            2 - Papel
            3 - Tijeras
        """
    )

    player_one = get_player_option(1)
    player_two = get_player_option(2)

    winner = rock_paper_scissors(player_one, player_two)

    print(winner)


if __name__ == "__main__":
    run()
