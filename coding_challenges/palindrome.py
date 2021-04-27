def solve(str_arg):
    str_list = [char for char in str_arg]
    str_list.reverse()
    s = ""
    return str_arg == s.join(str_list)


solve("abba")
solve("racecar!")
solve("ab ba")
solve("race car")
