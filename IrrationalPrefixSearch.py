import sys

class IrrationalPrefixSearch(object):

	def __init__(self, source):
		self.source = open(source, "r")
		self.digits = ["0","1","2","3","4","5","6","7","8","9"]

	def __del__(self):
		self.source.close()

	def find_longest(self, t, n):
		"""Find the longest prefix of target within the first n digits
		   returns index of result"""
		result = None
		best = 0
		offset = 0
		with open(t,'r') as target:
			first = target.read(1)
			first_loc = 0
			while first not in self.digits:
				first = self.source.read(1)
				first_loc += 1
			curr_off = 0
			for i in xrange(n):
				curr = self.source.read(1)
				while curr and curr not in self.digits:
					curr = self.source.read(1)
					curr_off+=1
				if not curr:
					print "File ended at digit "+str(i+1)
					break
				if curr == first:
					location = i
					length = 1
					t_curr = target.read(1)
					while t_curr not in self.digits:
						t_curr = target.read(1)
					while (self.source.read(1) == t_curr and i+length < n):
						length += 1
						t_curr = target.read(1)
						while t_curr not in self.digits:
							t_curr = target.read(1)
					if length > best:
						best = length
						result = location
						offset = curr_off
					target.seek(first_loc+1)
					self.source.seek(location+curr_off+1)
		print (result, best, offset)
		return (result, best, offset)

	def show(self, index, n, offest, margin):
		start = max(0, index+offset-margin)
		self.source.seek(start)
		output = ""
		output+=self.source.read(min(margin,index+offset))
		output+=" [ "
		count=0
		while count < n:
			curr = self.source.read(1)
			while curr not in self.digits+['.']:
				curr = self.source.read(1)
			output+=curr
			if curr == ".": continue
			else: count+=1
		output+=" ] "
		output+=self.source.read(margin)
		print output

	def find_earliest(self, target, n):
		"""Find the earliest prefix of target with length n
		   Returns index of result"""
		pass


if __name__=="__main__":
	source = sys.argv[1]
	target = sys.argv[2]
	n = int(sys.argv[3])

	ips = IrrationalPrefixSearch(source)
	(index, length, offset) = ips.find_longest(target, n)
	ips.show(index, length, offset, 5)