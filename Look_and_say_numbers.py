def name_list(data):
    res = ""
    cur_digit = data[0]
    cur_len = 0
    for c in data:
        if c == cur_digit:
            cur_len = cur_len+1
        else:
            res = res+str(cur_len)+str(cur_digit)
            cur_digit = c
            cur_len = 1
        
    res = res+str(cur_len)+str(cur_digit)
    return res


def look_and_say(data='1', maxlen=5):
  #populate result list with the look and say numbers
  ''' data:   starting number set
      maxlen: number of sequence to generate
  '''
  
  result = [data]
  for i in range(maxlen):
      result.append(name_list(result[-1]))
  return result[1:]
