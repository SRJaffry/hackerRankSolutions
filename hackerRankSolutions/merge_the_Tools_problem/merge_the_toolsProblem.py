# URL ink to problem
# https://www.hackerrank.com/challenges/merge-the-tools/problem
# Problem link: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string_, k):
    # your code goes here
    
    List = [l for l in string_]

    if len(string_)%k == 0 :     
        quotient_ = int(len(string_)/k)

        new_list = []
        for i in range(quotient_):
            # str = ''.join(List[quotient_*i : quotient_*(i+1)])
            # str = ''.join(List[quotient_*i : quotient_*i+k])
            str = ''.join(List[k*i : k*i + k])
            new_list.append(str)

    new_sub_str_list = []
    
    # print('-----------')
    # print('new_list is: ', new_list)
    # print('-----------')
    for sub_str in new_list:
        sub_str_list = [l for l in sub_str]
        temp_sub_str_list = []
        
        for idx_ in range(len(sub_str_list)):
            if len(temp_sub_str_list) == 0:
                temp_sub_str_list.append(sub_str_list[idx_])
            else:
                if sub_str_list[idx_] not in temp_sub_str_list:
                    temp_sub_str_list.append(sub_str_list[idx_])
    
        new_sub_str = ''.join(temp_sub_str_list)
        new_sub_str_list.append(new_sub_str)
        
    for str_lst in new_sub_str_list:
        print(str_lst)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)