class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nbrmap={"2":["a", "b", "c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        wrds = ""
        for d in digits:
            augmented_wrds = []
            for n in nbrmap[d]:
                for w in wrds:
                    augmented_wrds.append(w+n)
                if wrds == "":
                    augmented_wrds.append(n)
            wrds = augmented_wrds
        return wrds
                