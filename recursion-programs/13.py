def towers(n,src,temp,dest):
  if n==1:
    print(f"Move disc {n} from {src} to {dest}")
    return
  towers(n-1,src,dest,temp)
  print(f"Move disc {n} from {src} to {dest}")
  towers(n-1,temp,src,dest)
towers(5,"src","temp","dest")
