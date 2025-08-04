class Solution(object):
	def removeElement(self, nums, val):
		# подход двух указателей
		insert_pos = 0

		for i in range(len(nums)):
			if nums[i] != val:
				nums[insert_pos] = nums[i]
				insert_pos += 1

		del nums[insert_pos:]

		return len(nums)