# your code goes here
num=int(input())
d = { 0 : 'zero', 1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five', \
6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten', \
11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen', \
15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen', \
19 : 'Ninteen', 20 : 'Twenty', \
30 : 'Thirty', 40 : 'Fourth', 50 : 'Fifty', 60 : 'Sixty', \
70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninty' }
if (num < 20):
	print(d[num])
