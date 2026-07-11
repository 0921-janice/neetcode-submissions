class Solution:

    def encode(self, strs: List[str]) -> str:
        output_str = ""

        for s in strs:
            output_str += f"{len(s)}:{s}"
            print(output_str)

        return output_str

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            length_str = ""
            while s[i] != ":":
                length_str += s[i]
                i+=1
            print(length_str)
            length = int(length_str)
            i+=1

            output.append(s[i: i + length])
            i+=length

        return output
        
        
