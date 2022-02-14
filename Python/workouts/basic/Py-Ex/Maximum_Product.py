class Solution(object):
    def max_product(self, my_list):
        current_number = 0
        prev_num = 0
        current_max_product = 0
        last_num=0
        result = 0

        for i in range(0, len(my_list)):
            current_number = my_list[i]
            if prev_num == 0:
                last_num=prev_num
                prev_num = current_number
            else:
                current_max_product = prev_num * current_number
                last_num=prev_num
                prev_num = current_number
            
            print(str(last_num)+"*"+str(current_number)+"="+str(current_max_product))
            result = current_max_product if current_max_product > result else result
            result = current_number if current_number > result else result

        print("Maximum Product of Sub Array[{},{}]: {}".format(last_num,current_number,result if len(my_list) > 1 else my_list[0]))


obj1 = Solution()
my_list = [int(item) for item in input("Enter your array :").split()]
obj1.max_product(my_list)
