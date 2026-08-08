def split_by_mask(strng, mask):
    start=0
    end_list=[]
    if sum(mask) != len(strng):
        return None
    for s in mask:
        end_list.append("".join(strng[start:start + s]))
        start+=s     
    return end_list       
