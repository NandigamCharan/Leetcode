doit :: [a] -> Int -> Int
doit [] acc = acc
doit (x:xs) acc = doit xs (acc+1)


len :: [a] -> Int
len lst = doit lst 0

