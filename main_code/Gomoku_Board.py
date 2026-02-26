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

	def get_lines(self, x, y):
		"""
		입력 좌표 (x,y)의 돌(1/2)을 기준으로
		4개 축(가로/세로/대각/역대각)에서 이어진 연속 돌 길이를 계산해서
		3줄/4줄/5줄+ 개수를 반환한다.

		반환 예:
		{
			"type": 1,
			"lengths": {"h": 3, "v": 1, "d": 4, "ad": 2},
			"counts": {3: 1, 4: 1, 5: 0}
		}
		"""
		if not (0 <= x < SIZE and 0 <= y < SIZE):
			return None

		stone = self.board[y][x]
		if stone not in (1, 2):
			# 빈칸/마커면 라인 의미 없음
			return None

		def count_dir(dx, dy):
			"""(x,y)에서 (dx,dy) 방향으로 같은 돌이 몇 개 연속인지"""
			c = 0
			cx = x + dx
			cy = y + dy
			while 0 <= cx < SIZE and 0 <= cy < SIZE and self.board[cy][cx] == stone:
				c += 1
				cx += dx
				cy += dy
			return c

		# 4축 정의: (정방향, 역방향)
		axes = {
			"h": ((1, 0), (-1, 0)),		# 가로
			"v": ((0, 1), (0, -1)),		# 세로
			"d": ((1, 1), (-1, -1)),	# 대각 \
			"ad": ((1, -1), (-1, 1))	# 역대각 /
		}

		lengths = {}
		counts = {3: 0, 4: 0, 5: 0}	# 5는 "5 이상"으로 취급

		for name, (p, n) in axes.items():
			pos = count_dir(p[0], p[1])
			neg = count_dir(n[0], n[1])
			length = 1 + pos + neg
			lengths[name] = length

			if length >= 5:
				counts[5] += 1
			elif length == 4:
				counts[4] += 1
			elif length == 3:
				counts[3] += 1

		# 보기 좋게 출력도 해주고 싶으면:
		print(f"Stone type: {stone} at ({x},{y})")
		print("Axis lengths:", lengths)
		print("Counts: 3-in-row =", counts[3], ", 4-in-row =", counts[4], ", 5+-in-row =", counts[5])

		return {
			"type": stone,
			"lengths": lengths,
			"counts": counts
		}

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
					direction = [[-1, 1], [0, 1], [1, 1], [1,0], [1, -1], [0, -1], [-1, -1], [-1, 0]]
					for dr in direction:
						x1 = x + dr[0]
						y1 = y + dr[1]
						print(x1+1, y1+1)
						if x1 < 0:
							x1 = 0
						if x1 >= SIZE:
							x1 = SIZE-1
						if y1 < 0:
							y1 = 0
						if y1+1 >= SIZE:
							y1 = SIZE-1
						print(x1 + 1, y1 + 1)
						if self.board[y1][x1] != 1 and self.board[y1][x1] != 2:  # 흑돌 또는 백돌이 아니면:

							try:
								print(f"Pos: ({x1+1},{y1+1}) / {self.board[y1][x1]}")
								markers.append({"x": x1, "y": y1, "type": self.board[y1][x1]})
							except:
								print("ERROR")
		for _ in markers:
			print(_)
		return markers