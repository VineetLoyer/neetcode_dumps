def encode(strs):
    encode_str=''
    for s in strs:
        encode_str+=str(len(s))+'#'+s
    return encode_str

def decode(str):
    decode_lst=[]
    i=0
    while i<len(str):
        j=i
        while str[j]!='#':
            j+=1
        length =int(str[i:j])
        decode_lst.append(str[j+1:j+1+length])
        i=j+1+length
    return decode_lst


if __name__=='__main__':
    l = ['neet','code','love','you']
    string1 = encode(l)
    print(string1)
    print(decode(string1))
