class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Essa posição já está ocupada. Tente novamente.")

    def check_winner(self):
        # Verifica linhas
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Verifica colunas
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Verifica diagonais
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def play(self):
        print("Bem-vindo ao Jogo da Velha!")
        print("Para fazer uma jogada, digite as coordenadas (linha e coluna) da posição desejada.")
        print("Exemplo: 0 0 representa a primeira posição na primeira linha.")
        print()

        while True:
            self.print_board()

            row = int(input("Digite a linha da sua jogada (0, 1 ou 2): "))
            col = int(input("Digite a coluna da sua jogada (0, 1 ou 2): "))

            self.make_move(row, col)
            winner = self.check_winner()

            if winner:
                print()
                self.print_board()
                print(f"Parabéns! O jogador {winner} venceu!")
                break
            elif self.is_board_full():
                print()
                self.print_board()
                print("Empate! O jogo terminou sem vencedor.")
                break

            print()

game = TicTacToe()
game.play()
