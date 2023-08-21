class Solution(object):
    def plusOne(self, digits):
        to_str_arr =(map(str, digits))
        to_str = "".join(to_str_arr)
        to_int = int(to_str)
        add_one = to_int+1
        new_arr =[]
        to_strA = str(add_one)
        for x in to_strA:
            new_arr.append(x)
        new_arr = list(map(int, new_arr))
        return (new_arr)