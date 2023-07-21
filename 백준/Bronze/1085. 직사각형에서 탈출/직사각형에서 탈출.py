x, y, w, h = map(int,input().split())

xr = 0
yr = 0

if x > w/2 :
    xr = w - x
else:
    xr = x

if y > h/2 :
    yr = h - y
else:
    yr = y

if xr > yr:
    print(yr)
else:
    print(xr)