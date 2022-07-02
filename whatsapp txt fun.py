class Chat:
	def __init__(self, path):
		self.path = path
		self.chat = self.processChat()
		self.users = self.distinctUser()

	def processChat(self):
		chat = []
		with open(self.path, "r", encoding="utf-8") as tf:
			raw = tf.readlines()

		i = 0
		while i < len(raw):
			if raw[i][:10].__contains__("/") and raw[i].__contains__(" - "):
				chat.append(raw[i])
			else:
				chat[-1] += raw[i]
			i += 1

		if chat[0].__contains__("Messages to this chat and calls are now secured with end-to-end encryption. Tap for more info."):
			chat.pop(0)

		return chat

	def distinctUser(self):
		users = []
		for i in self.chat:
			username = ((i.split(" - ")[1]).split(":")[0])
			if username not in users:
				users.append(username)
		return users

	def compare(self):
		# find no of chats of each user
		userdict = dict.fromkeys(self.users, 0)
		for i in self.chat:
			for j in userdict:
				if i.__contains__(j+":"):
					userdict[j] += 1

		return userdict

	def daycount(self):
		# find accumulate day count of chat
		currdate = ""
		count = 0
		for i in self.chat:
			if i[:10] != currdate:
				currdate = i[:10]
				count += 1
		return count

	def distinctDate(self):
		# find no of chats started each day for each user
		currdate = ""
		userdict = dict.fromkeys(self.users, 0)
		for i in self.chat:
			if i[:10] != currdate:
				currdate = i[:10]
				for j in userdict:
					if i.__contains__(j+":"):
						userdict[j] += 1
		return userdict

	def longestChat(self):
		# find longest message
		maxLen = 0
		longestChat = ""
		for i in self.chat:
			if len(i) > maxLen:
				maxLen = len(i)
				longestChat = i
		return longestChat


def main():
	path = "Example.txt"
	chat = Chat(path)
	print(chat.compare())
	print(chat.daycount())
	print(chat.distinctDate())
	print(chat.longestChat())


if __name__ == "__main__":
	main()