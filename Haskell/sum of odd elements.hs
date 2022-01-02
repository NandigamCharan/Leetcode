
doit :: [Int] -> Int -> Int
doit [] acc = acc
doit (x:xs) acc = if mod x 2 == 1 
                    then doit xs (acc + x)
                  else doit xs acc

f :: [Int] -> Int 
f arr = doit arr 0


main :: IO ()
main = do
    inputdata <- getContents
    putStrLn $ show $ f $ map (read :: String -> Int) $ lines inputdata