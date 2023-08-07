pass_img=(By.XPATH,"//img[contains(@class,'attachment-large size-large wp-image-56579') and contains(@src,'https://spycloud.com/wp-content/uploads/2023/07/outcome-password.svg')]")

rus = [20,20,20,21,21,27,28,20,20,24,24,24,25,25,31,32,31,24,31,25,32,25,25,31,24,25,31,24,32,24,31,31,24,24,32,32]
def foo(n):
  ttl = int(( ( n * (n+1) / 2 ) * 200 ) + 50000 )
  #print(ttl)
  return ttl


ttl = []
for inx in rus:
    ttl.append(foo(inx))

print( sum(ttl)/len(ttl) )    
