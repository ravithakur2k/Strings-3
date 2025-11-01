# Time complexity: O(1) as the number of computation is constant.
# Space is also constant

# The intuition is to get triplets for the numbers and convert them into words and then for each triplet we can add Thousand, Million, Billion etc..
# To convert triplet to words, we can use recursive function to do it for 100s, 10s and 1s accordingly for the set of unique words showed in self.numbers and self.above_20

class Solution:
    def numberToWords(self, num: int) -> str:
        self.powerNums = ["", "Thousand", "Million", "Billion"]
        self.numbers = ["","One", "Two", "Three", "Four", "Five", "Six","Seven",
                    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
                    "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.above_20 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty",
                    "Ninety"]

        if num == 0: return "Zero"
        result = ""
        i = 0
        while num > 0:
            triplet = num%1000
            if triplet != 0:
                result = self.helper(triplet).strip() + " " + self.powerNums[i] + " " + result
            num = num//1000
            i += 1
        return result.strip()


    def helper(self, curr):
        if curr < 20:
            return self.numbers[curr]
        elif curr < 100:
            return self.above_20[curr//10] + " " + self.helper(curr%10)
        else:
            return self.numbers[curr//100] + " Hundred " + self.helper(curr%100)