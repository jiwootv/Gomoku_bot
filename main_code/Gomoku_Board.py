import json


SIZE = 15
class GomokuBoard:
	def __init__(self, board_list):
		# 보드 리스트는 2차원의 15*15 리스트이다.
		# 예: [ [0, 1, 0, 0, 0... ]
		# 흑은 1이고, 백은 2이다.
		self.board = board_list

	def edit_board(self, x, y, type): self.board[y][x] = type
	def get_nowboard(self): return self.board

	def get_now_lines(self):
		for y in self.board:
			for x in y:
				print(x, end=" ")
			print()

	def save_as(self, file_name):
		path = "Return"
		import json

		suction = {}
		for x in range(SIZE):
			for y in range(SIZE):
				suction[f"{x};{y}"] = self.board[y][x]

		data = {
			"size": SIZE,
			"data":
				suction

		}
		with open(path + "/" + file_name + ".json", "w", encoding="utf-8") as f:
			json.dump(data, f, ensure_ascii=False, indent=2)