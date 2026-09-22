class Solution:

    def encode(self, strs: List[str]) -> str:
        buffer_string = ""
        for s in strs:
            n = len(s)
            buffer_string += str(n) + "#" + s
        return buffer_string

    def decode(self, s: str) -> List[str]:
        sts = []

        reading_string = False
        buffer_string = ""
        length = 0

        for c in s:
            if reading_string:
                if length == 1:
                    buffer_string += c
                    sts.append(buffer_string)
                    buffer_string = ""
                    reading_string = False
                else:
                    buffer_string += c
                length -= 1
            else:
                if c == "#":
                    length = int(buffer_string)
                    if length == 0:
                        sts.append("")
                        continue
                    reading_string = True
                    buffer_string = ""
                else:
                    buffer_string += c
        return sts
