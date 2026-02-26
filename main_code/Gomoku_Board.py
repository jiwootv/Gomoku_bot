import json

SIZE = 15


class GomokuBoard:
	def __init__(self, board_list):
		# 보드 리스트는 2차원의 15*15 리스트이다.
		# 예: [ [0, 1, 0, 0, 0... ]
		# 흑은 1이고, 백은 2이다.
		self.board = board_list

	def edit_board(self, x, y, type):
		self.board[y][x] = type

	def get_nowboard(self):
		return self.board

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

	def setmarker(self):
		markers = []
		for x in range(SIZE):
			for y in range(SIZE):
				if self.board[y][x] == 1 or self.board[y][x] == 2:  # 흑돌또는 백돌이라면
					# 이제 한칸 주위를 마커로 둘@러싸 봅시다.
					"""
					방향: 
					* * *
					* / *
					* * *
					"""
					print("______")
					print(f"TYPE: {self.board[y][x]} / Position: ({x+1},{y+1})")
					direction = [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]
					for dr in direction:
						x1 = x + dr[0]
						y1 = y + dr[1]
						if x1 < 0:
							x1 = 0
						if x1 > SIZE - 1:
							x1 = SIZE
						if y1 < 0:
							y1 = 0
						if y1 > SIZE - 1:
							y1 = SIZE
						if self.board[y1][x1] != 1 and self.board[y1][x1] != 2:  # 흑돌 또는 백돌이 아니면:
							print(f"Pos: ({x1+1},{y1+1}) / {self.board[y1][x1]}")
							markers.append({"x": x1, "y": y1, "type": self.board[y1][x1]})
		for _ in markers:
			print(_)
		return markers